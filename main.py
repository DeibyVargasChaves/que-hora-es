import time
hora_actual = time.localtime()
hora = hora_actual[3]

if hora >= 7:
    print("Es hora de ir a casa")
else:
    tiempo_restante = 7 - hora
    print(f"Falta {tiempo_restante} horas para ir a casa")
