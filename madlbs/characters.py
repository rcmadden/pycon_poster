'''characters -- Details about Descendants characters

ref: http://disney.wikia.com/wiki/Descendants

'''

character_lines = '''
Mal - (Dove Cameron) daughter of Maleficent.
Jay - (Booboo Stewart) the son of Jafar.
Evie - (Sofia Carson) daughter of the Evil Queen.
Carlos De Vil - (Cameron Boyce), the son of Cruella De Vil.
Prince Ben - (Mitchell Hope), son of Belle and the Beast and soon to be king of Auradon.
Princess Audrey - (Sarah Jeffery), daughter of Aurora and Prince Phillip.
Prince Chad Charming - (Jedidiah Goodacre), son of Cinderella and Prince Charming.
Lonnie - (Dianne Doan), daughter of Fa Mulan and Li Shang.
Jane - (Brenna D'Amico), daughter of the Fairy Godmother.
Doug - (Zachary Gibson), son of Dopey.
'''.strip().split('\n')

characters = dict(line.split(' - ') for line in character_lines)

character_images = {
    'Mal': 'http://vignette2.wikia.nocookie.net/disney/images/e/e8/Mal_full_body.png/revision/latest?cb=20150609200925',
    'Jay': 'http://vignette1.wikia.nocookie.net/disney/images/4/43/Jay_Auradon.jpg/revision/latest/scale-to-width-down/184?cb=20150807165512',
    'Evie': 'http://vignette2.wikia.nocookie.net/disney/images/d/d6/Evvie_full_body.jpg/revision/latest?cb=20150415015349'
    }
