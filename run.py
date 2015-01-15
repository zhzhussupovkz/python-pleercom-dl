#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# The MIT License (MIT)

# Copyright (c) 2015 Zhassulan Zhussupov

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pleer_api import PleerApi
from optparse import OptionParser
import datetime

login = "login"
password = "password"

usage = "%prog [options]\n\n"
usage += "Command-line tool for downloading music from https://www.pleer.com\n"
usage += "Copyright (c) %s Zhussupov Zhassulan zhzhussupovkz@gmail.com\n" % datetime.datetime.now().year
usage += "While using this program, get API login, password from https://www.pleer.com"
option_parser = OptionParser(usage=usage, version="%prog 1.0")
option_parser.add_option("-q", "--query", help = "search for music by search term", default = "music")
option_parser.add_option("-d", "--dir", help = "folder, which will be downloaded music files", default = "music")
option_parser.add_option("-p", "--page", help = "specify result page(index). starts from 1", default = 1)
option_parser.add_option("-r", "--result", help = "number of tracks per page", default = 10)
option_parser.add_option("-y", "--quality", help = "quality (all, bad, good, best)", default = "all")
(options, args) = option_parser.parse_args()

pleer = PleerApi(login, password)
pleer.download(dir=options.dir, query=options.query, page=options.page, result=options.result, quality='best')
