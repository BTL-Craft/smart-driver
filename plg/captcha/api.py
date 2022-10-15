from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    f = open('./data/captcha.json', 'r')
    data = f.read()
    f.close()
    return data

if __name__ == '__main__':
    app.run(port=5001)