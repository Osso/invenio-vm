#!/bin/sh

# Ensure homebrew is installed
echo '* checking for Homebrew...'
which brew > /dev/null
if [ $? -ne 0 ]; then
    ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
else
    echo '   detected'
fi

echo '* checking for pip...'
which pip > /dev/null
if [ $? -ne 0 ]; then
    brew install python
else
    echo '   detected'
fi

echo '* checking for ruby (required by vagrant)...'
which ruby > /dev/null
if [ $? -ne 0 ]; then
    brew install ruby
else
    echo '   detected'
fi

echo '* checking for vagrant...'
which vagrant > /dev/null
if [ $? -ne 0 ]; then
    echo 'Please download and install vagrant'
    echo 'http://www.vagrantup.com/'
    exit 1
else
    echo '   detected'
fi

# Ensure plumbum is installed
python provisioning/scripts/ensure-plumbum.py
if [ $? -ne 0 ]; then
    print 'Failed to run plumbum installer'
    exit 1
fi

# Do stuff
python provisioning/scripts/kickstart.py
if [ $? -ne 0 ]; then
    print 'Failed to run kickstarter script'
    exit 1
fi

