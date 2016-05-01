import importlib
import reloader as reloader
from flask import Flask, request, render_template
from werkzeug.debug import DebuggedApplication
import characters_all as characters
import re # https://docs.python.org/2/library/re.html
from xml.sax.saxutils import quoteattr


app = Flask(__name__)
# TODO: Pyth6on 2/3 compatible? if python 2.x app.debug=True if python 3 use werkzeug.debug, if error no debugger
# app.debug=True # python 2.x
# python 3 error TypeError: can't use a string pattern on a bytes-like object
# http://stackoverflow.com/questions/10364854/flask-debug-true-does-not-work-when-going-through-uwsgi
app.wsgi_app = DebuggedApplication(app.wsgi_app, True) # python 3.x

basic_story_template = ''' One day {CHARACTER} was feeling {adjective} and then decided to {verb}  '''
basic_parts = ['CHARACTER', 'adjective', 'verb']



test_input = '''
This is my story with a {noun} and a {verb}
'''
def find_parts(story_template):
    '''
    >>> find_parts(test_input)
    ['noun', 'verb']
    '''
    # cribbed from:
    # https://docs.python.org/2/library/re.html#finding-all-adverbs

    # [abc]+ means one or more of a, b, or c
    # [^abc]+ means one or more of _not_ a, b, nor c
    # \{[^}]+\} means: a { followed by one-or-more not-} followed by }
    slots = re.findall(r"\{[^}]+\}", story_template)

    # '{noun}'[1:-1] => 'noun'
    return [slot[1:-1] for slot in slots]





@app.route('/')
def basic_story():
    if request.args.get("filledout") is None:
        return render_template('index_1.html', parts=basic_parts, action='/', characters=characters, story_template=None)
    else:
        story, picture = process_story_form(request.args, basic_parts, basic_story_template)
        next_link = '<p><a href="Make_your_own">Make your own</a></p>'
        url_query = story + picture + '\n' + next_link
        # return render_template('index_1.html', url_query=url_query)
        return story + picture + '\n' + next_link


def process_story_form(args, parts, story_template):
    input = {}
    for part in parts:
        input[part] = args.get(part)
    name = input['CHARACTER']
    url = characters.character_images[name]
    picture = '<img src="{url}" alt="{CHARACTER}">'.format(url=url, CHARACTER=name)
    story = story_template.format(**input) # keyword args
    return story, picture


@app.route('/Make_your_own/')
def make_your_own():
    if request.args.get("filledout"):
        custom_story_template = request.args.get('story_template')
        return parts_form(find_parts(custom_story_template), action='/custom/', story_template=custom_story_template)
    else:
        submit = '<input type = "submit" name="filledout">'
        story_form = '<form action=""><textarea rows="10" cols="50" name="story_template">Once upon a time ...</textarea>' + submit + '</form>'
        return story_form

@app.route('/custom/')
def custom_story():
    if request.args.get("filledout") is None:
        custom_story_template = request.args.get('story_template')
        custom_parts = find_parts(custom_story_template)
        return parts_form(custom_parts, action='/', story_template=custom_story_template)
    else:
        custom_story_template = request.args.get('story_template')
        custom_parts = find_parts(custom_story_template)
        story, picture = process_story_form(request.args, custom_parts, custom_story_template)
        return story + picture


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run()

