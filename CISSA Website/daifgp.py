# This script handle factor graph processing requests from CyberSAGE client app
# The factor graph in libdai language should be put in POST data
# Author: Vu An Hoa

import io
from subprocess import Popen, PIPE

def application(environ, start_response):
    try:
        # the environment variable CONTENT_LENGTH may be empty or missing
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    # print request_body_size
    # When the method is POST the query string will be sent in the HTTP request body which is passed by the WSGI server in the file like wsgi.input environment variable.
    request_body = environ['wsgi.input'].read(request_body_size)
    # print request_body
    p = Popen(["daifgp"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output = p.communicate(input=request_body)[0];    
    # print output
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]

# The following is for testing purpose

def resp(status, response_headers):
    print status
    print response_headers

if __name__ == "__main__":
    testinput = io.open("test.fg", "r")
    print testinput
    environ = {}
    environ['CONTENT_LENGTH'] = 3132
    environ['wsgi.input'] = testinput
    print environ
    application(environ, resp)
