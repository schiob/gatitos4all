import webbrowser
import sys

def main():
    URL = 'http://cataas.com/cat/gif/says/'
    webbrowser.open('{}{}'.format(URL, sys.argv[0]))

# Si el archivo es el hilo principal que se ejecute si no pos no juejuejue
if __name__ == '__main__':
    main() # Corre la función principal
