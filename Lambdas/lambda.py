import requests
import json
pokemon = "ditto"
def pokeApi():

    #Esta es una cadena de formato
    #La cual permite incrsutar valores dentro de una cadena de texto
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response_API = requests.get(url)
    if response_API.status_code == 200:
        #print(response_API.status_code)
        data = response_API.text
        parse_json = json.loads(data)
        active_case = parse_json['species']['name']
        resultado = mayuscula(pokemon)
        print("Aqui esta la respuesta: " + "https://pokeapi.co/api/v2/pokemon/",resultado)
        print("Sus caracteristicas: ", active_case.upper())
    else:
        print("No fue posible acceder a la API. ", response_API.status_code)

def mayuscula(pokemon):
    pokemonUpper= pokemon.upper()
    return pokemonUpper
    
pokeApi()