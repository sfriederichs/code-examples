#!/usr/bin/python

import logging


logLevel = logging.DEBUG 

# The 'format' option is new here:
logging.basicConfig(format='%(asctime)s - %(threadName)s - %(funcName)s  - %(levelname)-8s %(message)s',level=logLevel)

logging.debug("Logging is configured - Log Level %s , ",str(logLevel),) 