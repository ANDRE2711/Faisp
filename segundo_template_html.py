from flask import flask, render_template
app = Flask (__name__)
@app.route ('/')
def index () :
    return '<html><body><h1>Hello Word</h1></body></html>'
@app.route ('/home')
def home ():
    return_template ('index.html')
    if __name__== '__maim__':
        app.run (debug = True)
