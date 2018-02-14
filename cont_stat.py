#!/usr/bin/env	python

import sys
import requests
import gzip

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
      return archi
    else:
      print "Argument not in:", opts_archi 
  else:
    print "Nope"
    sys.exit(1)


def get_contentsIndex(arc):
  cont_url = "http://ftp.uk.debian.org/debian/dists/stable/main/Contents-"+ arc + ".gz"
  cont_get = requests.get(cont_url)
  file_archi =cont_url.split('/')[-1]
  with open(file_archi, "wb") as f: f.write(cont_get.content)
  return file_archi

def process_gzip(archivo):
  with gzip.open(archivo, "rb") as gz: gz_content = gz.read()
  return gz_content

print process_gzip(get_contentsIndex(get_archi()))


