
import configparser, os

#Writing to configfile

theconfig="Config/release.cfg"


def writeconfig(section,name,value):
    '''
    Wrinting data to config file
    '''
    config = configparser.ConfigParser()
    config.read(theconfig)
    config_out = configparser.RawConfigParser()
    #print "addind values"
    #Read config and ad new values
    for section_name in config.sections():
        config_out.add_section(section_name)
        if section == section_name:
            for c_name, c_value in config.items(section_name):
                    #config_out.set(section_name,c_name,c_value)
                    #print "renew"+c_name
                    config_out.set(section_name,c_name,c_value)

            config_out.set(section_name,name,value)
            #print "Adding"+name+value
        else:
            for c_name, c_value in config.items(section_name):
                config_out.set(section_name,c_name,c_value)

    #write new config
    with open(theconfig , 'wb') as configfile:
        config_out.write(configfile)


def getValue(section,name):
    '''
    Get a value back from the congifiles
    '''
    config = ConfigParser.ConfigParser()
    config.read(theconfig)
    return config.get(section, name )


def getSection(section):
    Config = configparser.ConfigParser()
    Config.read(theconfig)
    dict1 = []
    options = Config.options(section)
    for option in options:
            dict1.append([option,Config.get(section, option)])
    return dict1

#print getValue('Release','farepayment')

#writeconfig('Release','Webres','tag-2013-22-12')
#writeconfig('Release','Rentalfront','tag-2013-22-12')
#writeconfig('Release','Farepayment','tag-2013-22-12')
#writeconfig('Release','eff','tag-2013-22-12')