#!/usr/bin/python
import platform as p
import sys


class SystemInfo(object):
    info = {}

    def __init__(self):
        self.info = {'platform': p.platform(), 'release_version': p.uname()}

    def get(self):
        return self.info


system = SystemInfo()
if len(sys.argv) > 1:
    if sys.argv[1] == '--help':
        print("Helpful things!")
    else:
        print("Unexpected parameter...")
else:
    print(system.get().__str__().replace(',', '\n'))

