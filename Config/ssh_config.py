#!/usr/bin/env python
#
#

import paramiko
import subprocess


#key = paramiko.RSAKey(data=base64.decodestring('c8:9e:a0:a2:21:ee:99:e5:ee:a8:5a:68:83:fe:e9:7c'))
client = paramiko.SSHClient()
client.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())

client.connect('10.100.0.65', username='root', password='fo5Loogo')
stdin, stdout, stderr  = client.exec_command('ls')
print stdout.readlines()
stdin, stdout, stderr  = client.exec_command('ls')
print stdout.readlines()


print subprocess.Popen("scp example.cfg root@10.100.0.65:/tmp/",shell=True,stdout=subprocess.PIPE).communicate()[0]
