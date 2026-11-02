#variable nombre con string la cual imprimira el nombre del usuario
nombre = input("¿Cuál es tu nombre? ")
#variable apellido paterno con string la cual imprimira el apellido del usurario
apellido_paterno= input("¿Cuál es tu apellido paterno? ")
#variable apellido materno con string la cual imprimira el segundo apellido del usuario
apellido_materno = input("¿Cuál es tu apellido materno? ")
#variable edad con entero la cual imprimira la edad del usuario
edad = int(input("¿Cuántos años tienes? "))
#variable peso con float la cual imprimira el peso del usuario 
peso = float(input("¿Cuánto pesas (kg)? "))
#variable estatura con float la cual imprimira la estatura del usuario
estatura = float(input("¿Cuánto mides (m)? "))
#va a calcular el IMC del usuario con la formula peso/estatura^2
imc = peso / (estatura ** 2)
#nos va a imprimir las respuestas del usuario
print(f"variables:{nombre}, {apellido_paterno}, {apellido_materno}, {edad} años, {peso} kg, {estatura} metros")
print(f"Tu IMC es: {imc:.2f}")