#!/usr/bin/env	python

import sys
import requests
import gzip
import collections


def get_archi():
    if len(sys.argv) == 2:
        opts_archi = ['amd64', 'arm64', 'armel', 'armhf', 'i386', 'mips',
        'mips64el', 'mipsel', 'ppc64el', 's390x']

        if sys.argv[1] in opts_archi:
            return sys.argv[1]
        elif sys.argv[1].startswith("udeb-"):
            if sys.argv[1].split("udeb-")[-1] in opts_archi:
                return sys.argv[1]
            else:
                print "Parameter '" + sys.argv[1] + "' not valid"
                print "Should be one of: udeb-", opts_archi
                sys.exit(1)
        else:
            print "Parameter \"" + sys.argv[1] + "\" not valid:"
            print "Should be one of: ", opts_archi
            sys.exit(1)
    else:
        print "Nope"
        sys.exit(1)


def get_contentsIndex(arc):
    url = "http://ftp.uk.debian.org/debian/dists/stable/main/Contents-"
    cont_url = url + arc + ".gz"

    print "Downloading:"
    print cont_url

    cont_get = requests.get(cont_url)
    file_archi = cont_url.split('/')[-1]
    print "Writing to: " + file_archi

    with open(file_archi, "wb") as f:
        f.write(cont_get.content)
    return file_archi


def process_gzip(archivo):
    print "Processing gunzip: " + archivo

    with gzip.open(archivo, "rb") as gz:
        gz_content = gz.read()
    return gz_content.replace(',', '\n')


def sort_list(processed):
    package_list = []

    for pepe in processed.splitlines():
        package_list.append(pepe.split()[-1].split('/')[-1])

    contador = collections.Counter(package_list)

    top_ten = contador.most_common(10)
    print "\n Printing output: \n"
    no = 1
    for pepe in top_ten:
        print str(no) + " {0[0]} {0[1]}".format(pepe)
        no = no + 1


def main():
    l = process_gzip(get_contentsIndex(get_archi()))

    sort_list(l)

if __name__ == "__main__":
    main()
