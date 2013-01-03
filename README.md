ConfigParserExtend
==================

## Python 2.X ConfigParser module is inconvenient.

This module is a little bit extend the default ConfigParser module.

###How to use

	>>> from ConfigParserExtend import *
	>>> CP = ConfigParserExtend("server.conf")
	>>> ConfigParse = CP.ReturnConfigDict()

	>>> ConfigParse["Server"]["IP"]
	192.168.0.1

