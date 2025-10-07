# 🍵 Backend-V2 de MatchaFunding

## 🗂️ Resumen

Microservicio que maneja el flujo de datos duros, como las empresas, proyectos, personas,
miembros y usuarios.

La intencion de esta nueva implementacion nueva es adaptarse al nuevo modelo de datos,
procurar mejor rendimiento, uso de buenas practicas y mejor compatibilidad con la API
de QDrant y BERTopic.

## 🔥 Tecnologia

El Back-End ha sido re-escrito en _C_, utilizando _MySQL_, _Redis_, _libmicrohttpd_ y _cJSON_ dentro de su _stack_.

El servidor ahora corre bajo _libmicrohttpd_, un servidor nativo en C que se enfoca en traer funcionalidad moderna al entorno _UNIX_.

La base de datos sigue siendo _MySQL_, de esta forma los datos son compatibles con las iteraciones anteriores, ademas de ser la base de datos por excelencia.

Ahora se agrega _Redis_ en el stack, lo cual remplaza a _Pandas_ para mantener los datos calientes en memoria RAM y asi optimizar el uso de recursos limitado.

Finalmente, se usa _cJSON_ para parsear y formatear datos en _JSON_.

## ✅ Requisitos

Para lograr compilar y ejecutar el programa, se necesita tener un entorno _UNIX_ con las librerias necesarias.

#### 🐧 Arch Linux

Para Arch Linux (o en el servidor), se pueden instalar las dependencias a traves del siguiente comando:

```
pacman -S gcc mariadb libmicrohttpd redis cjson
```

*Nota*: Correr el comando anterior con _sudo_ o desde _root_

#### 🪟 Windows

La forma mas rapida de poder lograr correr el programa en Windows es a traves de _Windows Subsystem for Linux_. Se puede instalar Arch Linux para WSL a traves de los siguientes comandos:

Primero, actualizar WSL
```
wsl --update
```

Luego, instalar Arch Linux para WSL
```
wsl --install archlinux
```

Listo! ahora seguir los pasos del inciso anterior para instalar las librerias utilizadas.

Tutorial: https://wiki.archlinux.org/title/Install_Arch_Linux_on_WSL

## 🐍 Ejecucion

Una vez se cumplan los requisitos necesarios, para compilar el proyecto hay que hacer el siguiente comando desde la raiz del repositorio:

```
make
```

Luego para ejecutar el programa, correr el siguiente comando como _root_ o mediante _sudo_:

```
./bin/out
```
