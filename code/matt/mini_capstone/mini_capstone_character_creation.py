import PySimpleGUI as sf
from PySimpleGUI.PySimpleGUI import Combo


def main():
    classes = ['Barbarion', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
               'Paladin', 'Ranger', 'Rouge', 'Sorcerer', 'Warlock', 'Wizard']

    barbarion_p = ['Athletics', 'Animal Handling', 'Athletics', 'Intimidation',
                   'Nature', 'Perception', 'Survival']

    bard_p = ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics',
              'Deception', 'History', 'Insight', 'Intimidation', 'Investigation',
              'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion',
              'Religion', 'Sleight of Hand', 'Stealth', 'Survival']

    cleric_p = ['History', 'Insight', 'Medicine', 'Persuasion', 'Medicine']

    druid_p = ['Animal Handling', 'Arcana', 'Insight', 'Medicine', 'Nature', 'Perception',
               'Religion', 'Survival']

    fighter_p = ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight',
                 'Intimidation', 'Perception', 'Survival']

    monk_p = ['Acrobatics', 'Athletics', 'History',
              'Insight', 'Religion',  'Stealth', ]

    paladin_p = ['Athletics', 'Insight', 'Intimidation',
                 'Medicine', 'Persuasion', 'Religion', ]

    ranger_p = ['Animal Handling', 'Athletics', 'Insight', 'Investigation',
                'Nature', 'Perception', 'Stealth', 'Survival']

    rouge_p = ['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation',
               'Investigation', 'Perception', 'Performance', 'Persuasion', 'Sleight of Hand',
               'Stealth', ]

    sorcerer_p = ['Arcana', 'Deception',  'Insight', 'Intimidation', 'Persuasion',
                  'Religion']

    warlock_p = ['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation',
                 'Nature', 'Religion']

    wizard_p = ['Arcana', 'History', 'Insight',
                'Investigation', 'Medicine', 'Religion']

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
        [sf.Combo(classes, key='class', enable_events=True, size=(15, 1)),
         sf.Combo([], key='proficiencies', enable_events=True, size=(15, 1))],
        [sf.Text(key='output')],
        [sf.Button('Save'), sf.Button('Cancel')]]

    stats = []
    # Create the Window
    window = sf.Window('Character Creation', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sf.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break

        if event == 'class':
            if values['class'] == 'Barbarion':
                window['proficiencies'].update(values=barbarion_p)
            elif values['class'] == 'Bard':
                window['proficiencies'].update(values=bard_p)
            elif values['class'] == 'Cleric':
                window['proficiencies'].update(values=cleric_p)
            elif values['class'] == 'Druid':
                window['proficiencies'].update(values=druid_p)
            elif values['class'] == 'Fighter':
                window['proficiencies'].update(values=fighter_p)
            elif values['class'] == 'Monk':
                window['proficiencies'].update(values=monk_p)
            elif values['class'] == 'Paladin':
                window['proficiencies'].update(values=paladin_p)
            elif values['class'] == 'Ranger':
                window['proficiencies'].update(values=ranger_p)
            elif values['class'] == 'Rouge':
                window['proficiencies'].update(values=rouge_p)
            elif values['class'] == 'Sorcerer':
                window['proficiencies'].update(values=sorcerer_p)
            elif values['class'] == 'Warlock':
                window['proficiencies'].update(values=warlock_p)
            elif values['class'] == 'Wizard':
                window['proficiencies'].update(values=wizard_p)
        # rouge 4 ranger 3 bard 3
        selected_p = []
        selected_p2 = []
        if event == 'proficiencies':
            selected_p.append(values['proficiencies'])
            window['output'].update(selected_p)
        if event == 'proficiencies':
            selected_p2.append(values['proficiencies'])
            window['output'].update(selected_p2)

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
