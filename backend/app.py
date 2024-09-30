from flask import Flask, send_from_directory
from flask_cors import CORS
from routes import overlay_blueprint  # Assuming 'overlay_blueprint' is in routes.py
import os

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})  # Allow requests from your frontend


# Register the overlay blueprint
app.register_blueprint(overlay_blueprint)

# Set the upload folder
UPLOAD_FOLDER = "./uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route to serve images from the uploads folder
# @app.route('/uploads/<filename>')
# def serve_image(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Serving the 'uploads' directory
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'uploads'), filename)


if __name__ == "__main__":
    app.run()
