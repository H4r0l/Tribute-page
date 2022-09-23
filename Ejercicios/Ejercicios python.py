peso = float(input("Ingresa tu peso en kilogramos"))
while(type(peso) != float):
  if(type(peso) != float):
    peso = input("Ingresa un numero valido: ")
  else:
    pass
masa = float(peso)/9.8
opciones = {'1':3.7,
            '2':8.87,
            '3':3.71,
            '4':24.79,
            '5':10.44,
            '6':8.87,
            '7':11.15}
ans = int(input("En cual planeta te gustaria ver tu peso: ""\n"
            "1. Mercurio""\n"
            "2. Venus" "\n"
            "3. Marte" "\n"
            "4. Jupiter" "\n"
            "5. Saturno" "\n"
            "6. Urano" "\n"
            "7. Neptuno" "\n""\n"))
if(0 < ans > 7):
  print("Opcion inexistente")
elif(ans == 1):
  x = opciones['1'] * float(masa)
  print("Tu peso en Mercurio seria: ", x,"kg" )
elif(ans == 2):
  x = opciones['2'] * float(masa)
  print("Tu peso en venus seria: ", x,"kg" )
elif(ans == 3):
  x = opciones['3'] * float(masa)
  print("Tu peso en Marte seria: ", x,"kg")
elif(ans == 4):
  x = opciones['4'] * float(masa)
  print("Tu peso en Júpiter seria: ", x,"kg")
elif(ans == 5):
  x = opciones['5'] * float(masa)
  print("Tu peso en Saturno seria: ", x,"kg")
elif(ans == 6):
  x = opciones['6'] * float(masa)
  print("Tu peso en Urano seria: ", x,"kg")
elif(ans == 7):
  x = opciones['7'] * float(masa)
  print("Tu peso en Neptuno seria: ", x,"kg")
