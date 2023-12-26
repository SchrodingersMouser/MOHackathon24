import PySimpleGUI as psg
layout = [
            [psg.Text(text='Hello World', font=('Quicksand', 20), size=20, expand_x=True, justification='center')],
            [psg.Checkbox(text = "This is a Checkbox", default = False)],
            [psg.Button(button_text = "Exit", font = ("Quicksand", 20), button_color = "Blue")]
         ]
window = psg.Window("Caleb's Test Window", layout)
while True:
   event, values = window.read()
   print(event, values)
   if event in (None, 'Exit'):
        break
   if event == "Close" or event == psg.WIN_CLOSED:
        break
window.close()

"""
import PySimpleGUI as sg

layout = [  [sg.Text('My Window'), sg.Push(), sg.Button('Upper Right')],
            [sg.Input(key='-IN-')],
            [sg.Button('Exit'), sg.Push(), sg.Button('Lower Right')]  ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
"""