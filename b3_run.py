#!/usr/bin/env python
#
# BigBrotherBot(B3) (www.bigbrotherbot.com)
# Copyright (C) 2005 Michael "ThorN" Thornton
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

# This section is DoxuGen information. More information on how to comment your code
# is available at http://wiki.bigbrotherbot.net/doku.php/customize:doxygen_rules
## @mainpage
# <p>This documentation is the Bigbrotherbot Reference for developers.</p>
# <p>If you are a B3 developer, please document your classes, methods properly.<br />
# More information on how to document code can be found on http://wiki.bigbrotherbot.net/doku.php/customize:doxygen_rules</p>
# <p><a href="http://doc.bigbrotherbot.net">doc.bigbrotherbot.net</a></p>
## @file
# The entry point to run B3

__author__  = 'ThorN'
__version__ = '1.1.1'

try:
    import b3.run
except:
    print("Sorry, cannot continue, B3 is not yet compatible with python version 3 and is not compatible with versions older than 2.6!")
    exit(1)

def main():
    b3.run.main()

if __name__ == '__main__':
    main()