invenio-vm
==========

Will setup a virtual machine environment with Invenio installed and ready
for development.

Installation
------------

Clone the repository and edit the main Invenio configuration:

    cd ~/src/invenio-vm/provisioning/files
    vim invenio-local.conf

Then go back and run `kickstart.sh`:

    cd ~/src/invenio-vm
    ./kickstart.sh

(You will be prompted with sudo password)

To make sure all is good, ssh to the VM and run `serve`:

    vagrant ssh
    (vagrant) serve

Now open your browser and visit `http://localhost:4000` and you should see
a shiny new installation!


Usage
-----

A new project will be created during installation, outside your VM, under `~/Projects/invenio`. This folder will contain the git sources that you will develop on.

    cd ~/Projects/invenio/invenio
    git checkout -b my-dev-branch
    # edit edit save

When `serve` is running inside the VM, any changes you make to Invenio/INSPIRE sources under `~/Projects/invenio` will be automatically copied. So you just need to reload the web-page.

To run commands such as `bibsched` or `inveniocfg`, you need to ssh into the VM.

    cd ~/src/invenio-vm
    vagrant ssh
    (vagrant) bibsched


Configure
---------

You can configure the VM parameters and more inside the `provisioning` folder of `invenio-vm` repository:

    cd ~/src/invenio-vm/provisioning

Inside this folder you will find all the setup scripts as well as the Invenio config. For example, the `invenio-local.conf` (which is recommended to change)

    cd ~/src/invenio-vm/provisioning/files
    vim invenio-local.conf

Enjoy!
