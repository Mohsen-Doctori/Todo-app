import PySimpleGUI as sg


def km_to_milse(km):
    pass



while True:
    window = sg.Window
    event, values = window.read(self=)
    match event:
        case "Convert":
            km: object = values["kms"]
            result = km_to_milse(km)
            window['output'].update(value=result)
        case sg.WIN_CLOSED:
            break

window.close()