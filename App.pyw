import sys
from tkinter import messagebox
from tkinter import *
import ctypes
import requests
import json

def getNumberAndNameSeason(season_value):
    headerDict = {"Authorization":"YOUR_API_KEY"}
    
    try:
        _seasonRequest = 'https://fortniteapi.io/v1/seasons/list?lang=en'
        responseSeason = requests.get(_seasonRequest, headers=headerDict)
        jsonResponseSeason =  responseSeason.json()

        chapter_season_name = []

        for seasons in jsonResponseSeason['seasons']:
            chapter_season_name.append(seasons['displayName'])

        return chapter_season_name[season_value - 1]
    except:
        return 0

def getDataFromPlayer(_valor):
    headerDict = {"Authorization":"YOUR_API_KEY"}

    try:
        _idPlayer = 'https://fortniteapi.io/v1/lookup?username=' + _valor
        response1 = requests.get(_idPlayer, headers=headerDict)
        jsonResponse1 = response1.json()
        jsonResponse1_formatted = json.dumps(jsonResponse1, indent=2)

        try:
          _statsPlayer = 'https://fortniteapi.io/v1/stats?account=' + jsonResponse1["account_id"]
          response2 = requests.get(_statsPlayer, headers=headerDict)
          jsonResponse2 = response2.json()

          value = json.dumps(jsonResponse2['account']['season'], indent=2)
          returnValueInt = json.loads(value)

          seasonValue = getNumberAndNameSeason(int(returnValueInt))
          
          # jsonResponse2_formatted = json.dumps(jsonResponse2, indent=2)
          
          list_data = (
              "ACCOUNT NAME: " + json.dumps(jsonResponse2['name'], indent=2),
              "ACTUAL SEASON: " + seasonValue.upper(),
              "LEVEL: " + json.dumps(jsonResponse2['account']['level'], indent=2),
              "",
              "KD SOLO: " + json.dumps(jsonResponse2['global_stats']['solo']['kd'], indent=2),
              "KD DUO: " + json.dumps(jsonResponse2['global_stats']['duo']['kd'], indent=2),
              "KD TRIO: " + json.dumps(jsonResponse2['global_stats']['trio']['kd'], indent=2),
              "KD SQUAD: " + json.dumps(jsonResponse2['global_stats']['squad']['kd'], indent=2),
              "",
              "KILLS SOLO: " + json.dumps(jsonResponse2['global_stats']['solo']['kills'], indent=2),
              "KILLS DUO: " + json.dumps(jsonResponse2['global_stats']['duo']['kills'], indent=2),
              "KILLS TRIO: " + json.dumps(jsonResponse2['global_stats']['trio']['kills'], indent=2),
              "KILLS SQUAD: " + json.dumps(jsonResponse2['global_stats']['squad']['kills'], indent=2),
              ""
          )
        
          return list_data
        except:
          messagebox.showerror(title="ERROR", message="AN ERROR OCCURRED")
          return ""
    except:
        messagebox.showerror(title="ERROR", message="AN ERROR OCCURRED")
        return ""

def hacer_click():
    try:
        listbox.delete(0, END)
        _valor = entrada_texto.get()
        data = getDataFromPlayer(_valor)
        listbox.insert(0, *data)
    except ValueError:
        listbox.insert(END,text="PLEASE ENTER A NAME")

ctypes.windll.shcore.SetProcessDpiAwareness(1)

app = Tk()
app.geometry("400x350")
app.configure(bg='black')
app.iconbitmap("logo.ico")

app.title("FORTNITE TRACKER")

frame = Frame()
scrollbar = Scrollbar(frame, orient=VERTICAL)

listbox = Listbox(frame, yscrollcommand=scrollbar.set, width = 55)
scrollbar.config(command=listbox.yview)

label = Label(app, text="PLAYER NAME:")

boton = Button(app, text="SEARCH", command=hacer_click)

valor = ""
entrada_texto = Entry(app, width=25, textvariable=valor)

scrollbar.pack(side=RIGHT, fill=Y)
label.pack(pady=10)
entrada_texto.pack(pady=15)
boton.pack(pady=15)
frame.pack()
listbox.pack()

app.mainloop()
