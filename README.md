# Django-Blog

EFI Ingeniería de Software.

## Crear un blog con Django
Debe contener los siguientes modelos:\
-Post \
-Categoria


Cada Post debera estar asociado a un Usuario (Utilizar modelo automatico de Django).\
Cada Post debera estar asociado a una Categoria.\
Los Post y las Categorias se crearan desde el BackOffice (Django Admin).

Desde el Django Admin crear 3 tipo de usuarios (Superuser, Staff, Usuario X(que no sea ninguno de los anteriores)).\
El usuario X no podra Eliminar o Editar Post ni Categorias.

Crear un formulario donde se pueda crear un post desde el frontend.\
El usuario será seleccionado desde un desplegable que consuma los usuario ya existentes.


Desde el front debo poder visualizar todos los Post con su respectiva Categoria y Autor.\
Ordenado cronologicamente del más nuevo al más viejo.\
Al hacer click a la Categoria debera mostrarme todos los Post de dicha Categoria independientemente del Autor.\
Al hacer click en el Autor debera mostrarme todos los Post del Autor independientemente de la Categoria.


## Getting Started with Django App
Use a virtual environment.
### `pipenv shell`
Install dependencies.
### `pip install -r requirements.txt`
Run app.
### `python manage.py runserver`
