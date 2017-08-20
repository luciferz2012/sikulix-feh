from sys import path as lib_path
from os import path

parent_path = path.abspath(path.join(lib_path[0], '..'))
lib_path.append(parent_path)

import feh

feh.commons += [
       Pattern("team 4, battle 5.png").similar(0.90),
       ]

def main():
    # for i in range(64):
    for i in range(64 * 64):
        feh.findClick(feh.commons)
        feh.auto()
        feh.close()

if __name__ == '__main__':
    main()