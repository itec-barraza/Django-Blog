## Django-Blog
#EFI Ingeniería de Software
#Crear con Django, un blog que contenga los siguientes modelos:
-Post
-Categoria


Cada Post debera estar asociado a un Usuario (Utilizar modelo automatico de Django)
Cada Post debera estar asociado a una Categoria
Los Post y las Categorias se crearan desde el BackOffice (Django Admin)
Desde el Django Admin crear 3 tipo de usuarios (Superuser, Staff, Usuario X(que no sea ninguno de los anteriores))
El usuario X no podra Eliminar o Editar Post ni Categorias
Crear un formulario donde se pueda crear un post desde el frontend, no contendra login por lo que el usuario que lo creo sera seleccionado desde un desplegable que consuma los usuario ya existentes


#Frontend
Desde el front debo poder visualizar todos los Post con su respectiva Categoria y Autor, ordenado cronologicamente del más nuevo al más viejo.
Al hacer click a la Categoria debera mostrarme todos los Post de dicha Categoria independientemente del Autor
Al hacer click en el Autor debera mostrarme todos los Post del Autor independientemente de la Categoria


