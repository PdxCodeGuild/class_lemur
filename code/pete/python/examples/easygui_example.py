import easygui

# num = easygui.integerbox(msg='give me a number and I\'ll multiply it by 3:  ')
# easygui.msgbox(msg=f'{num} times 3 is {num * 3}')


# muscle_group = easygui.choicebox(msg="which muscle group", choices=["legs", 'arms', 'back'])

# print(muscle_group)
# num = int(input('give me a number and I\'ll multiply it by 3:  '))
# print(f'{num} times 3 is {num * 3}')\


values = easygui.multenterbox(msg='type in your stuff', fields=['name', 'age', 'job'])

print(values)