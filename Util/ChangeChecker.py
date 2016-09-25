'''
Created on 26 Jul 2016

@author: twixtMaD
'''
import difflib
import logging.config

logging.config.fileConfig('/projects/maydayGrabber/Config/logger.config')
logger = logging.getLogger()

class ChangeChecker(object):

    def compareDocument(self,src,tar):
        diffList = []
        with open(src, 'r', encoding='UTF-8') as srcFile, open(tar, 'r', encoding='UTF-8') as tarFile:
            src_line = srcFile.readlines()
            tar_line = tarFile.readlines()
            logger.debug('src_line: %s', src_line)
            logger.debug('tar_line: %s', tar_line)
            for line in difflib.ndiff(src_line,tar_line):
                if line.startswith('+ '):
                    diffList.append(line[2:-2])
            if len(diffList) < 2:
                logger.debug('Nothing Changed')
            return diffList