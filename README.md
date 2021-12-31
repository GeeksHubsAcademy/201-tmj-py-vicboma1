<p align="center">
    <img src="https://github.com/GeeksHubsAcademy/2020-geekshubs-media/blob/master/image/logo.png" >	
</p>


    Considere el siguiente problema:

    Escriba un programa corto que permita re-calcular el posicionamiento de los elementos dentro de un array.
	La dirección de moviento debe de ser en el orden contrario a las agujas del reloj.
    
    Se atiente al siguiente ejemplo:
       
	 Array			Mov		Resultado

    [2,3,5]      		2     		[5,2,3]   
    
	[0,2,8,6,7,8]      	5     		[8,0,2,8,6,7] 
   
    Para los casos excepcionales :
		- Un input nulo, no definido, NAN o array vacío debe devolver -1.
		- Arrays con el mismo número de elementos debe de devolver un array con un solo elemento.
    ``

    En la carpeta 'src/kata.py' se encuentra el fichero con la 
    definición de nuestro método vacío.
    En la carpeta 'tests/test_kata.py'se encuentra el fichero 
    con la suite de test.

    El modus operandi de trabajo es el siguiente:
    
    Debes 'forkear' el proyecto a tu cuenta.
    Puedes hacer PR's ilimitadas e ir validando poco a poco la solución contra nuestro respositorio con CI.
    Puedes trabajar en local y subir la solución haciendo un PR a nuestro repositorio.
    Cuando se envíe la PR final, debes indicar el tiempo de dedicación y los intentos que has hecho.
    También puedes añadir un comentario para dar cualquier tipo de feedback.
    
    En caso de duda, revisa en el apartado de 'Referencias'.
    
    Results :
    
    tests/test_kata.py::Test_kata::test_apply_1 PASSED                       [ 11%]
    tests/test_kata.py::Test_kata::test_apply_2 PASSED                       [ 22%]
    tests/test_kata.py::Test_kata::test_apply_3 PASSED                       [ 33%]
    tests/test_kata.py::Test_kata::test_apply_4 PASSED                       [ 44%]
    tests/test_kata.py::Test_kata::test_apply_5 PASSED                       [ 55%]
    tests/test_kata.py::Test_kata::test_apply_6 PASSED                       [ 66%]
    tests/test_kata.py::Test_kata::test_apply_7 PASSED                       [ 77%]
    tests/test_kata.py::Test_kata::test_apply_8 PASSED                       [ 88%]
    tests/test_kata.py::Test_kata::test_apply_9 PASSED                       [100%]

=========================== 9 passed in 0.04 seconds ===========================
    
 ## Referencias

* [Tutorial - Testing Automatizado](https://github.com/GeeksHubsAcademy/2020-js-vanilla-testing-FFFF/blob/master/README.md)

