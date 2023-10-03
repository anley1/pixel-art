from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = Image.open(request.files['file'])
        image = image.resize((64, 64))  # Resize to get the pixelated effect
        pixels = list(image.getdata())
        print(len(pixels))
        return render_template('pixel_art.html', pixels=pixels)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

