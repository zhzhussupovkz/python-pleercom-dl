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
import argparse
import datetime

login = "your login"
password = "your password"

desc = "Command-line tool for downloading music from https://www.pleer.com\n"
desc += "Copyright (c) %s Zhussupov Zhassulan zhzhussupovkz@gmail.com\n" % datetime.datetime.now().year
desc += "While using this program, get API login, password from https://www.pleer.com"

parser = argparse.ArgumentParser(description=desc)
parser.add_argument("-q", "--query", help = "search for music by search term", default = "music")
parser.add_argument("-d", "--dir", help = "folder, which will be downloaded music files", default = "music")
parser.add_argument("-p", "--page", help = "specify result page(index). starts from 1", type = int, default = 1)
parser.add_argument("-r", "--result", help = "number of tracks per page", type = int, default = 10)
parser.add_argument("-y", "--quality", help = "track's quality", default = "all", choices = ['all', 'bad', 'good', 'best'])

args = parser.parse_args()
pleer = PleerApi(login, password)
pleer.download(directory=args.dir, query=args.query, page=args.page, result=args.result, quality=args.quality)
