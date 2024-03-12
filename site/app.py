from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)


UPLOAD_FOLDER = "../bot/data/base/"
DOWNLOAD_FOLDER = "../bot/data/sheets/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER


@app.route('/')
def page():
        return render_template('an_page.html')


@app.route('/an_page')
def an_page():
    return render_template('an_page.html')

@app.route('/bot_set_page')
def bot_set_page():
    return render_template('bot_set_page.html')

@app.route('/user_set_page')
def user_set_page():
    return render_template('user_set_page.html')

@app.route('/download')
def download():
    filename = 'base.json'
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = os.path.join(DOWNLOAD_FOLDER, file.filename)
        file.save(filename)
        # You can perform additional processing or redirect to another page if needed
        return redirect(url_for('an_page'))

if __name__ == "__main__":
    app.run()
