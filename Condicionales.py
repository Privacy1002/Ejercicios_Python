#Condicionales simples 
'''temperature = 40

if temperature > 35:
    print('Aviso por alta temperatura')
else:
    print('Parámetros normales')'''
    
#Condicionales anidadas

'''temperature = 28

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
else:
    if temperature < 30:
        print('Nivel naranja')
    else:
        print('Nivel rojo')'''
    
#Asignacion de condicionales 

'''temperature: 28 

fire_risk = 'LOW' if temperature < 30 else 'HIGH'

fire_risk'''

'''color = '#FF0000'''

#Match case

'''match color:
    case '#FF0000':
        print('🔴')
    case '#00FF00':
        print('🟢')
    case '#0000FF':
        print('🔵')'''
        
'''point = (2, 5)

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')

point = (3, 1, 7)

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')'''
        
#Operador morsa

'''radius = 4.25
perimeter = 2 * 3.14 * radius
if perimeter < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)'''