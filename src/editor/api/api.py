import sqlite3
import sampa_mbrola
from flask import Flask, g, jsonify, render_template, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/espeak', methods=['GET'])
def frontend():
    converter = sampa_mbrola.Converter()
    sentence = converter.convert_sentence("Bom dia, comunidade")
    return jsonify(sentence.dictify())

@app.route('/api/mbrola', methods=['GET'])
def mbrola(page):
    pass

if __name__ == '__main__':
    app.run(debug=True)
