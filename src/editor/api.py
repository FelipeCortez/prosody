import sqlite3
from flask import Flask, g, jsonify, render_template, abort

app = Flask(__name__)

@app.route('/api/espeak', methods=['GET'])
def frontend():
    pass

@app.route('/api/mbrola', methods=['GET'])
def mbrola(page):
    pass

if __name__ == '__main__':
    app.run(debug=True)
