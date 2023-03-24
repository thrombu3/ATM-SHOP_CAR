# author:liu_ll
import logging


def get_logger(name='django'):
    my_logger = logging.getLogger(name)
    return my_logger
