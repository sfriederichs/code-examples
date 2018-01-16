#!/usr/bin/python
""""
Python Command-Line Arguments Example v0.1
Version 0.1 Build 23 (1/15/18)
Author: Stephen Friederichs
License: Beerware License: If you find this program useful and you ever met me, buy me a beer. (I like Saisons)
This script demonstrates the use of the getopt library to parse command-line arguments passed to the Python script.
The following command-line parameters control the behavior of the script:
-h, --help - Shows this screen and exits
-v, --version - Display version information
-l, --license - Display author and license information
-f, -logfilepath=<PATH> - Set the log file path
"""

import textwrap
import logging
import getopt
import sys

logFilePath = "default.log"
logLevel = logging.DEBUG 

def prettyPrint(uglyString):
    """This function properly formats docstrings for printing on the console"""
    
    #Remove all newlines
    uglyString = uglyString.replace('\n','').replace('\r','')
    #Use textwrap module to automatically wrap lines at 79 characters of text
    print textwrap.fill(uglyString,width=79)
    

def license():
    for line in __doc__.splitlines()[3:5]:
        prettyPrint(line)
        
def help():
    for line in __doc__.splitlines()[5:]:
        prettyPrint(line)

def version():
    prettyPrint(__doc__.splitlines()[2])
 
def progId():
    prettyPrint(__doc__.splitlines()[1])
        
progId()

try: 
    opts, args = getopt.getopt(sys.argv[1:], 'hvlf:', ['help','version','license','logfile='])    
except getopt.GetoptError:
    print "Bad argument(s)"  
    help()
    sys.exit(2)   
    
for opt, arg in opts:                 
    if opt in ('-h', '--help'):     
        help()                         
        sys.exit(2)                 
    elif opt in ('-l','--license'):    
        license()
    elif opt in ('-f','--logfilepath='):
        logFilePath=str(arg)
    elif opt in ('-v','--version'):
        version()
    else: 
        help()
        sys.exit(2)
        
logging.basicConfig(filename=logFilePath,filemode='a',level=logLevel)

logging.debug("Logging is configured - Log Level %s , Log File: %s",str(logLevel),logFilePath) 

