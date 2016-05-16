from flask import Flask, render_template
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

character_images = {
    'Spider-Man': 'http://x.annihil.us/u/prod/marvel/i/mg/6/60/538cd3628a05e.jpg',
    'Captain Marvel': 'http://x.annihil.us/u/prod/marvel/i/mg/6/30/537ba61b764b4.jpg',
    'Hulk': 'http://x.annihil.us/u/prod/marvel/i/mg/e/e0/537bafa34baa9.jpg',
    'Iron Man': 'http://i.annihil.us/u/prod/marvel/i/mg/c/60/55b6a28ef24fa.jpg',
    'Captain America': 'http://x.annihil.us/u/prod/marvel/i/mg/9/80/537ba5b368b7d.jpg',
    'Wolverine': 'http://i.annihil.us/u/prod/marvel/i/mg/9/00/537bcb1133fd7.jpg',
    'Ant Man': 'http://i.annihil.us/u/prod/marvel/i/mg/5/d0/54ad72b6084a0.jpg'
}


@app.route('/')
def index():
    heroes = character_images.keys()
    return render_template('index.html', character_images=character_images, heroes=heroes)


@app.route('/<name>/')
def projects(name):
    return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
