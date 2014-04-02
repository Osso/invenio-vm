#!/usr/bin/env python

import os
import sys

CFG_INSPIRE_BIBTASK_USER = os.environ.get('CFG_INSPIRE_BIBTASK_USER')
CFG_INVENIO_PREFIX = os.environ.get('CFG_INVENIO_PREFIX')
PATH = os.environ.get('PATH')

from plumbum import local
local.env['PATH'] = "%s:%s/bin" % (PATH, CFG_INVENIO_PREFIX)

from plumbum.cmd import (bibupload, bibrank,
                         bibindex, webcoll, bibauthorid)



def die(msg):
    print >>sys.stderr, msg
    sys.exit(1)


def silence(cmd):
    return cmd > "/dev/null"


def main():
    if not CFG_INVENIO_PREFIX:
        die("CFG_INVENIO_PREFIX is empty")
    bibupload['1']()
    bibindex['2']()
    webcoll['3']()
    bibrank['4']()
    bibauthorid['--update-personid', '--all-records', '-u', CFG_INSPIRE_BIBTASK_USER]()
    bibauthorid['5']()

    print "Done"


if __name__ == '__main__':
    main()
