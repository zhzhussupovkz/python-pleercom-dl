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

import urllib
import urllib2
import json
import base64
import os
import time

class PleerApi:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.token_url = 'http://api.pleer.com/token.php'
        self.api_url = 'http://api.pleer.com/index.php'
        self.exp = time.time()
        self.get_access_token()

    # get access token from server
    def get_access_token(self):
        base64str = base64.encodestring('%s:%s' % (self.login, self.password)).replace('\n', '')
        url = self.token_url
        data = 'grant_type=client_credentials'
        req = urllib2.Request(url, data)
        req.add_header('Authorization', "Basic %s" % base64str)
        req.add_header('Host', 'api.pleer.com')
        try:
            resp = urllib2.urlopen(req)
            if resp.getcode() == 200:
                page = json.loads(resp.read())
                self.access_token = page.get('access_token')
                resp.close()
            else:
                print "Server response code: %s" % resp.getcode()
        except Exception, e:
            print "Error: unable to obtain access token"
            exit()

    # send request to server
    def send_request(self, api_method, query):
        if time.time() > self.exp + 3600:
            self.get_access_token
            self.exp = time.time()
        required = {'access_token' : self.access_token, 'method' : api_method }
        query.update(required)
        data = urllib.urlencode(query)
        req = urllib2.Request(self.api_url, data)
        resp = urllib2.urlopen(req)
        if resp.getcode() == 200:
            try:
                page = json.loads(resp.read())
                resp.close()
                return page
            except:
                resp.close()
                return False
        else:
            print "Server response code: %s" % resp.getcode()

    # search track
    def search(self, query = 'music', page = 1, result = 10, quality = 'all'):
        query_args = {'query' : query, 'page' : page, 'result_on_page' : result, 'quality' : quality}
        json = self.send_request('tracks_search', query_args)
        if json:
            return json.get('tracks')

    # get track download link
    def get_download_link(self, track_id, reason = 'save'):
        query = {'track_id' : track_id, 'reason' : reason}
        json = self.send_request('tracks_get_download_link', query)
        if json:
            return json.get('url')

    # download track
    def download(self, directory = 'music', query = 'music', page = 1, result = 10, quality = 'all'):
        tracks = self.search(query=query, page=page, result=result, quality=quality)
        print "Found %s tracks for search query: %s" % (len(tracks), query)
        if len(tracks) > 0:
            for k, t in tracks.iteritems():
                track_id = t.get('id')
                artist = t.get('artist').replace(' ', '_')
                name = t.get('track').replace(' ', '_')
                track_name = artist + '-' + name
                link = self.get_download_link(track_id)
                try:
                    resp = urllib2.urlopen(link)
                    if resp.getcode() == 200:
                        ext = (link.split('/')[-1]).split('.')[-1]
                        filename = './'+ directory + '/' + track_name + '.' + ext
                        if not os.path.exists(os.path.dirname(filename)):
                            os.makedirs(os.path.dirname(filename))
                        size = resp.info().getheaders('Content-Length')[0]
                        print "Starting downloading track: %s.%s. Size: %s bytes" % (track_name, ext, size)
                        f = open(filename, "wb")
                        f.write(resp.read())
                        f.close()
                        print "Track %s: OK" % filename
                    else:
                        print "Track %s: NOK. Server response code: %s" % (filename, resp.getcode())
                except:
                    print "Cannot download track %s: NOK." % filename
                    pass
