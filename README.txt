# Primer pre entrega del proyecto final - PYTHON

Se trata de la primer pre-entrega del proyecto final para el curso de PYTHON dictado por CH.
Dentro se encuentra un proyecto de aplicacion web realizado en django.

"Entrega" (proyecto principal) y "appentrega" (aplicacion dentro del proyecto)

Instrucciones de uso y control:

1. Descargar el repositorio: Entrega desde github
2. Dentro encontraremos dos carpetas: Entrega (project principal) y appentrega(aplicacion)
3. Desde una terminal VSC ejecutar: python manage.py runserver
4. Acceder al servidor virtual, a la pagina de inicio: http://127.0.0.1:8000/appentrega/inicio/ 
5. Desde http://127.0.0.1:8000/appentrega/inicio/ podremos navegar por toda la web
6. Dentro del home encontraremos un texto de bienvenida y algunas aclaraciones
7. En los links del menu de navegacion superior: Libros, Autores, Sucursales y Miembros podremos encontrar
   las vistas a los diferentes formularios. Totalmente funcionales, que impactan los datos ingresados en los modelos
   correspondientes.
8. El boton buscar (tambien ubicado en la barra de navegacion) nos lleva a una vista de busqueda de libros.
   Se debe ingresar el titulo de un libro, y trae los resultados, sugerencias para probar:

   "El Aleph"
   "Dorian Gray"

NOTA: Sobre la vista Autores, respetar el formato de de fecha AAAA-MM-DD, de lo contrario dara error.