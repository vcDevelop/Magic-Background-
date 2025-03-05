# Magic Background - Flask & Cloudinary API

This project allows users to upload an image and apply transformations using the Cloudinary API. The application is built using Flask and provides a user-friendly interface to modify image backgrounds based on user prompts.

## Features
- Upload images and apply transformations
- Modify the background using Cloudinary API
- Simple and user-friendly UI
- Flask backend for handling requests

## Technologies Used
- Flask
- Cloudinary API ```https://cloudinary.com/documentation/django_image_and_video_upload```
- HTML/CSS/JavaScript

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vcDevelop/Magic-Background.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Magic-Background
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up Cloudinary API credentials:
   - Create a `.env` file and add your Cloudinary API credentials:
   ```env
   CLOUDINARY_URL=cloudinary://API_KEY:API_SECRET@CLOUD_NAME
   ```

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```
2. Open the browser and go to:
   ```
   http://127.0.0.1:5000/
   ```
3. Upload an image and enter a prompt to transform it.
4. View and download the transformed image.

## Before and After Examples

### Before Transformation
![Before Image](https://raw.githubusercontent.com/vcDevelop/Magic-Background/main/path/to/before_image.jpg)

### After Transformation
![After Image](https://raw.githubusercontent.com/vcDevelop/Magic-Background/main/path/to/after_image.jpg)
