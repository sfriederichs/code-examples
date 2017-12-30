#!/usr/bin/python

import logging

logFilePath = "default.log"
logLevel = logging.DEBUG 
formatStr = '%(asctime)s - %(threadName)s - %(funcName)s  - %(levelname)-8s %(message)s'

logging.basicConfig(format=formatStr,filename=logFilePath,filemode='a',level=logLevel)

#Here's all the new stuff to handle the configuration of the console output

#First, generate a formatter object with the common format
formatter = logging.Formatter(formatStr)

#Then, retrieve a StreamHandler - this outputs log data to the console
console = logging.StreamHandler()

#Now configure the stream handler to the same settings as the file handler
#Note, however that you don't need them both to be configured the same - it may be
#entirely appropriate to have different settings for console vs. file.

console.setLevel(logLevel)
console.setFormatter(formatter)

#And finally, attach the console handler to the logger so the output goes both places
logging.getLogger('').addHandler(console)

#This will now show up on the console and in the log file
logging.debug("Logging is configured - Log Level %s , Log File: %s",str(logLevel),logFilePath) 