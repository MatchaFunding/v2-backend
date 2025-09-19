# 🍵 Backend-V2 de MatchaFunding

## 🧮 Resumen

Microservicio que maneja el flujo de datos duros, como las empresas, proyectos, personas,
miembros y usuarios.

La intencion de esta nueva implementacion nueva es adaptarse al nuevo modelo de datos y
poder segregar el microservicio en dos fases: Usuarios y Core. _Usuarios_ refiere a la
autenticacion, creacion de proyectos y manejo de personasl. Mientras que _Core_ es el
manejo de datos masivos obtenidos a traves de _Web-Scraping_ e investigacion, el cual
se usa para hacer los calculos con la IA y vectorizacion.

Dicha separacion de servicios permite balancear las cargas de forma mas adecuada, ya que
finalmente los datos de _Usuarios_ y _Core_ nunca interactuan entre si (a pesar de usar
los mismos modelos).

## 🐼 Tecnologia

Esta nueva implementacion usa las librerias _Pandas_ y _FastAPI_, para facilitar el manejo
de clases de _APIs_ en comun con los microservicios de _QDrant_, _BERTopic_ y _Ollama_.

* Para mas detalles, vease el archivo: ```requirements.txt```

## 🐍 Ejecucion

Antes de ejecutar cualquier cosa, primero instalar los requisitos en ```requirements.txt```.

Luego, corroborar de tener la ultima base de datos instalada: [https://github.com/MatchaFunding/bd](https://github.com/MatchaFunding/bd).

Hecho esto, seguir alguno de los dos pasos a continuacion dependiendo de su sistema operativo.

### Linux / Bash

Para correr el microservicio desde Linux, basta con ejecutar el siguiente comando:

```
./start.sh
```

### Windows

Para correr el microservicio desde Windows 10/11, basta con ejecutar el siguiente comando:
```
uvicorn main:app --reload --host 127.0.0.1 --port 8080
```
