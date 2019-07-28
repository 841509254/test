from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<name>/<age>',)
def hello(name,age):
    return '''<h1 style="color:red">("name:%s,age:%s")</h1>'''%(name,age)

if __name__ == '__main__':
    app.run(debug=True)
