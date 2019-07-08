import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl


def definirAntecedentes():
    tamano_tazas = [0,30,60,90,120,150,200,250,300,350,400,450]
    temperatura = ctrl.Antecedent(np.arange(0,41,1),'temperatura')
    tamano = ctrl.Antecedent(tamano_tazas,'tamano')
    intensidad = ctrl.Antecedent(np.arange(0,6,1),'intensidad')
    #temperatura.automf(3)
    #temperatura.view()
    temperatura['frio'] = fuzz.trapmf(temperatura.universe,[0,0,10,20])
    temperatura['calido'] = fuzz.trapmf(temperatura.universe,[15,25,28,30])
    temperatura['caluroso'] = fuzz.trapmf(temperatura.universe,[28,35,40,40])
    tamano['pequeno'] = fuzz.trapmf(tamano.universe,[0,0,60,120])
    tamano['mediano'] = fuzz.trapmf(tamano.universe,[100,120,200,300])
    tamano['grande'] = fuzz.trapmf(tamano.universe,[250,350,450,450])
    #tamano.automf(3)
    #tamano.view()
    intensidad['suave'] = fuzz.trapmf(intensidad.universe,[0,0,1,2])
    intensidad['medio'] = fuzz.trapmf(intensidad.universe,[1,2,3,4])
    intensidad['fuerte'] = fuzz.trapmf(intensidad.universe,[3,4,5,5])
    #intensidad.automf(3)
    
    #intensidad.view()
    plt.show()
    return intensidad,temperatura,tamano

def definirConsecuentes():
    agua = ctrl.Consequent(np.arange(0,451,1),'agua')
    cafe = ctrl.Consequent(np.arange(0,301,1),'cafe')
    leche = ctrl.Consequent(np.arange(0,101,1),'leche')
    tiempo = ctrl.Consequent(np.arange(0,121,1),'tiempo')
    chocolate = ctrl.Consequent(np.arange(0,101,1),'chocolate')
    
    #agua.automf(3)
    agua['poca'] = fuzz.trapmf(agua.universe,[0,0,60,120])
    agua['media'] = fuzz.trapmf(agua.universe,[100,120,200,300])
    agua['mucha'] = fuzz.trapmf(agua.universe,[250,350,450,450])
    agua.view()
    #cafe.automf(3)
    cafe['poca'] = fuzz.trapmf(cafe.universe,[0,0,90,120])
    cafe['media'] = fuzz.trapmf(cafe.universe,[100,125,200,250])
    cafe['mucha'] = fuzz.trapmf(cafe.universe,[225,250,300,300])
    #cafe.view()
    leche.automf(3)
    #leche['poca'] = fuzz.trapmf(leche.universe,[0,0,30,40])
    #leche['media'] = fuzz.trapmf(leche.universe,[35,45,70,75])
    #leche['mucha'] = fuzz.trapmf(leche.universe,[60,80,100,100])
    #leche.view()
    #tiempo.automf(3)
    tiempo['poca'] = fuzz.trapmf(tiempo.universe,[0,0,10,30])
    tiempo['media'] = fuzz.trapmf(tiempo.universe,[25,40,60,70])
    tiempo['mucha'] = fuzz.trapmf(tiempo.universe,[65,90,120,120])
    #tiempo.view()
    chocolate.automf(3)
    #chocolate['poca'] = fuzz.trapmf(chocolate.universe,[0,0,30,40])
    #chocolate['media'] = fuzz.trapmf(chocolate.universe,[35,45,70,75])
    #chocolate['mucha'] = fuzz.trapmf(chocolate.universe,[60,80,100,100])
    #chocolate.view()
    #plt.show()
    return agua,cafe,leche,tiempo,chocolate
'''
def definirReglas(tipoCafe):
    if tipoCafe == "espresso":
        rule1 = ctrl.Rule(tamano['pequeno'] & temperatura['frio'] & intensidad['suave'],(agua['poca'], cafe['poca'], tiempo['media']))
        rule2 = ctrl.Rule(tamano['pequeno'] & temperatura['calido'] & intensidad['suave'],(agua['poca'], cafe['media'], tiempo['poca']))
        rule3 = ctrl.Rule(tamano['mediano'] & temperatura['calido'] & intensidad['medio'],(agua['media'], cafe['poca'], tiempo['poca']))
        rule4 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['suave'],(agua['media'], cafe['media'], tiempo['poca']))
        rule5 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['suave'],(agua['mucha'], cafe['media'], tiempo['media']))
        rule6 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['fuerte'],(agua['mucha'], cafe['media'], tiempo['poca']))
    elif tipoCafe == "capuccino":
        rule1 = ctrl.Rule(tamano['pequeno'] & temperatura['frio'] & intensidad['suave'],(agua['poca'], cafe['poca'], leche['media'], tiempo['media']))
        rule2 = ctrl.Rule(tamano['pequeno'] & temperatura['calido'] & intensidad['fuerte'],(agua['poca'], cafe['media'], leche['poca'], tiempo['poca']))
        rule3 = ctrl.Rule(tamano['mediano'] & temperatura['calido'] & intensidad['medio'],(agua['media'], cafe['media'], leche['media'], tiempo['media']))
        rule4 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['fuerte'],(agua['media'], cafe['media'], leche['poca'], tiempo['poca']))
        rule5 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['suave'],(agua['mucha'], cafe['poca'], leche['media'], tiempo['media']))
        rule6 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['fuerte'],(agua['mucha'], cafe['media'], leche['poca'], tiempo['mucha']))
    elif tipoCafe == "latte":
        rule1 = ctrl.Rule(tamano['pequeno'] & temperatura['frio'] & intensidad['suave'],(agua['poca'], cafe['poca'], leche['media'], tiempo['media']))
        rule2 = ctrl.Rule(tamano['pequeno'] & temperatura['caluroso'] & intensidad['medio'],(agua['poca'], cafe['poca'], leche['poca'], tiempo['poca']))
        rule3 = ctrl.Rule(tamano['mediano'] & temperatura['calido'] & intensidad['medio'],(agua['media'], cafe['media'], leche['media'], tiempo['poca']))
        rule4 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['fuerte'],(agua['media'], cafe['mucha'], leche['poca'], tiempo['poca']))
        rule5 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['fuerte'],(agua['mucha'], cafe['mucha'], leche['poca'], tiempo['mucha']))
        rule6 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['suave'],(agua['mucha'], cafe['poca'], leche['mucha'], tiempo['media']))
    elif tipoCafe == "mocaccino":
        rule1 = ctrl.Rule(tamano['pequeno'] & temperatura['calido'] & intensidad['fuerte'],(agua['poca'], cafe['media'], leche['poca'], chocolate['poca'], tiempo['poca']))
        rule2 = ctrl.Rule(tamano['pequeno'] & temperatura['caluroso'] & intensidad['suave'],(agua['poca'], cafe['poca'], leche['media'], chocolate['poca'], tiempo['poca']))
        rule3 = ctrl.Rule(tamano['mediano'] & temperatura['frio'] & intensidad['medio'],(agua['media'], cafe['media'], leche['media'], chocolate['poca'], tiempo['media']))
        rule4 = ctrl.Rule(tamano['mediano'] & temperatura['caluroso'] & intensidad['fuerte'],(agua['media'], cafe['media'], leche['poca'], chocolate['poca'], tiempo['poca']))
        rule5 = ctrl.Rule(tamano['grande'] & temperatura['frio'] & intensidad['fuerte'],(agua['mucha'], cafe['media'], leche['media'], chocolate['poca'], tiempo['mucha']))
        rule6 = ctrl.Rule(tamano['grande'] & temperatura['calido'] & intensidad['suave'],(agua['mucha'], cafe['poca'], leche['media'], chocolate['poca'], tiempo['media']))
    return [rule1,rule2,rule3,rule4,rule5,rule6]'''


def definirReglas(tipoCafe):
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
        rule1 = ctrl.Rule(tamano['poor'] & temperatura['poor'] & intensidad['poor'],(agua['poor'], cafe['poor'], leche['average'], tiempo['average']))
        rule2 = ctrl.Rule(tamano['poor'] & temperatura['average'] & intensidad['good'],(agua['poor'], cafe['average'], leche['poor'], tiempo['poor']))
        rule3 = ctrl.Rule(tamano['average'] & temperatura['average'] & intensidad['average'],(agua['average'], cafe['average'], leche['average'], tiempo['average']))
        rule4 = ctrl.Rule(tamano['average'] & temperatura['good'] & intensidad['good'],(agua['average'], cafe['average'], leche['poor'], tiempo['poor']))
        rule5 = ctrl.Rule(tamano['good'] & temperatura['average'] & intensidad['poor'],(agua['good'], cafe['poor'], leche['average'], tiempo['average']))
        rule6 = ctrl.Rule(tamano['good'] & temperatura['poor'] & intensidad['good'],(agua['good'], cafe['average'], leche['poor'], tiempo['good']))
    elif tipoCafe == "latte":
        rule1 = ctrl.Rule(tamano['poor'] & temperatura['poor'] & intensidad['poor'],(agua['poor'], cafe['poor'], leche['average'], tiempo['average']))
        rule2 = ctrl.Rule(tamano['poor'] & temperatura['good'] & intensidad['average'],(agua['poor'], cafe['poor'], leche['poor'], tiempo['poor']))
        rule3 = ctrl.Rule(tamano['average'] & temperatura['average'] & intensidad['average'],(agua['average'], cafe['average'], leche['average'], tiempo['poor']))
        rule4 = ctrl.Rule(tamano['average'] & temperatura['good'] & intensidad['good'],(agua['average'], cafe['good'], leche['poor'], tiempo['poor']))
        rule5 = ctrl.Rule(tamano['good'] & temperatura['poor'] & intensidad['good'],(agua['good'], cafe['good'], leche['poor'], tiempo['good']))
        rule6 = ctrl.Rule(tamano['good'] & temperatura['average'] & intensidad['poor'],(agua['good'], cafe['poor'], leche['good'], tiempo['average']))
    elif tipoCafe == "mocaccino":
        rule1 = ctrl.Rule(tamano['poor'] & temperatura['average'] & intensidad['good'],(agua['poor'], cafe['average'], leche['poor'], chocolate['poor'], tiempo['poor']))
        rule2 = ctrl.Rule(tamano['poor'] & temperatura['good'] & intensidad['poor'],(agua['poor'], cafe['poor'], leche['average'], chocolate['poor'], tiempo['poor']))
        rule3 = ctrl.Rule(tamano['average'] & temperatura['poor'] & intensidad['average'],(agua['average'], cafe['average'], leche['average'], chocolate['poor'], tiempo['average']))
        rule4 = ctrl.Rule(tamano['average'] & temperatura['good'] & intensidad['good'],(agua['average'], cafe['average'], leche['poor'], chocolate['poor'], tiempo['poor']))
        rule5 = ctrl.Rule(tamano['good'] & temperatura['poor'] & intensidad['good'],(agua['good'], cafe['average'], leche['average'], chocolate['poor'], tiempo['good']))
        rule6 = ctrl.Rule(tamano['good'] & temperatura['average'] & intensidad['poor'],(agua['good'], cafe['poor'], leche['average'], chocolate['poor'], tiempo['average']))
    return [rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27]

def realizarCalculo(input_temperatura,input_tamano,input_intensidad,reglas):
    cafetera_ctrl = ctrl.ControlSystem(reglas)
    cafetera = ctrl.ControlSystemSimulation(cafetera_ctrl)
    cafetera.input['temperatura'] = input_temperatura
    cafetera.input['tamano'] = input_tamano
    cafetera.input['intensidad'] = input_intensidad
    cafetera.compute()
    return cafetera

def graficarResultados(cafetera,tipoCafe):
    print(cafetera.output['agua'],cafetera.output['cafe'],cafetera.output['tiempo'])
    agua.view(sim=cafetera)
    cafe.view(sim=cafetera)
    tiempo.view(sim=cafetera)
    if tipoCafe != "espresso":
        leche.view(sim=cafetera)
        if tipoCafe == "mocaccino":
            chocolate.view(sim=cafetera)
    plt.show()

intensidad,temperatura,tamano = definirAntecedentes()
agua,cafe,leche,tiempo,chocolate = definirConsecuentes()
#temperatura.view()
#tamano.view()
#plt.show()
reglas = definirReglas("espresso")
cafetera = realizarCalculo(26,225,3,reglas)
graficarResultados(cafetera,"espresso")










