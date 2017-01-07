'''
Created on Jan 7, 2017

@author: admin
'''
import unittest

import ipgetter


class Test(unittest.TestCase):


    def test_not_my_home_ip(self):
        ip = '45.50.220.30'
        IP = ipgetter.myip()
        self.assertTrue( ip != str(IP), "Failed to hide ip %s" % IP)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_not_my_home_ip']
    unittest.main()