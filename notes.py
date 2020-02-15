# import sys
#
#
# test = sys
#
#
# print([a for a in dir(test)])
# print([a for a in dir(test) if not a.startswith('__')])
# print(', '.join(i for i in dir(sys) if not i.startswith('__')))

import sys
import platform

def getsysinfo():
    return [a for a in dir(platform) if not a.startswith('__')
            and print(getattr(platform, a)
                      and print(a))]


print(getsysinfo())
