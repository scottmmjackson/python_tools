#!/usr/bin/python
# is_pdf.py
import pyPdf # pip install pyPdf to correct errors
import argparse
import sys
import os
p = argparse.ArgumentParser()
p.add_argument("testFile",metavar="FILE",type=file,help="file to test for pdf or not")
p.add_argument("-p","--posix",dest="posixReturn",action="store_true",help="Do not print anything, return true or false to shell")
args = p.parse_args()
try:
   d = pyPdf.PdfFileReader(args.testFile)
   assert d.getNumPages() > 0
   if(args.posixReturn): sys.exit(os.EX_OK)
   print args.testFile.name+": confirmed PDF"
except:
   if(args.posixReturn): sys.exit(os.EX_NOTFOUND)
   print args.testFile.name+": not a PDF"
   raise
