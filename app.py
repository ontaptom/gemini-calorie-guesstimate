from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import vertexai
from vertexai.generative_models import GenerativeModel, Part
from markdown2 import Markdown
markdowner = Markdown()

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize Vertex AI
PROJECT_ID = "<your_project>"  # Replace with your actual project ID
vertexai.init(project=PROJECT_ID, location="us-central1") # optionally change the location

instructions = """As an AI assistant, when provided with an image of a food, 
    analyze the picture to recognize the ingredients and guesstimate the total 
    calorie intake. Present your findings with first of the overall calorie 
    estimation of a dish, and later in a list format, each identified ingredient 
    alongside its estimated calorie count, If you don\'t recognize food on picture, 
    inform user that it seems the wrong picture was uploaded. Start with 
    \"Here we go with a calorie guesstimate\", to indicate this is raw esitmation."""

model = GenerativeModel("gemini-1.5-flash-002", system_instruction=[instructions])

def analyze_image(image_path):
    with open(image_path, 'rb') as f:
        image_bytes = f.read()
    image_part = Part.from_data(image_bytes, mime_type="image/jpeg")
    
    response = model.generate_content([image_part, "Estimate calorie intake"])
    return response.text

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            
            # Analyze the uploaded image
            analysis_result = analyze_image(filename)
            analysis_html = markdowner.convert(analysis_result)
            return render_template('result.html', 
                                filename=file.filename,
                                analysis=analysis_html)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)