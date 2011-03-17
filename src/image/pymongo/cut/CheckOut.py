# encoding: utf-8
'''
Created on 2011-3-17

@author: leishouguo
'''

#!/usr/bin/env python

import sys
from subprocess import *

#
# subprocess.check_output() is new in Python 2.7
#
def _check_output(*popenargs, **kwargs):
    r"""Run command with arguments and return its output as a byte string.

If the exit code was non-zero it raises a CalledProcessError. The
CalledProcessError object will have the return code in the returncode
attribute.

The arguments are the same as for the Popen constructor. Example:

>>> check_output(["ls", "-l", "/dev/null"])
'crw-rw-rw- 1 root root 1, 3 Oct 18 2007 /dev/null\n'

The stdout argument is not allowed as it is used internally.
To capture standard error in the result, use stderr=STDOUT.

>>> check_output(["/bin/sh", "-c",
... "ls -l non_existent_file ; exit 0"],
... stderr=STDOUT)
'ls: non_existent_file: No such file or directory\n'
"""
    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')
    process = Popen(stdout=PIPE, *popenargs, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = popenargs[0]
        raise CalledProcessError(retcode, cmd)
    return output

if __name__ == '__main__':
    try:
        output = _check_output(["ls", "-l"])
        print output,
        
        imagefile = "/usr/local/src/linux-soft/image/s290x360_mLbmkJbmiLcozLcG.jpg"
        output = _check_output(['identify', '-format', '%m %w %h %Q', imagefile])
        print output,
    except KeyboardInterrupt:
        print 'Aborted.'
    except (OSError, CalledProcessError), e:
        print e