##Bienvenido a Mi Proyecto Calistenia.
Podremos encontrar diferentes tipos de ejercicios de calistenia.
#### Inicio de Proyecto desde GitHub:
1. Crear un nuevo repositorio en GitHub.
1. agregarmos modulos **.gitignore** y **README.md**.
1. copiamos link de repositorio **https://github.com/Rousher/EntregaFinal-Agustin-Tapia.git**
1. Nos vamos al **Visual Studio.**

------------

### Inicio de Proyecto desde Visual Studio:
1. Empezamos abriendo la consola y escribimos: *git clone https://github.com/Rousher/EntregaFinal-Agustin-Tapia.git*. Con esto conectamos el visual con nuestro repositorio en **GitHub.**
1. django-admin startproject **Proyecto .** <---- *NO HAY QUE OLVIDARSE DEL PUNTO*
1. python manage.py startapp **app** <--- *NOMBRE DE NUESTRA APP*
1. Agregamos en **settings.py** el nombre de nuestra app:

------------


**`INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

'EjemploConfig', <-- NOMBRE DE NUESTRA APP 
]`**

------------


1. Hacemos **python manage.py migrate** para crear nuestra primera migración a la base de datos.
1. Creamos la siguiente estructura de carpeta: **templates/app/registration**
- Dentro de estas carpetas creamos el archivo **index.html**
1. Creamos la siguiente estructura de carpeta:  **static/app/css/js/assets** 
-  En las carpetas **css/js/assets** agregamos los respectivos archivos descargados.

En este punto ya tendriamos todo lo necesario para poder avanzar con los **html** y las **views**

------------


## WORK FLOW:
> Vamos a seguir una serie de pasos que nos van a ayudar a mantener la organizacion de las cosas.:

1. Creamos la **view** que necesitemos.
`
def index(request):
    return render(request, "ejemplo/indexr.html")`
1. Hacemos el **.html** respectivo a la view
*h1>
*Hola esto es el template index*/h1>*

1. Terminamos macheando con la **url **de la view
from django.contrib import admin
from django.urls import path
from ejemplo***<-nombre de nuestra app***.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index , name= 'index'), # ESTA ES LA NUEVA FUNCTION
]
###### Con este WROK FLOW podemos crear view, html y urls correctamente.

------------
## Página web:

- Corremos ***Python manage.py runserver***
- Como se tiene que ver si esta todo bien:

[![](https://kbimages.dreamhosters.com/images/2018-04_django-create-project.png)](http://https://kbimages.dreamhosters.com/images/2018-04_django-create-project.png)

------------


###Pasos para hacer un Push a github: 

Correr en la terminal: **git add .**

Correr en la terminal:**git commit -m "primer commit de mi proyecto"**

Correr en la terminal: **git push origin main**


------------

# Mi Proyecto de Calistenia: LAS FUNCIONES
###### Inicio con cuenta registrada:
- Tenemos al rededor de 10 funciones diferentes entre las cuales se encuentra:
1. "**About"**: Se encuentra información sobre mi y el origen de la página web.
1. "**Home"**: Podemos observar un texto diciendonos que nos registremos en las secciones de arriba al lado de "Home".
1. "**SignUp"**: Template donde podras registrate y tener acceso a mas en la pagina del admin.
1. "**Login"**: Template donde podras ingresar con tu cuenta creada previamente.
1. "**Ejercicios"**: Template donde se encuentran todos los ejercicios de calistenia/gym con botones de *detalle*, *actualizar* y *borrar*.  *Solo si sos dueño podes actualizar o borrar*.
1. "**Enviar Mensaje"**: Un template con formulario de envio de mensajes a diferentes usarios registrados.
1. "**Mis ejercicios"**: Template con los ejercicios ingresados (si no hay ninguno ingresado, se presentera un texto "sin ejercicios") por el usuario dueño. con botones de *detalle*, *actualizar* y *borrar*. 
1. "**Agregar ejercicio"**: Template usado para agregar cualquier tipo de ejercicio de calistenia u otro deporte si es que prefiere. Con *titulo, tipo, descripcion , creador e imagen. * Descargar la foto de google.
1. "**Ejercicios"**: Template donde almacenan los ejercicios recibidos donde no podras editarlos, pero si ver el detalles de ellos.
1. "**Tus mensajes"**: Template con los mensajes ingresados (si no hay ninguno ingresado, se presentera un texto "No hay mensajes agregados.") por el admin. con botones de *detalle*, *actualizar* y *borrar*. 
1. "**Crear Perfil"**: Template para poder crear tu propio avatar con imagen.
1. "**Buscar Post"**: Template donde podras buscar y filtrar los ejercicios registrados en la pagina.
1. "**tu usuario | Logout"**: Boton usado para salir de la cuenta del usuario. 
