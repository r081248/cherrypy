import random
import string

import cherrypy

"""
when browser access index page, index function gets called and html string will be returned, browser renders
the html. User can send the length value and click on submit button.
HTTP GET <host>:<port>/generate?length=<value> gets passed to webserver.
generate function gets invoked. and length query parameter will be passed to generate function
"""


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="8" name="length" />
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, length="8"):
        return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())