import subprocess
from multiprocessing import Process
from uuid import uuid4

from flask import Flask
from flask import render_template
from flask import request
from task import *




ssh = "/home/mattias/projects/Release/Config/sshCommand.py ssh"
file_location= "/home/mattias/projects/Release/static/"

def f(file,cmd):
    #print "Running ssh"
    #print "run ssh " + file
    subprocess.Popen(ssh+ " "+cmd+" >> "+file_location+file,shell=True,stdout=subprocess.PIPE).communicate()[0]
    print ssh+ " "+cmd+" >> "+file_location+file



@app.route('/run',methods=['POST', 'GET'])
def run():

    what = request.form['loca']
    filename = request.form['file']
    subprocess.Popen("rm -f "+str(file_location)+str(filename),shell=True,stdout=subprocess.PIPE).communicate()[0]
    print "rm -f "+str(file_location)+str(filename)

    #######################################3
    ### WEBRES
    ######################################
    if "we-men-on" == what:
        '''
        Turn mantencemod on
        '''

        p = Process(target=f,args=(filename,"10.0.0.70 'syco men-on' root password"))
        p.start()

    elif "we-men-off" == what:
        '''
        Turn mantencemod off
        '''

        p = Process(target=f,args=(filename,"10.100.0.24 'syco men-off' root password"))
        p.start()

    elif "we-ap-on" == what:
        '''
        Turn webres apache on
        '''

        p = Process(target=f,args=(filename,"10.100.0.24 'syco httpd-on' root password"))
        p.start()

    elif "we-men-off" == what:
        '''
        Turn apache off
        '''

        p = Process(target=f,args=(filename,"10.100.0.24 'syco httpd-off' root password"))
        p.start()
    ####################################
    # RENTALFRONT
    #####################################

    elif "rf-ap-on" == what:
        '''
        Turn rentalfron apache on
        '''

        p = Process(target=f,args=(filename,"10.100.0.24 'syco httpd-start' root password"))
        p.start()


    elif "rf-ap-off" == what:
        '''
        Turn rentalfron apache off
        '''

        p = Process(target=f,args=(filename,"10.100.0.24 'syco httpd-stop' root password"))
        p.start()
    elif "rf-gf-on" == what:
        '''
        Turn rentalfron Glassfish on
        '''

        p = Process(target=f,args=(filename,"10.100.0.24 'syco gf-start' root password"))
        p.start()


    elif "rf-gf-off" == what:
        '''
        Turn rentalfron glassfish off
        '''
        p = Process(target=f,args=(filename,"10.100.0.24 'syco gf-on' root password"))
        p.start()
    ################################################3
    # FAREPAYMENT
    ################################################


    elif "fp-ap-on" == what:
        '''
        Turn farepayment apache on
        '''

        p = Process(target=f,args=(filename,"10.100.0.24 'syco httpd-start' root password"))
        p.start()


    elif "fp-ap-off" == what:
        '''
        Turn Farepayment apache off
        '''

        p = Process(target=f,args=(filename,"10.100.0.24 'syco httpd-stop' root password"))
        p.start()

    elif "fp-gf-on" == what:
        '''
        Turn farepayment Glassfish on
        '''

        p = Process(target=f,args=(filename,"10.100.0.24 'syco gf-start' root password"))
        p.start()


    elif "fp-gf-off" == what:
        '''
        Turn farepayment glassfish off
        '''

        p = Process(target=f,args=(filename,"10.100.0.24 'syco gf-on' root password"))
        p.start()

    ###################################
    # EFF
    #######################################
    elif "eff-on" == what:
        '''
        Turn eff apache on
        '''

        p = Process(target=f,args=(filename,"10.100.0.24 'syco httpd-start' root password"))
        p.start()


    elif "eff-off" == what:
        '''
        Turn ell apache off
        '''

        p = Process(target=f,args=(filename,"10.100.0.24 'syco httpd-on' root password"))
        p.start()

    ###################################
     # PBK
    #######################################
    elif "pbk-on" == what:
        '''
        Turn eff apache on
        '''

        p = Process(target=f,args=(filename,"10.100.0.24 'syco httpd-start' root password"))
        p.start()


    elif "pbk-off" == what:
        '''
        Turn ell apache off
        '''

        p = Process(target=f,args=(filename,"10.100.0.24 'syco httpd-on' root password"))
        p.start()


    else:
        '''
        No match
        '''
        print "No match"



    return "hej"