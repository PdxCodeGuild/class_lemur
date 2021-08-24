import mini_capstone_character
import PySimpleGUI as sg
from random import randint


def roll_dice(type_of_dice, number_of_dice, mod):
    i = 0
    dice_total = 0
    while i < number_of_dice:
        dice_total += randint(1, type_of_dice)
        i += 1
    dice_total += mod
    if dice_total < 1:
        return 1
    return(dice_total)


dice = {'d4': 4, 'd6': 6, 'd8': 8, 'd10': 10,
        'd12': 12, 'd20': 20, 'd100': 100}
mod = 0

sg.theme('DarkAmber')

strength_layout1 = [
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('  Strength   ')],
    [sg.Text(f'       {mini_capstone_character.stats[1]}')],
    [sg.Text('')],
    [sg.Text('')]
]
strength_layout2 = [
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text(f'{mini_capstone_character.character.strength()[0]} Saving Throw    ')],
    [sg.Text(f'{mini_capstone_character.character.strength()[1]} Athletics')],
    [sg.Text('')],
    [sg.Text('')],
]
dexterity_layout1 = [
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('  Dexterity  ')],
    [sg.Text(f'       {mini_capstone_character.stats[2]}')],
    [sg.Text('')],
    [sg.Text('')]
]
dexterity_layout2 = [
    [sg.Text('')],
    [sg.Text(f'{mini_capstone_character.character.dexterity()[0]} Saving Throw')],
    [sg.Text(f'{mini_capstone_character.character.dexterity()[1]} Acrobatics')],
    [sg.Text(f'{mini_capstone_character.character.dexterity()[2]} Sleight of Hand ')],
    [sg.Text(f'{mini_capstone_character.character.dexterity()[3]} Stealth')],
    [sg.Text('')]
]
constitution_layout1 = [
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('Constitution')],
    [sg.Text(f'       {mini_capstone_character.stats[3]}')],
    [sg.Text('')],
    [sg.Text('')],
]
constitution_layout2 = [
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text(f'{mini_capstone_character.character.constitution()} Saving Throw    ')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('')],
]
intelligence_layout1 = [
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text(' Inteligence ')],
    [sg.Text(f'      {mini_capstone_character.stats[4]}')],
    [sg.Text('')],
    [sg.Text('')]
]
intelligence_layout2 = [
    [sg.Text(
        f'{mini_capstone_character.character.intelligence()[0]} Saving Throw    ')],
    [sg.Text(f'{mini_capstone_character.character.intelligence()[1]} Arcana')],
    [sg.Text(f'{mini_capstone_character.character.intelligence()[2]} History ')],
    [sg.Text(f'{mini_capstone_character.character.intelligence()[3]} Investigation')],
    [sg.Text(f'{mini_capstone_character.character.intelligence()[4]} Nature')],
    [sg.Text(f'{mini_capstone_character.character.intelligence()[5]} Religion')]
]
wisdom_layout1 = [
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('  Wisdom   ')],
    [sg.Text(f'      {mini_capstone_character.stats[5]}')],
    [sg.Text('')],
    [sg.Text('')]
]
wisdom_layout2 = [
    [sg.Text(f'{mini_capstone_character.character.wisdom()[0]} Saving Throw')],
    [sg.Text(f'{mini_capstone_character.character.wisdom()[1]} Animal Handling')],
    [sg.Text(f'{mini_capstone_character.character.wisdom()[2]} Insight')],
    [sg.Text(f'{mini_capstone_character.character.wisdom()[3]} Medicene')],
    [sg.Text(f'{mini_capstone_character.character.wisdom()[4]} Perception')],
    [sg.Text(f'{mini_capstone_character.character.wisdom()[5]} Survival')]
]
charisma_layout1 = [
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text(' Charisma  ')],
    [sg.Text(f'     {mini_capstone_character.stats[6]}')],
    [sg.Text('')],
    [sg.Text('')]
]
charisma_layout2 = [
    [sg.Text(f'{mini_capstone_character.character.charisma()[0]} Saving Throw     ')],
    [sg.Text(f'{mini_capstone_character.character.charisma()[1]} Deception')],
    [sg.Text(f'{mini_capstone_character.character.charisma()[2]} Intimidation')],
    [sg.Text(f'{mini_capstone_character.character.charisma()[3]} Performance')],
    [sg.Text(f'{mini_capstone_character.character.charisma()[4]} Persuasion')],
    [sg.Text('')],
]
character_stats_layout = [

    [sg.Frame('', strength_layout1, pad=(0, 0)),
     sg.Frame('', strength_layout2, pad=(0, 0)),
     sg.Frame('', dexterity_layout1, pad=(0, 0)),
     sg.Frame('', dexterity_layout2, pad=(0, 0)),
     sg.Frame('', constitution_layout1, pad=(0, 0)),
     sg.Frame('', constitution_layout2, pad=(0, 0))],
    [sg.Frame('', intelligence_layout1, pad=(0, 0)),
     sg.Frame('', intelligence_layout2, pad=(0, 0)),
     sg.Frame('', wisdom_layout1, pad=(0, 0)),
     sg.Frame('', wisdom_layout2, pad=(0, 0)),
     sg.Frame('', charisma_layout1, pad=(0, 0)),
     sg.Frame('', charisma_layout2, pad=(0, 0))]
]
character_stats = [
    [sg.Frame(f'{mini_capstone_character.character.name} Stats',
              character_stats_layout)],
]
character_hp = [
    [sg.Text('   HP      ')],
    [sg.Text(f'    {mini_capstone_character.character.health()[0][1]}')]
]
character_ac = [
    [sg.Text('   AC    ')],
    [sg.Text(f'   {mini_capstone_character.character.health()[1][1]}')]
]
character_temp_hp = [
    [sg.Text('Temp HP')],
    [sg.Text(f'    {mini_capstone_character.character.health()[2][1]}')]
]
character_hit_dice = [
    [sg.Text('Hit Dice')],
    [sg.Text(f'  {mini_capstone_character.character.health()[3][1]}')]
]
character_speed = [
    [sg.Text('Speed    ')],
    [sg.Text(f'   {mini_capstone_character.character.health()[4][1]}')]
]
character_initiative = [
    [sg.Text('Initative ')],
    [sg.Text(f'     {mini_capstone_character.character.health()[5][1]}')]
]
character_health_layout = [
    [sg.Frame('', character_hp, pad=(0, 0)),
     sg.Frame('', character_ac, pad=(0, 0))],
    [sg.Frame('', character_temp_hp, pad=(0, 0)),
     sg.Frame('', character_hit_dice, pad=(0, 0))],
    [sg.Frame('', character_speed, pad=(0, 0)),
     sg.Frame('', character_initiative, pad=(0, 0))]

]
character_health = [
    [sg.Frame('', character_health_layout)]
]

# Define the window's contents
dice_roller = [
    [sg.Text('Dice    Number            Roll')],
    [[sg.Text((die), size=(4, 1)), sg.InputText(
        key=die, size=(4, 1)), sg.Text(size=(4, 1)), sg.Button(f'Roll {die}')] for die in dice],
    [sg.Radio('Modifier +', 'mods', default=True, key='p'),
     sg.Radio('Modifier -', 'mods', default=False, key='n'),
     sg.InputText(key='mod', default_text='0', size=(4, 1)),
     sg.Text('', size=(20, 1), key='mod_text')],
    [sg.Text('',), sg.Text(size=(40, 1), key=f'dice_output')],
    [sg.Button('Reset'), sg.Button('Quit')]
]

layout = [
    character_stats,
    character_health,
    dice_roller
]
# Create the window

window = sg.Window('Dice Roller', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == 'Reset':
        for value in values:
            window[value].update('')
        window[f'dice_output'].update('')

    # Output a message to the window
    try:
        if values['p'] == True:
            text = values['mod']
            mod = int(text)
        elif values['p'] == False:
            text = values['mod']
            mod = -1 * int(text)
    except:
        window['mod_text'].update('Try a number next time')
        mod = 0
    for die in dice:
        if event == f'Roll {die}':
            try:
                text = values[die]
                d = int(text)
                di = dice[die]
                if mod == 0:
                    window[f'dice_output'].update(
                        f'You rolled {d} {die} and got {roll_dice(di, d, mod)}')
                else:
                    window[f'dice_output'].update(
                        f'You rolled {d} {die} and got {roll_dice(di, d, mod)} with a modifier of {mod}')
            except:
                window[f'dice_output'].update('Try a number next time')

# Finish up by removing from the screen
window.close()
