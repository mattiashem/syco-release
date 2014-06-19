#!/usr/bin/env python
#
#
# To run rin from jenkins server to deploy to pbk inte server.
import os.path
import paramiko
import subprocess
import getpass
import sys



#Settings for servers
int_server="10.100.0.65"
root_dir="/opt"
tmp="${ROOT_DIR}/tmp"
run_dir"${ROOT_DIR}/ehi-pbk-standalone"


#Take the first file as deploy
if sys.argv[1]
    deploy_file = sys.argv[1]
    #Check so files is there
    if not os.path.isfile(deploy_file):
        #No file
        break
else:
    print "add file to deploy"
    break




#############################################
#Logging into server
client = paramiko.SSHClient()
client.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())

client.connect(int_server, username='root', password='fo5Loogo')

#Removing old release
stdin, stdout, stderr  = client.exec_command("\rm -rf /opt/tmp")
print stdout.readlines()

#Coping file to server
print subprocess.Popen('scp '+deploy_file+' root@'+int_server+':/opt/tmp')

#Extract file
stdin, stdout, stderr  = client.exec_command("unzip -o {0}/{1}.zip -d {0}".format(tmp,deploy_file,))
print stdout.readlines()

#stoping old server
stdin, stdout, stderr  = client.exec_command("/opt/stop-pbk")
print stdout.readlines()

#Removing old release and switching folders
stdin, stdout, stderr  = client.exec_command("rm -rf {0}".format(run_dir))
print stdout.readlines()
stdin, stdout, stderr  = client.exec_command("mv {0}/${EXTRACTED_DIR} {2}".format(tmp,deploy_file,run_dir))
print stdout.readlines()

#Starting server
stdin, stdout, stderr  = client.exec_command("chmod 755 {0}/start".format(run_dir))
print stdout.readlines()
stdin, stdout, stderr  = client.exec_command("nohup {0}/start -Dconfig.file=/opt/application_uat.conf `</dev/null` >nohup.out 2>&1 &".format(run_dir))
print stdout.readlines()

#Test so server is running
stdin, stdout, stderr  = client.exec_command("ps aux | grep java | awk sdsdds")
print stdout.readlines()

if status = "Running":
    print "Server is runing"
else:
    print "No server is down"


