'''
Created on 26 Jul 2016

@author: twixtMaD
'''

import re
from bs4 import BeautifulSoup
import logging.config

logging.config.fileConfig('/projects/maydayGrabber/Config/logger.config')
logger = logging.getLogger()


def tableDecode(inHtml, targetLine, rex, result, td_class):
    with open(inHtml, 'r', encoding='UTF-8') as f:
        try:
            txt = (f.readlines())[targetLine]
        except:
            logger.debug('The table should be offline. It cant be read the contents.')
    htmlTable = re.search(rex, txt).group(0)
    #print(htmlTable)
    soup = BeautifulSoup(htmlTable, "lxml")
    rows = soup.find_all('tr')
    with open(result, 'w', encoding='UTF-8') as res:
        for row in rows:
            items = row.find_all("td", {"class":td_class})
            ticket=''
            for item in items:
                if item.string not in [None, '', '\n']:
                    ticket += str(item.string) + '|'
            res.write(ticket + '\n')
            
def skipBlank(resultTable, cleanedTable):
    with open(resultTable, 'r', encoding='UTF-8') as srcTable, open(cleanedTable, 'w', encoding='UTF-8') as cleanedT:
        lines = (line.rstrip() for line in srcTable)
        lines = (line for line in lines if line)
        for line in lines:
            cleanedT.write(str(line) + '\n')