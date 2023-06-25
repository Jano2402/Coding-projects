print("Super calculadora de gasto energético")

print("")

Peso = float(input("Ingrese su peso(kg): "))

print("")

Altura = int(input("Ingrese su altura(cm): "))

print("")

Edad = int(input("Ingrese su edad: "))

print("")

print("1. Hombre")
print("2. Mujer")

print("")

Sexo = int(input("Ingrese su sexo: "))
print("")

if Sexo == 1:
    Cal = ((Peso * 10)+(Altura * 6.25)-(Edad * 5)-161)

else:
    Cal = ((Peso*10)+(Altura*6.25)-(5*Edad)+5)

print("1. Sedentario")
print("2. Actividad normal (1-3 veces por semana)")
print("3. Actividad moderada (3-5 veces por semana)")
print("4. Actividad muy alta (6-7 veces por semana)")
print("5. Atletas profesionales (Hasta 2 entrenamientos por día)")

print("")

act_fisi = int(input("Ingrese cantidad de actividad física: "))

print("")

if act_fisi == 1:
    Cal_mant = Cal * 1.2
elif act_fisi == 2:
    Cal_mant = Cal * 1.375
elif act_fisi == 3:
    Cal_mant = Cal * 1.55
elif act_fisi == 4:
    Cal_mant = Cal * 1.75
elif act_fisi == 5:
    Cal_mant = Cal * 1.9

print("Elige que quieres hacer")
print("")
print("1. Déficit normal")
print("2. Déficit agresivo")
print("3. Volumen normal")
print("4. Volumen agresivo")

print("")

objetivo = int(input("Ingrese su objetivo: "))

print("")

if objetivo == 1:
    Dieta = Cal_mant - 300
elif objetivo == 2:
    Dieta = Cal_mant -500
elif objetivo == 3:
    Dieta = Cal_mant + 300
elif objetivo == 4:
    Dieta = Cal_mant + 500
    
print("")

print(f"Debes comer {Dieta} calorías para alcanzar tu objetivo")
