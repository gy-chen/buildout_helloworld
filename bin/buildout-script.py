#!"C:\Python27\python.exe"

import sys
sys.path[0:0] = [
  'd:\\playground\\buildout\\helloworld_new\\eggs\\zc.buildout-2.9.4-py2.7.egg',
  'c:\\python27\\lib\\site-packages',
  ]

import zc.buildout.buildout

if __name__ == '__main__':
    sys.exit(zc.buildout.buildout.main())
