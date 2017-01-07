'''
Created on Dec 22, 2016

@author: admin
'''



from abc import ABCMeta, abstractmethod, abstractclassmethod
from pprint import pprint

import requests
from scipy import iterable
import xml.etree.ElementTree as ET

feed_list = [ r'https://www.upwork.com/ab/feed/jobs/atom?category2=web_mobile_software_dev&contractor_tier=1%2C2&subcategory2=desktop_software_development%2Cmobile_development%2Cqa_testing%2Cscripts_utilities%2Cweb_development%2Cweb_mobile_design%2Cother_software_development&sort=create_time+desc&api_params=1&q=&securityToken=4aa606ee391dec6bd271cea909cb55cfbe6f8b7cf22f9a1e3f265214784c96377651feb5902eaca5a02e2f38f4ea27b5392b5a89ca1e62910236ae039307a1f5&userUid=757003863694090240&orgUid=757003863698284545',
             'https://www.freelancer.com/rss.xml',
             'http://www.juju.com/add-jobs/feeds/'
    ]

feeds = [{'url' : item}  for item in feed_list ]

class Feed_Bot(object, iterable, metaclass= ABCMeta):
    '''
    An abstract feeder object to be implemented by each indivudial website's API and input controls   
    '''
    def __init__(self, feed):
        '''
        Attem
        '''
        self.proxies = []
        self.feed = feed
        
    def apply_job(self, regex = ''):
        '''
        Applies to jobs using 
        '''
        
        if not self.proxies:
            self.proxies.append(['localhost:8080'])
        
        pass
    
    @abstractmethod
    def __iter__(self):
        '''
        Subclasses 
        '''
        pass
    
    def get_iterator(self):
        return self.__iter__()
    
    @abstractmethod
    def update_feed(self):
        pass

class Upwork_Bot(object, Feed_Bot):
    @abstractmethod
    def __iter__(self):
          
          
        xml = requests.get(self.feed)
        tree = ET.parse(xml.text)
        
        for child in tree.getroot():
            yield child.tag, child.attrib          
                    
    
    def get_iterator(self):
        return self.__iter__()
    
class Bot_Manager(object ):
    def ___init__(self, bots = []):
        super().__init__()
        self.simaltaneous_connection_limit = 4
        self.bots = bots
    
    
        '''
        For each bot scrape,
        update in memory dict,
        commit dict to database
        
        '''
    def scrape_all(self):
        '''
        Return an iterator of bots scrapes
        '''
        return (bot for bot in self.bots)
    
    
        
def scrape():
    '''
    Generator for lists of rss feeds
    '''
    upwork_feed = 'https://www.upwork.com/ab/feed/topics/rss?securityToken=4aa606ee391dec6bd271cea909cb55cfbe6f8b7cf22f9a1e3f265214784c96377651feb5902eaca5a02e2f38f4ea27b5392b5a89ca1e62910236ae039307a1f5&userUid=757003863694090240&orgUid=757003863698284545&topic=2545277'
    upwork_feeder = Feed_Bot(upwork_feed)
    

if __name__ == '__main__':
    scrape()