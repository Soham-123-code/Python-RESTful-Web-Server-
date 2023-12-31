from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<int:articleid>')
@app.route('/articles/<float:articleid>')
@app.route('/articles/<path:articleid>')
def api_articleid():
    return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run()

@app.route('/Hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello' + request.args['name']
    else:
        return 'Hello John Doe'

