from flask import Flask

app = Flask(__name__)


@app.route('/')
def pump():
    return app.send_static_file('pump.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
