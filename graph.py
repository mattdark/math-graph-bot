import re
import numpy as np
import matplotlib.pyplot as plt

def graph(string, x_range):
    replacements = {
        'sen' : 'np.sin',
        'cos' : 'np.cos',
        'tan' : 'np.tan',
        'exp': 'np.exp',
        'raiz': 'np.sqrt',
        '^': '**',
    }
    allowed_words = [
        'x',
        'sen',
        'cos',
        'tan',
        'raiz',
        'exp',
    ]
    ''' evaluates the string and returns a function of x '''
    # find all words and check if all are allowed:
    for word in re.findall('[a-zA-Z_]+', string):
        if word not in allowed_words:
            raise ValueError(
                '"{}" is forbidden to use in math expression'.format(word)
            )

    for old, new in replacements.items():
        string = string.replace(old, new)

    x = np.array(x_range)
    y = eval(string)
    plt.plot(x, y)
    plt.savefig('graph.png', bbox_inches='tight')
