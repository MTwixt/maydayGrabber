'''
Created on 26 Jul 2016

@author: twixtMaD
'''
from Util import TableDecoder
from Util.ChangeChecker import ChangeChecker
from Config.Config import Config
import os, logging.config, time

from Util.JsonMaker import JsonMaker

logging.config.fileConfig('/projects/maydayGrabber/Config/logger.config')
logger = logging.getLogger()

if __name__ == '__main__':
    
    config = Config()
    
    os.system('mv %s %s' %(config.freshGrabTable, config.oldGrabTable))
    os.system('curl %s > %s' %(config.url, config.htmlTablePath)) 
    
    TableDecoder.tableDecode(config.htmlTablePath,config.targetLine,config.rex,config.immTable, config.td_Class)
    TableDecoder.skipBlank(config.immTable, config.freshGrabTable)
    
    os.system('rm -f %s' %(config.immTable))

    cc = ChangeChecker()

    tickets = cc.compareDocument(config.oldGrabTable, config.freshGrabTable)
    jsonCreator = JsonMaker()
    
    for ticket in tickets:
        logger.debug('main: ticket: %s', ticket)
        slackMsg = jsonCreator.slackJson(ticket)
        slackInstruction = 'curl -X POST --data-urlencode \'' + slackMsg + '\' ' + config.slackURL
        logger.debug(slackInstruction)
        os.system(slackInstruction)
        time.sleep(1)
    logger.debug('END')