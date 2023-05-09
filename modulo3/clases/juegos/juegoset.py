

libros_prestados = {'Cien anos de soledad', 'El amor en los tiempos del c61era', 
                    'La ciudad y los perros', 'La casa verde', 'El otono del patriarca', 
                    'Rayuela', 'Pedro Påramo', 'La tregua'}

print("cantidad de libros prestados:",len(libros_prestados))
libros_devueltos ={'Cien anos de soledad', 'El amor en los tiempos del c61era', 
                    'La ciudad y los perros'}
print("los libros prestados no devueltos son", libros_prestados^libros_devueltos, len(libros_prestados^libros_devueltos)) 


while True: 
    opciones = input('''que quieres hacer? 
                     Consultar libros prestados (c) 
                     Agregar libros devuetos (a) 
                     Salir (s) ''').lower().strip() 
    libros_prestados = {'Cien afios de soledad', 'El amor en los tiempos del c61era', 
                        'La ciudad y los perros', 'La casa verde', 
                        'El otoöo del patriarca', 'Rayuela', 'Pedro Påramo', 'La tregua'} 
    libros_devueltos = {"caperucita roja", 'Python Machine Learning'} 
    base_actualizada = libros_devueltos.symmetric_difference(libros_prestados) 
    match opciones: 
        case "c" | "consultar": 
            print(f'La cantidad de libros prestados son {len(libros_prestados)}') 
            print(f'Falta por devolver {base_actualizada}') 
        case "a" | "agregar": 
                    libro_dev = input('Ingresa el libro ') 
                    libros_devueltos.add(libro_dev) 
                    print(f' Los libros devueltos son {libros_devueltos}') 
        case "s" | "salir": 
            print("Adios") 
            break




