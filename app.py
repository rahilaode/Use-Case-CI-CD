# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Selamat datang di halaman utama!'

if __name__ == '__main__':
    app.run()