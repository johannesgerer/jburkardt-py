#!/usr/bin/env python

import sys

print " "
print "ARGS"
print "  Python version"
print "  Count and print the arguments."
print " "
print "  The number of arguments was " + repr ( len ( sys.argv ) ) + "."
print " "
print "  Arg[0] = the program name = '" + sys.argv[0] + "'"

i = 1;

while 1 < len ( sys.argv ):
  print "  Arg[" + repr ( i ) + "] = '" + sys.argv[1] + "'"
  del sys.argv[1];
  i = i + 1;

