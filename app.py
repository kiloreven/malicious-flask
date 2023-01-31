from flask import Flask
from useless_package import message


app = Flask(__name__)


@app.route('/')
def hello_world():
    return message()


if __name__ == '__main__':
    app.run()
