'''
Created on 26 Jul 2016

@author: twixtMaD
'''
import configparser
import logging.config


config = configparser.ConfigParser()
config.read('/projects/maydayGrabber/Config/config.ini')
logging.config.fileConfig('/projects/maydayGrabber/Config/logger.config')
logger = logging.getLogger()

class JsonMaker(object):

    def slackJson(self, ticket):
        logger.debug('ticket : [%s]', ticket)
        username = config.get('slack', 'username')
        channel = config.get('slack', 'channel')
        icon_emoji = config.get('slack', 'icon')
        payloadMsg = 'payload={\"channel\": \"#%s\",\"username\": \"%s\",\"text\":\"%s\",\"icon_emoji\":\"%s\"}' %(channel, username, ticket, icon_emoji)
        logger.debug('payloadMsg: %s', payloadMsg )
        return payloadMsg