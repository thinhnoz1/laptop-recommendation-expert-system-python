from typing import runtime_checkable
import PySimpleGUI as sg
import main as expert
from math import sqrt

layout = [
    [
        sg.Radio("Gaming","RADIO1", default= True, key="-gaming-"),
        sg.Radio("Dev",  "RADIO1", default= False, key="-dev-"),
        sg.Radio("Clerk", "RADIO1", default= False, key="-clerk-"),
        sg.Radio("Home", "RADIO1", default= False, key="-home-"),
    ],
    [
        sg.T("Your budget", key="lbl_a", font="Helvetica 16"),
        sg.I("0", key="edit_a", size=(10, 1), pad=(10, 10)),
    ],
    [sg.B("Find", key="find", border_width=5, pad=(10, 10), size=(200, 1))],
    [
        sg.Multiline(
            "", size=(25, 25), font="Helvetica 14", disabled=True, key="-multiline-"
        )
    ],
]

window = sg.Window("Laptop finder", layout, size=(300, 300))

while True:
    event, values = window.read()
    rules = expert.import_rules()
    facts = expert.import_facts()

    purpose = ""
    if (values["-gaming-"] == True):
        purpose = "gaming"
    if (values["-dev-"] == True):
        purpose = "dev"
    if (values["-clerk-"] == True):
        purpose = "clerk"
    if (values["-home-"] == True):
        purpose = "home"
    
    budget = int(values['edit_a'])

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == "find":
        try:
            result = ""
            index_result = expert.recommend(rules, facts, purpose, budget)
            for idx in index_result:
                result = result + facts[idx]["brand"] + " " + facts[idx]["model"] + "\n"
            #text_elem.update("This is a random integer: {}".format(r))
            text_elem = window["-multiline-"]
            text_elem.update(result)

        except:
            sg.popup_error("Some error happened!")
            break

window.close()
