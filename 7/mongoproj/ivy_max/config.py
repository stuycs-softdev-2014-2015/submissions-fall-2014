import ConfigParser
import os.path
from os import urandom

def createConfig():
    config = ConfigParser.ConfigParser()
    cf = open('config.ini', 'w')
    config.add_section('Info')
    config.set('Info', 'secret', urandom(24))
    config.write(cf)
    cf.close()

def getSecret():
    if not os.path.isfile('config.ini'):
        createConfig()
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    return config.get('Info', 'secret')



