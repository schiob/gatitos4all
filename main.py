"""Twittea gifs de gatitos en un intervalo determinado de tiempo.

Uso:

    python main.py
"""

import urllib.request
import urllib.parse
import re
import tweepy, time
import sys
import requests
import os

def twitter_api():
	# Obtén tus propias credenciales del API de Twitter y ponlas aquí.
	# https://apps.twitter.com/
	CONSUMER_KEY = ""
	CONSUMER_SECRET = ""
	ACCESS_KEY = ""
	ACCESS_SECRET = ""
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	return api


def tweet_image(url):
	# Toma el response del URL seleccionado y lo manda como status a Twitter.
	# Sólo testeado con imágenes y gifs.
	api = twitter_api()
	filename = 'temp.gif'
	request = requests.get(url, stream=True)
	if request.status_code == 200:
		with open(filename, 'wb') as image:
			for chunk in request:
				image.write(chunk)

		api.update_with_media(filename)
		os.remove(filename)
	else:
		print("Unable to download image")
		tweet_image(url)

def main():
			
	url = "http://cataas.com/cat/gif"
	
	while True:
		# Loop principal.
		# Manda status con contenido.
		tweet_image(url)
		# Imprime timestamp a consola de cuando fue enviado.
		print("[" + time.ctime() + "] - Random cat was sent!")
		# Espera una cantidad determinada en segundos para reiniciar el loop.
		time.sleep(1800)


# Si el archivo es el hilo principal que se ejecute si no pos no juejuejue
if __name__ == '__main__':
	main() # Corre la función principal
