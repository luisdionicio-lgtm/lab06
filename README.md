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


#######  CAPTURAS JOSE SOTELO 


### 🔹 Visual 1: Vista general de la app Genre
![Visual 1](./docs6/visual1.jpeg)

---

### 🔹 Visual 2: Visualización de géneros registrados
![Visual 2](./docs6/visual2.jpeg)

---

### 🔹 Visual 3: Detalle de género en el sistema
![Visual 3](./docs6/visual3.jpeg)

---

### 🔹 Visual 4: Creación de género (POST)
![Visual 4](./docs6/visual4.jpeg)

---

### 🔹 Visual 5: Consulta de géneros (GET)
![Visual 5](./docs6/visual5.jpeg)

---

### 🔹 Visual 6: Actualización de género (PUT)
![Visual 6](./docs6/visual6.jpeg)

---

### 🔹 Visual 7: Eliminación de género (DELETE)
![Visual 7](./docs6/visual7.jpeg)

---

### 🔹 Visual 8: Vista general de la aplicación en ejecución
![archivo](./docs6/visual8.jpeg)



###### JERONIMO ORTIZ ORTIZ

## 📸 Evidencias del desarrollo del sistema

---

### 🔹 Ortiz_1: Visualización del proyecto en ejecución
![Ortiz_1](./docs6/Ortiz_1.jpeg)

---

### 🔹 Ortiz_2: Panel administrativo (Django Admin)
![Ortiz_2](./docs6/Ortiz_2.jpeg)

---

### 🔹 Ortiz_3: Código del proyecto (estructura o implementación)
![Ortiz_3](./docs6/Ortiz_3.jpeg)

---

### 🔹 Ortiz_4: Creación de datos (POST)
![Ortiz_4](./docs6/Ortiz_4.jpeg)

---

### 🔹 Ortiz_5: (POST)
![Ortiz_5](./docs6/Ortiz_5.jpeg)

---

### 🔹 Ortiz_6: GET
![Ortiz_6](./docs6/Ortiz_6.jpeg)

### 🔹 Ortiz_8: GET DE VERIFICACION
![Ortiz_8](./docs6/Ortiz_8.jpeg)

---

### 🔹 Ortiz_7: PUT
![Ortiz_7](./docs6/Ortiz_7.jpeg)

---

### 🔹 Ortiz_9: DELETE
![Ortiz_9](./docs6/Ortiz_9.jpeg)