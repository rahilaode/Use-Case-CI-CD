# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Selamat datang di halaman utama!'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')