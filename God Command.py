from flask import Flask, jsonify
import requests
import random

app = Flask(__name__)

@app.route('/random-god', methods=['GET'])
def random_god():
    response = requests.get('https://docs.google.com/spreadsheets/d/1QpEYfFsdDaTsvtFQbszgh0tz-xo4i94b8L_XWF_3DLs/export?format=csv')
    lines = response.text.splitlines()
    gods = [line for line in lines if line]
    return jsonify(random.choice(gods))

if __name__ == '__main__':
    app.run()
