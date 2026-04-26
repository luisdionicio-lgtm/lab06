1. Clonar el repositorio

Abre tu terminal (PowerShell, CMD o Git Bash):

git clone https://github.com/luisdionicio-lgtm/lab05.git

Luego entra al proyecto:

cd lab05
2. Crear entorno virtual
python -m venv .venv
3. Activar entorno virtual
En Windows:
.venv\Scripts\activate

Si todo está bien verás:

(.venv)
4. Instalar dependencias
pip install -r requirements.txt
5. Aplicar migraciones
python manage.py migrate
6. Crear superusuario (opcional pero recomendado)
python manage.py createsuperuser
7. Ejecutar el servidor
python manage.py runserver
 ¿Cómo se visualiza?
🔹 API (DRF - Navegador)

Abre en tu navegador:

http://127.0.0.1:8000/api/movies/
http://127.0.0.1:8000/api/genres/

#######CAPTURAS DE LUIS DIONICIO

## 1. Existencias del Genres
![Genre](./docs6/genres1.png)

---

![Genre](./docs6/genres2.png)

---

## 2. Añadir  genero (GET)
![Genres](./docs6/genres3.png)

---

## 3. Visualizar el proyecto
![Genre](./docs6/genres4.png)

---

## 4. Post añadir
![Post](./docs6/genres5.png)

---

## 5. (GET)
![GET Genre](./docs6/genres6.png)

---

## 6. añadir nuevo genero de peliculas
![DELETE Genre](./docs6/genres7.png)

---

## 7. ELIMINAR
![GET Deleted Genre](./docs6/genres8.png)

---

## 8. VERIFICAR EN EL SISTEMA WEB
![Verificar](./docs6/genres9.png)


##### JOSE SOTELO 


### 🔹 Visual 1: Vista general de la app Genre
![Visual 1](./docs6/visual1.png)

---

### 🔹 Visual 2: Visualización de géneros registrados
![Visual 2](./docs6/visual2.png)

---

### 🔹 Visual 3: Detalle de género en el sistema
![Visual 3](./docs6/visual3.png)

---

### 🔹 Visual 4: Creación de género (POST)
![Visual 4](./docs6/visual4.png)

---

### 🔹 Visual 5: Consulta de géneros (GET)
![Visual 5](./docs6/visual5.png)

---

### 🔹 Visual 6: Actualización de género (PUT)
![Visual 6](./docs6/visual6.png)

---

### 🔹 Visual 7: Eliminación de género (DELETE)
![Visual 7](./docs6/visual7.png)

---

### 🔹 Visual 8: Vista general de la aplicación en ejecución
![Visual 8](./docs6/visual8.png)

