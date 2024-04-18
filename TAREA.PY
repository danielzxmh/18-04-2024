list_nombrecompleto = []
list_identificacion = []
list_correo = []
list_contact = []
list_edad = []
list_añosdeExp = []
list_profesion = []
list_ciudad = []
list_sexo = []
import os 


def fnt_registrar(nombre,identificacion,correo,contacto,edad,añosdeExp,profesion,ciudad,sexo):
    if nombre == " " or identificacion == " " or correo == " " or contacto == " " or edad == " " or añosdeExp == " " or profesion == " " or ciudad == " " or sexo == " ":
        enter = input("\nDEBE INGRESAR DATOS VALIDOS")     
    
    else:
        if nombre in list_nombrecompleto:
            enter = ("Esta persona ya se encuentra registrada <ENTER>")
        list_nombrecompleto.append(nombre)
        list_identificacion.append(identificacion)
        list_correo.append(correo)
        list_contact.append(contacto)
        list_edad.append(edad)
        list_añosdeExp.append(añosdeExp)
        list_profesion.append(profesion)
        list_ciudad.append(ciudad)
        list_sexo.append(sexo)
        
def fnt_selector(opcion):
    fnt_limpiar()
    if opcion == "1":
        nombre = list_nombrecompleto
        if nombre in list_nombrecompleto:
            print("Esta persona ya se encuentra registrada <ENTER>")
        else:
            nombre = input("NOMBRE COMPLETO:  ")
            identificacion = input("IDENTIFICACION: ")
            correo = input("correo: ")
            edad = input("edad: ")
            añosdeExp = input("AÑOS DE EXPERIENCIA: ")
            profesion = input("PROFESION: ")
            ciudad = input("CIUDAD: ")
            sexo = input("SEXO: ")
            fnt_registrar (nombre,identificacion,correo,edad,añosdeExp,profesion,ciudad,sexo)
    elif opcion == "2":
        fnt_limpiar()
        for i in range(len(list_nombrecompleto)):
            print(f"{list_nombrecompleto[i]}  {list_identificacion[i]}  {list_correo[i]} {list_contact[i]} {list_edad[i]} {list_añosdeExp[i]} {list_profesion[i]} {list_ciudad[i]} {list_sexo[i]}")
                
   
            
        
               
