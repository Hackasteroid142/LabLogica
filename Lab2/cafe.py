import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import math, sys

'''
    Proceso: Define los rangos y las funciones de pertencencia para los antecedentes que son la temperatura ambiental, la intensidad del cafe y el tamano de la taza.
    Salida: Funciones de pertenencia de las entradas.
'''
def definirAntecedentes():
    tamano_tazas = [0,30,60,90,120,150,200,250,300,350,400,450]
    temperatura = ctrl.Antecedent(np.arange(0,41,1),'temperatura')
    tamano = ctrl.Antecedent(tamano_tazas,'tamano')
    intensidad = ctrl.Antecedent(np.arange(0,6,1),'intensidad')

    temperatura['frio'] = fuzz.trapmf(temperatura.universe,[0,0,10,20])
    temperatura['calido'] = fuzz.trapmf(temperatura.universe,[15,25,28,30])
    temperatura['caluroso'] = fuzz.trapmf(temperatura.universe,[28,35,40,40])
    temperatura.view()
    plt.title("Temperatura Ambiental")

    tamano['pequeno'] = fuzz.trapmf(tamano.universe,[0,0,60,120])
    tamano['mediano'] = fuzz.trapmf(tamano.universe,[100,120,200,300])
    tamano['grande'] = fuzz.trapmf(tamano.universe,[250,350,450,450])
    tamano.view()
    plt.title("Tamano de la taza")

    intensidad['suave'] = fuzz.trapmf(intensidad.universe,[0,0,1,2])
    intensidad['medio'] = fuzz.trapmf(intensidad.universe,[1,2,3,4])
    intensidad['fuerte'] = fuzz.trapmf(intensidad.universe,[3,4,5,5])   
    intensidad.view()
    plt.title("Intensidad de cafe")
    plt.show()
    return intensidad,temperatura,tamano


'''
    Proceso: Crea los rangos y las funciones de pertencencia para los consecuentes que son la cantidad de agua, cafe, leche, chocolate y el tiempo de preparacion.
    Salida: Funciones de pertenencia para los consecuentes. 
'''
def definirConsecuentes():
    agua = ctrl.Consequent(np.arange(0,451,1),'agua')
    cafe = ctrl.Consequent(np.arange(0,301,1),'cafe')
    leche = ctrl.Consequent(np.arange(0,101,1),'leche')
    tiempo = ctrl.Consequent(np.arange(0,121,1),'tiempo')
    chocolate = ctrl.Consequent(np.arange(0,101,1),'chocolate')
    
    agua['poca'] = fuzz.trapmf(agua.universe,[0,0,60,120])
    agua['media'] = fuzz.trapmf(agua.universe,[100,120,200,300])
    agua['mucha'] = fuzz.trapmf(agua.universe,[250,350,450,450])

    cafe['poca'] = fuzz.trapmf(cafe.universe,[0,0,90,120])
    cafe['media'] = fuzz.trapmf(cafe.universe,[100,125,200,250])
    cafe['mucha'] = fuzz.trapmf(cafe.universe,[225,250,300,300])

    leche['poca'] = fuzz.trapmf(leche.universe,[0,0,30,40])
    leche['media'] = fuzz.trapmf(leche.universe,[35,45,70,75])
    leche['mucha'] = fuzz.trapmf(leche.universe,[60,80,100,100])

    tiempo['poca'] = fuzz.trapmf(tiempo.universe,[0,0,10,30])
    tiempo['media'] = fuzz.trapmf(tiempo.universe,[25,40,60,70])
    tiempo['mucha'] = fuzz.trapmf(tiempo.universe,[65,90,120,120])

    chocolate['poca'] = fuzz.trapmf(chocolate.universe,[0,0,30,40])
    chocolate['media'] = fuzz.trapmf(chocolate.universe,[35,45,70,75])
    chocolate['mucha'] = fuzz.trapmf(chocolate.universe,[60,80,100,100])

    return agua,cafe,leche,tiempo,chocolate


'''
    Entrada: El tipo de cafe y las funciones de pertenencia para el tamano, temperatura, cafe, tiempo, leche y chocolate.
    Proceso: Define las reglas segun el tipo de cafe.
    Salida: Retorna un arreglo con todas las reglas.
'''
def definirReglas(tipoCafe,tamano,temperatura,intensidad,agua,cafe,tiempo,leche,chocolate):
    if tipoCafe == "espresso":
        rule1 = ctrl.Rule(tamano['pequeno'] & temperatura['frio'] & intensidad['suave'],(agua['poca'], cafe['poca'], tiempo['media']))
        rule2 = ctrl.Rule(tamano['pequeno'] & temperatura['frio'] & intensidad['medio'],(agua['poca'], cafe['poca'], tiempo['media']))
        rule3 = ctrl.Rule(tamano['pequeno'] & temperatura['frio'] & intensidad['fuerte'],(agua['poca'], cafe['mucha'], tiempo['media']))
        rule4 = ctrl.Rule(tamano['pequeno'] & temperatura['calido'] & intensidad['suave'],(agua['poca'], cafe['poca'], tiempo['poca']))
        rule5 = ctrl.Rule(tamano['pequeno'] & temperatura['calido'] & intensidad['medio'],(agua['poca'], cafe['media'], tiempo['poca']))
        rule6 = ctrl.Rule(tamano['pequeno'] & temperatura['calido'] & intensidad['fuerte'],(agua['poca'], cafe['media'], tiempo['poca']))
        rule7 = ctrl.Rule(tamano['pequeno'] & temperatura['caluroso'] & intensidad['suave'],(agua['poca'], cafe['poca'], tiempo['poca']))
        rule8 = ctrl.Rule(tamano['pequeno'] & temperatura['caluroso'] & intensidad['medio'],(agua['poca'], cafe['media'], tiempo['poca']))
        rule9 = ctrl.Rule(tamano['pequeno'] & temperatura['caluroso'] & intensidad['fuerte'],(agua['poca'], cafe['media'], tiempo['poca']))
        rule10 = ctrl.Rule(tamano['mediano'] & temperatura['frio'] & intensidad['suave'],(agua['media'], cafe['poca'], tiempo['media']))
        rule11 = ctrl.Rule(tamano['mediano'] & temperatura['frio'] & intensidad['medio'],(agua['media'], cafe['media'], tiempo['media']))
        rule12 = ctrl.Rule(tamano['mediano'] & temperatura['frio'] & intensidad['fuerte'],(agua['media'], cafe['mucha'], tiempo['mucha']))
        rule13 = ctrl.Rule(tamano['mediano'] & temperatura['calido'] & intensidad['suave'],(agua['media'], cafe['media'], tiempo['media']))
        rule14 = ctrl.Rule(tamano['mediano'] & temperatura['calido'] & intensidad['medio'],(agua['media'], cafe['media'], tiempo['media']))
        rule15 = ctrl.Rule(tamano['mediano'] & temperatura['calido'] & intensidad['fuerte'],(agua['media'], cafe['mucha'], tiempo['media']))
        rule16 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['suave'],(agua['media'], cafe['poca'], tiempo['poca']))
        rule17 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['medio'],(agua['media'], cafe['poca'], tiempo['poca']))
        rule18 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['fuerte'],(agua['media'], cafe['media'], tiempo['poca']))
        rule19 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['suave'],(agua['mucha'], cafe['poca'], tiempo['mucha']))
        rule20 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['medio'],(agua['mucha'], cafe['media'], tiempo['mucha']))
        rule21 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['fuerte'],(agua['mucha'], cafe['media'], tiempo['mucha']))
        rule22 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['suave'],(agua['mucha'], cafe['poca'], tiempo['media']))
        rule23 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['medio'],(agua['mucha'], cafe['mucha'], tiempo['media']))
        rule24 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['fuerte'],(agua['mucha'], cafe['mucha'], tiempo['media']))
        rule25 = ctrl.Rule(tamano['grande'] & temperatura['caluroso'] & intensidad['suave'],(agua['mucha'], cafe['media'], tiempo['poca']))
        rule26 = ctrl.Rule(tamano['grande'] & temperatura['caluroso'] & intensidad['medio'],(agua['mucha'], cafe['mucha'], tiempo['poca']))
        rule27 = ctrl.Rule(tamano['grande'] & temperatura['caluroso'] & intensidad['fuerte'],(agua['mucha'], cafe['mucha'], tiempo['poca']))
    elif tipoCafe == "capuccino":
        rule1 = ctrl.Rule(tamano['pequeno'] & temperatura['frio'] & intensidad['suave'],(agua['poca'], cafe['poca'], leche['media'], tiempo['media']))
        rule2 = ctrl.Rule(tamano['pequeno'] & temperatura['frio'] & intensidad['medio'],(agua['poca'], cafe['poca'], leche['poca'], tiempo['media']))
        rule3 = ctrl.Rule(tamano['pequeno'] & temperatura['frio'] & intensidad['fuerte'],(agua['poca'], cafe['mucha'], leche['poca'], tiempo['media']))
        rule4 = ctrl.Rule(tamano['pequeno'] & temperatura['calido'] & intensidad['suave'],(agua['poca'], cafe['poca'], leche['media'], tiempo['poca']))
        rule5 = ctrl.Rule(tamano['pequeno'] & temperatura['calido'] & intensidad['medio'],(agua['poca'], cafe['media'], leche['poca'], tiempo['poca']))
        rule6 = ctrl.Rule(tamano['pequeno'] & temperatura['calido'] & intensidad['fuerte'],(agua['poca'], cafe['media'], leche['poca'], tiempo['poca']))
        rule7 = ctrl.Rule(tamano['pequeno'] & temperatura['caluroso'] & intensidad['suave'],(agua['poca'], cafe['poca'], leche['mucha'], tiempo['poca']))
        rule8 = ctrl.Rule(tamano['pequeno'] & temperatura['caluroso'] & intensidad['medio'],(agua['poca'], cafe['media'], leche['media'], tiempo['poca']))
        rule9 = ctrl.Rule(tamano['pequeno'] & temperatura['caluroso'] & intensidad['fuerte'],(agua['poca'], cafe['media'], leche['poca'], tiempo['poca']))
        rule10 = ctrl.Rule(tamano['mediano'] & temperatura['frio'] & intensidad['suave'],(agua['media'], cafe['poca'], leche['media'], tiempo['media']))
        rule11 = ctrl.Rule(tamano['mediano'] & temperatura['frio'] & intensidad['medio'],(agua['media'], cafe['media'], leche['media'], tiempo['media']))
        rule12 = ctrl.Rule(tamano['mediano'] & temperatura['frio'] & intensidad['fuerte'],(agua['media'], cafe['mucha'], leche['poca'], tiempo['mucha']))
        rule13 = ctrl.Rule(tamano['mediano'] & temperatura['calido'] & intensidad['suave'],(agua['media'], cafe['media'], leche['mucha'],  tiempo['media']))
        rule14 = ctrl.Rule(tamano['mediano'] & temperatura['calido'] & intensidad['medio'],(agua['media'], cafe['media'], leche['media'], tiempo['media']))
        rule15 = ctrl.Rule(tamano['mediano'] & temperatura['calido'] & intensidad['fuerte'],(agua['media'], cafe['mucha'], leche['poca'], tiempo['media']))
        rule16 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['suave'],(agua['media'], cafe['poca'], leche['mucha'], tiempo['poca']))
        rule17 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['medio'],(agua['media'], cafe['poca'], leche['media'], tiempo['poca']))
        rule18 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['fuerte'],(agua['media'], cafe['media'], leche['poca'], tiempo['poca']))
        rule19 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['suave'],(agua['mucha'], cafe['poca'], leche['mucha'], tiempo['mucha']))
        rule20 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['medio'],(agua['mucha'], cafe['media'], leche['media'], tiempo['mucha']))
        rule21 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['fuerte'],(agua['mucha'], cafe['media'], leche['poca'], tiempo['mucha']))
        rule22 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['suave'],(agua['mucha'], cafe['poca'], leche['medio'], tiempo['media']))
        rule23 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['medio'],(agua['mucha'], cafe['mucha'], leche['media'], tiempo['media']))
        rule24 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['fuerte'],(agua['mucha'], cafe['mucha'], leche['poca'], tiempo['media']))
        rule25 = ctrl.Rule(tamano['grande'] & temperatura['caluroso'] & intensidad['suave'],(agua['mucha'], cafe['media'], leche['mucha'], tiempo['poca']))
        rule26 = ctrl.Rule(tamano['grande'] & temperatura['caluroso'] & intensidad['medio'],(agua['mucha'], cafe['mucha'], leche['media'], tiempo['poca']))
        rule27 = ctrl.Rule(tamano['grande'] & temperatura['caluroso'] & intensidad['fuerte'],(agua['mucha'], cafe['media'], leche['poca'], tiempo['mucha']))
    elif tipoCafe == "latte": 
        rule1 = ctrl.Rule(tamano['pequeno'] & temperatura['frio'] & intensidad['suave'],(agua['poca'], cafe['poca'], leche['media'], tiempo['media']))
        rule2 = ctrl.Rule(tamano['pequeno'] & temperatura['frio'] & intensidad['medio'],(agua['poca'], cafe['poca'], leche['media'], tiempo['media']))
        rule3 = ctrl.Rule(tamano['pequeno'] & temperatura['frio'] & intensidad['fuerte'],(agua['poca'], cafe['mucha'], leche['poca'], tiempo['media']))
        rule4 = ctrl.Rule(tamano['pequeno'] & temperatura['calido'] & intensidad['suave'],(agua['poca'], cafe['poca'], leche['media'], tiempo['poca']))
        rule5 = ctrl.Rule(tamano['pequeno'] & temperatura['calido'] & intensidad['medio'],(agua['poca'], cafe['media'], leche['media'], tiempo['poca']))
        rule6 = ctrl.Rule(tamano['pequeno'] & temperatura['calido'] & intensidad['fuerte'],(agua['poca'], cafe['media'], leche['poca'], tiempo['poca']))
        rule7 = ctrl.Rule(tamano['pequeno'] & temperatura['caluroso'] & intensidad['suave'],(agua['poca'], cafe['poca'], leche['mucha'], tiempo['poca']))
        rule8 = ctrl.Rule(tamano['pequeno'] & temperatura['caluroso'] & intensidad['medio'],(agua['poca'], cafe['poca'], leche['poca'],tiempo['poca']))
        rule9 = ctrl.Rule(tamano['pequeno'] & temperatura['caluroso'] & intensidad['fuerte'],(agua['poca'], cafe['media'], leche['poca'], tiempo['poca']))
        rule10 = ctrl.Rule(tamano['mediano'] & temperatura['frio'] & intensidad['suave'],(agua['media'], cafe['poca'],  leche['mucha'], tiempo['media']))
        rule11 = ctrl.Rule(tamano['mediano'] & temperatura['frio'] & intensidad['medio'],(agua['media'], cafe['media'], leche['media'], tiempo['media']))
        rule12 = ctrl.Rule(tamano['mediano'] & temperatura['frio'] & intensidad['fuerte'],(agua['media'], cafe['mucha'], leche['poca'], tiempo['mucha']))
        rule13 = ctrl.Rule(tamano['mediano'] & temperatura['calido'] & intensidad['suave'],(agua['media'], cafe['media'], leche['mucha'], tiempo['media']))
        rule14 = ctrl.Rule(tamano['mediano'] & temperatura['calido'] & intensidad['medio'],(agua['media'], cafe['media'], leche['media'], tiempo['poca']))
        rule15 = ctrl.Rule(tamano['mediano'] & temperatura['calido'] & intensidad['fuerte'],(agua['media'], cafe['mucha'], leche['media'], tiempo['media']))
        rule16 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['suave'],(agua['media'], cafe['poca'], leche['media'], tiempo['poca']))
        rule17 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['medio'],(agua['media'], cafe['poca'], leche['media'], tiempo['poca']))
        rule18 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['fuerte'],(agua['media'], cafe['mucha'], leche['poca'], tiempo['poca']))
        rule19 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['suave'],(agua['mucha'], cafe['poca'], leche['media'], tiempo['mucha']))
        rule20 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['medio'],(agua['mucha'], cafe['media'], leche['mucha'], tiempo['mucha']))
        rule21 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['fuerte'],(agua['mucha'], cafe['mucha'], leche['poca'], tiempo['mucha']))
        rule22 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['suave'],(agua['mucha'], cafe['poca'], leche['mucha'], tiempo['media']))
        rule23 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['medio'],(agua['mucha'], cafe['mucha'], leche['media'], tiempo['media']))
        rule24 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['fuerte'],(agua['mucha'], cafe['mucha'], leche['poca'], tiempo['media']))
        rule25 = ctrl.Rule(tamano['grande'] & temperatura['caluroso'] & intensidad['suave'],(agua['mucha'], cafe['media'], leche['mucha'], tiempo['poca']))
        rule26 = ctrl.Rule(tamano['grande'] & temperatura['caluroso'] & intensidad['medio'],(agua['mucha'], cafe['mucha'], leche['mucha'], tiempo['poca']))
        rule27 = ctrl.Rule(tamano['grande'] & temperatura['caluroso'] & intensidad['fuerte'],(agua['mucha'], cafe['mucha'], leche['media'], tiempo['poca']))
    elif tipoCafe == "mocaccino":
        rule1 = ctrl.Rule(tamano['pequeno'] & temperatura['frio'] & intensidad['suave'],(agua['poca'], cafe['poca'], leche['media'], chocolate['media'], tiempo['media']))
        rule2 = ctrl.Rule(tamano['pequeno'] & temperatura['frio'] & intensidad['medio'],(agua['poca'], cafe['poca'], leche['media'], chocolate['poca'], tiempo['media']))
        rule3 = ctrl.Rule(tamano['pequeno'] & temperatura['frio'] & intensidad['fuerte'],(agua['poca'], cafe['mucha'], leche['poca'], chocolate['poca'], tiempo['media']))
        rule4 = ctrl.Rule(tamano['pequeno'] & temperatura['calido'] & intensidad['suave'],(agua['poca'], cafe['poca'], leche['media'], chocolate['mucha'], tiempo['poca']))
        rule5 = ctrl.Rule(tamano['pequeno'] & temperatura['calido'] & intensidad['medio'],(agua['poca'], cafe['media'], leche['media'], chocolate['poca'], tiempo['poca']))
        rule6 = ctrl.Rule(tamano['pequeno'] & temperatura['calido'] & intensidad['fuerte'],(agua['poca'], cafe['media'], leche['poca'], chocolate['poca'], tiempo['poca']))
        rule7 = ctrl.Rule(tamano['pequeno'] & temperatura['caluroso'] & intensidad['suave'],(agua['poca'], cafe['poca'], leche['media'], chocolate['poca'], tiempo['poca']))
        rule8 = ctrl.Rule(tamano['pequeno'] & temperatura['caluroso'] & intensidad['medio'],(agua['poca'], cafe['media'], leche['media'], chocolate['media'], tiempo['poca']))
        rule9 = ctrl.Rule(tamano['pequeno'] & temperatura['caluroso'] & intensidad['fuerte'],(agua['poca'], cafe['media'], leche['poca'], chocolate['media'], tiempo['poca']))
        rule10 = ctrl.Rule(tamano['mediano'] & temperatura['frio'] & intensidad['suave'],(agua['media'], cafe['poca'], leche['media'], chocolate['mucha'], tiempo['media']))
        rule11 = ctrl.Rule(tamano['mediano'] & temperatura['frio'] & intensidad['medio'],(agua['media'], cafe['media'], leche['media'], chocolate['media'], leche['media'], chocolate['poca'], tiempo['media']))
        rule12 = ctrl.Rule(tamano['mediano'] & temperatura['frio'] & intensidad['fuerte'],(agua['media'], cafe['mucha'], leche['poca'], chocolate['media'], tiempo['mucha']))
        rule13 = ctrl.Rule(tamano['mediano'] & temperatura['calido'] & intensidad['suave'],(agua['media'], cafe['media'], leche['media'], chocolate['mucha'], tiempo['media']))
        rule14 = ctrl.Rule(tamano['mediano'] & temperatura['calido'] & intensidad['medio'],(agua['media'], cafe['media'], leche['media'], chocolate['media'], tiempo['media']))
        rule15 = ctrl.Rule(tamano['mediano'] & temperatura['calido'] & intensidad['fuerte'],(agua['media'], cafe['mucha'], leche['poca'], chocolate['poca'], tiempo['media']))
        rule16 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['suave'],(agua['media'], cafe['poca'], leche['media'], chocolate['media'], tiempo['poca']))
        rule17 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['medio'],(agua['media'], cafe['poca'], leche['media'], chocolate['mucha'], tiempo['poca']))
        rule18 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['fuerte'],(agua['media'], cafe['media'], leche['poca'], chocolate['poca'], tiempo['poca']))
        rule19 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['suave'],(agua['mucha'], cafe['poca'], leche['mucha'], chocolate['mucha'], tiempo['mucha']))
        rule20 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['medio'],(agua['mucha'], cafe['media'], leche['poca'], chocolate['media'], tiempo['mucha']))
        rule21 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['fuerte'],(agua['mucha'], cafe['media'], leche['poca'], chocolate['poca'], tiempo['mucha']))
        rule22 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['suave'],(agua['mucha'], cafe['poca'], leche['media'], chocolate['mucha'], tiempo['media']))
        rule23 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['medio'],(agua['mucha'], cafe['mucha'], leche['media'], chocolate['media'], tiempo['media']))
        rule24 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['fuerte'],(agua['mucha'], cafe['mucha'], leche['poca'], chocolate['poca'], tiempo['media']))
        rule25 = ctrl.Rule(tamano['grande'] & temperatura['caluroso'] & intensidad['suave'],(agua['mucha'], cafe['media'], leche['mucha'], chocolate['mucha'], tiempo['poca']))
        rule26 = ctrl.Rule(tamano['grande'] & temperatura['caluroso'] & intensidad['medio'],(agua['mucha'], cafe['mucha'], leche['media'], chocolate['mucha'], tiempo['poca']))
        rule27 = ctrl.Rule(tamano['grande'] & temperatura['caluroso'] & intensidad['fuerte'],(agua['mucha'], cafe['mucha'], leche['media'], chocolate['poca'], tiempo['poca']))
    else:
        print("Cafe no es el apropiado.")
        exit()
    return [rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27]

'''
    Entradas: Los parametros de entrada y las reglas a utilizar.
    Proceso: Crea la simulacion a la cual se le entrega los parametros. Esta simulacion calcula los valores defuzzificados.
    Salida: Simulacion con los resultados. 
'''
def realizarCalculo(input_temperatura,input_tamano,input_intensidad,reglas):
    cafetera_ctrl = ctrl.ControlSystem(reglas)
    cafetera = ctrl.ControlSystemSimulation(cafetera_ctrl)
    cafetera.input['temperatura'] = input_temperatura
    cafetera.input['tamano'] = input_tamano
    cafetera.input['intensidad'] = input_intensidad
    cafetera.compute()
    return cafetera

'''
    Entrada: La simulacion de cafetera, el tipo de cafe y las funciones de pertenencia del cade, tiempo, leche, agua y chocolate.
    Proceso: Grafica los resultados de la defuzzificacion segun el tipo de cafe.
'''
def graficarResultados(cafetera,tipoCafe,agua,cafe,tiempo,leche,chocolate):
    agua.view(sim=cafetera)
    plt.title("Nivel del Agua")
    cafe.view(sim=cafetera)
    plt.title("Cantidad de Cafe")
    tiempo.view(sim=cafetera)
    plt.title("Tiempo de preparacion")
    if tipoCafe != "espresso":
        leche.view(sim=cafetera)
        plt.title("Cantidad de Leche")
        if tipoCafe == "mocaccino":
            chocolate.view(sim=cafetera)
            plt.title("Cantidad de Chocolate")
    plt.show()

'''
    Entrada: Cantidad de agua y el tiempo de preparacion. 
    Proceso: Redondea el valor de la cantidad del agua segun las tazas disponible y transforma el tiempo a minutos.
    Salida: Cantidad de agua aproximada y el tiempo de preparacion.
'''   
def transformarValores(cantidadAgua,tiempo_preparacion):
    tamano_tazas = [0,30,60,90,120,150,200,250,300,350,400,450]
    minutos = int(tiempo_preparacion / 60)
    segundos  = tiempo_preparacion % 60
    if segundos >= 30: 
        minutos += 0.5
    cantidadAgua_aprox = 0
    for x in tamano_tazas:
        dif = cantidadAgua - x
        if (dif <= 0):
            cantidadAgua_aprox = x
            break
    return cantidadAgua_aprox,minutos

'''
    Entradas: Valores de entrada del tamano de la taza, el tipo de cafe, el tipo de cafe y el nivel de temperatura, ademas de la simulacion de la cafetera.
    Proceso: Escribe en un archivo los resultados numericos obtenidos.
'''
def escribirArchivo(tamanoTaza,tipoCafe,nivelIntensidad,nivelTemperatura,cafetera):
    valorAgua,minutos= transformarValores(cafetera.output['agua'],math.ceil(cafetera.output['tiempo']))
    nombre_archivo = "Cafe_"+tamanoTaza+"_"+tipoCafe+"_"+nivelIntensidad+"_"+nivelTemperatura+".txt"
    nuevo_archivo = open(nombre_archivo,"w")
    respuesta = "Nivel del Agua: " + str(valorAgua) + " mL\nCantidad de Cafe: " + str(math.ceil(cafetera.output['cafe'])) +" grs\n"
    if tipoCafe != "espresso":
        respuesta += "Cantidad de leche: " + str(math.ceil(cafetera.output['leche'])) + " grs\n"
        if tipoCafe == "mocaccino":
            respuesta += "Cantidad de chocolate: " + str(math.ceil(cafetera.output['chocolate'])) +" grs\n"
    respuesta += "Tiempo de preparacion: " + str(minutos) + " minutos"
    nuevo_archivo.write(respuesta)

'''
    Proceso: Recibe los parametros de entrada desde la linea de comando.
    Salida: Las entradas ingresadas.
'''
def recibirParametros():
    if len(sys.argv) == 5: 
        input_tamano = int(sys.argv[1])
        input_temp = int(sys.argv[2])
        input_intensidad = int(sys.argv[3])
        input_tipoCafe = sys.argv[4]
    else:
        print("La cantidad de parametros es la incorrecta")
        exit()
    return input_tamano,input_temp,input_intensidad,input_tipoCafe

###################### MAIN ###############################
input_tamano,input_temp,input_intensidad,input_tipoCafe = recibirParametros()
intensidad,temperatura,tamano = definirAntecedentes()
agua,cafe,leche,tiempo,chocolate = definirConsecuentes()
reglas = definirReglas(input_tipoCafe,tamano,temperatura,intensidad,agua,cafe,tiempo,leche,chocolate)
cafetera = realizarCalculo(input_temp,input_tamano,input_intensidad,reglas)
graficarResultados(cafetera,input_tipoCafe,agua,cafe,tiempo,leche,chocolate)
escribirArchivo(str(input_tamano),input_tipoCafe,str(input_intensidad),str(input_temp),cafetera)










