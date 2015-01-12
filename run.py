#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from pleer_api import PleerApi

login = "login"
password = "password"
pleer = PleerApi(login, password)
pleer.download(query="It's A Sin", result=1, quality='best')
