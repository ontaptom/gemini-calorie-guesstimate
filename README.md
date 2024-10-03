# Gemini Calorie Guesstimate

<p align="center">
  <img src="static/app-logo.png" alt="Gemini Calorie Guesstimate Logo" width="400"/>
</p>

## About

Gemini Calorie Guesstimate is an #BuildWithGemini educational project that uses Google's Gemini AI model to estimate calories in food from photos. Simply snap a picture of your meal, and let AI do the guesswork for you!

This project serves as a demonstration of integrating Google's Vertex AI with a Flask web application, providing a user-friendly interface for AI-powered food analysis.

## Educational Purpose

This project is intended for educational purposes, showcasing:
- Integration of Google Cloud Vertex AI
- Building a responsive web application with Flask
- Handling file uploads and image processing
- Docker containerization of a Python web app

## Setup and Deployment

### Prerequisites
- Google Cloud Platform account
- Python 3.9 or higher
- Docker (optional, for containerized deployment)

### Configuration

1. Clone the repository:
```bash
git clone https://github.com/yourusername/gemini-calorie-guesstimate.git
cd gemini-calorie-guesstimate
```

2. Edit `app.py` and replace the project ID:
```python
PROJECT_ID = ""  # Replace with your actual project ID
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Locally

```bash
python app.py
```

Make sure that user (or service account) running the application have sufficient permissions to call "Gemini-1.5-Flash-002" model. Example role `roles/aiplatform.user` you might try for your PoC. But long term about the 'least privilege' approach! ;)  

### Docker Deployment

The project includes an example Dockerfile for containerized deployment:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Run the app
CMD ["python", "app.py"]

# Expose the port
EXPOSE 8080
```

To build and run the Docker container:

```bash
docker build -t gemini-calorie-guesstimate .
docker run -p 8080:8080 gemini-calorie-guesstimate
```

## License

This project is licensed under the Apache License 2.0 - see below for details:

```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## Customization

Feel free to fork this repository and modify the code to suit your needs. Some ideas for customization:
- Add user authentication
- Implement a history feature to track meals over time
- Enhance the UI with additional styling or animations
- Add nutritional information beyond just calories

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.