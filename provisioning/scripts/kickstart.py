#!/usr/bin/env python

import os

from distutils.version import LooseVersion
from plumbum import local
from plumbum.cmd import brew, git, vagrant

def main():
    print('* checking for Ansible...')
    try:
        import ansible
    except ImportError:
        needs_ansible = True
    else:
        if LooseVersion(ansible.__version__) < LooseVersion('1.6'):
            needs_ansible = True
        else:
            needs_ansible = False

    if needs_ansible:
        print('   installing')
        brew['install', 'ansible', '--HEAD']()
    else:
        print('   detected')


    invenio_dir = os.environ.get('CFG_INVENIO_SRCDIR', os.path.expanduser('~/src'))
    if not os.path.isdir(invenio_dir):
        print('* creating project directory')
        os.makedirs(invenio_dir)
    else:
        print('* project directory exists')

    with local.cwd(invenio_dir):
        if not os.path.isdir('vm'):
            print('* cloning vm repo')
            git['clone', '/afs/cern.ch/user/a/adeiana/public/repo/vm.git']()
        else:
            print('* vm repo exists')
        if not os.path.isdir('invenio'):
            print('* cloning invenio repo')
            git['clone', '/afs/cern.ch/user/a/adeiana/public/repo/cds-invenio-adeiana.git']()
        else:
            print('* invenio repo exists')
        with local.cwd('ops'):
            print('* bringing up virtual machine')
            vagrant['up']()


if __name__ == '__main__':
    main()
