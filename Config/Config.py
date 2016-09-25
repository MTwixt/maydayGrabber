'''
Created on 26 Jul 2016

@author: twixtMaD
'''

import configparser

config = configparser.ConfigParser()
config.read('/projects/maydayGrabber/Config/config.ini')

class Config(object):
    '''
    classdocs
    '''
    
    url = config.get('Google', 'url')
    htmlTablePath = config.get('Local', 'HtmlTablePath')
    targetLine = int(config.get('Util', 'targetLine'))  
    rex = config.get('Util', 'rex')
    td_Class = config.get('Util', 'td_Class')
    freshGrabTable = config.get('Util', 'freshGrabTable')
    oldGrabTable = config.get('Util', 'oldGrabTable')
    immTable = config.get('Util', 'immTable')
    ticketStatus = config.get('Local', 'ticketStatus')
    slackURL = config.get('Local', 'slackURL')