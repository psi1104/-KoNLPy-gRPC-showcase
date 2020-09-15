from flask import Flask, render_template
from flask_cors import CORS
from waitress import serve


app = Flask(__name__, template_folder='templates')
cors = CORS(app)

@app.route('/health')
def health():
    return "ok"


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=80)
