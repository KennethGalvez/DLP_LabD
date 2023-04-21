import re
from postfix import *
from afn import *

def tokens(filename):
    # Función para obtener los tokens del archivo
    rege = r'let\s+([a-zA-Z0-9_-]+)\s+=\s+"([^"]*)"'
    with open(filename, 'r') as f:
        content = f.read()
    tonkensito = re.findall(rege, content)
    tokens = {name: {'regex': regex} for name, regex in tonkensito}
    return tokens

def convert_to_afn(regex, counter):
    # Función para convertir una expresión regular a un AFN
    exp = convertExpression(len(regex))
    # Postfix
    exp.RegexToPostfix(regex)
    if exp.ver:
        postfix = exp.res
        # AFN
        afn = PostifixToAFN(postfix=postfix, counter=counter)
        # método para convertir AFN
        afn.conversion(name)
        counter = afn.counter
        almacen_de_afns.append((name, afn))
    return counter

def simulate_string(mega_automata, string):
    # Función para simular una cadena en el AFN final y obtener el resultado
    return mega_automata.simular(string)

# archivo yalex
archivo = 'ya.lex'

# Obtener los tokens del archivo
tokens = tokens(archivo)

# Crear una lista para almacenar los AFN
almacen_de_afns = []
counter = -1

# creamos un AFN por cada token
for name, token in tokens.items():
    if 'regex' in token:
        regex = token['regex']
        counter = convert_to_afn(regex, counter)

tokens_nuevo = []

# Crear una nueva lista de tokens con las expresiones regulares modificadas
for name, token in tokens.items():
    if 'regex' in token:
        tokens_nuevo.append((name, token['regex'], True))
    else:
        operandos = []
        split = re.findall('\w+|[+*?()|.]', token)
        operandos.extend(split)

        for i, element in enumerate(operandos):
            for afn in almacen_de_afns:
                if element == afn[0]:
                    operandos[i] = "(" + afn[1] + ")"
        regex_n = ''.join(operandos)

        tokens_nuevo.append((name, regex_n, False))

# Por cada token compuesto en tokens creamos un AFN
for name, token, is_simple in tokens_nuevo:
    if not is_simple:
        counter = convert_to_afn(token, counter)

# Crear una lista con solo los AFN
chiquito = []
for afn in almacen_de_afns:
    chiquito.append(afn[1])

# Instancia de clase para convertir a AFN
mega_automata = PostifixToAFN(counter=counter, afns=chiquito)

# Unir todos los AFN y graficarlos
mega_automata.union("mega")
counter = mega_automata.counter

# Imprimir pruebas de simulación de cadenas
print("\nSimulacion")
print(simulate_string(mega_automata , "1"))
print(simulate_string(mega_automata , "b"))

"""
# -*- coding: utf-8 -*-
from afn import PostifixToAFN 
import json
import argparse

def cargar_afns():
    with open('afns.json', 'r') as f:
        afns_dict = json.load(f)
    afns = []
    for nombre, (afn, alfabeto) in afns_dict.items():
        afns.append(((nombre, alfabeto), afn))
    return afns

def cargar_afn_final():
    with open('afn_final.json', 'r') as f:
        afn_final_dict = json.load(f)
    return afn_final_dict['afn'], afn_final_dict['alfabeto']

def simular_palabras(afns, afn_final, palabras):
    resultado_verificaciones = []
    for palabra in palabras:
        valor = afn_final.simular_cadena(palabra)
        try:
            if valor == False:
                resultado_verificaciones.append(
                    "'" + palabra + "'" + " --> No se reconoce")
            if valor[0] == True:
                for afn in afns:
                    if valor[1] in afn[1].ef:
                        resultado_verificaciones.append(
                            "'" + palabra + "'" + " --> " + str(afn[0][0]).upper())
                        break
        except:
            pass
    return resultado_verificaciones

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('archivo', help='nombre del archivo a resolver')
    args = parser.parse_args()

    # cargar AFNs y AFN final desde archivos JSON
    afns = cargar_afns()
    afn_final = cargar_afn_final()

    # leer palabras del archivo
    with open(args.archivo, 'r') as f:
        contenido = f.read()
        palabras = contenido.split()

    # simular las palabras en los AFNs
    resultado_verificaciones = simular_palabras(afns, afn_final, palabras)

    # escribir el resultado en el archivo file_resuelto.txt
    with open('file_resuelto.txt', 'w') as f:
        f.write(contenido)
        f.write('\n\n')
        for resultado in resultado_verificaciones:
            f.write(resultado)
            f.write('\n')
    print('\nArchivo resuelto con exito')

"""