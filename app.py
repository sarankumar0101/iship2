from flask import Flask, render_template, request, jsonify
from PIL import Image
import pytesseract
import io

app = Flask(__name__)

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Use your installation path

# Route to render the sign-in page
@app.route('/signin')
def signin():
    return render_template('signin.html')

# Route to render the sign-up page
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Route to render the main services page
@app.route('/services')
def services():
    return render_template('services.html')

# Route to render the main page
@app.route('/')
def main():
    return render_template('main.html')

# Route to render the image-to-text converter page
@app.route('/image-to-text')
def image_to_text():
    print("Rendering image-text.html")
    return render_template('image-text.html')

# Route to render the PDF-to-Word converter page
@app.route('/pdf-to-word')
def pdf_to_word():
    return render_template('pdf_to_word.html')

# Route to render the PPT-to-PDF converter page
@app.route('/ppt-to-pdf')
def ppt_to_pdf():
    return render_template('ppt_to_pdf.html')

# Route to render the Text-to-PDF converter page
@app.route('/text-to-pdf')
def text_to_pdf():
    return render_template('text_to_pdf.html')

# Route to render the Word-to-PDF converter page
@app.route('/word-to-pdf')
def word_to_pdf():
    return render_template('word_to_pdf.html')

# Route to render the Contact Us page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route to handle image upload and text extraction
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Open image file and extract text using pytesseract
        image = Image.open(file.stream)
        text = pytesseract.image_to_string(image)
        
        # Return the extracted text as JSON
        return jsonify({'text': text if text else 'No text found.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
