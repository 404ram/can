#!/usr/bin/env	python

import sys
import requests

def get_archi():
  if len(sys.argv) == 2:
    opts_archi = ['amd64', 
      'arm64', 
      'armel', 
      'armhf',
      'i386', 
      'mips',
      'mips64el',
      'mipsel',
      'ppc64el',
      's390x']
  
    if  sys.argv[1] in opts_archi:
      archi = sys.argv[1]
      print "Architecture set to", archi
    else:
      print "Argument not in:", opts_archi 
  else:
    print "Nope"
    sys.exit(1)

get_archi()

