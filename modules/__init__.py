from flask import Flask
#app = Flask(__name__)
app = Flask(__name__, static_folder='/code/static')
import modules.centos
import modules.index
import modules.webres
import modules.commands



