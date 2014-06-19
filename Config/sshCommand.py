#!/usr/bin/env python
#
#
# To run ssh commands on remote host using python

import paramiko
import sys








def runcmd(host,user,commands,password):
    '''
    Execute the command on the host
    '''

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(
                    paramiko.AutoAddPolicy())
        client.connect(host, username=user, password=password)

        for c in commands:
            print c
            stdin, stdout, stderr  = client.exec_command(c)
            print stdout.readlines()
            #print stdout.read.splitlines()
            for line in stdout:
                print line


        client.close()


    except paramiko.AuthenticationException:
        print "ssh failed on login."



def sendfile(host,files):
    '''
    Sending file to server
    '''
    for file in files:
        copy = pexpect.spawn('scp '+file+' root@'+host+':/tmp')
        i=copy.expect([pexpect.EOF])
        if i == 0:
            print "file sent"
        else:
            print "ERROR"


if sys.argv[1] == "ssh":
    '''
    Use ssh to login and run commands
    '''
    hosts = [x.strip() for x in  sys.argv[2].split(',')]
    commands = [x.strip() for x in  sys.argv[3].split(',')]
    user = sys.argv[4]
    password = sys.argv[5]

    for h in hosts:
        runcmd(h,user,commands,password)


if sys.argv[1] == "copy":
    '''
    Copy files to server
    '''
    hosts = [x.strip() for x in  sys.argv[2].split(',')]
    commands = [x.strip() for x in  sys.argv[3].split(',')]

    for h in hosts:
        print h + str(commands)
        #sendfile(h,files)
else:
    print "No correct argumnets provided use"