from flask import Flask
from flask import render_template
from flask import request

from modules import app
from uuid import uuid4
from modules.status_check import check_dns,check_con_tcp
from modules.config_control import writeconfig, getSection
import cgi


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    #Check what servers are in prod
    dns_name =['prod.farepayment.com','alamo-couk-enterprise-production.fareoffice.com','pbk.partnerbookingkit.com']
    dns = check_dns(dns_name)

    #Check for open tcp conenctions
    hosts=[['www.elino.se',80],['www.dn.se',80],['www.alamo.co.uk',443]]
    tcp_con = check_con_tcp(hosts)

    release = getSection("Release")

    return render_template('status.html',tcp_con=tcp_con,dns=dns,release=release)


@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/control')
def control():
    filename = str(uuid4())
    return render_template('control.html',file = filename)






def meny():
    return ['index','/']