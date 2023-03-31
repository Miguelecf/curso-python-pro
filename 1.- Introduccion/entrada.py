#La funcion input siempre va a retornar un str entonces casteamos al tipo de dato que necesitamos
nombre_completo = input('Ingresa tu nombre completo: ')
print(type(nombre_completo))

edad = int(input('Ingresa tu edad '))
print(type(edad))

altura = float(input('Ingresa tu altura '))
print(type(altura))

autorizacion  = input('¿Autorizas al programa? (si/no)') == 'si'
print(autorizacion)