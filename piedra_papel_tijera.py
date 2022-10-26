import random
from time import sleep

def players():
    nombre = str(input('Decime tu nombre: ').upper())
    jugadores = ['CPU', nombre]
    return jugadores

def options():
    opciones = ['PIEDRA','PAPEL','TIJERA']
    return opciones

def number_validation(numero):
    try:
        int(numero) 
        return True
    except ValueError:
        return False

def player_options(valor):
    validar_numero = number_validation(valor)
    opcion = options()
    if validar_numero == True:
        valor = int(valor)
        for i in range(len(opcion)):
            if i == int(valor-1):
                player_option = opcion[i]
                return player_option
    else:
        for i in opcion:
            if valor == i:
                player_option = i
                return player_option

def playing(n):

    n_games = n
    jugadores = players()
    opciones = options()
    jugador_1 = jugadores[0]
    jugador_2 = jugadores[1]

    for opcion in opciones:
        print(opcion) 

    counter = 0 
    cpu_counter = 0
    player_counter = 0
    ties_counter = 0

    while counter < n_games:
        opciones_jugador = input('Elegí una opción de la lista: ').upper()
        validar_opcion = player_options(opciones_jugador)
        opciones_jugador = validar_opcion
        if not opciones_jugador in opciones:
            print('Opción no válida.')
            r = str(input('¿Querés empezar dde nuevo? ("s") para aceptar) '))
            if r == 's':
                playing(n)
            else:
                print(f'\nResultado final:\n{jugador_1}: {cpu_counter}\n{jugador_2}: {player_counter}\nEmpates: {ties_counter}')
                if player_counter > cpu_counter:
                    print('GANASTE!!!\n')
                elif player_counter < cpu_counter:
                    print('Ganó la máquina. Suerte para la próxima!\n')
                else:
                    print('Es un empate!!\n')
                print('Juego terminado.')
                exit()
        opciones_cpu = random.choice(opciones)
        print('Jugando...')
        sleep(0.5)
        if  opciones_cpu == 'PIEDRA' and  opciones_jugador == 'TIJERA':
            cpu_counter += 1
            print(f'{jugador_1}: {opciones_cpu}\n{jugador_2}: {opciones_jugador}')
            print(f'{jugador_1} gana!')
        elif opciones_cpu == 'PAPEL' and opciones_jugador == 'PIEDRA':
            cpu_counter += 1
            print(f'{jugador_1}: {opciones_cpu}\n{jugador_2}: {opciones_jugador}')
            print(f'{jugador_1} gana!')
        elif opciones_cpu == 'TIJERA' and opciones_jugador == 'PAPEL':
            cpu_counter += 1
            print(f'{jugador_1}: {opciones_cpu}\n{jugador_2}: {opciones_jugador}')
            print(f'{jugador_1} gana!')
        elif opciones_jugador == 'PIEDRA' and opciones_cpu == 'TIJERA':
            player_counter += 1
            print(f'{jugador_1}: {opciones_cpu}\n{jugador_2}: {opciones_jugador}')
            print(f'{jugador_2} gana!')
        elif opciones_jugador == 'PAPEL' and opciones_cpu == 'PIEDRA':
            player_counter += 1
            print(f'{jugador_1}: {opciones_cpu}\n{jugador_2}: {opciones_jugador}')
            print(f'{jugador_2} gana!')
        elif opciones_jugador == 'TIJERA' and opciones_cpu == 'PAPEL':
            player_counter += 1
            print(f'{jugador_1}: {opciones_cpu}\n{jugador_2}: {opciones_jugador}')
            print(f'{jugador_2} gana! ')
        else:
            ties_counter += 1
            print(f'{jugador_1}: {opciones_cpu}\n{jugador_2}: {opciones_jugador}')
            print('Empate')
        counter += 1

    print(f'\nResultado final:\n{jugador_1}: {cpu_counter}\n{jugador_2}: {player_counter}\nEmpates: {ties_counter}')
    if player_counter > cpu_counter:
        print('GANASTE!!!')
    elif player_counter < cpu_counter:
        print('Ganó la máquina. Suerte para la próxima!')
    else:
        print('Es un empate!!')


if __name__ == '__main__':
    print('¡¡Bienvenidos a "Piedra Papel o Tijera"!!')
    n = int(input('Al mejor de cuántos partidos será el match? '))
    playing(n)
    
