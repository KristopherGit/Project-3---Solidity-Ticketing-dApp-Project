# config file for JSONbin API Secret Keys

import os

class Config:
    JSONBIN_SECRET_KEY = os.environ.get('JSONBIN_SECRET_KEY')
    #JSONBIN_SECRET_KEY = os.environ.get('$2b$10$TBShXqVtrokNLIU1b2GD7upkZ7ZV6cgi1gv0rRXYVkS656gRM1tqq')
    