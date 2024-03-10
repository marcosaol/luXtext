import PySimpleGUI as sg

menu_def = [['&Arquivo', ['!&Abrir::abrirkey', '&Novo::novokey', '&Salvar::savekey']], ['&Ajuda', ['&Sobre']]]

tab_layout1 = [[]],

layout = [
    [sg.TabGroup([[sg.Tab(f"{Arquivo}", tab_layout1)]])],
    [sg.Menu(menu_def)],
    [[sg.Text('Your window!', size=(30, 5))]],
]
window = sg.Window('LuxText', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered ', values[0])

window.close()