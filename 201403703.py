
import time
import random

def reflex_agent(location, state):
    if state  == "SUCIO":
        return 'LIMPIO'
    elif location == 'A':
        return 'RIGHT'
    elif location == 'B':
        return 'LEFT'

# Se marcan los estados que se visitaron 
def visitar_estado(states, estados_visitados):
    if states[0] == 'A': #Si el agente está en la posición A
        if states[1] == 'SUCIO':
            if states[2] == 'SUCIO':
                estados_visitados[0] = 1 #Visitó estado 1
            else:
                estados_visitados[2] = 1 #Visitó estado 3
        else:
            if states[2] == 'SUCIO':
                estados_visitados[4] = 1 #Visitó estado 5
            else:
                estados_visitados[6] = 1 #Visitó estado 7

    else: #Si el agente está en la posición B
        if states[1] == 'SUCIO':
            if states[2] == 'SUCIO':
                estados_visitados[1] = 1 #Visitó estado 2
            else:
                estados_visitados[3] = 1 #Visitó estado 4
        else:
            if states[2] == 'SUCIO':
                estados_visitados[5] = 1 #Visitó estado 6
            else:
                estados_visitados[7] = 1 #Visitó estado 8

#Con esta función veo si ensucio o no una parte para buscar visitar todos los estados
def ensuciar(states):
    if states[1] == 'LIMPIO':
        states[1] = ('LIMPIO', 'SUCIO') [random.randint(0, 1) == 1] #Si el valor coincide cambia a SUCIO
    if states[2] == 'LIMPIO':
        states[2] = ('LIMPIO', 'SUCIO') [random.randint(0, 1) == 1] #Si el valor coincide cambia a SUCIO


def prueba(states):
    estados_visitados = [0, 0, 0, 0, 0, 0, 0, 0] 
    
    contador = 0

    while True:
        contador += 1
        
        #Imprimo el estado actual
        print("Estado actual: ", states)
        #Marco el estado que se visita
        visitar_estado(states, estados_visitados)
        print("Estados visitados: ", estados_visitados)

        #Verifico si ya visité los 8 estados
        if sum(estados_visitados) == 8:
            break #Si ya visité los 8 estados me salgo


        location = states[0] #Posición actual del agente
        state = (states[2], states[1])[location == 'A'] #Obtengo cómo se encuentra actualmente la posición (SUCIO o LIMPIO)
        #print("----------> " + state)
        
        action = reflex_agent(location, state) #Veo la acción que va a tomar el agente
        print("Location: " + location + " | Action: " + action)
        
        if action == "LIMPIO":
            if location == 'A':
                states[1] = "LIMPIO"
            elif location == 'B':
                states[2] = "LIMPIO"
        elif action == "RIGHT":
            states[0] = 'B'
        elif action == "LEFT":
            states[0] = 'A'

        ensuciar(states)

    #número de iteraciones para pasar por los 8 estados
    print("Número de iteraciones: " + str(contador))



test(['B', 'SUCIO', 'LIMPIO'])


