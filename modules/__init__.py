from flask import Flask
#app = Flask(__name__)
app = Flask(__name__, static_folder='/home/mattias/projects/Release/static')





import modules.centos
import modules.index
import modules.webres
import modules.commands
import modules.rentalfront
import modules.farepayment
import modules.pbk
import modules.eff


