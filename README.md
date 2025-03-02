# Flask Tutorial

## Introduction
This repository contains a step-by-step guide to building web applications using Flask, a lightweight and powerful web framework for Python.

## Prerequisites
Before starting, ensure you have the following installed:
- Python (3.x recommended)
- pip (Python package manager)
- Virtual Environment (optional but recommended)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Ashis-Mishra07/flask-tutorial.git
   cd flask-tutorial
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Flask App

1. Set the environment variable (Windows PowerShell):
   ```powershell
   $env:FLASK_APP = "app.py"
   $env:FLASK_ENV = "development"
   ```
   On macOS/Linux:
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

2. Run the application:
   ```bash
   flask run
   ```

3. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure
```
flask-tutorial/
│── static/           # CSS, JavaScript, Images
│── templates/        # HTML Templates
│── app.py           # Main Flask Application
│── requirements.txt  # Dependencies
│── README.md        # Documentation
```

## Deploying the Application
To deploy your Flask app, consider using platforms like:
- **Heroku**
- **Render**
- **AWS Elastic Beanstalk**
- **Docker + Cloud Run**

## Additional Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja Templating](https://jinja.palletsprojects.com/)