#guardar_estadisticas
import random
adjetivos = ['valiente', 'hermoso', 'torpe', 'odiado', 'temido', 'avaricioso', 'astuto', 'incauto', 'sucio']
amigos = ['Boole', 'Bernoulli', 'Euler', 'Alan Turing', 'Raabe',\
     'Weierstrass', 'Riemann', 'Lagrange', 'Bolzano', 'Gauss', 'Newton', 'Taylor', 'Mc-Laurin', 'Hooke']
temario = [
'el concepto de L(S)', 'el teorema de Reflexividad Dual', 'la equivalencia del logaritmo', 'las V.A. multivariantes',
'su fallo en el examen de física', 'la diapositiva de "el hecho religioso"', 'el motivo de modularizar el código',
'las sumas de series telescópicas', 'cómo funcionan los objetos de Python', 'los diccionarios de Python',
'la fórmula de Bernoulli para fluidos',
'por qué sus compañeros del MTC eran tan inútiles', 'la clase del día anterior de David Alfaya',
'la temperatura a la que hay que poner el aire acondicionado en clase para que la gente no se queje',
'la manera de escanear el QR de asistencia a la primera', 'de dónde había conseguido rascar 0,25 puntos en cálculo',
'los ejercicios de topología en 3 o más dimensiones',
'la demostración de la desigualdad triangular aplicada a la distancia euclídea',
'la clave para seguir las explicaciones de MATLAB de David Alfaya sin quedarse atrás',
'qué es una condición necesaria pero no suficiente', 'la manera de sobornar a David Alfaya para que te apruebe',
'las preguntas 10 del MTC de Álgebra y Cálculo', 'por qué no le funciona el matplotlib.pyplot',
'el diseño óptimo de péndulo para sacar mediciones legibles en phyphox y además no estampar su móvil en el proceso',
'que estudiar la semana de antes no ayuda casi nada y hay que llevar el temario al día',
'los anuladores de subespacios vectoriales', 'los problemas de la hoja B sin mirar las soluciones',
'la manera de identificar una serie numérica y el criterio a utilizar en cada caso',
'para qué sirven los créditos de las asignaturas', 'el orden de los infinitésimos y los infinitésimos estándares',
'a qué se refiere David Contreras cuando usa el término "slicing"', 'que Visual Studio Code es mucho mejor entorno de programación que Jupyter',
'que hacer treinta y siete módulos de python para un programa que se puede resolver en 80 líneas es contraproducente',
'que este es el mejor proyecto final de programación sin lugar a dudas y merece una nota acorde',
'la manera en la que se calcula la nota de Álgebra y Cálculo',
'que la dimensión de un subespacio más la de su anulador es igual a la dimensión del espacio ambiente',
'dónde vive cada vector en una demostración de Álgebra', 'la relación entre la derivada de una función y la de su inversa',
'por qué en algunos casos se puede hacer equivalencias y en otros hay que usar taylor'
]

nombre_str = 'Escobas'
clase = 'mago'
class A():
    def __init__(self): 
        self.exp = 1075
player = A()
text =  open('Estadísticas.txt', 'a')
text.write(f'''
==================================================================================================================
Aquí yace {nombre_str.rstrip()}, el {clase} más 
{random.choice(adjetivos)} que haya puesto pie en este reino. 
La leyenda dice que logró comprender
{random.choice(temario)}
justo antes de su muerte. Muchos dudan
que sea cierto, pero si en algún momento 
lo supo, esta valiosa sabiduría le
acompañó a la tumba. 
Además, Alcanzó una puntuación de {player.exp}.
Tu amigo {random.choice(amigos)} te recuerda, aunque tú no recuerdes su fórmula.
Gracias por haber jugado.
==================================================================================================================
''')
text.close()
