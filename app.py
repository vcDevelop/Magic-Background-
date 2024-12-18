from flask import Flask, render_template, request, redirect, url_for
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from cloudinary import CloudinaryImage
from werkzeug.utils import secure_filename
import os
from config import api_key, cloud_name, api_secret

# Initialize Flask App
app = Flask(__name__)

# Configure Cloudinary
cloudinary.config( 
cloud_name ="dkwnwsfz7", 
api_key ="764752576949631", 
api_secret ="lLFS5AFJ1aRwAaPJ6Tx7zSPY2RY", # Click 'View API Keys' above to copy your API secret 
secure=True
)

# Define Upload Folder
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png'}

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Home route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    prompt = request.form['prompt']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Upload the image to Cloudinary
        upload_result = cloudinary.uploader.upload(file_path, public_id="user_upload")
        
        # Transform the image with the prompt (Cloudinary effect)
        a = CloudinaryImage("user_upload").image(effect=f"gen_background_replace:prompt_{prompt}")
        
        # Get transformed image URL
        transformed_image_url = a
        url = transformed_image_url.replace('<img src="', '').replace('"/>', '')
        return render_template('result.html', image_url=url)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
