#!/usr/bin/env python

'''
	wploginchecker.py - Login Checker for Wordpress
	
	Copyright (c) 2011, Ruel Pagayon
	All rights reserved.

	Redistribution and use in source and binary forms, with or without
	modification, are permitted provided that the following conditions are met:
		* Redistributions of source code must retain the above copyright
		  notice, this list of conditions and the following disclaimer.
		* Redistributions in binary form must reproduce the above copyright
		  notice, this list of conditions and the following disclaimer in the
		  documentation and/or other materials provided with the distribution.
		* Neither the name of the author nor the names of its contributors 
		  may be used to endorse or promote products derived from this software 
		  without specific prior written permission.

	THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS "AS IS" AND ANY 
	EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
	DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, 
	INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT 
	LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, 
	OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF 
	LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE 
	OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
	ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import sys
import urllib2
import urllib
import os

def main(argv):
	'''
		Main function, exits if there's no filename argument
		or the path is invalid
	'''
	
	if len(argv) == 0:
		'''
			Check if the there's no filename argument
		'''
		print 'No filename for dictionary specified.'
		sys.exit()
	elif not os.path.isfile(argv[0]):
		'''
			Check if the file does not exist
		'''
		print '%s does not exist.' % argv[0]
		sys.exit()
	
	baseurl = 'http://ruel.me/blog'
	
	file = open(argv[0], 'r')
	for line in file:
		'''
			Read line by line
		'''
		user, passw = line.strip().split(':')
		
		data = urllib.urlencode({ 'log' : user, 'pwd' : passw, 'wp-submit' : 'Log+In' })
		response = urllib2.urlopen('%s/wp-login.php' % baseurl, data)
		html = response.read()
		
		if '<div id="login_error">' in html:
			'''
				Check if response HTML has error
			'''
			print '%s:%s - INVALID' % (user, passw)
		else:
			print '%s:%s - VALID' % (user, passw)
			save = open('valid.txt', 'a+')
			save.write("%s:%s\n" % (user, passw))
			save.close()
	
	file.close()
	

if __name__ == '__main__':
	main(sys.argv[1:])
