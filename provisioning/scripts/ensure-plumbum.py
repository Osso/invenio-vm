#!/usr/bin/env python

print('* checking for Plumbum...')
try:
    import plumbum
except ImportError:
    import subprocess
    print('   installing Plumbum')
    subprocess.check_call('pip install plumbum', shell=True)
else:
    print('   detected')