#!/usr/bin/env python2.7

from config import Config
import urllib2
from subprocess import check_output,call
from os import path
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

def gitZipRepo():
	call(['git','init'])
	call(['git','remote', 'add', 'origin', 'https://github.com/amonstra/test.git'])
	call(['git', 'fetch','--all'])
	call(['git','reset','--hard','origin/master'])

Rchangelog = geturlcfg('https://raw.githubusercontent.com/amonstra/test/master/CHANGELOG')
with open('update','w') as resp:
	resp.write(Rchangelog),resp.close()
master,remote = file('CHANGELOG'),file('update')
LogL,LogR = getchangelog(master),getchangelog(remote)
if LogR['size'] > LogL['size']:
	for commit in LogR['lines'][LogL['size']:]:
		print('new commit: '+commit)
	if not path.isdir('.git/'):
		gitZipRepo()
	call(['git','pull','origin','master'])
else:
	print('teste')