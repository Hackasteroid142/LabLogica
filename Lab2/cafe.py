import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl


temperatura = ctrl.Antecedent(np.arange(0,101,1),'temperatura')
tamano = ctrl.Antecedent(np.arange(0,151,1),'tamano')
intensidad = ctrl.Antecedent(np.arange(0,6,1),'intensidad')

agua = ctrl.Consequent(np.arange(0,601,1),'agua')
cafe = ctrl.Consequent(np.arange(0,601,1),'cafe')
leche = ctrl.Consequent(np.arange(0,601,1),'leche')
tiempo = ctrl.Consequent(np.arange(0,601,1),'tiempo')

temperatura.automf(3)
tamano.automf(3)
intensidad.automf(3)

agua['baja'] = fuzz.trimf(agua.universe,[0,0,250])
agua['media'] = fuzz.trimf(agua.universe,[200,350,450])
agua['alta'] = fuzz.trimf(agua.universe,[400,500,600])

cafe['poca'] = fuzz.trimf(cafe.universe,[0,0,250])
cafe['media'] = fuzz.trimf(cafe.universe,[200,350,450])
cafe['mucha'] = fuzz.trimf(cafe.universe,[400,500,600])

leche['poca'] = fuzz.trimf(leche.universe,[0,0,250])
leche['media'] = fuzz.trimf(leche.universe,[200,350,450])
leche['mucha'] = fuzz.trimf(leche.universe,[400,500,600])

tiempo['poca'] = fuzz.trimf(tiempo.universe,[0,0,250])
tiempo['media'] = fuzz.trimf(tiempo.universe,[200,350,450])
tiempo['mucha'] = fuzz.trimf(tiempo.universe,[400,500,600])

temperatura.view()

tamano.view()

intensidad.view()

cafe.view()

plt.show()



rule1 = ctrl.Rule(temperatura['poor'] & tamano['poor'] & intensidad['poor'],(agua['baja'], cafe['poca']))

rule2 = ctrl.Rule(temperatura['average'] & tamano['poor'] & intensidad['good'],(agua['baja'], cafe['media']))

rule3 = ctrl.Rule(temperatura['average'] & tamano['average'] & intensidad['average'],(agua['media'], cafe['poca']))

rule4 = ctrl.Rule(temperatura['good'] & tamano['average'] & intensidad['poor'],(agua['media'], cafe['media']))

rule5 = ctrl.Rule(temperatura['average'] & tamano['good'] & intensidad['poor'],(agua['alta'], cafe['media']))

rule6 = ctrl.Rule(temperatura['poor'] & tamano['good'] & intensidad['good'],(agua['alta'], cafe['media']))


tipping_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5])

tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['temperatura'] = 20
tipping.input['tamano'] = 340
tipping.input['intensidad'] = 2

tipping.compute()

print(tipping.output['agua'])
agua.view(sim=tipping)
cafe.view(sim=tipping)
plt.show()


