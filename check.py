#!/usr/bin/env python2.7

from config import Config
import urllib2
from subprocess import check_output

def geturlcfg(url):
	response = urllib2.urlopen(url)
	return response.read()

def getchangelog(f):
	cfg = Config(f)
	commits = {'size': None,'lines': []}
	for m in cfg.master:
		if hasattr(m,'changelog'):
			commits['lines'].append(m['changelog'])
	commits['size'] = len(commits['lines'])
	return commits

Rchangelog = geturlcfg('https://raw.githubusercontent.com/amonstra/test/master/CHANGELOG')
with open('update','w') as resp:
	resp.write(Rchangelog),resp.close()

master = file('CHANGELOG')
remote = file('update')
LogL,LogR = getchangelog(master),getchangelog(remote)
if LogR['size'] > LogL['size']:
	print LogR['lines'][LogL['size']]
	n = check_output(['git','pull'])
	print n
else:
	print('teste')