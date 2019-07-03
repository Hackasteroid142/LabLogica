import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl


def definirAntecedentes():
    temperatura = ctrl.Antecedent(np.arange(0,101,1),'temperatura')
    tamano = ctrl.Antecedent(np.arange(0,151,1),'tamano')
    intensidad = ctrl.Antecedent(np.arange(0,6,1),'intensidad')
    temperatura['frio'] = fuzz.trimf(temperatura.universe,[0,0,50])
    temperatura['calido'] = fuzz.trimf(temperatura.universe,[0,50,100])
    temperatura['caluroso'] = fuzz.trimf(temperatura.universe,[50,100,100])
    tamano['pequeno'] = fuzz.trimf(tamano.universe,[0,0,75])
    tamano['mediano'] = fuzz.trimf(tamano.universe,[0,75,150])
    tamano['grande'] = fuzz.trimf(tamano.universe,[75,150,150])
    intensidad['suave'] = fuzz.trimf(intensidad.universe,[0,0,3])
    intensidad['medio'] = fuzz.trimf(intensidad.universe,[0,3,5])
    intensidad['fuerte'] = fuzz.trimf(intensidad.universe,[3,5,5])
    return intensidad,temperatura,tamano

def definirConsecuentes():
    agua = ctrl.Consequent(np.arange(0,601,1),'agua')
    cafe = ctrl.Consequent(np.arange(0,601,1),'cafe')
    leche = ctrl.Consequent(np.arange(0,601,1),'leche')
    tiempo = ctrl.Consequent(np.arange(0,601,1),'tiempo')
    chocolate = ctrl.Consequent(np.arange(0,601,1),'chocolate')
    agua['poca'] = fuzz.trimf(agua.universe,[0,0,250])
    agua['media'] = fuzz.trimf(agua.universe,[200,350,450])
    agua['mucha'] = fuzz.trimf(agua.universe,[400,500,600])

    cafe['poca'] = fuzz.trimf(cafe.universe,[0,0,250])
    cafe['media'] = fuzz.trimf(cafe.universe,[200,350,450])
    cafe['mucha'] = fuzz.trimf(cafe.universe,[400,500,600])

    leche['poca'] = fuzz.trimf(leche.universe,[0,0,250])
    leche['media'] = fuzz.trimf(leche.universe,[200,350,450])
    leche['mucha'] = fuzz.trimf(leche.universe,[400,500,600])

    tiempo['poca'] = fuzz.trimf(tiempo.universe,[0,0,250])
    tiempo['media'] = fuzz.trimf(tiempo.universe,[200,350,450])
    tiempo['mucha'] = fuzz.trimf(tiempo.universe,[400,500,600])

    chocolate['poca'] = fuzz.trimf(chocolate.universe,[0,0,250])
    chocolate['media'] = fuzz.trimf(chocolate.universe,[200,350,450])
    chocolate['mucha'] = fuzz.trimf(chocolate.universe,[400,500,600])
    return agua,cafe,leche,tiempo,chocolate

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
    return [rule1,rule2,rule3,rule4,rule5,rule6]

intensidad,temperatura,tamano = definirAntecedentes()
agua,cafe,leche,tiempo,chocolate = definirConsecuentes()
reglas = definirReglas("mocaccino")
#temperatura.automf(3)
#tamano.automf(3)
#intensidad.automf(3)



temperatura.view()

tamano.view()

intensidad.view()

cafe.view()

plt.show()


######################### ESPRESSO ############################



######################### CAPUCCINO ############################
'''



######################### LATTE ############################



######################### MOKACCINO ############################


'''


tipping_ctrl = ctrl.ControlSystem(reglas)

tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['temperatura'] = 18
tipping.input['tamano'] = 20
tipping.input['intensidad'] = 2

tipping.compute()

print(tipping.output['agua'])
agua.view(sim=tipping)
cafe.view(sim=tipping)
tiempo.view(sim=tipping)
plt.show()


