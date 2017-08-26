import webbrowser
import sys


from menu import menu


def main():
    a = menu.eligeGato()
    while (a!= 0): 
        a = menu.eligeGato()	

# Si el archivo es el hilo principal que se ejecute si no pos no juejuejue
if __name__ == '__main__':
    main() # Corre la función principal
