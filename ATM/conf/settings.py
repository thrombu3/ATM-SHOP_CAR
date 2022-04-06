import os

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
DIR_PATH = os.path.dirname(__file__)
DB_PATH = os.path.join(PROJECT_PATH, 'db')
STANDARD_FORMAT = '[%(asctime)s][%(threadName)s:%(thread)d][场景:%(name)s][%(filename)s:%(lineno)d][%(levelname)s][%(message)s]'
SIMPLE_PATH = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
LOGGER_PATH = os.path.join(PROJECT_PATH, 'logger')


def logging_dic():
    if not os.path.exists(LOGGER_PATH):
        os.makedirs(LOGGER_PATH)
    logfile_path = os.path.join(LOGGER_PATH, 'logger.log')
    LOGGING_DIC = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': STANDARD_FORMAT
            },
            'simple': {
                'format': SIMPLE_PATH
            },
        },
        'filters': {},  # 过滤日志
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'default': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'standard',
                'filename': logfile_path,
                'maxBytes': 1024 * 1024 * 5,
                'backupCount': 5,
                'encoding': 'utf-8',
            },
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': 'DEBUG',
                'propagate': True,
            }
        },
    }
    return LOGGING_DIC
