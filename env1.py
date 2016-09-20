# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:37:49 2016

@author: Aaron
"""

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
from Translator3 import Translated

html = """
<html>
<body>
   <form method="get" action="">
        <textarea name='comm' value="%(comm)s" style="width: 600px; height: 100px;"></textarea><br />
        

        <p>
            <input type="submit" value="Submit">
        </p>
    </form>
<pre>
ORIGINAL  : %(OG)s<br>
TRANSLATED: %(comm)s<br>
WHAT I AM : %(what)s<br>
</pre>
</body>
</html>
"""
    #<p>
    #       Comment: <input type="hidden" name="age" value="%(age)s" style="width:600px;height:100px;">
    #    </p>
def application (environ, start_response):


#    # the environment variable CONTENT_LENGTH may be empty or missing
#    try:
#        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
#    except (ValueError):
#        request_body_size = 0
#
#    # When the method is POST the variable will be sent
#    # in the HTTP request body which is passed by the WSGI server
#    # in the file like wsgi.input environment variable.
#    request_body = environ['wsgi.input'].read(request_body_size)
#    d = parse_qs(request_body)


    # Returns a dictionary in which the values are lists
    d = parse_qs(environ['QUERY_STRING'])

    # As there can be more than one value for a variable then
    # a list is provided as a default value.
    comm = d.get('comm', [''])[0] # Returns the first age value

    # Always escape user input to avoid script injection
    comm = escape(comm)
    [trans, what] = Translated(comm)
    what_str = ''
    tp = 0
    for jk in what.values():
        what_str = what_str + ('I AM ' + str(jk) + (', '))
        tp += 1
    body1 = [
        '%s' % (trans)
    ]
    body1 = '\n'.join(body1)
    
    body2 = [
        '%s' % (what_str)
    ]
    body2 = '\n'.join(body2)
    
    #body = body1 + '\n' + 'What I Am: ' + body2
    
    response_body = html % { # Fill the above html template in
        'comm': body1,
        'what': body2,
        'OG': comm
    }

    status = '200 OK'

    # Now content type is text/html
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body.encode('utf-8')]

httpd = make_server('localhost', 8051, application)

# Now it is serve_forever() in instead of handle_request()
httpd.serve_forever()