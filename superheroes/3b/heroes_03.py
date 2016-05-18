from flask import Flask, render_template, request
from werkzeug.debug import DebuggedApplication
from marvel_characters import character_info, character_images
import random

app = Flask(__name__)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route('/')
def index():
    heroes = character_images.keys()
    return render_template('index.html', heroes=heroes, character_info=character_info, character_images=character_images)


@app.route('/question')
def show_question():
    random_hero = random.choice(list(character_images.keys()))
    heroes = character_images.keys()
    return render_template('index.html', random_hero=random_hero, character_images=character_images, heroes=heroes, character_info=character_info)


@app.route('/answer', methods=['POST'])
def show_answer():
    random_hero = random.choice(list(character_images.keys()))
    heroes = character_images.keys()
    real_name = character_images.values()
    answer = request.form['answer']
    previous_hero = request.form['random_hero']
    # raise Exception
    # if request.form['answer'] == request.form['random_hero']:
    #    correct = True
    # else:
    #    correct = False
    return render_template('index.html', random_hero=random_hero, character_images=character_images, heroes=heroes, character_info=character_info, answer=answer, previous_hero=previous_hero, real_name=real_name)


if __name__ == "__main__":
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
