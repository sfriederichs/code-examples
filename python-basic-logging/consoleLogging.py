#!/usr/bin/python

#Import the logging library
import logging

#Set the default log level
#Options are (in order of increasing priority):
# * logging.DEBUG
# * logging.INFO
# * logging.WARNING
# * logging.ERROR
#Log levels allow all higher priority messages to go through, so if you set the level to DEBUG,
#you get every single log message, but if you set it to WARNING you only get WARNING and 
#ERROR

logLevel = logging.DEBUG 

#This call configures logging to a file at logFilePath with a level of logLevel
logging.basicConfig(level=logLevel)

#Basic logging - debug level
#Note: the logging functions do not support typical Python string concatenation
#E.g. logging.debug("Logging is configured - Log Level " + str(logLevel)) 
#The above example will produce an error
#You have to use printf-style casting as seeen below
#Note that when in doubt about data types and which cast you should use remember that you can just use %s 
#and use Python casts to make anything a string

logging.debug("Logging is configured - Log Level %s ",str(logLevel)) 
logging.info("Informational... uh... *information*")
logging.warn("You have been put on notice")
logging.error("You done messed up")