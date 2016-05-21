from flask import Flask, render_template, request
from werkzeug.debug import DebuggedApplication
from marvel_characters import character_info, character_images
import decendents_characters
import random

app = Flask(__name__)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

heroes = list(character_images.keys())
real_name = sorted(character_images.values())
right_answers = set()


@app.route('/')
def index():
    return render_template('index.html', heroes=heroes, character_info=character_info, character_images=character_images)


@app.route('/question')
def show_question():
    random_hero = random.choice(list(character_images.keys()))
    heroes = character_images.keys()
    return render_template('answer.html', random_hero=random_hero, character_images=character_images, heroes=heroes, character_info=character_info)

@app.route('/answer', methods=['POST'])
def show_answer():
    global right_answers
    if len(right_answers) == len(heroes):
        raise NotImplementedError
    while True:
        random_hero = random.choice(heroes)
        if random_hero not in right_answers:
            break
    answer = request.form['answer']
    previous_hero = request.form['random_hero']
    previous_hero_real_name = character_info[previous_hero]['Real Name']
    print(answer, previous_hero_real_name)
    if answer == previous_hero_real_name:
        # right_answers += 1
        right_answers.add(random_hero)
    # else:
    #     right_answers += 0
    print(right_answers)
    return render_template('answer.html', random_hero=random_hero, character_images=character_images, heroes=heroes, character_info=character_info, answer=answer, previous_hero=previous_hero, real_name=real_name, previous_hero_real_name=previous_hero_real_name, right_answers=len(right_answers))


worlds = {'heroes':(character_images, character_info, 'Real Name'),
          'decendents':(decendents_characters.character_images, decendents_characters.character_info, 'Parents')}
@app.route('/question/<world>')
def show_question2(world):
    images, info, identity = worlds[world]
    characters = list(info.keys())
    random_character = random.choice(characters)
    return render_template('answer.html', random_hero=random_character, character_images=images, heroes=characters, character_info=info)

@app.route('/answer/<world>', methods=['POST'])
def show_answer2(world):
    global right_answers
    images, info, identity = worlds[world]
    characters = list(info.keys())
    if len(right_answers) == len(characters):
        raise NotImplementedError
    while True:
        random_character = random.choice(characters)
        if random_character not in right_answers:
            break
    answer = request.form['answer']
    # TODO: change random hero
    previous_character = request.form['random_hero']
    previous_character_secret = info[previous_character][identity]
    print(answer, previous_character_secret)
    if answer == previous_character_secret:
        # right_answers += 1
        right_answers.add(random_character)
    # else:
    #     right_answers += 0
    print(right_answers)
    return render_template('answer.html', random_hero=random_character, character_images=images, heroes=characters, character_info=info, answer=answer, previous_hero=previous_character, real_name=real_name, previous_hero_real_name=previous_character_secret, right_answers=len(right_answers))

if __name__ == "__main__":
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
