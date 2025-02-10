from logger import logging

def add(a,b):
    logging.debug(' This is an addition function')
    return a+b

logging.debug('addition function is called')
add(10, 15)
