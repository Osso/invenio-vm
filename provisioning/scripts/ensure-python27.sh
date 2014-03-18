#!/bin/sh

# Ensure python2.7 is installed
which python2.7 > /dev/null
if [ $? -ne 0 ]; then
    echo emerge python:2.7
fi

# Ensure python2.7 is select
if [ "$(python -V 2>&1)" != "$(python2.7 -V 2>&1)" ]; then
    eselect python set python2.7
fi


