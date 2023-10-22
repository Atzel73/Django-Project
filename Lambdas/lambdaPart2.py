from django.shortcuts import render
import requests
import json


def getURL():
    poke_text = "raichu"
    url = f'https://pokeapi.co/api/v2/pokemon/{poke_text}'
    r = requests.get(url)
    if r.status_code == 200:
     data = json.loads(r.text)
     active_case = data['name']
     second_case = data['id']
     image_case = data['sprites']['front_default']
     print("El pokemon es: ", active_case)
     print("Y su ID es: ", second_case)
     texto_corregido = separateURL(url)
     print("Aqui esta la URL corregida: ", texto_corregido)
     
    else:
        print("No fue posible conectar a la API. ")



def separateURL(pokemon):
    pokeAfter = pokemon.split("/")
    frase = pokeAfter[-1]
    pokemonUpper = frase.upper()

    
    sendText = pokemon.replace(frase, pokemonUpper)
    return sendText



def getLow(pokemon):  
    pokemonLow = pokemon.lower() 
    return pokemonLow
getURL()