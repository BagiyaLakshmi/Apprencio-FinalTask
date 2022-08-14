from contextlib import redirect_stderr
from flask import Flask, request,\
    render_template

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route("/redirect", methods=['post'])
def sample():
    val=[i for i in request.form.values()]
    return render_template('redirect.html', Val=val)


if __name__=='__main__':
    app.run()(host='127.0.0.1', port=7000)