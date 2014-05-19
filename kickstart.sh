#!/bin/bash -x

sudo apt-get install git vagrant virtualbox nfs-kernel-server ansible

mkdir -p ~/Projects/invenio
git clone -b prod https://github.com/inspirehep/ops.git ~/Projects/invenio/invenio
git clone https://github.com/inspirehep/inspire.git ~/Projects/invenio/inspire

vagrant up
