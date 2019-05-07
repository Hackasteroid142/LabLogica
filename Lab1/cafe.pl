%###################################################################

%Laboratorio realizado por Alan Barahona Ruiz y Vicente Vega Toro

%Supuestos: Para calcular el cambio de intensidad se le da un valor a cada intensidad y si en el tipo de preparacion
%			la cantidad de Chocolate y Leche supera a la cantidad de cafe, este baja de intensidad, si no esta se mantiene.
%			Para el tamaño de las tazas solo se le dan valores, donde una taza grande equivale a tres pequeñas y una mediana a dos pequeñas. 

%###################################################################

%intensidad(TipoCafe,Intensidad)
%preparacion(TipoPreparacion,Cafe,Agua,Leche,Chocolate)
%estacion(EstacionAno,TiempoPreparacion)
%taza(TamanoTaza,ProporcionTaza)
%razonIntensidad(Intensidad,ValorIntensidad): Creada con la razon de poder cambiar el valor de la intensidad de ser necesario.

afirmacion(si).

intensidad(arabica,suave).
intensidad(robusta,intenso).
intensidad(combinado,medio).
intensidad(descafeinado,suave).

preparacion(espresso,7,30,0,0).
preparacion(americano,7,60,0,0).
preparacion(cortado,7,50,3,0).
preparacion(capuccino,7,150,19,0).
preparacion(latte,7,90,9,0).
preparacion(mokaccino,7,100,9,3).

estacion(verano,60).
estacion(primavera,90).
estacion(otono,90).
estacion(invierno,120).

taza(grande,3).
taza(mediana,2).
taza(pequeno,1).

razonIntensidad(suave,1).
razonIntensidad(medio,2).
razonIntensidad(intenso,3).

%###################################################################

%Entrada: N cantidad de veces a sumar, X cantidad a sumar
%Procedimiento: Entrega el valor de una sumatoria.
%Salida: Sum resultado de la sumatoria.
suma(0,_,0).
suma(N,X,Sum):- Nant is N - 1,
				suma(Nant,X,SumNuevo),
				Sum is SumNuevo + X.


%Entrada: TamanoTaza es el tamaño de la taza, Cafe, Agua, Leche y Chocolate son la cantidad de ingredientes que se utilizan en la preparacion.
%Procedimiento: Por cada ingredientes se suman hasta alcanzar la cantidad de veces que puedan estar en la taza.
%Salida: CafeIngre, AguaIngre, LecheIngre y ChocolateIngre es la cantidad de ingredientes que caen dentro de la taza.
cantidadIngredientes(TamanoTaza,Cafe,CafeIngre,Agua,AguaIngre,Leche,LecheIngre,Chocolate,ChocolateIngre):-suma(TamanoTaza,Cafe,CafeIngre),
																										  suma(TamanoTaza,Agua,AguaIngre),
																										  suma(TamanoTaza,Leche,LecheIngre),
																										  suma(TamanoTaza,Chocolate,ChocolateIngre). 

%Entrada:TamanoTaza es el tamaño de la taza, TipoPreparacion es la preparacion del cafe, TipoCafe es el cafe a usar y EstacionAno es la estacion en la que se realiza el cafe. 
%Procedimiento: Busca el tiempo de preparacion, la intensidad del cafe y busca los ingredientes que se necesita en la preparacion para poder calcular cuanto se necesita para realizar el cafe.
%Salida: Salida es una lista con las intrucciones para realizar el cafe, en el siguiente orden [Cafe,Leche,Agua,Chocolate,Intensidad,Tiempo].
prepararCafe(TamanoTaza,TipoPreparacion,TipoCafe,EstacionAno,Salida):-taza(TamanoTaza,Tamano),
																	  estacion(EstacionAno,TiempoPreparacion),
																	  intensidad(TipoCafe,IntensidadCafe),
																	  preparacion(TipoPreparacion,Cafe,Agua,Leche,Chocolate),
																	  cantidadIngredientes(Tamano,Cafe,CafeIngre,Agua,AguaIngre,Leche,LecheIngre,Chocolate,ChocolateIngre),
																	  atomic_list_concat([CafeIngre,",",LecheIngre,",",AguaIngre,",",ChocolateIngre,",",IntensidadCafe,",",TiempoPreparacion],Salida).

%Entrada: CantidadCafe,CantidadLeche,CantidadAgua y CantidadChoco son la cantidad total de ingredientes para preparar N tazas de cafe.
%		  CafeIngre,LecheIngre,AguaIngre y ChocoIngre es la cantidad de ingrediente que requiere la preparacion.  
%Procedimiento: Resta la cantidad de ingredientes que necesita la preparacion a los ingredientes totales hasta que no se pueden preparar mas casos. 
%				Cada llamado se considera una taza.
%Salida: Numero  es la cantidad de tazas que se pueden preprarar.
numeroTazas(CantidadCafe,CafeIngre,CantidadLeche,LecheIngre,CantidadAgua,AguaIngre,CantidadChoco,ChocoIngre,Numero):-CantidadCafe>=CafeIngre,
																							CantidadAgua>=AguaIngre,
																							CantidadLeche>=LecheIngre,
																							CantidadAguaAnt is CantidadAgua - AguaIngre,
																							CantidadCafeAnt is CantidadCafe - CafeIngre,
																							CantidadLecheAnt is CantidadLeche - LecheIngre,
																							CantidadChocoAnt is CantidadChoco - ChocoIngre,
																							numeroTazas(CantidadCafeAnt,CafeIngre,CantidadLecheAnt,LecheIngre,CantidadAguaAnt,AguaIngre,CantidadChocoAnt,ChocoIngre,NumeroNuevo),
																							Numero is NumeroNuevo + 1.

numeroTazas(_,_,_,_,_,_,_,_,0).

%Entrada: TamanoTaza es el tamaño de la taza, tipo preparacion es la preparacion a realizar, TipoCafe es el cafe que se utiliza, EstacionAno es la estacion en la que se esta y
%		  CantidadLeche, CantidadAgua, CantidadChoco, CantidadCafe es la cantidad total de ingredientes con los que se quiere calcular.
%Procedimiento: Se buscan los datos para calcular la cantidad de ingredientes que requiere la preparacion, a lo que se llama a la funcion numeroTazas() para obtener el numero
%				de tazas que se pueden preparar. Luego, se calcula el tiempo que se toma preparar las tazas segun la cantidad de tazas se pueden preparar y en que estacion del año se esta.
%Salida: Lista con los datos de las taza en el orden de [Numero de tazas a realizar, Tiempo total de preparacion]
cantidadTazas(TamanoTaza,TipoPreparacion,TipoCafe,EstacionAno,CantidadCafe,CantidadLeche,CantidadAgua,CantidadChoco,Salida):-preparacion(TipoPreparacion,Cafe,Agua,Leche,Chocolate),
																											   taza(TamanoTaza,Tamano),
																											   cantidadIngredientes(Tamano,Cafe,CafeIngre,Agua,AguaIngre,Leche,LecheIngre,Chocolate,ChocolateIngre),
																											   numeroTazas(CantidadCafe,CafeIngre,CantidadLeche,LecheIngre,CantidadAgua,AguaIngre,CantidadChoco,ChocolateIngre,Numero),
																											   estacion(EstacionAno,Tiempo),
																											   suma(Numero,Tiempo,Sum),
																											   atomic_list_concat([Numero,",",Sum],Salida).


%Entrada: Instalada es la afirmacion/negacion de si esta instalada la cafetera, CantidadAgua, CantidadLeche y CantidadCafe es la cantidad de ingredientes que se le puede hechar a la cafetera.
%Procedimiento: Revisa variables y las compara para saber si la cafetera se puede implementar.
%Salida: True o False.
sePuedeUsar(Instalada,CantidadAgua,CantidadCafe,CantidadLeche):- afirmacion(Instalada),CantidadLeche>=30,CantidadCafe>=30,CantidadAgua>=150.

%Entrada: Intensidad del cafe, CantidadLeche, CantidadCafe,CantidadChoco son la cantidad de ingredientes que necesita la preparacion. 
%Procedimiento: Busca el valor de la intensidad y si la suma de la leche con el chocolate es mayor y la intensidad no es suave, entonces se le baja una intensidad al cafe.
%				Si no el cafe se mantiene su intensidad.
%Salida: Intensidad resultante segun la preparacion.
razon(Intensidad,CantidadLeche,CantidadCafe,CantidadChoco,Resp):-razonIntensidad(Intensidad,Num),
												((CantidadLeche+CantidadChoco>CantidadCafe,Num=\=1,Nant is Num - 1, razonIntensidad(Resp,Nant));
												((CantidadLeche<CantidadCafe;Num=:=1),razonIntensidad(Resp,Num))).

%Entrada: TipoCafe es el cafe a utilizar, TipoPreparacion es la preparacion que se quiere realizar.
%Procedimiento: Busca la intensidad actual del cafe y los ingredientes que utiliza la preparacion que se quiere, entonces se verifica si la intensidad del cafe debe bajar.
%Salida:Intensidad final del cafe preparado.
intensidadCafe(TipoCafe,TipoPreparacion,Salida):-intensidad(TipoCafe,IntensidadCafe),
												 preparacion(TipoPreparacion,Cafe,Agua,Leche,Chocolate),
												 razon(IntensidadCafe,Leche,Cafe,Chocolate,Salida).