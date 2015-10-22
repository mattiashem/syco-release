Release tool
=======


#######Installation

-- Install docker and docker-compose on your machine.

    https://docs.docker.com/installation/
    https://docs.docker.com/compose/install/

-- Build the app
    docker-compose build

-- To run the type
    docker-compose run app

    http://localhost:5000




#######Flow

-- wepage (flask) show form to do release and get a post

-- The post is recived in examle relesewebres.
The view extract the data that it need for the release example the release tag and datacenter.

It also creates a uniq filename. and start a new background process

        filename = str(uuid4())   <--- uniq file name
        p = Process(target=f,args=(filename,target,tag,datacenter)) <--- start background process
        p.start()




-- the backgrounden process take tha values and trigges the correct fabric script

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


This is the call for the fabric script

        subprocess.Popen("fab webres_release:"+tag+","+datacenter+" >> "+file_location+"file_"+file, shell=True, stdout=subprocess.PIPE).communicate()[0]

It also setup so that all info from teh fabric script is sent to a file.



-- The pages is up and now two new bottons show "start" and "stop" they will start i javascript that sill live fead the data from
the file we created before and that the fabric script is sending its data to.







