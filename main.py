import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template("bloghtml/blog.html")
        self.response.write(template.render())


class SecretHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<p>You have found the secret page</p>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/secret', SecretHandler)
], debug=True)
