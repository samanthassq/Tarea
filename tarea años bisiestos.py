#El usuario ingresa años hasta acertar un año bisiesto
x = int(input ("Ingresa un año entre 1900 y 2199"))

#Se establece el rango de valor de x
1900 < x < 2199

#Condicionales y ciclos para determinar años bisiestos y no bisiestos
i = 0
while i == 0:   
    if  1900 < x < 2199:
        if x / 4  == int(x / 4):
            print("El año ingresado es bisiesto ")
            i += 1
        else:
            print("El año ingresado no es bisiesto, intenta ingresar un año bisiesto")  
    else:
        print("El año ingresado es inválido") 
while i == 1:
    y = int(input("Vuelve a ingresar el año para calcular la cantidad"
              " de años bisiestos que existen desde el año 1900")) 
    i += 1   
 
#Se establecen los valores
años_bisiestos = int(y / 4)
cantidad_de_años_bisiestos = (y - 1900) / 4

#Condicionales y ciclos de los años ingresados
while i == 2:
    if y / 4 == años_bisiestos:
        print(f"Hay {int(cantidad_de_años_bisiestos)} años bisiestos entre el año 1900 y el año {y}")
        i += 1
    else:
        print ("El año ingresado no es bisiesto, por tanto es inválido")
        
