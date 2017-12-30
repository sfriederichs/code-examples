"""
Python Docstring Example v0.1
Author: Stephen Friederichs
This script demonstrates the use of docstrings versus conventional Python comments.
It also has other wicked awesome things going on like automatic text wrapping and command-line argument handling.
The following command-line parameters control the behavior of the script:
-h, --help - Shows this screen and exits
-a, --functiona - Shows the docstring for *funcA*
-b, --functionb - Shows the docstring for *funcB*
"""

import textwrap
import getopt
import sys

def prettyPrint(uglyString):
	"""This function properly fomats docstrings for printing on the console"""
	
	#Remove all newlines
	uglyString = uglyString.replace('\n','').replace('\r','')
	#Use textwrap module to automatically wrap lines at 79 characters of text
	print textwrap.fill(uglyString,width=79)
	

def funcA():
	"""Function A (funcA): This function accepts no inputs, returns no outputs and does no work"""
	pass

def funcB():
	"""Function B (funcB): This function is just as lazy and useless as funcA"""
	pass
	
def help():
	for line in __doc__.splitlines()[3:]:
		prettyPrint(line)
	
def version():
	for line in __doc__.splitlines()[1:3]:
				prettyPrint(line)
		
version()

try: 
	opts, args = getopt.getopt(sys.argv[1:], 'hab', ['help','functiona','functionb'])    
except getopt.GetoptError:
	print "Bad argument(s)"     
	sys.exit(2)                 

for opt, arg in opts:                 
	if opt in ('-h', '--help'):     
		help()                         
		sys.exit(2)                 
	elif opt in ('-a','--functiona'):    
		prettyPrint(funcA.__doc__)
	elif opt in ('-b','--functionb'):
		prettyPrint(funcB.__doc__)
	else: 
		help()
		sys.exit(2)
