'''
Created on Dec 22, 2016

@author: admin
'''



from _collections_abc import Iterable
from abc import ABCMeta, abstractmethod, abstractclassmethod
import abc
from pprint import pprint
from test.test_xml_etree import ET

import requests
import sqlite3


class Feed_Bot(object, metaclass= ABCMeta):
    '''
    An abstract feeder object to be implemented by each indivudial website's API and input controls   
    '''
    @classmethod
    def __init__(self, feed):
        '''
        Attem
        '''
        self.proxies = []
        self.feed = feed
        self.feed_list = [ r'https://www.upwork.com/ab/feed/jobs/atom?category2=web_mobile_software_dev&contractor_tier=1%2C2&subcategory2=desktop_software_development%2Cmobile_development%2Cqa_testing%2Cscripts_utilities%2Cweb_development%2Cweb_mobile_design%2Cother_software_development&sort=create_time+desc&api_params=1&q=&securityToken=4aa606ee391dec6bd271cea909cb55cfbe6f8b7cf22f9a1e3f265214784c96377651feb5902eaca5a02e2f38f4ea27b5392b5a89ca1e62910236ae039307a1f5&userUid=757003863694090240&orgUid=757003863698284545',
             'https://www.freelancer.com/rss.xml',
             'http://www.juju.com/add-jobs/feeds/'
    ]
    
        
    def apply_job(self, regex = ''):
        '''
        Applies to jobs using 
        '''
        
        if not self.proxies:
            self.proxies.append(['localhost:8080'])
        
        pass
    
    
    def __iter__(self):
        '''
        Subclasses 
        '''
        pass
    
    def get_iterator(self):
        return self.__iter__()
    
    
    def update_feed(self):
        pass

class Upwork_Bot(Feed_Bot):
    
    def __init__(self, feed, target = ''):
        super().__init__(feed)
        self.parse_dict = ['rss','channel', 'item']
        self.target = target
        self.db = sqlite3.connect(':in')
        def build_scrape(self):
            xml = requests.get(self.feed)
            tree = ET.parse(xml.text)
            for feed_item in tree.getroot().iter(self.target):
                yield feed_item.attrib
        return [build_scrape(self)]
   
    
    
    def __iter__(self):
        pass
    
    def get_iterator(self, target = ''):
        return self.__iter__(target)
    
class Bot_Manager(object):    
    
    def ___init__(self, bots = []):
        super().__init__()
        self.bots = bots
        
        self.simaltaneous_connection_limit = 4
    
        '''
        For each bot scrape,
        update in memory dict,
        commit dict to database
        
        '''
    def scrape_all(self):
        '''
        Return an iterator of bots scrapes
        '''
        for bot in self.bots:
            while 0 > self.simaltaneous_connection_limit < 4:
                yield bot
            
    
    
        
def scrape():
    '''
    Generator for lists of rss feeds
    '''
    upwork_feed = 'https://www.upwork.com/ab/feed/topics/rss?securityToken=4aa606ee391dec6bd271cea909cb55cfbe6f8b7cf22f9a1e3f265214784c96377651feb5902eaca5a02e2f38f4ea27b5392b5a89ca1e62910236ae039307a1f5&userUid=757003863694090240&orgUid=757003863698284545&topic=2545277'
    upwork_feeder = Feed_Bot(upwork_feed)
    

if __name__ == '__main__':
    pass
