#!/usr/bin/python
# is_pdf.py
import sys
import os
try:
   import pyPdf # pip install pyPdf to correct errors
except ImportError:
   sys.exit("pyPdf is required. If you don't have pyPdf, try 'pip install pyPdf'. If you don't have pip, go here: https://pypi.python.org/pypi/pip")
if sys.version_info[0] != 2 or sys.version_info[1] < 7:
   sys.exit("Python 2.7+ required. Got Python "+".".join(sys.version_info))

def isPdf(filehandle):
	try:
	   d = pyPdf.PdfFileReader(filehandle)
	   assert d.getNumPages() > 0
	   return True
	except:
	   return False

def isPdfOpen(filename):
	return isPdf(file(filename))

if __name__ == '__main__':
	import argparse
	p = argparse.ArgumentParser()
	p.add_argument("testFile",metavar="FILE",type=file,help="file to test for pdf or not")
	p.add_argument("-p","--posix",dest="posixReturn",action="store_true",help="Do not print anything, return true or false to shell")
	args = p.parse_args()
	if(isPdf(args.testFile)):
		if(args.posixReturn): 
			sys.exit(os.EX_OK)
		else: 
			print args.testFile.name+": confirmed PDF"
	else:
		if(args.posixReturn): 
			sys.exit(os.EX_NOTFOUND)
		else:
			print args.testFile.name+": not a PDF"