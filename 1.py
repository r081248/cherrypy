import cherrypy
import random
import string
'''
cherrypy matches exposed function name with resource
ex: localhost:8080/ --> cherrypy webserves invokes index function
    localhost:8080/generate --> cherrypy webserver invokes generate function
'''
class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

    @cherrypy.expose
    def generate(self):
        return ''.join(random.sample(string.hexdigits, 8))

if __name__ == "__main__":
    cherrypy.quickstart(HelloWorld())