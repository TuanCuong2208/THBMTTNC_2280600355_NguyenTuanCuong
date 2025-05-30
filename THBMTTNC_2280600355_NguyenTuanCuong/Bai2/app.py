from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Route cho trang chủ
@app.route('/')
def home():
    return render_template('index.html')

# Route cho trang Caesar Cipher
@app.route('/caesar')
def caesar():
    return render_template('caesar.html', encrypted_text=None, decrypted_text=None)

# Route cho mã hóa
@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt(text, key)
    return render_template('caesar.html', encrypted_text=encrypted_text, decrypted_text=None)

# Route cho giải mã
@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt(text, key)
    return render_template('caesar.html', encrypted_text=None, decrypted_text=decrypted_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)