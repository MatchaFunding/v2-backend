# 🍵 Backend-V2 de MatchaFunding

## 🧮 Resumen

Microservicio que maneja el flujo de datos duros, como las empresas, proyectos, personas,
miembros y usuarios.

La intencion de esta nueva implementacion nueva es adaptarse al nuevo modelo de datos,
procurar mejor rendimiento, uso de buenas practicas y mejor compatibilidad con la API
de QDrant y BERTopic.

## 🐼 Tecnologia

Esta nueva implementacion usa las librerias _Pandas_ y _FastAPI_, para facilitar el manejo
de clases de _APIs_ en comun con los microservicios de _QDrant_, _BERTopic_ y _Ollama_.

* Para mas detalles, vease el archivo: ```requirements.txt```

Estas nuevas librerias tambien aseguran mayor rendimiento para operaciones complejas de
datos ya que todas las operaciones estan optimizadas por _Pandas_ y _NumPy_, ademas de
ser realizadas en memoria en vez de disco duro como en _MySQL_ / _MariaDB_.

## 🐍 Ejecucion

Antes de ejecutar cualquier cosa, primero instalar los requisitos en ```requirements.txt```.

Luego, corroborar de tener la ultima base de datos instalada: [https://github.com/MatchaFunding/bd](https://github.com/MatchaFunding/bd).

Hecho esto, seguir alguno de los dos pasos a continuacion dependiendo de su sistema operativo.

### Linux / Bash

Para correr el microservicio desde Linux, basta con ejecutar el siguiente comando:

```
./run.sh
```

### Windows

Para correr el microservicio desde Windows 10/11, basta con ejecutar el siguiente comando:
```
uvicorn main:app --reload --host 127.0.0.1 --port 8080
```
