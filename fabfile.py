__author__ = 'mattias'


#fabric
from fabric.api import *
from ilogue.fexpect import expect, expecting, run
#libs
import time
#custom
from modules.config_control import writeconfig




env.roledefs = {
    'webres-release':['192.168.44.2'],
    'webres-prod':['10.101.1.134','10.101.2.134']
}

env.user = 'root'
env.password = 'olle!66'

'''
Release of webres
'''

@roles('webres-release')
def webres_release(tags,datacenter):
    if datacenter == "av":
        print("RELEASEING WITH PRODUCTION AV")

        #Making mysql backup by sending request to mysql server
        execute(mysql_backup_dump, tags='tags', db='bacula', host='192.168.44.2')


        #Running the release
        run('ls -l')
        #Putting new installation file on server
        #put('localfile','remotefile')
        #Running sudo command
        sudo("cat /etc/passwd")

        #Adding release tag to config file
        writeconfig('Release','Webres',tags)


    elif datacenter == "tc":
        print("RELEASEING WITH PRODUCTION TC")
        #Adding release tag to config file
        writeconfig('Release','Webres',tags)
        #Running the release
        run('ls -l')
        #Putting new installation file on server
        #put('localfile','remotefile')
        #Running sudo command
        sudo("cat /etc/passwd")
    else:
        print ("ERROR IN DATACENTER")




def mysql_backup_dump(tags, db):
    print(Making mysql_backup_dump)
    date = time.strftime("%Y-%m-%d")

    run('mysqldump '+db+' > /var/backup/mysqldumpt_'+db+'_'+tags+'_'+date+'.sql')
    run('tar czf /var/backup/mysqldumpt_'+db+'_'+tags+'_'+date+'.tar.gz /var/backup/mysqldumpt_'+db+'_'+tags+'_'+date+'.sql')