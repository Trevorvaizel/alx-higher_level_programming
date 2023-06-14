
import hidden_4

def dir_print():
    definitions = dir(hidden_4)
    definitions.sort()
    for n in definitions:
        if not n.startswith('_'):
            print(n)

dir_print()
