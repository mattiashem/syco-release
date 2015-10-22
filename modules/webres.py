import subprocess
from multiprocessing import Process
from uuid import uuid4
from modules import app
from flask import Flask
from flask import render_template
from flask import request
from modules.status_check import check_dns_hosts


file_location= "/code/static/"

'''
Setting upp the fab command that will be run when releasing
Reciving the target value from webpage in dropdown.
And determent what command to run depending on target
'''


def f(file,target,tag,datacenter):
     if "Release" == target:
        #Running release commands
        subprocess.Popen("fab webres_release:"+tag+","+datacenter+" >> "+file_location+"file_"+file, shell=True, stdout=subprocess.PIPE).communicate()[0]
        print("release")
     elif target is "Uat":
        #Running UAT commands
        pass
     elif target is "Production":
        #Running on prod servers
        pass
     else:
        print("Incorrect target")


'''
contoling the page and to do an release.

collecting tag,target from webpage and activating an background job that will run the fab command to do the release.
'''
@app.route('/relese-webres',methods=['POST', 'GET'])
def relesewebres():
    result=""
    filename=""

    if request.method == 'POST':
        '''
        Recving from the webbpage what tag and target user has choosen.
        And sending to script.
        '''
        tag = request.form['tag']
        target = request.form['target']
        datacenter = request.form['datacenter']
        filename = str(uuid4())
        p = Process(target=f,args=(filename,target,tag,datacenter))
        p.start()
        result="yes"

    #Fidnig what datacenter is active
    dns_resolved = check_dns_hosts('alamo-couk-enterprise-production.fareoffice.com')
    datacenter =  dns_resolved.split('-', 1 )[0]

    return render_template('relese-webres.html',result = result,file = filename,datacenter=datacenter)