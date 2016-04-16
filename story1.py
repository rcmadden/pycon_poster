from flask import Flask, request
from werkzeug.debug import DebuggedApplication
import characters


app = Flask(__name__)
# TODO: Python 2/3 compatible? if python 2.x app.debug=True if python 3 use werkzeug.debug, if error no debugger
# app.debug=True # python 2.x
# python 3 error TypeError: can't use a string pattern on a bytes-like object
# http://stackoverflow.com/questions/10364854/flask-debug-true-does-not-work-when-going-through-uwsgi
app.wsgi_app = DebuggedApplication(app.wsgi_app, True) # python 3.x

story = ''' One day {CHARACTER} was feeling {adjective} and then decided to {verb}  '''
parts = ['CHARACTER', 'adjective', 'verb']

def parts_form(parts):
    markup = '<form action="">'
    options = ['<option value="{name}">{name}</option>'.format(name=name) for name in characters.characters.keys()]
    picker = '<select name="CHARACTER">' + '\n' .join(options) + '</select>'
    for part in parts:
        if part == 'CHARACTER':
            markup = markup + '<p><label>Pick your favorite character' + picker + '</label></p>'
        else:
            markup = markup + '<p><label>{part}<input name="{part}"></label></p>'.format(part=part)
    submit = '<input type = "submit" name="filledout">'
    return markup + submit + '</form>'


@app.route('/')
def home():
    if request.args.get("filledout"):
        input = {}
        for part in parts:
            input[part] = request.args.get(part)
        return story.format(**input) # keyword args
    else:
        return parts_form(parts)


@app.route('/<yourname>/')
def show_visitor_name(yourname):
    return '<h1>Hello {}</h1>'.format(yourname)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run()

