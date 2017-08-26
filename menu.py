import webbrowser
import sys


class menu:


    def eligeGato():
        print("GATOS BÁSICOS.")
        print("¿Cuál es el gato de tu elección?")
        print("1: Gato random.")
        print("2: Gato random con un filtro de búsqueda(sleepy, angry, drunk, cute, etc...).")
        print("3: Gif random de un gatito cutie.")
        print("4: Gato random con algún texto.")
        print("5: Gato random con un texto de tamaño y color a elegir.")
        print("6: Gato random con una etiqueta (cute, angry, etc.) y un texto.")
        print("0: Salir.")
        
        gato = int(input(""))
        
        if gato == 1 :
            webbrowser.open(menu.gatoRandom())
        elif gato == 2: 
            webbrowser.open(menu.gatoFilter())
        elif gato == 3: 
            webbrowser.open(menu.gatoGifRandom())
        elif gato == 4:
            webbrowser.open(menu.gatoRandomConTexto())
        elif gato ==5:
            webbrowser.open(menu.gatoCustomTexto())
        elif gato ==6:
            webbrowser.open(menu.gatoEtiquetaTexto())
        return gato
    
    def gatoRandom():
        url = 'http://cataas.com/cat'
        return url
    
    def gatoFilter():
        filtro = input("Filtro para tu kittie: ")
        url = "http://cataas.com/cat/" + filtro
        return url
	
    def gatoGifRandom():
        url = "http://cataas.com/cat/gif"
        return url
	
    def gatoRandomConTexto():
        texto = input("Texto para el kittie: ")
        url = "http://cataas.com/cat/says/" + texto 
        return url
    
    def gatoCustomTexto():
        texto = input("Texto para el kittie: ")
        size = input("Tamaño del texto: ")
        color = input("Color del texto: ")
        url = 'http://cataas.com/cat/says/'+ texto + '?size=:' + size + '&color=:' + color
        return url
    
    def gatoEtiquetaTexto():
        etiqueta = input("Etiqueta para el gatito: ")
        texto = input("Texto para el kittie: ")
        url = "http://cataas.com/cat/" + etiqueta + "/says/" + texto
        return url 

