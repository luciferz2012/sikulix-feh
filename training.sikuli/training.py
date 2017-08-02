from sys import path as lib_path
from os import path

parent_path = path.abspath(path.join(lib_path[0], '..'))
lib_path.append(parent_path)

import feh

feh.commons += []

from sys import argv

def main():
    print(argv)
    for i in range(64 * 64):
        feh.findClick(feh.commons)
        feh.auto()

if __name__ == '__main__':
    main()