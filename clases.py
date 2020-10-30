# -*- coding: utf-8 -*-
"""Clases.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fN2JLNMEB6_SbYEJhNcGIp1Ky_sK6VG9

# 2. Clases

## 2.1 Introducción
Programación Orientada Objetos es uno de los paradigmas más efectivos al momento de querer desarrollar algún tipo de software.En este pardigma se desarrollan *clases* que que representan cosas y/o situaciones, y de las clases se derivan los objetos.

Cuando se desarrola una clase, se define de manera general el comportamiento de toda una gama de objetos relacionados a la semántica.

Cuando se declara o define un objeto de una clase, cada objeto es equpado de manera automática con el comportamiento general de la clase, después se puede ir defiendo de manera más dellada el objeto. 

Cuando se dice que se *crea una instancia de una clase* se hace referencia a la creación de un objeto derivado de una clase en particular, y dentro del programa principal se trabaja con la instancia, no con la clase tal cual.

## 2.2 Creando y usando una clase

Se puede modelar casi cualquier cosa utilizando clases. En esta sección comenzaremos a definir una clase `Perro` que  describa a cualquier tipo de perro, ninguno en particular. Inicialmente se considerarán sólo dos campos el `Nombre` y la `Edad`, ya que en cualquier mascota perro son comunes. Una vez definida la clase se mostrará la forma de poder generar dos instancias (objetos) de esta clase. Se definirán dos acciones `Sentarse` y `Rodar`. 

### 2.2.1 Creando la clase perro
Cada instancia creada de la clase `Perro` deberá tener un `Nombre` y la `Edad`, observe la siguiente celda.
"""

class Perro():
    """Un modelo muy abstacto de un Perro"""
    
    def __init__(self,Nombre,Edad):
        """Inicializa los atributos de Nombre y Edad"""
        self.Nombre = Nombre
        self.Edad = Edad
        
    def Sentarse(self):
        """Simula a un perro sentarse después de que se le da orden"""
        print(self.Nombre.title() + " está sentado.")
        
    def Rodar(self):
        """Simula a un perro rodarse en el piso después que se le da la orden"""
        print(self.Nombre.title() + " está rodando.")

"""Hay muchos elementos que se deben de analizar con detalle, observe que la sintaxis para definir una clase es 

`class <Nombre_clase>():`

donde `Nombre_clase` es el nombre de la clase, observe que las siguientes líneas debn de estar indentadas ya que así lo pide python para el alcance de las funciones y de las variables. 

Se pueden visualizar tres funciones dentro de la clase y todas ellas tienen como argumeto `self` que implica que éstas funciones pertenecen a la estructura de la clase. observe que los comportamientos `Sentarse(self)` y `Rodar(self)` son comportamientos o clases que se definen por el usuario, a éstas funciones se le conocen como **METODOS** y son definidos completamente por el usuario. 

La primer función `def __init__(self,Nombre,Edad)` se le conoce como constructor, observe que tiene los campos de Nombre y Edad, que son los campos que se habían considerando comunes entre los perros, observe que dentro de esa función hay dos elementos `self.Nombre` y `self.Edad`, a estos elementos se le conocen como atributos y y deben de llevar el prefijo `self.` ya esta directiva indica que son elementos propios de la clase.

### 2.2.2 Creando una instancia de una clase
Una clase puede ser vidat como un conjunto de instrucciones para realizar un objet. La clase `Perro` es un conjutno de instrucciones que le indica a Python coo crear instancias indiiduales que representen perros de forma general.

En la siguiente celda se muestra la manera de hacer un perro específico pero basádonos en la clase `Perro`
"""

mi_perro = Perro('Orejas',7)
print("El nombre de mi perro es " + mi_perro.Nombre.title() + ".")
print("La edad de mi perro es " + str(mi_perro.Edad) + " anios.")

"""En la línea 1 de la celda anterior, se genera un objeto de la clase `Perro` y manda a llamar al constructor, el string `'Orejas'` lo asigna a attibuto `self.Nombre`, mientras que el número `7` lo asigna al atributo `self.Edad`. 

### 2.2.3 Accediendo a atributos y métodos

Observe que en la anterior en la línea 2 y 3 se está accediendo a los atributos de una clase, para esto se debe de tener en cueta el nombre de la instancia (objeto), que en este caso es `mi_perro` y después se debe de poner el nombre del atributo acompañado previamente de un `.` De tal manera que con `mi_perro.Edad` se está accediendo al atributo de Edad.

De la misma manera se puede acceder a los métodos de una clase, de tal forma que si se utiliza la instrucción `mi_perro.Sentarse()` se estaría invocando el método sentarse propio de la clase `Perro` como se muestra en la siguiente celda.
"""

mi_perro = Perro('Orejas',7)
print("El nombre de mi perro es " + mi_perro.Nombre.title() + ".")
print("La edad de mi perro es " + str(mi_perro.Edad) + " anios.")

mi_perro.Sentarse()
mi_perro.Rodar()

"""### 2.2.4 Creando múltiples instancias.
Se pueden crear tantas instancias como lo desee de una sóla clase, la única condición que debe de tener en cuenta es que los nombres de las instancias deben de ser distantas aunque los atributos que sean iguales, observe la siguente celda.
"""

mi_perro = Perro('Orejas',7)
tu_perro = Perro('Bony',8)

print("El nombre de mi perro es: " + mi_perro.Nombre.title())
print(mi_perro.Nombre.title() + " tiene " + str(mi_perro.Edad) + " anios de edad.")
print("\n")

print("El nombre de tu perro es: " + tu_perro.Nombre.title())
print(tu_perro.Nombre.title() + " tiene " + str(tu_perro.Edad) + " anios de edad.")

"""## 2.3 Ejercicios

1. **Restaurante:** a) Crear una clase llamada `Restaurant`. El método `__init__()` debe de aceptar dos atributos: El `nombre_restaurant` y el `tipo_cocina`.b) Crear un método que se llame `describe_restaurant` que imprima: *El nombre del restaurant es: ------* y *El tipo de comida que se sirve es: -------*. c) Generar
2. **Tres Restaurantes:** Crear tres restaurantes utilizando la clase que se ha definido con anterioridad y llame al método `describe_restaurant` para cada instancia de la clase. 
3. **Usuarios:** a) Cree una clase que se llame `Usuario`. b)Cree dos atributos llamados `Nombre` y `Apellido`, agregue atributos como `CURP`,`Fecha_Nacimiento`, `Sexo`, `Grado_estudios`. c)Genere un método llamado `Saluda_usuario` y que despliegue en pantalla algo como *Hola Juan Ruiz de Alarcón*. d)Genere un método que se llame `Describe_usuario` y que muestre toda la información del usuario. e)Genere 5 objetos tipo usuario y ejecute los dos métodos anteriormente descritos.
"""

#1.RESTAURANTE
class Restaurant():

    def _init_(self,nombre,tipo_cocina):
      self.nombre=nombre 
      self.tipo_cocina=tipo_cocina

    def describe_restaurant(self): 
      print("El restaurant se llama " + self.nombre.title() + " y sirven comida estilo" + self.tipo_cocina.title() + "." )

restaurant_1 = Restaurant("Thai "," Estadounidense ")
restaurant_1.describe_restaurant()

#2.TRES RESTAURANTES
restaurant_1 = Restaurant("Thai ","Estadounidense")
restaurant_2 = Restaurant("La Mansión ","Mexicana" )
restaurant_3 = Restaurant("Pielago ","sabor a mar")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

#3.USUARIOS
class usuario(): 
    def _init_(self,nombre,apellido,edad,oficio):
      self.nombre=nombre
      self.apellido=apellido
      self.edad=edad
      self.oficio=oficio

    def saluda_usuario(self):
      print("Hola "+ self.nombre.title() + " " + self.apellido.title() + ".")
    
    def describe_usuario(self):
      print("Sus datos son los siguientes: ")
      print("Nombre: " + self.nombre + " " + self.apellido)
      print("Edad: " + str(self.edad) + " Años")
      print("Oficio: " + self.oficio )
      print("\n")

usuario_1=usuario("","A",32,"estudiante")
usuario_2=usuario("B", "Arteaga", 23, "Empresario")
usuario_3=usuario("X"4 "Mendoza", 27, "Conserje")
usuario_4=usuario("2", "Torres", 19, "Artista")
usuario_1.describ   Z
usuario_2.describe_usuario()
usuario_3.describe_usuario()
usuario_4.describe_usuario()

"""## 2.4 Trabajando con Clases e instancias

### 2.4.1 Introducción
Una vez que se desarrollado la clase, la mayor parte del tiempo se trabaja con las instancias de la clase más que con la clase misma. Es necesario saber cómo acceder a los atributos , esto se puede hacer de manera directa o indirecta. 

Observe la siguiente celda de código, donde se presenta una clase tipo `Carro`
"""

class Carro():
    """Clase carro"""
    
    def __init__(self, modelo, marca, anio):
        """Inicializa los atributos del carro"""
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def Describe_Carro(self):
        """Imprime la descripción del carro creado"""
        Descripcion = str(self.anio) + ' ' + self.marca + ' ' + self.modelo
        return Descripcion.title()
    
mi_auto = Carro('a4','audi',2020)
print(mi_auto.Describe_Carro())

"""En la línea *1* se define la clase `Carro()`, en la línea *4* está el constructor que pide la marca, modelo y año del auto. En la línea *10* está el atributo `Describe_Carro()`. En la línea *15* se muestra la creación del un objeto tipo `Carro` y en la siguiente línea se muestra el uso del único método de la clase.

### 2.4.2 Definiendo atributos predeterminados en las clases
Cada atributo en la clase necesita un valor inicial, no importa si es 0 o una cadena de caracteres vacía. En ocasiones hay atributos que no se mandarán como argumentos en el constructor, sin embargo, dentro del constructor se deben de inicializar. Observe el siguiente código.
"""

class Carro():
    """Clase carro"""
    
    def __init__(self,modelo,marca = 'Nissan', anio=2020):
        """Inicializa los atributos del carro"""
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0
    
    def Describe_Carro(self):
        """Imprime la descripción del carro creado"""
        Descripcion = str(self.anio) + ' ' + self.marca + ' ' + self.modelo
        return Descripcion.title()
    
    def muestra_Kilometraje(self):
        """Imprime el kilometraje del auto"""
        print("Este auto tiene " + str(self.kilometraje) +" kilómetros recorridos")
        
    
mi_auto = Carro('audi','a4',2020)
print(mi_auto.Describe_Carro())
mi_auto.muestra_Kilometraje()

mi_auto_2 = Carro(anio = 2019, marca = 'Nissan',modelo='Sentra')
print(mi_auto_2.Describe_Carro())
mi_auto.muestra_Kilometraje()

mi_auto_3 = Carro(modelo = 'Versa')
print(mi_auto_3.Describe_Carro())
mi_auto_3.muestra_Kilometraje()

"""Observe que en la línea *9* está el atributo kilometraje que se está inicializando con un valor numérico de *0*. El atributo de `kilometraje` no está como atributo en la función que define el constructor, sin embargo, si debe de estar inicializado en el cuerpo del constructor. 

Observe también que en la celda anterior, ya se pusieron algunos valores predeterminados para los atributos del constructor.

En la clase también se ha generado un método para poder imprimir el kilometraje de cada auto.

En la creación de los objetos se muestra que el constructor tiene propiedades de funciones y de argumentos posicionales.

### 2.4.3 Modificando los valores de los atributos
Existen dos maneras de poder modificar los atributos de de una clase, la primera es de manera directa y aunque es lo más fácil y directo no es muy recomendable ya que el usuario de manera accidental podría modificar el valor de ciertos atributos que sólo deberían de ser tratados internamente (dentro de la clase) y no deberían de estar disponibles para los usuarios, a este hecho se le conoce como encapsulamiento. 

La otra forma que es la más recomendable y es propia del encapsulamiento es a través de métodos, además que cuando se hace a través de métodos se puede agregar cierta lógica en la manera en que se deben de modificar los atributos. 

#### 2.4.3.1 Modificando los valores de manera directa.
La manera más simple y sencilla par amodificar los valores de los atributos es acceder a ellos de manera directa, observe la siguiente celda, donde se modificará el valor del kilometraje de un auto
"""

class Carro():
    """Clase carro"""
    
    def __init__(self,modelo,marca = 'Nissan', anio=2020):
        """Inicializa los atributos del carro"""
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0
    
    def Describe_Carro(self):
        """Imprime la descripción del carro creado"""
        Descripcion = str(self.anio) + ' ' + self.marca + ' ' + self.modelo
        return Descripcion.title()
    
    def muestra_Kilometraje(self):
        """Imprime el kilometraje del auto"""
        print("Este auto tiene " + str(self.kilometraje) +" kilómetros recorridos")
        
    
mi_auto = Carro('audi','a4',2020)
print(mi_auto.Describe_Carro())
mi_auto.muestra_Kilometraje()

# Modificando el atributo de manera directa
mi_auto.kilometraje = 50

#Mostrando el kilometraje para verificar que realmente se ha modificado
mi_auto.muestra_Kilometraje()

"""A veces esta forma de modificar puede funcionar, pero... ¿Qué pasaría si se le quisiera poner un kilometraje negativo al auto?.... La respuesta es que numéricamente se puede hacer eso, sin embargo, lógicamente no puede ser posible, o si el auto tiene 200 km recorridos ¿Se podría disminuir ese kilometraje?... La respuesta es similar, numéricamente si, aunque lógicamente no se debería de poder.

#### 2.4.3.2  Modificando los atributos  a través de un método

PUede ser útil métodos que puden modificar los atributos y noacceder a los atributos de manera directa, la idea es generar un atributo (función) que reciba el valor y que modifique el atributo de la clase, en la siguiente celda se muestra un ejemplo.
"""

class Carro():
    """Clase carro"""
    
    def __init__(self,modelo,marca = 'Nissan', anio=2020):
        """Inicializa los atributos del carro"""
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0
    
    def Describe_Carro(self):
        """Imprime la descripción del carro creado"""
        Descripcion = str(self.anio) + ' ' + self.marca + ' ' + self.modelo
        return Descripcion.title()
    
    def muestra_Kilometraje(self):
        """Imprime el kilometraje del auto"""
        print("Este auto tiene " + str(self.kilometraje) +" kilómetros recorridos")
    
    def Leer_Kilometraje(self,valor_usuario):
        """Asigna el valor de de valor_usuario a kilometraje"""
        self.kilometraje = valor_usuario
        
    
mi_auto = Carro('audi','a4',2020)
print(mi_auto.Describe_Carro())
mi_auto.muestra_Kilometraje()

# Modificando el atributo de manera directa
mi_auto.Leer_Kilometraje(60)

#Mostrando el kilometraje para verificar que realmente se ha modificado
mi_auto.muestra_Kilometraje()

"""Observe que  en la línea *20* se ha puesto un método que además de tener como atributo *self* que indica pertenencia a una clase, se ha agregado otro argumento llamado **valor_usuario** y en la línea *23* se le asigna el valor de *valor_usuario* al atributo *self.kilometraje*.

En la línea *30* se invoca el método y se le manda el valor de `60`, y en la línea `33` se muestra el efecto de haber cambiado el kilometraje.

Sin embargo, este método no muestra ninguna ventaja respecto al hecho de poder modificar el atributo de manera directa. Una gran ventaja de modificar el atributo utilizando métodos es que cuando se quiere hacer con métodos se puede agregar un procesamiento de los argumentos de entrada, tal como se muestra en la siguiente celda.
"""

class Carro():
    """Clase carro"""
    
    def __init__(self,modelo,marca = 'Nissan', anio=2020):
        """Inicializa los atributos del carro"""
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0
    
    def Describe_Carro(self):
        """Imprime la descripción del carro creado"""
        Descripcion = str(self.anio) + ' ' + self.marca + ' ' + self.modelo
        return Descripcion.title()
    
    def muestra_Kilometraje(self):
        """Imprime el kilometraje del auto"""
        print("Este auto tiene " + str(self.kilometraje) +" kilómetros recorridos")
    
    def Leer_Kilometraje(self,valor_usuario):
        """Asigna el valor de de valor_usuario a kilometraje"""
        if valor_usuario >= self.kilometraje:
            print("Asignación correcta")
            self.kilometraje = valor_usuario
        else:
            print("Asignación incorrecta, no se ha llevado a cabo")
        
    
mi_auto = Carro('audi','a4',2020)
print(mi_auto.Describe_Carro())
mi_auto.muestra_Kilometraje()

# Modificando el atributo de manera directa
mi_auto.Leer_Kilometraje(60)

# Mostrando el kilometraje para verificar que realmente se ha modificado
mi_auto.muestra_Kilometraje()

# Modificando el kilometraje, utilizando un valor menor
mi_auto.Leer_Kilometraje(20)

# Mostrando el kilometraje actual
mi_auto.muestra_Kilometraje()

"""El método `Leer_Kilometraje(self,valor_usuario)`, se ha modificado observe que ahora verifica si el valor por el que se quiere modificar el kilometraje es mayor o igual al kilometraje que el auto tiene, si se cumple la condición imprimirá `Asignación correcta` y ejecutará la asignación del valor del usuario al kilometraje del auto. Si el kilometraje es menor, muestra un error y la asginación no se lleva a cabo.

En la línea `34` se hace una modificación correcta y en la línea `37` se muestra el kilometraje actual que es de `60km`, y en la línea `40` se muestra una asginación incorrecta, en la línea `43` se muestra el kilometraje actual del auto y observe que sigue siendo `60km`, ya que la segunda asignación fue incorrecta y no se llevó a cabo.

En la siguiente celda, se muestra un segundo ejemplo, en el que se agrega otro método que ayuda a ir aumentando el kilometraje
"""

class Carro():
    """Clase carro"""
    
    def __init__(self,modelo,marca = 'Nissan', anio=2020):
        """Inicializa los atributos del carro"""
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0
    
    def Describe_Carro(self):
        """Imprime la descripción del carro creado"""
        Descripcion = str(self.anio) + ' ' + self.marca + ' ' + self.modelo
        return Descripcion.title()
    
    def muestra_Kilometraje(self):
        """Imprime el kilometraje del auto"""
        print("Este auto tiene " + str(self.kilometraje) +" kilómetros recorridos")
    
    def Leer_Kilometraje(self,valor_usuario):
        """Asigna el valor de de valor_usuario a kilometraje"""
        if valor_usuario >= self.kilometraje:
            print("Asignación correcta")
            self.kilometraje = valor_usuario
        else:
            print("Asignación incorrecta, no se ha llevado a cabo")
            
    def Actualizar_Kilometraje(self,valor_suma):
        """Suma el valor del usuario al kilometraje del auto"""
        if valor_suma >= 0:
            print("Incremento correcto")
            self.kilometraje += valor_suma
            #self.kilometraje = self.kilometraje + valor_suma
        else:
            print("Incremento incorrecto, no se llevará a cabo")
        
    
mi_auto = Carro('audi','a4',2020)
print(mi_auto.Describe_Carro())
mi_auto.muestra_Kilometraje()

# Modificando el atributo de manera directa
mi_auto.Leer_Kilometraje(60)

# Mostrando el kilometraje para verificar que realmente se ha modificado
mi_auto.muestra_Kilometraje()

# Sumar 20 km al kilometraje actual
mi_auto.Actualizar_Kilometraje(20)

# Mostrando el kilometraje actual
mi_auto.muestra_Kilometraje()

#Modificando el kilometraje utilizando un valor negativo
mi_auto.Actualizar_Kilometraje(-10)

# Mostrando el kilometraje actual
mi_auto.muestra_Kilometraje()

"""### 2.4.4 Ejercicios

1. **Clientes atendidos:**   Retomar la clase de **Restaurante** que se generó a lo largo de este *notebook* y agregar un atributo que `clientes_atendidos`  y agregar dos métodos: 
    1. `Clientes_Atendidos(self,numero):` que pueda modificar el número de clientes
        2.`Aumenta_Clientes(self,numero):` que pueda aumentar el número de clientes que se han atendido
        
2. **Control de acceso**    Acompletar el código de la siguiente celda, que crea una clase Usuario, donde el constructor debe de aceptar el nombre de usuario y la contraseña, cuando se invoque el método `ingresar` debe de pedir la contraseña del usuario, si la contraseña es correcta, debe de imprimir `Bienvenido a su cuenta`, si la contraseña se ingresa incorrectamente 3 veces debe de imprimir `Cuenta bloquead, intente más tarde` y debe de reiniciar la varialbe `self.intentosAcceso` a cero.
"""



class User():
    def __init__(self,Nickname,password):
        self.nombre_usuario = Nickname
        self.password = password
        self.intentosAcceso = 0
        
    def ingresar(self):
        while(1):
            cont = input("Ingrese su contraseña:")
            if :
                prit("Bienvenido ")
                
            else:
                print("Contraseña incorrecta")
                
                if self.intentosAcceso == 3:
                    print("C, intente más tarde")
                    break

user1 = User('Juan','juan1234')
user1.ingresar()

"""## 2.5 Herencia

Al momento de iniciar un nuevo programa o proyecto, no necesariamente se debe de comenzar desde cero y definr las clases y todos los slementos propios para le nuevo proyecto, se puede reciclar y reutilizar código de proyectos anteriores, por ejemplo es muy común que las bases de datos tengan varios campos en común, en vez de ir desarrollando cada campo de manera individual se utiliza una clase base y que de ésta clase base se derive una clase secundaria que contenga todos elementos de la clase base, a este hecho se le conoce como herencia.


Cuando una clase es heredada o ha sido derivada de otra clase, hereda todos atributos y métodos de la primera clase. La calse original se le conoce como *clase padre*, y a la nueva clase se le conoce como *clase hijo*.La clase hijo o hija hereda todos los atributs y métodos de la clase pdre pero también es libre de poder definir atributos y métodos propios que la diferencian de la clase padre.

### 2.5.1 El constructor de la clase hijo

Como se ha comentado anteriormente el método que tien *def __init__()* se le conoce como el constructor de la clase, y todas las clases deben de dener un constructor. A continuación se retoma la clase `Carro` con la que se han hecho los ejemplos de las celdas anteriores. El código de la clase está dado por
"""

class Carro():
    """Clase carro"""
    
    def __init__(self,modelo,marca = 'Nissan', anio=2020):
        """Inicializa los atributos del carro"""
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0
    
    def Describe_Carro(self):
        """Imprime la descripción del carro creado"""
        Descripcion = str(self.anio) + ' ' + self.marca + ' ' + self.modelo
        return Descripcion.title()
    
    def muestra_Kilometraje(self):
        """Imprime el kilometraje del auto"""
        print("Este auto tiene " + str(self.kilometraje) +" kilómetros recorridos")
    
    def Leer_Kilometraje(self,valor_usuario):
        """Asigna el valor de de valor_usuario a kilometraje"""
        if valor_usuario >= self.kilometraje:
            print("Asignación correcta")
            self.kilometraje = valor_usuario
        else:
            print("Asignación incorrecta, no se ha llevado a cabo")
            
    def Actualizar_Kilometraje(self,valor_suma):
        """Suma el valor del usuario al kilometraje del auto"""
        if valor_suma >= 0:
            print("Incremento correcto")
            self.kilometraje += valor_suma
            #self.kilometraje = self.kilometraje + valor_suma
        else:
            print("Incremento incorrecto, no se llevará a cabo")

"""Observe que esta clase tiene su constructor y que debe de tener por lo menos un parámetro para que es `marca`, ya que los otros dos parámetros están predeterminados, sin emgargo, el usuario puede definir los tres parámetros, los demás métodos se han explicado en las secciones anteriores. 
 
 Ahora se quiere generr una clase `CarroElectrico` y se requiere que herede todos atributos de la clase `Carro`, La clase hija debe su propio constructor y dentro de ésta se debe de manda a llmar al constructor de la clase padre, tal como se muestra en la siguiente celda
"""

class CarroElectrico(Carro):
    """Representa a un auto eléctrico"""
    def __init__(self,marca, modelo, anio): 
        #inicializa los elementos de la clase padre.
        super().__init__(marca,modelo,anio)

"""En la celda anterior, se muestra la sintaxis para poder definir la herencia, observe que primero debe de ir 
    `class Clase_hijo(Clase_padre):`, que en nuestro caso la clase hijo es `CarroElectrico` y la  clase padre es  `Carro`. 
    
Una vez que se ha definido la herencia en la implmentación de la clase hijo, se debe de definir el constructor y aquí hay una parte interesante, el constructor de la clase hijo, debe de tener los elementos necesarios para poder inicializar el constructor de la clase padre, argumentos necesarios y propios de la clase hijo:

`def _init__(self,argumentos_necesarios_para_clase_padre, argumentos_propios):`

y observe que dentro del constructor de la clase hijo, se debe de mandar a llamar al constructor de la clase padre de la siguiente forma:

`super()._init__(argumentos_del_constructor_de_la_clase_padre)`

observe que el constructor de la clase padre ya no debe de tener como argumento  `self`.

En la siguiente celda se observa la creación de un objeto de la clase `CarroElectrico` y se utilizarán los métodos de la clase a la cual se le ha heredado.
"""

miTesla = CarroElectrico('tesla','model_s', 2020)
print(miTesla.Describe_Carro())

"""### 2.5.2 Definiendo Atributos y métodos de la clase hija
Una vez que se ha logrado la herencia la clase hija NO ESTÁ LIMITADA a tener sólo los métodos y atributos de la clase padre, LA CLASE HIJO PUEDE TENER SUS PROPIOS METODOS Y ATRIBUTOS.

Como ejemplo se agregará un atributo a la calse `CarroElectrico`, el atributo que se agregará será `Bateria` que mostrará la corriente por hora que es capaz de brindar al auto. Para agregar el atributo sería el siguiente código
"""

class CarroElectrico(Carro):
    """Representa los aspectos de un auto eléctrico"""
    
    def __init__(self,marca,modelo,anio):
        """Constructor de la clase Hijo"""
        #Inicialización de la clase padre
        super().__init__(marca,modelo,anio)
        
        # Nuevo atributo de la clase 
        self.Bateria = 70 
        
    def Describe_Bateria(self):
        """Imprime la información de la batería"""
        print("Este auto tiene una batería: " + str(self.Bateria) + "-kWh")

"""En la celda superior se observa que a la clase `CarroElectrico` se le ha agregado un atributo nuevo y también un método, observe que es la misma metodología que se ha utilizado para definir los métodos y atributos de cualquier clase. 

Para hacer uso de los métodos es necesario hacerlo como se haría con cualquier clase normal.

### 2.5.3 Sobrecarga de Métodos de la clase padre.

Supongamos que la calse padre tiene un método y al momento que hereda, el método pasa a ser parte de la clase hijo, sin embargo, puede que el método de la clase padre no apegue a los requerimientos de la clase hijo, entonces, la clase hijo puede  *redefinir* el método que ha heredado, a este fenómeno se le conoce como **Sobrecarga de funciones o de métodos**

Como ejemplo, se muestra la clase padre, que es la clase asociada a un `Carro` y se le agregará un método llamado `Cargar` que simulará el hecho de cargar gasolina. Después se generará la clase de un `CarroElectrico` que hereda de la clase `Carro`, sin embargo, el método `Cargar` deberá de ser distinto, observe los códigos de las siguientes celdas.
"""

class Carro():
    """Clase carro"""
    
    def __init__(self,modelo,marca = 'Nissan', anio=2020):
        """Inicializa los atributos del carro"""
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0
    
    def Describe_Carro(self):
        """Imprime la descripción del carro creado"""
        Descripcion = str(self.anio) + ' ' + self.marca + ' ' + self.modelo
        return Descripcion.title()
    
    def muestra_Kilometraje(self):
        """Imprime el kilometraje del auto"""
        print("Este auto tiene " + str(self.kilometraje) +" kilómetros recorridos")
    
    def Leer_Kilometraje(self,valor_usuario):
        """Asigna el valor de de valor_usuario a kilometraje"""
        if valor_usuario >= self.kilometraje:
            print("Asignación correcta")
            self.kilometraje = valor_usuario
        else:
            print("Asignación incorrecta, no se ha llevado a cabo")
            
    def Actualizar_Kilometraje(self,valor_suma):
        """Suma el valor del usuario al kilometraje del auto"""
        if valor_suma >= 0:
            print("Incremento correcto")
            self.kilometraje += valor_suma
            #self.kilometraje = self.kilometraje + valor_suma
        else:
            print("Incremento incorrecto, no se llevará a cabo")
    
    def Cargar(self):
        print("El auto se está cargando de gasolina")

class CarroElectrico(Carro):
    """Representa los aspectos de un auto eléctrico"""
    
    def __init__(self,marca,modelo,anio):
        """Constructor de la clase Hijo"""
        #Inicialización de la clase padre
        super().__init__(marca,modelo,anio)
        
        # Nuevo atributo de la clase 
        self.Bateria = 70 
        
    def Describe_Bateria(self):
        """Imprime la información de la batería"""
        print("Este auto tiene una batería: " + str(self.Bateria) + "-kWh")
        
    def Cargar(self):
        print("El auto se ha conectado a la energía eléctrica para cargar la batería")

miCamioneta = Carro('Ford','Lobo',2018)
print("Detalles de la camioneta: " + miCamioneta.Describe_Carro())
print(miCamioneta.Cargar())

"""En la celda anterior se ha declarado una camioneta Ford, y se ha llamado el método `Describe_Carro` y después se ha llamado el método `Cargar` e imprime el que se está cargando con gasolina. Observemos que pasa ahora si se hace un auto eléctico y llamaremos al método `Cargar` para ver las diferencias."""

miNissan = CarroElectrico('Nissan', 'Leaf', 2020)
print("Detalles de auto: " + miNissan.Describe_Carro())
print(miNissan.Cargar())

"""Observa que se ha generado un auto eléctrico y en la definición de la case se agregó el método `Cargar`, en la celda anterior, cuando se manda a llamar el método `Cargar` se llama al método de la clase `CarroElectrico` y no al del `Carro` llevándose a cabo la sobrecarga de funciones.

### 2.5.4 Intancias como atributos

Existe otro fenómeno que se llama **Composición de clases** que es muy distinto a la herencia de clases. En la composición un objeto puede ser parte de los atributos, como ejemplo. Suponga que se tiene un robot diferencial como el que se muestra en el link de abajo

https://www.youtube.com/watch?v=i-JHGbDN4GA

Como se observa en el video, el robot tiene dos motores y nos enfocaremos en ese ejemplo. Se creará una clase que describa un motor, que tenga como atributos el `voltaje` de funcionamiento, se agregarán tres métodos para el motor `girar_derecha(self)`, `girar_izquierda(self)` y `paro(self)`
"""

class motor():
    def __init__(self, volts):
        self.voltaje = volts
        
    def girar_derecha(self):
        print("El motor está girando a la derecha")
        
    def girar_izquierda(self):
        print("El motor está girando a la izqiuerda")
        
    def paro(self):
        print("El motor está parado")

"""Una vez que se ha creado la clase motor, se generará la clase `RobotDiferencial` y tendrá como atributos los dos motores. Se agregarán sólo los métodos `Paro` para y `Avanza` para el robot. Para que el robot avance hacia delante, es necesario que el un motor gire a la derecha y el otro a la izquierda. Observe la implmentación de la clase robot"""

class Robot():
    def __init__(self, volts):
        self.motor1 = motor(volts)
        self.motor2 = motor(volts)
        print("Se ha creado el robot")
        
    def Avanza(self):
        print("El motor está avanzando")
        self.motor1.girar_derecha()
        self.motor2.girar_izquierda()
        
        
    def Paro(self):
        print("El motor se ha parado")
        self.motor1.paro();
        self.motor2.paro();

miRobot = Robot(5)

miRobot.Avanza()

miRobot.Paro()

"""En las celdas anteriores se ha creado la clase motor y robot, observe que la clase robot está compuesta de dos objetos tipo motor, observe que el constructor de `Robot` debe de tener por lo menos los elementos necesarios para poder incializar los objetos `self.motor1` y `self.motor2`, en el método `Avanza` se utilizan los metodos de los motores para simular que el robot estaría avanzando. Lo mismo sucede para el método de `Paro`, se ingresa a los métodos de los motores para pararlos.

### 2.5.5 Ejercicio

1. **Heladería:** Una heladería se puede ver como un tipo específico de restaurante. Cree una clase que se llame `Heladeria` que herede de la clase `Restaurante` que se ha desarrollado en los ejercicios anteriores. Cree un atributo que se llame `sabores` que debe de ser una lista (estructura de datos). Agregar un método a la clase `Heladeria` que muestre los sabores que tiene.
"""