#!/usr/bin/python

import logging

logFilePath = "default.log"
logLevel = logging.DEBUG 

#The new thing here is the 'filemode' option - it determines how the data is written to the file
# 'a' - This will append the data to the end of the file. This behavior is the default if you 
# don't specify the option
# 'w' - This will overwrite the existing file every time the script is called
 
logging.basicConfig(filename=logFilePath,filemode='a',level=logLevel)

logging.debug("Logging is configured - Log Level %s , Log File: %s",str(logLevel),logFilePath) 