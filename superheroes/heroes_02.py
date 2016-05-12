from flask import Flask, render_template
from werkzeug.debug import DebuggedApplication
from marvel_characters import character_info, character_images

app = Flask(__name__)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route('/')
def index():
    heroes = character_images.keys()
    return render_template('index_02.html', heroes=heroes, character_info=character_info, character_images=character_images)

if __name__ == "__main__":
    app.run(debug=True)
