from flask import Flask
from flask import render_template


from modules import app


@app.route('/centos')
def centosss():
    return render_template('centos.html')