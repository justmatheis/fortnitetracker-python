# fortnitetracker-python

Estadísticas de Fortnite mediante el ID de Epic Games, a través de una interfaz realizada con la librería Tkinter de Python.

![image](https://user-images.githubusercontent.com/70301117/211180595-d070ea56-eb24-4c3c-92f4-841165e17517.png)

Los datos obtenidos son por medio de la API de Fortnite (No oficial):
https://fortniteapi.io/

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
