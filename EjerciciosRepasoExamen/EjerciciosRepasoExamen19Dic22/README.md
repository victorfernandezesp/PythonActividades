<h1>Ejercicios: </h1>
<div>
<div>
<p><h3>Ejercicio 1<br /></h3></p>
<p>Pide un DNI y comprueba que es correcto, será correcto si tiene 9 caracteres y la letra es correcta. Para calcular la letra se divide el número entre 23 y el resto indica la posición de la cadena de letras: "TRWAGMYFPDXBNJZSQVHLCKE"
CON FUNCIONES</p>


<p><h3>Ejercicio 2<br /></h3></p>
<p>Programa para una “mini” gestión de una almazara de aceite. Dicha almazara tiene como clientes a “Cosecheros”, 
que traen aceituna a la almazara, dicha aceituna se analiza en laboratorio y se calcula su “rendimiento”, que es el 
% de aceite que va a producir (es decir, si, por ejemplo, se traen 1000kg de aceituna y se determina que su 
rendimiento es de un 23.40%, eso querrá decir que se estima que dicha aceituna va a producir 234kg de aceite 
una vez procesada)
Nuestro programa debe realizar los siguientes procesos:
- En primer lugar, pedir y almacenar los datos de los cosecheros que son clientes de la almazara. Para ello 
primero se pedirá al operador del programa que indique el nº de cosecheros existentes, y, a continuación, para 
cada cosechero se pedirán lo siguientes datos: su DNI (NO hace falta comprobar que es un dni válido), su 
nombre y su localidad (texto libre, es decir, NO hay un repertorio de localidades ”predefinidas” –aunque sería 
lo suyo-)
- Una vez acabada la petición de datos de los cosecheros, el programa irá pidiendo los datos correspondientes 
a las aportaciones de aceituna. Para cada una de ellas se solicita : cosechero que trae la aceituna (debes pedirlo 
con el interfaz de usuario que te consideres más adecuado, pero, por supuesto, debe de comprobarse que el 
cosechero que se indique es efectivamente uno de los que anteriormente se almacenaron como clientes de la 
almazara), kilos de aceituna entregados (que debe comprobarse que es un número mayor o igual que cero) y 
rendimiento de dicha aceituna (para no complicar el programa supondremos que cuando se trae la aceituna 
ya se sabe el rendimiento que producirá, esto es algo que no ocurre en la realidad, la aceituna se analiza 
posteriormente, si eres capaz de ello puedes hacer que los rendimientos se introduzcan en un proceso 
posterior). El programa irá pidiendo datos hasta que se introduzca un cero en los kgs de aceituna (si lo deseas 
puedes cambiar el orden en que se piden los datos, se ha propuesto cosechero/kgs/rendimiento pero no hay 
problema si ves mejor pedirlos en otro orden). Un mismo cosechero puede haber traído aceituna más de una 
vez, no hay límite en este sentido, pero, IMPORTANTE, sí que estableceremos un límite en las capacidades 
de nuestro programa, que será que es capaz de procesar un MAXIMO de 100 entregas de aceituna (este valor 
debería estar definido en una constante, para poder ser cambiado con facilidad si se deseara)
- Finalmente, el programa pedirá el precio al que se va a liquidar el ACEITE producido a los cosecheros, será 
un valor numérico que corresponde a € por cada kilo 
Con esto habrá concluido la introducción de datos y pasaremos a calcular e imprimir los resultados solicitados
a) Un listado de cosecheros (en el que salga su dni, nombre y localidad) ordenado por nombre de localidades. 
En caso de que dos localidades coincidan, se ordenan (esas dos) por el nombre del cosechero.
b) Un listado de cosecheros en el que salga su nombre, localidad, total de kgs de aceituna aportados, total de 
kgs de aceite teórico que se producirá con su aceituna e importe que le tendremos que liquidar (pagar) 
teniendo en cuenta esa cantidad de aceite y el precio de aceite solicitado al final del proceso de petición 
de datos. De forma opcional (se valora como extra) que este listado salga ordenado por total de aceituna 
traída (de mayor a menor)
</p>
<p>Programa para gestionar los datos que genera un concurso de pesca. En este concurso han participado pescadores de una serie de provincias españolas (hay un número indeterminado a priori de pescadores de cada provincia).
Cada pescador, al finalizar la jornada, presenta un máximo de 4 capturas (sus 4 mejores pescados) al concurso (pero puede que no haya pescado 4 o que haya pescado más).

Se requiere la siguiente petición de datos: en primer lugar, pedir y almacenar los nombres de las provincias participantes, a continuación, pedir cuantos pescadores se han presentado al concurso y finalmente pedir los datos de dichos pescadores y sus capturas. Para cada pescador se pedirá: su nombre, a qué provincia pertenece (se debe de evitar que se introduzca una provincia inexistente) y los pesos de sus 4 mejores capturas. Si el pescador no tuviera esos 4 peces para presentar al concurso, se introducirá un cero en el para decir que no hay más capturas a procesar para ese pescador.

Una vez Introducidos todos los datos se pretende obtener los siguientes resultados:

a) Nombre y provincia del pescador con mayor peso total pescado (que sería el ganador del concurso).
b) Nombre y provincia del pescador que ha pescado el pez más grande (premio especial del jurado).
c) Provincia con más participantes, provincia cuyos pescadores han pescado más peces (unidades) y provincia cuyos pescadores han pescado más peso.
d) Diseñar una función que reciba como parámetro el nombre de un número "n" de pescadores y muestre sus capturas. Dicho número "N" será un número aleatorio entre 1 y 4 (usar función random int). Una vez seleccionado se pedirá al usuario que introduzca los nombres de los pescadores a mostrar.

ATENCION se ha indicado que se procesarán las 4 mejores capturas de cada pescador, pero estos datos deberían ser modificables de la manera más rápida y posible si se requiere, haciendo el mínimo cambio posible en el código. Por ejemplo, por ti mismo mientras estás haciendo las pruebas de programa: puedes poner inicialmente el número de capturas a 3 y luego cambiarlo antes de hacer la entrega. Solo se deben usar las instrucciones herramientas explicadas hasta hoy en Clase.

</p>
</div>
</div>
