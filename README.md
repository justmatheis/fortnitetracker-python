# fortnitetracker-python

Estadísticas de Fortnite mediante el ID de Epic Games, a través de una interfaz realizada con la librería Tkinter de Python.

Los datos obtenidos son por medio de la API de Fortnite (No oficial):
https://fortniteapi.io/

## Requisitos

Se requiere tener instaladas las siguientes librerías:

```python
import sys
from tkinter import messagebox
from tkinter import *
import ctypes
import requests
import json
```

Así como de igual forma, la última versión de Python y PIP.

https://www.python.org/

## Funcionamiento

Para que funcione al 100%, es necesario obtener una API KEY a traves del enlace superior.

Indicando la API KEY en la siguiente función:

```python
def getNumberAndNameSeason(season_value):
    headerDict = {"Authorization":"YOUR_API_KEY"}
```

Así como también en la función:

```python
def getDataFromPlayer(_valor):
    headerDict = {"Authorization":"YOUR_API_KEY"}
```
## Actualizaciones

| Fecha | Autor | Versión |
| --- | --- | --- |
| 07/01/2023 | Eduardo Ulises M. | 1.0 |
