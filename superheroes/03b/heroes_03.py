from flask import Flask, render_template, request
from werkzeug.debug import DebuggedApplication
from marvel_characters import character_info, character_images
import random

app = Flask(__name__)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

heroes = character_images.keys()
real_name = character_images.values()
# right_answers = 0

# counter = 0
# def score_counter(count):
#     if count != 0:
#        count = count + 1
#        #current_count = score_counter(current_count)
#     else:
#        count = count + 0
#     return count

# from jinja2 import Template
# t = '''{% set correct_count=correct_count or 0 %}Count= {{ correct_count }}'''
# template = Template(t)
# print(template.render(correct_count=1))
# print(template.render())

@app.route('/')
def index():
    return render_template('index.html', heroes=heroes, character_info=character_info, character_images=character_images)


@app.route('/question')
def show_question():
    random_hero = random.choice(list(character_images.keys()))
    heroes = character_images.keys()
    return render_template('answer.html', random_hero=random_hero, character_images=character_images, heroes=heroes, character_info=character_info)

right_answers = 0
@app.route('/answer', methods=['POST'])
def show_answer():
    random_hero = random.choice(list(character_images.keys()))
    answer = request.form['answer']
    previous_hero = request.form['random_hero']
    previous_hero_real_name = character_info[previous_hero]['Real Name']
    # right_answers = int(request.form['correct_count'])
    if answer == previous_hero:
        right_answers += 1
    else:
        right_answers += 0
    # if right_answers > 0:
    #     print(score_counter(right_answers))
    return render_template('answer.html', random_hero=random_hero, character_images=character_images, heroes=heroes, character_info=character_info, answer=answer, previous_hero=previous_hero, real_name=real_name, previous_hero_real_name=previous_hero_real_name, right_answers=right_answers)


if __name__ == "__main__":
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
