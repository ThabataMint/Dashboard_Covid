from tkinter import *
from tkinter import ttk

#########importando bibliotecas##################

from PIL import Image
import requests
import string

import json
import datetime

########################################cores##############################################################

co0 = "#000000"  # black
co1 = "#cc1d4e"  # red
co2 = "#feffff"  # white
co3 = "#0074eb"  # blue
co4 = "#435e5a"  # #435e5a
co5 = "#59b356"  # green
co6 = "#d9d9d9"  # grey

##############################################CRIA ANELA PRINCIPAL do aplicativo#############################################

janela = Tk()

janela.resizable(width=FALSE, height=FALSE)
janela.geometry('840x380')  ############################ALTEREI AS MEDIDAS
janela.title('')
janela.configure(bg=co6)

##################################CRIANDO FRAMES#############################################

app_nome_frame = Frame(janela, width=700 , height=50, bg=co2, relief="flat") # width estava comm 840 e height 50
app_nome_frame.grid(row=0, column=0, columnspan=3, sticky=NSEW)

mostrar_frame_infectados = Frame(
    janela, width=400, height=100, bg=co2, relief="flat") # width estava com 220
mostrar_frame_infectados.grid(row=1, column=0, sticky=NW, pady=5, padx=5)

# mostrar_frame_recuperados = Frame(
# janela, width=220, height=100, bg=co3, relief="flat")
# mostrar_frame_recuperados.grid(row=1, column=1, sticky=NW, pady=5, padx=5)


mostrar_frame_mortes = Frame(
    janela, width=400, height=100, bg=co2, relief="flat")  # width estava com 220
mostrar_frame_mortes.grid(row=1, column=2, sticky=NW, pady=5, padx=5)

selct_frame = Frame(janela, width=840, height=50, bg=co6, relief="flat")
selct_frame.grid(row=2, column=0, columnspan=3, sticky="n", pady=10)

#####################################CRIANDO LABEL PARA APP_nome_FRAME#############################################
img=Image.open("covid1.jpg")
img=img.resize((50,50))
img=img.save("covid.png")
imagem=PhotoImage(file= "covid.png")

app_imagem = Label(app_nome_frame, image=imagem, width=350,
                 pady=20, relief="flat", anchor=NE, bg=co2)
app_imagem.grid(row=0, column=0, pady=5)


app_nome = Label(app_nome_frame, text="COVID-19", width=20, height=1,
                 pady=20, relief="flat", anchor=NW, font="Courier 20 bold ", bg=co2, fg=co0)
app_nome.grid(row=0, column=1, pady=5)


###################################Chamando API####################################

response = requests.get("https://covid19.mathdro.id/api")
info = response
info = json.loads(info.text)

infectados = info["confirmed"]["value"]
mortes = info["deaths"]["value"]
dia = info["lastUpdate"]
dia = datetime.datetime.strptime(dia, "%Y-%m-%dT%H:%M:%S.000Z")
dia = dia.strftime("%c")

###################################CRIANDO LABEL PARA mostrar_frame_infectados#############################################

label_infectados = Label(mostrar_frame_infectados, text="INFECTADOS", width=15, height=1, #width estava 20
                         pady=7, padx=0, relief="flat", anchor=CENTER, font=("Courier 15 bold"), bg=co2, fg=co0)
label_infectados.grid(row=0, column=0, pady=1, padx=13)

mostrar_infectados = Label(mostrar_frame_infectados, text=infectados, width=12, height=1,
                           pady=7, padx=0, relief="flat", anchor=CENTER, font=("Courier 25 bold"), bg=co2, fg=co0)
mostrar_infectados.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_frame_infectados, text=str(dia), width=33, height=1,  # vou manter widh 33
                     pady=7, padx=0, relief="flat", anchor=CENTER, font=("Courier 11 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=2, column=0, pady=1)

mostrar_info = Label(mostrar_frame_infectados, text="Total de casos ativos", width=50, height=1,
                     # alterei width para 65
                     pady=7, padx=0, relief="flat", anchor=CENTER, font=("Courier 8 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=3, column=0, pady=1, padx=13)

mostrar_azul = Label(mostrar_frame_infectados, text="", width=19, height=1,  # alterei width para 65
                     pady=1, padx=0, relief="flat", anchor=CENTER, font=("Courier 1 bold"), bg=co3, fg=co0)
mostrar_azul.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

##################################CRIANDO LABEL PARA mostrar_frame_mortes#############################################

label_mortes = Label(mostrar_frame_mortes, text="MORTES", width=15, height=1, #width estava 20
                     pady=7, padx=0, relief="flat", anchor=CENTER, font=("Courier 15 bold"), bg=co2, fg=co0)
label_mortes.grid(row=0, column=0, pady=1, padx=13)

mostrar_mortes = Label(mostrar_frame_mortes, text=mortes, width=12, height=1,
                       pady=7, padx=0, relief="flat", anchor=CENTER, font=("Courier 25 bold"), bg=co2, fg=co0)
mostrar_mortes.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_frame_mortes, text=str(dia), width=33, height=1,  # vou manter widh 33
                     pady=7, padx=0, relief="flat", anchor=CENTER, font=("Courier 11 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=2, column=0, pady=1)

mostrar_info = Label(mostrar_frame_mortes, text="Total de mortes", width=50, height=1,  # alterei width para 65
                     pady=7, padx=0, relief="flat", anchor=CENTER, font=("Courier 8 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=3, column=0, pady=1, padx=13)

mostrar_vermelho = Label(mostrar_frame_mortes, text="", width=19, height=1,  # alterei width para 65
                         pady=1, padx=0, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=co1, fg=co0)
mostrar_vermelho.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

#################################CRIANDO caixa de seleção#############################################

# label_pais = Label(selct_frame, text="Selecione o país", width=20, height=1,
# pady=10,padx=0, relief="flat", anchor=NW, font=("Ivi 15 bold"), bg=co6, fg=co0)
# label_pais.grid(row=0, column=0, pady=8, padx=13)

label_pais = Label(selct_frame, text="Selecione o país", width=20, height=1,
                   pady=1, padx=0, relief="flat", anchor=CENTER, font=("Roboto 12 bold "), bg=co6, fg=co0) #pady estava 7 E anchor"flat"
label_pais.grid(row=0, column=0, pady=1, padx=13)

pais = ["Global", "Angola", "Brazil", "India", "Portugal", "USA", "China"]

combo = ttk.Combobox(selct_frame, width=20, font="Roboto 10 bold") #width estava 30
combo["values"] = (pais)
combo.grid(row=0, column=1, padx=0, pady=8) #pady estava 13


###################################Chamando API####################################


def selecionado(eventObject):

    if combo.get() == "Global":
        response = requests.get("https://covid19.mathdro.id/api")
        info = response
        info = json.loads(info.text)

        infectados = info["confirmed"]["value"]
        mortes = info["deaths"]["value"]

        mostrar_infectados.configure(text=infectados)
        mostrar_mortes.configure(text=mortes)

    else:

        sel_pais = combo.get()
        response = requests.get(
            "https://covid19.mathdro.id/api/countries/{}".format(sel_pais))
        info = response
        info = json.loads(info.text)

        infectados = info["confirmed"]["value"]
        mortes = info["deaths"]["value"]
        dia = info["lastUpdate"]
        dia = datetime.datetime.strptime(dia, "%Y-%m-%dT%H:%M:%S.000Z")
        dia = dia.strftime("%c")

        mostrar_infectados.configure(text=infectados)
        mostrar_mortes.configure(text=mortes)

        #print(infectados, mortes, dia)

combo.bind("<<ComboboxSelected>>" , selecionado)

janela.mainloop()
