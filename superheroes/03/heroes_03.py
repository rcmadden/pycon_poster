from flask import Flask, render_template, request
from werkzeug.debug import DebuggedApplication
from marvel_characters import character_info, character_images
import random

app = Flask(__name__)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

heroes = list(character_images.keys())
real_name = sorted(character_images.values())
# right_answers = 0
# wrong_answers = 0
right_answers = set()
wrong_answers = set()


@app.route('/')
def index():
    random_hero = random.choice(list(character_images.keys()))
    heroes = character_images.keys()
    return render_template('index.html', random_hero=random_hero, character_images=character_images, heroes=heroes, character_info=character_info)


@app.route('/question')
def show_question():
    random_hero = random.choice(list(character_images.keys()))
    heroes = character_images.keys()
    return render_template('question.html', random_hero=random_hero, character_images=character_images, heroes=heroes, character_info=character_info)


@app.route('/answer', methods=['POST'])
def show_answer():
    global right_answers # python 3 needs global keyword to recognize variables
    global wrong_answers
    random_hero = random.choice(list(character_images.keys()))
    while True:
        random_hero = random.choice(heroes)
        if random_hero not in right_answers:
            play_again = ''
            break
    answer = request.form['answer']
    previous_hero = request.form['random_hero']
    previous_hero_real_name = character_info[previous_hero]['Real Name']
    if answer == previous_hero_real_name:
        # right_answers += 1
        right_answers.add(random_hero)
    else:
        # wrong_answers += 1
        wrong_answers.add(random_hero)
    return render_template('answer.html', random_hero=random_hero, character_images=character_images, heroes=heroes, character_info=character_info, answer=answer, previous_hero=previous_hero, real_name=real_name, previous_hero_real_name=previous_hero_real_name, right_answers=len(right_answers), wrong_answers=len(wrong_answers), total=len(heroes))

if __name__ == "__main__":
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
