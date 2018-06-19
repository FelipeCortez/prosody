import sqlite3
import subprocess
import sampa_mbrola
import secrets
from flask import Flask, g, jsonify, render_template, abort, request, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/espeak', methods=['POST'])
def frontend():
    text = request.form['text']
    converter = sampa_mbrola.Converter()
    sentence = converter.convert_sentence(text)
    return jsonify(sentence.dictify())

@app.route('/api/mbrola', methods=['GET'])
def mbrola():
    converter = sampa_mbrola.Converter()
    return jsonify({"mp3_file": converter.phones_to_mbrola()})

@app.route('/api/gen_audio', methods=['GET'])
def gen_audio():
    converter = sampa_mbrola.Converter()
    sentence = converter.convert_sentence("Vamos que vamos")

    token = secrets.token_hex(nbytes=4)
    with open(f"out/{token}.pho", 'w') as f:
        f.write(str(sentence))

    mbrola_str = f"mbrola br3/br3 out/{token}.pho out/{token}.wav"
    p = subprocess.Popen(mbrola_str, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()

    return jsonify({"token": token})

@app.route('/api/get_audio/<token>', methods=['GET'])
def get_audio(token):
    return send_file(
        f"out/{token}.wav",
        mimetype="audio/wav",
        as_attachment=True,
        attachment_filename=f"out/{token}.wav")

if __name__ == '__main__':
    app.run(debug=True)
