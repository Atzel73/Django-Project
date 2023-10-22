from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.http import HttpResponseRedirect
from django.urls import reverse

def inicio(request):
    return render(request, 'inicio.html')

def contacto(request):
    return render(request, 'contact.html')

def getURL(request):
    if request.method == 'POST':
        poke_text = request.POST.get('texto')
        url = f'https://pokeapi.co/api/v2/pokemon/{poke_text}'

        # Aplicar la corrección de texto
        if poke_text.isupper():
            poke_text = poke_text.lower()
        
        r = requests.get(url)

        if r.status_code == 200:
            data = json.loads(r.text)
            active_case = data['name']
            second_case = data['id']
            image_case = data['sprites']['other']['official-artwork']['front_default']
            corrected_url = separateURL(url)
            return render(request, 'result_template.html', {'active_case': active_case, 'second_case': second_case, 'corrected_url': corrected_url, 'image_case': image_case})
        else:
            return render(request, 'error_template.html')

    return render(request, 'result_template.html')

def separateURL(pokemon):
    pokeAfter = pokemon.split("/")
    frase = pokeAfter[-1]
    pokemonUpper = frase.upper()

    
    sendText = pokemon.replace(frase, pokemonUpper)
    return sendText
