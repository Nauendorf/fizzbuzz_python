import platform as p
import os as o


class SystemInfo(object):
    info = {}

    def __init__(self):
        self.info = {'platform': p.platform(), 'release_version': p.uname()}

    def get(self):
        return self.info


system = SystemInfo()
print(system.get().__str__().replace(',', '\n'))


