import re # https://docs.python.org/2/library/re.html

from flask import Flask, request, render_template
from werkzeug.debug import DebuggedApplication

from madlbs import characters_all as characters

app = Flask(__name__)
# TODO: Python 2/3 compatible? if python 2.x app.debug=True if python 3 use werkzeug.debug, if error no debugger
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
        return render_template('index_1b.html', parts=basic_parts, action='/', characters=characters, story_template=None)
    else:
        name = request.args['CHARACTER']
        url = characters.character_images[name]
        story_template = request.args.get('story_template')
        story = story_template.format(**request.args) # keyword args
        # return story + picture + '\n' + next_link
        return render_template('custom_story.html', CHARACTER=name, url=url, story=story)


@app.route('/Make_your_own/')
def make_your_own():
    if request.args.get("filledout"):
        custom_story_template = request.args.get('story_template')
        custom_parts = find_parts(custom_story_template)
        return render_template('index_1b.html', parts=custom_parts, action='/', characters=characters, story_template=custom_story_template)
    else:
        return render_template('Make_your_own.html')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run(debug=True)
