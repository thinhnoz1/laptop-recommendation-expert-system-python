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
    [sg.B("Find one", key="findOne", border_width=5, pad=(10, 10), size=(200, 1))],
    [
        sg.Multiline(
            "", size=(25, 25), font="Helvetica 14", disabled=True, key="-multiline-"
        )
    ],
]

window = sg.Window("Laptop finder", layout, size=(300, 300))

rules = expert.import_rules()
facts = expert.import_facts()
index_result = []

while True:
    event, values = window.read()
    purpose = ""
    result = ""

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
            index_result = expert.recommend(rules, facts, purpose, budget)
            for idx in index_result:
                result = result + facts[idx]["brand"] + " " + facts[idx]["model"] + "- Price: " + str(facts[idx]["price"]) + "\n"
            #text_elem.update("This is a random integer: {}".format(r))
            text_elem = window["-multiline-"]
            text_elem.update(result)

        except:
            sg.popup_error("Some error happened!")
            break

    if event == "findOne":
        try:   
            if (len(index_result) != 0):
                best_result = expert.choose_one_best_option(index_result, facts)
                text_elem = window["-multiline-"]
                text_elem.update(facts[best_result]["brand"] + " " + facts[best_result]["model"] + "- Price: " + str(facts[best_result]["price"]))
            else:
                sg.popup_error("Press find first!")
        except:
            sg.popup_error("Some error happened!")
            break
window.close()
