import subprocess
from multiprocessing import Process
from uuid import uuid4

from flask import Flask
from flask import render_template
from flask import request
from task import *


ssh = "/home/mattias/projects/Release/Config/sshCommand.py ssh"
file_location= "/home/mattias/projects/Release/static/"

def f(file,tag):
    #print "Running ssh"

    '''
    Releasing to release server
    '''
    subprocess.Popen(ssh+ " 10.0.0.70 'syco release-pbk "+tag+"' root password >> "+file_location+"file_"+file,shell=True,stdout=subprocess.PIPE).communicate()[0]
    print ssh+ " 10.0.0.70 'syco release-pbk "+tag+"' root password"+ file_location+"file_"+file







@app.route('/relese-pbk',methods=['POST', 'GET'])
def relesepbk():
    result=""
    filename=""
    if request.method == 'POST':
        tag = request.form['tag']
        file = "sdf"
        filename = str(uuid4())
        print "create = " + filename
        p = Process(target=f,args=(filename,tag))
        p.start()


        result ="running"
    return render_template('relese-pbk.html',result = result,file = filename)