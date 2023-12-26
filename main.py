
import PySimpleGUI as sg

layout = [[sg.Text("This is a test")], [sg.Button("Close")]]

# Create the window
window = sg.Window("Creative Window Name", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Close" or event == sg.WIN_CLOSED:
        break

window.close()