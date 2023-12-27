
import PySimpleGUI as psg
layout = [
            [psg.Text(text='Hello World', font=('Quicksand', 20), size=20, expand_x=True, justification='center')],
            [psg.Checkbox(text = "This is a Checkbox", default = False)],
            [psg.Button(button_text = "Exit", font = ("Quicksand", 20), button_color = "Black", justification = 'center')]
        ]
window = psg.Window("Caleb's Test Window", layout, resizable = True).Finalize()
window.Maximize()
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

# import PySimpleGUI as sg

# def main():
#     column_to_be_centered = [  [sg.Text('My Window')],
#                 [sg.Input(key='-IN-')],
#                 [sg.Text(size=(12,1), key='-OUT-')],
#                 [sg.Button('Go'), sg.Button('Exit')]]

#     layout = [[sg.VPush()],
#               [sg.Push(), sg.Column(column_to_be_centered,element_justification='c'), sg.Push()],
#               [sg.VPush()]]

#     window = sg.Window('Window Title', layout, size=(500,300))

#     while True:
#         event, values = window.read()
#         if event == sg.WIN_CLOSED or event == 'Exit':
#             break

#     window.close()


# if __name__ == '__main__':
#     main()