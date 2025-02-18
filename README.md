# Joke Button App

## 📌 Overview (English)
Joke Button App is a web application that fetches random jokes from an API when the user clicks a button. The frontend is built with React, while the backend is powered by FastAPI. The app serves as an example of how to structure a full-stack application using these technologies, demonstrating backend and frontend integration.

### 🎯 Features
- Fetches and displays a random joke at the click of a button.
- Example implementation of a backend (FastAPI) and frontend (React) working together.
- FastAPI backend that handles joke retrieval from an external API.
- Dockerized architecture for smooth deployment.

### 🏗️ Tech Stack
- **Frontend:** React, JavaScript, HTML, CSS
- **Backend:** FastAPI, Python
- **Containerization:** Docker

### 🚀 Setup Instructions
#### Prerequisites
Ensure you have the following installed:
- [Node.js](https://nodejs.org/)
- [Python 3.11](https://www.python.org/)
- [Docker](https://www.docker.com/)

#### Installation Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/davo16dev/joke-button-app.git
   ```
   ```sh
   cd joke-button-app
   ```
2. Build and run the app using Docker:
   ```sh
   docker buildx build --platform linux/amd64 -t joke-button-app .
   ```
   ```sh
   docker run -p 8080:8080 joke-button-app
   ```
3. Access the app at:
   ```
   http://localhost:8080
   ```

## Disclaimer

This project fetches jokes from the [JokeAPI](https://jokeapi.dev/).  
The jokes are selected randomly and filtered to display only programming-related jokes.  

While the content is filtered for this context, any issues or concerns regarding the jokes displayed are the responsibility of the source API, as this project simply consumes the provided data without modifying its content.  

For more information about the API and how it works, visit [JokeAPI](https://jokeapi.dev/).
---

## 📌 Descripción (Español)
Joke Button App es una aplicación web que obtiene chistes aleatorios de una API cada vez que el usuario presiona un botón. El frontend está desarrollado en React, mientras que el backend utiliza FastAPI. La aplicación sirve como un ejemplo de cómo estructurar una aplicación full-stack utilizando estas tecnologías, mostrando la integración entre backend y frontend.

### 🎯 Características
- Obtiene y muestra un chiste aleatorio al hacer clic en un botón.
- Implementación de ejemplo de un backend (FastAPI) y frontend (React) funcionando juntos.
- Backend en FastAPI que maneja la recuperación de chistes desde una API externa.
- Arquitectura basada en Docker para facilitar la implementación.

### 🏗️ Stack Tecnológico
- **Frontend:** React, JavaScript, HTML, CSS
- **Backend:** FastAPI, Python
- **Contenerización:** Docker

### 🚀 Instrucciones de Instalación
#### Requisitos Previos
Asegúrate de tener instalado lo siguiente:
- [Node.js](https://nodejs.org/)
- [Python 3.11](https://www.python.org/)
- [Docker](https://www.docker.com/)

#### Pasos de Instalación
1. Clona el repositorio:
   ```sh
   git clone https://github.com/davo16dev/joke-button-app.git
   ```
   ```sh
   cd joke-button-app
   ```
2. Construye y ejecuta la aplicación con Docker:
   ```sh
   docker buildx build --platform linux/amd64 -t joke-button-app .
   ```
   ```sh
   docker run -p 8080:8080 joke-button-app
   ```
3. Accede a la aplicación en:
   ```
   http://localhost:8080
   ```

## Disclaimer

Este proyecto obtiene los chistes desde la API de [JokeAPI](https://jokeapi.dev/).  
Los chistes se seleccionan al azar y están filtrados para mostrar únicamente chistes de programación.  

Si bien el contenido ha sido filtrado para este contexto, cualquier problema o inconveniente con los chistes mostrados es responsabilidad de la API fuente, ya que el proyecto simplemente consume la información proporcionada sin realizar modificaciones en su contenido.  

Para más información sobre la API y su funcionamiento, puedes visitar [JokeAPI](https://jokeapi.dev/).
---

## 📜 License
MIT License - Feel free to use and modify this project as needed.

---

💡 **Feel free to contribute!** If you find any issues or have feature requests, submit a pull request or open an issue.

