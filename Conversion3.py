import PySimpleGUI as sg
sg.theme('DarkBlue1')
startLayout = [[sg.Text('Choose a conversion type')],
          [sg.Button('Ft-M'), sg.Button('In-Cm'), sg.Button('Cups-Liters'), sg.Button('Lbs-Kg')],
          [sg.Button('M-Ft'), sg.Button('Cm-In'), sg.Button('Liters-Cups'), sg.Button('Kg-Lbs')]]
window = sg.Window('Conversion 3.0', startLayout)
while True:
    event, values = window.read()
    if event == 'Ft-M':
        window.close()
        layout1 = [[sg.Text('Enter amount of feet you would like to convert to meters:')],
                   [sg.InputText (key='-IN-'), sg.Submit()]]
        window = sg.Window('Ft-M', layout1)
        event, values = window.read()
        window.close()
        feet = (values['-IN-'])
        meters = float(feet)*0.3048
        layout2 = [[sg.Text('-------That is equal to:-------')],
                     [sg.Text(str(meters) + ' meters')]]
        window = sg.Window('Conversion Complete!', layout2)
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        break
    if event == 'M-Ft':
        window.close()
        layout2 = [[sg.Text('Enter amount of meters you would like to convert to feet:')],
                   [sg.InputText (key='-IN-'), sg.Submit()]]
        window = sg.Window('M-Ft', layout2)
        event, values = window.read()
        window.close()
        meters = (values['-IN-'])
        feet = float(meters)/0.3048
        layout3 = [[sg.Text('-------That is equal to:-------')],
                     [sg.Text(str(feet) + ' feet')]]
        window = sg.Window('Conversion Complete!', layout3)
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        break
    if event == 'In-Cm':
        window.close()
        layout4 = [[sg.Text('Enter amount of inches you would like to convert to centimeters:')],
                   [sg.InputText (key='-IN-'), sg.Submit()]]
        window = sg.Window('In-Cm', layout4)
        event, values = window.read()
        window.close()
        inches = (values['-IN-'])
        cm = float(inches)*2.54
        layout5 = [[sg.Text('-------That is equal to:-------')],
                     [sg.Text(str(cm) + ' centimeters')]]
        window = sg.Window('Conversion Complete!', layout5)
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        break
    if event == 'Cm-In':
        window.close()
        layout6 = [[sg.Text('Enter amount of centimeters you would like to convert to inches:')],
                   [sg.InputText (key='-IN-'), sg.Submit()]]
        window = sg.Window('Cm-In', layout6)
        event, values = window.read()
        window.close()
        cm = (values['-IN-'])
        inches = float(cm)/2.54
        layout7 = [[sg.Text('-------That is equal to:-------')],
                     [sg.Text(str(inches) + ' inches.')]]
        window = sg.Window('Conversion Complete!', layout7)
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        break
    if event == 'Cups-Liters':
        window.close()
        layout8 = [[sg.Text('Enter amount of cups you would like to convert to liters:')],
                   [sg.InputText (key='-IN-'), sg.Submit()]]
        window = sg.Window('Cups-Liters', layout8)
        event, values = window.read()
        window.close()
        cups = (values['-IN-'])
        liters = float(cups)*0.236588
        layout9 = [[sg.Text('-------That is equal to:-------')],
                     [sg.Text(str(liters) + ' liters.')]]
        window = sg.Window('Conversion Complete!', layout9)
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        break
    if event == 'Liters-Cups':
        window.close()
        layout10 = [[sg.Text('Enter amount of liters you would like to convert to cups:')],
                   [sg.InputText (key='-IN-'), sg.Submit()]]
        window = sg.Window('Liters-Cups', layout10)
        event, values = window.read()
        window.close()
        liters = (values['-IN-'])
        cups = float(liters)/0.236588
        layout11 = [[sg.Text('-------That is equal to:-------')],
                     [sg.Text(str(cups) + ' cups.')]]
        window = sg.Window('Conversion Complete!', layout11)
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        break
    if event == 'Lbs-Kg':
        window.close()
        layout12 = [[sg.Text('Enter amount of pounds you would like to convert to kilos:')],
                   [sg.InputText (key='-IN-'), sg.Submit()]]
        window = sg.Window('Lbs-Kg', layout12)
        event, values = window.read()
        window.close()
        lbs = (values['-IN-'])
        kg = float(lbs)*0.453592
        layout13 = [[sg.Text('-------That is equal to:-------')],
                     [sg.Text(str(kg) + ' kilograms.')]]
        window = sg.Window('Conversion Complete!', layout11)
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        break
    if event == 'Kg-Lbs':
        window.close()
        layout14 = [[sg.Text('Enter amount of kilos you would like to convert to pounds:')],
                   [sg.InputText (key='-IN-'), sg.Submit()]]
        window = sg.Window('Kg-Lbs', layout14)
        event, values = window.read()
        window.close()
        kg = (values['-IN-'])
        lbs = float(kg)/0.453592
        layout15 = [[sg.Text('-------That is equal to:-------')],
                     [sg.Text(str(lbs) + ' pounds.')]]
        window = sg.Window('Conversion Complete!', layout15)
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        break
    break
window.close()
        
