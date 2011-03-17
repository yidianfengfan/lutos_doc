# encoding: utf-8

'''
Created on 2011-3-17

@author: leishouguo
'''

import ConfigParser,os

class Config():
    """docstring for Config"""
    def __init__(self):
        
        defaulting = {
              'mongo.server': 'localhost',
              'mongo.database': 'images',
              'mongo.port': 27017
        }
        self.config = ConfigParser.SafeConfigParser(defaulting)
        ini_file = os.path.join(os.path.dirname(__file__), '../config/app.ini')
        self.config.read(ini_file)
    
    def get(self, name):
        """docstring for get"""
        section = 'app'
        return self.config.get(section, name)

if __name__ == '__main__':
    config = Config()
    print(config.get('mongo.server'))