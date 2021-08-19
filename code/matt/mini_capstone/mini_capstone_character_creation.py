import PySimpleGUI as sf
from PySimpleGUI.PySimpleGUI import Combo


def main():
    classes = [
        'Barbarion', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
        'Paladin', 'Ranger', 'Rouge', 'Sorcerer', 'Warlock', 'Wizard'
    ]

    #  sf.Combo(barbarion_p, key='p')],
    # barbarion_p = ['Athletics', 'Animal Handling', 'Athletics', 'Intimidation',
    #                'Nature', 'Perception', 'Survival'
    #                ]
    # bard_p = ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics',
    #           'Deception', 'History', 'Insight', 'Intimidation', 'Investigation',
    #           'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion',
    #           'Religion', 'Sleight of Hand', 'Stealth', 'Survival'
    #           ]
    sf.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [
        [sf.Text('''Enter all feilds and save to create new character or hit cancel
    to continue with previous character.''', size=(50, 2))],
        [sf.Text('Enter your characters name: ', size=(22,  1)),
         sf.InputText(size=(20, 1), key='name')],
        [sf.Text('Enter your strength: ', size=(22,  1)),
         sf.InputText(size=(20, 1), key='str')],
        [sf.Text('Enter your dexterity: ', size=(22,  1)),
         sf.InputText(size=(20, 1), key='dex')],
        [sf.Text('Enter your constistution: ', size=(22,  1)),
         sf.InputText(size=(20, 1), key='con')],
        [sf.Text('Enter your intelligence: ', size=(22,  1)),
         sf.InputText('', size=(20, 1), key='intel')],
        [sf.Text('Enter your wisdom: ', size=(22,  1)),
         sf.InputText(size=(20, 1), key='wis')],
        [sf.Text('Enter your charisma: ', size=(22,  1)),
         sf.InputText(size=(20, 1), key='char')],
        [sf.Text(key='output')],
        [sf.Combo(classes, key='class')],
        [sf.Button('Save'), sf.Button('Cancel')]]

    stats = []
    # Create the Window
    window = sf.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sf.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        # if event == 'class':
        #     if 'class' == 'Barbarion':
        #         window.Values['p'] = barbarion_p
        #         selected_p = []
        #         if 'p' == value:
        #             while len(selected_p) < 2:
        #                 selected_p.append('p')
        if event == 'Save':
            for value in values:
                if values[value] == '':
                    window['output'].update("Please fill out all feilds.")
                    stats.clear()
                elif values[value] != '':
                    stats.append(values[value])
            if len(stats) == 8:
                with open("character.txt", 'w', encoding='utf-8') as f:
                    for value in values:
                        f.write(values[value])
                        f.write('\n')
            break

    window.close()
