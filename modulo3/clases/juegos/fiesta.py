
def agregar_invitados(invitados):
    invitados =set()
    print("Cuantas personas desea invitar?")
    personas = int(input("Ingrese la cantidad: "))
    for i in range(personas):
        invitados.add(input(f"Nombre del {i+1} invitado. "))
    return invitados


llegaron =set()
invitados = agregar_invitados(set())

while len(invitados^llegaron)>=0: 
    opciones = input('''FIESTA DEL SIGLO
                     Consultar quienes han llegado y faltan (c) 
                     Agregar un invitado que ha llegado (a) 
                     Salir (s) ''').lower().strip() 
    faltan_por_llegar = invitados^llegaron 
    match opciones: 
        case "c" | "consultar": 
            print(f'La cantidad de invitados que llegaron es {len(llegaron)}') 
            print(f"La cantidad de invitados confirmados son", len(invitados))
            print(f'Falta por llegar {len(faltan_por_llegar)} y son {faltan_por_llegar}') 
        case "a" | "agregar": 
                    nuevo = input('Ingresa nombre de quien ha llegado ')
                    if nuevo in invitados: 
                        llegaron.add(nuevo)
                    else: 
                        print("invitado no registrado, ingrese otro")
                    print(f' los invitados que han llegado son {llegaron}') 
        case "s" | "salir": 
            print("Adios") 
            break
else:
    print("llegaron todos los invitados, exito!")