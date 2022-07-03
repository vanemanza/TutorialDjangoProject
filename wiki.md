
### Paquetes de Python

https://docs.python.org/3/tutorial/modules.html#tut-packages

Un paquete de Python es una colección de módulos.

### Función path()

* Recibe 4 argumentos:
    - Dos obligatorios (route y view)
    - Dos opcionales (kwargs y name)

    1) Route: es un string q contiene un patrón de URL. Al procesar una solicitud Django buscará en la lista de patrones hasta encontrar una coincidencia.

    2) View: cuando Django encuentra un patrón coincidente, llama a la función de la vista espedificada con un objeto HttpRequest como primer argumento?

    3) Kwargs: A la vista se le pueden pasar argumentos de palabras clave, como un diccionario

    4) Name: sirve para hacer referencia a una URL, especialmente desde un template

