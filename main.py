# -*- coding: utf-8 -*-
import webbrowser
import sys

def main():
    URL = 'http://cataas.com/cat/gif/says/'
    if len(sys.argv) > 1:
        webbrowser.open('{}{}'.format(URL, ' '.join(sys.argv[1:])))
    else:
        webbrowser.open('{}{}'.format(URL, 'holi'))

# Si el archivo es el hilo principal que se ejecute si no pos no juejuejue
if __name__ == '__main__':
    main() # Corre la función principal
