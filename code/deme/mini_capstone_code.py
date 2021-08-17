import json
import pandas as pd
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#photo
logo = Image.open('logo.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column = 1, row= 0)

#instructions
instructions = tk.Label(root, text = "Select a PDF file", font = "Raleway")
instructions.grid(columnspan=3, column=0, row=1)

#function
def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("PDF file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        print(page_content)
        
        #text box
        text_box = tk.Text(root, height=10, width = 50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify = "center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")


#browse button
old_workout = tk.StringVar()
old_workout_btn = tk.Button(root, textvariable=old_workout, command=lambda:open_file(), font="Raleway", bg = "black", fg="white", height=2, width=15)
old_workout.set("View Past Workout")
old_workout_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

new_workout = tk.StringVar()
new_workout_btn = tk.Button(root, textvariable=new_workout, command=lambda:open_file(), font="Raleway", bg = "black", fg="white", height=2, width=15)
new_workout.set("New Workout")
new_workout_btn.grid(column=2, row=2)

root.mainloop()




'''determine sets and reps based off of 1rm
    -lay out workout plan
    -IF you completed written set/reps, move on to other set
    -ELIF calculate adjustment to plan'''
workout = {}
workout['Legs'] = []
workout['Legs'].append({
    'Exercise': 'Back Squat',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': 90,
    'Percentage of 1RM': 75
})
workout['Legs'].append({
    'Exercise': 'Front Squat',
    'Sets' : 3,
    'Reps' : 6,
    'Weight': 90,
    'Percentage of 1RM': 80
})
workout['Legs'].append({
    'Exercise': 'Leg Extension',
    'Sets' : 4,
    'Reps' : 15,
    'Weight': 90,
    'Percentage of 1RM': 65
})
workout['Legs'].append({
    'Exercise': 'Lying Hamstring Curl',
    'Sets' : 4,
    'Reps' : 15,
    'Weight': 90,
    'Percentage of 1RM': 65
})
workout['Legs'].append({
    'Exercise': 'Standing Calf Raise',
    'Sets' : 4,
    'Reps' : 15,
    'Weight': 90,
    'Percentage of 1RM': 65
})
workout['Back'] = []
workout['Back'].append({
    'Exercise': 'Deadlift',
    'Sets' : 3,
    'Reps' : 6,
    'Weight': 90,
    'Percentage of 1RM': 80
})
workout['Back'].append({
    'Exercise': 'Bent Over Row',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': 90,
    'Percentage of 1RM': 75
})
workout['Back'].append({
    'Exercise': 'Lat Pulldown',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': 90,
    'Percentage of 1RM': 75
})
workout['Back'].append({
    'Exercise': 'T-Bar Row',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': 90,
    'Percentage of 1RM': 75
})
workout['Back'].append({
    'Exercise': 'Wide Grip Pull-up',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': 90,
    'Percentage of 1RM': 75
})


# df = pd.DataFrame.from_dict(workout, orient='index')
# print(df)


###########   workout2 = pd.DataFrame(workout)

# back = pd.DataFrame(workout['Back'])
# print(back)
set_count = 0 # set counter to keep track of number of sets

def programming():
    group = input("Which body part would you like to work: Legs, Back, Chest, Arms, Abs, Shoulders?\n")
    for exercise in workout[group]:
        print(f"Exercise: {exercise['Exercise']}, Sets: {exercise['Sets']}, Reps: {exercise['Reps']}")
    # print(workout2[group])
    count = 0
    max_weight = int(input("What is your max on this exercise?"))
    workout[group][count]['Weight'] = ((workout[group][count]['Percentage of 1RM'] / 100) * max_weight)
    # workout2[group][count]['Weight'] = 5
    print(workout2)
    print(workout2[group][count])

    #set count
    while set_count < workout[group][count]['Sets']:
        user_reps = input("How many reps did you complete?")
        if user_reps < workout[group]['Reps']:
            new_one_rep_max = max_weight * (36 / (37 - user_reps) )
            workout[group]['Weight'] = new_one_rep_max
            print(workout[group])    
    
programming()

max_weight = int(input("What is your max on this exercise?"))
weight = int(input("Enter the weight:"))
reps = int(input("Enter the amount of reps you were able to perform"))
# percent_of_1rm = (100 - (reps * 2.5)) / 100
# new_one_rep_max = weight / percent_of_1rm
new_one_rep_max = weight * (36 / (37 - reps) )
print(new_one_rep_max)
# percentage_of_1rm = (36 / (37 + reps)) / weight
# print(percentage_of_1rm)

if workout['Legs'][1]['Reps'] == reps:
    set_count += 1
if workout['Legs'][1]['Reps'] > reps:
    percent_of_1rm = (100 - (reps * 2.5)) / 100
    # one_rep_max = weight / percent_of_1rm
    # print(one_rep_max)
    print(new_one_rep_max)
# gui = show(workout)

# print(one_rep_max)

# if reps == 

# print(workout)
with open('workout.json', 'w') as outfile:
    json.dump(workout, outfile)

with open('workout.json') as json_file:
    workout = json.load(json_file)
    for exercise in workout['Legs']:
        print(f"Exercise: {exercise['Exercise']}, Sets: {exercise['Sets']}, Reps: {exercise['Reps']}")
# print(workout)
# df = pd.read_json(params = {'path' : workout})
# print(df)
# df = pd.io.json.read_json('workout.json')
df = pd.DataFrame.from_dict(workout, orient='index')
print(df)
# show(workout)
# show(df)


#recalculates reps based off of 1rm of performance. 


import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#photo
logo = Image.open('logo.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column = 1, row= 0)

#instructions
instructions = tk.Label(root, text = "Select a PDF file", font = "Raleway")
instructions.grid(columnspan=3, column=0, row=1)

#function
def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("PDF file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        print(page_content)
        
        #text box
        text_box = tk.Text(root, height=10, width = 50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify = "center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")


#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg = "black", fg="white", height=2, width=15)
browse_text.set("Enter")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()



