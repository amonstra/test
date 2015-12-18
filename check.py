#!/usr/bin/env python2.7

from config import Config
import urllib2

def geturlcfg(url):
	response = urllib2.urlopen(url)
	return response.read()

def getchangelog(f):
	cfg = Config(f)
	commits = []
	for m in cfg.master:
		if hasattr(m,'changelog'):
			commits.append(m['changelog'])
	return len(commits)

f = file('CHANGELOG')
print len(commits)