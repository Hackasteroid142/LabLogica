
afirmacion(si).


intensidad(arabica,suave).
intensidad(robusta,intenso).
intensidad(combinado,medio).
intensidad(descafeinado,suave).

%preparacion(tipo,cafe,agua,leche,chocolate).
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

suma(0,_,0).
suma(N,X,Sum):- Nant is N - 1,
				suma(Nant,X,SumNuevo),
				Sum is SumNuevo + X.



cantidadIngredientes(TamanoTaza,A,Ax,B,Bx,C,Cx,D,Dx):-suma(TamanoTaza,A,Ax),
													  suma(TamanoTaza,B,Bx),
													  suma(TamanoTaza,C,Cx),
													  suma(TamanoTaza,D,Dx). 

prepararCafe(TamanoTaza,TipoPreparacion,TipoCafe,EstacionAno,Salida):-taza(TamanoTaza,X),
																	  estacion(EstacionAno,Y),
																	  intensidad(TipoCafe,Z),
																	  preparacion(TipoPreparacion,A,B,C,D),
																	  cantidadIngredientes(X,A,Ax,B,Bx,C,Cx,D,Dx),
																	  atomic_list_concat([Ax,",",Cx,",",Bx,",",Dx,",",Z,",",Y],Salida).


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

cantidadTazas(TamanoTaza,TipoPreparacion,TipoCafe,EstacionAno,CantidadCafe,CantidadLeche,CantidadAgua,CantidadChoco,Salida):-preparacion(TipoPreparacion,A,B,C,D),
																											   taza(TamanoTaza,X),
																											   cantidadIngredientes(X,A,Ax,B,Bx,C,Cx,D,Dx),
																											   numeroTazas(CantidadCafe,Ax,CantidadLeche,Cx,CantidadAgua,Bx,CantidadChoco,Dx,Numero),
																											   estacion(EstacionAno,Z),
																											   suma(Numero,Z,Sum),
																											   atomic_list_concat([Numero,",",Sum],Salida).


sePuedeUsar(Instalada,CantidadAgua,CantidadCafe,CantidadLeche):- afirmacion(Instalada),CantidadLeche>=30,CantidadCafe>=30,CantidadAgua>=150.

cambiarIntensidad(CantidadLeche,CantidadCafe,Num,Resp):-CantidadLeche>CantidadCafe,Num =\= 1, Nant is Num - 1, razonIntensidad(Resp,Num).

cambiarIntensidad(CantidadLeche,CantidadCafe,Num,Resp):-CantidadLeche>CantidadCafe,razonIntensidad(Resp,Num).

razon(Intensidad,CantidadLeche,CantidadCafe,CantidadChoco,Resp):-razonIntensidad(Intensidad,Num),
												((CantidadLeche+CantidadChoco>CantidadCafe,Num=\=1,Nant is Num - 1, razonIntensidad(Resp,Nant));
												((CantidadLeche<CantidadCafe;Num=:=1),razonIntensidad(Resp,Num))).
											  %cambiarIntensidad(CantidadLeche,CantidadCafe,Num,Resp).

intensidadCafe(TipoCafe,TipoPreparacion,Salida):-intensidad(TipoCafe,X),
												 preparacion(TipoPreparacion,A,B,C,D),
												 razon(X,C,A,D,Salida).