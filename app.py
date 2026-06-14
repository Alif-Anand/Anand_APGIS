from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/peta')
def peta():
    return render_template('peta.html')

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

if __name__ == '__main__':
    app.run(debug=True)