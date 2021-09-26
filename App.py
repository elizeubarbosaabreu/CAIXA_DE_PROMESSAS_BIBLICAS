import PySimpleGUI as sg
import webbrowser, clipboard
from random import choice

#   ____      _                 _      
#  / ___|__ _(_)_  ____ _    __| | ___ 
# | |   / _` | \ \/ / _` |  / _` |/ _ \
# | |__| (_| | |>  < (_| | | (_| |  __/
#  \____\__,_|_/_/\_\__,_|  \__,_|\___|
#                                      
#  ____                                              
# |  _ \ _ __ ___  _ __ ___   ___  ___ ___  __ _ ___ 
# | |_) | '__/ _ \| '_ ` _ \ / _ \/ __/ __|/ _` / __|
# |  __/| | | (_) | | | | | |  __/\__ \__ \ (_| \__ \
# |_|   |_|  \___/|_| |_| |_|\___||___/___/\__,_|___/
#                                                    
#  ____  _ _     _ _               
# | __ )(_) |__ | (_) ___ __ _ ___ 
# |  _ \| | '_ \| | |/ __/ _` / __|
# | |_) | | |_) | | | (_| (_| \__ \
# |____/|_|_.__/|_|_|\___\__,_|___/
#                                  

# Software desenvolvido por Elizeu Barbosa Abreu
# https://github.com/elizeubarbosaabreu

url = 'https://www.bible.com/pt/bible/211/JHN.3.NTLH'

def novo_versiculo():
    with open('versos.txt') as f: # se não funcionar use um caminho real  ex.: 'C:\DIRETÓRIO\CAIXA_DE_PROMESSAS_BIBLICAS\versos.txt'
        lines = f.readlines()
    return choice(lines)

sg.theme('Reddit')

layout = [    
    [sg.Multiline(f'{novo_versiculo()}', key='-output-', font=('Courier', 12), size=(60, 7), reroute_cprint=True, write_only=False)],
    [sg.Stretch(),
     sg.Button('Novo Versiculo', size=(20, 1)),
     sg.VerticalSeparator(),
     sg.Button('Copiar Versiculo', size=(20, 1)),
     sg.VerticalSeparator(),
     sg.Button('Leia a Biblia', size=(20, 1)),
     sg.Stretch()]
    ]
    
window = sg.Window('CAIXA DE PROMESSAS BÍBLICAS', layout)


while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    elif event == 'Novo Versiculo':
        
        window['-output-'].update(novo_versiculo())
        
    elif event == 'Copiar Versiculo':
        versiculo = values['-output-']
        clipboard.copy(versiculo)
        sg.Popup('Versículo Copiado', 'O versículo está na área de transferência. Use as combinações [CTRL]+[V] ou botão direito do mouse e a opção "colar"...')
    
    elif event == 'Leia a Biblia':
        sg.Popup('Leia a Bíblia', 'A leitura da Bíblia Sagrada deve ser um hábito constante daqueles que creem em Deus e uma busca constante daqueles que ainda desconhecem-no ou pensam que Ele não existe...')
        webbrowser.open(f'{url}')
    
window.close
    
