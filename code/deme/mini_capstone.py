import easygui

'''determine sets and reps based off of 1rm
    -lay out workout plan
    -IF you completed written set/reps, move on to other set
    -ELIF calculate adjustment to plan'''
workout = {}
workout_log=[]
answer = []
workout['Legs'] = []
workout['Legs'].append({
    'Exercise': 'Back Squat',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Legs'].append({
    'Exercise': 'Front Squat',
    'Sets' : 3,
    'Reps' : 6,
    'Weight': '',
    'Percentage of 1RM': 80
})
workout['Legs'].append({
    'Exercise': 'Leg Extension',
    'Sets' : 4,
    'Reps' : 15,
    'Weight': '',
    'Percentage of 1RM': 65
})
workout['Legs'].append({
    'Exercise': 'Lying Hamstring Curl',
    'Sets' : 4,
    'Reps' : 15,
    'Weight': '',
    'Percentage of 1RM': 65
})
workout['Legs'].append({
    'Exercise': 'Standing Calf Raise',
    'Sets' : 4,
    'Reps' : 15,
    'Weight': '',
    'Percentage of 1RM': 65
})
workout['Back'] = []
workout['Back'].append({
    'Exercise': 'Deadlift',
    'Sets' : 4,
    'Reps' : 6,
    'Weight': '',
    'Percentage of 1RM': 80
})
workout['Back'].append({
    'Exercise': 'Bent Over Row',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Back'].append({
    'Exercise': 'Lat Pulldown',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Back'].append({
    'Exercise': 'T-Bar Row',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Back'].append({
    'Exercise': 'Wide Grip Pull-up',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Shoulders'] = []
workout['Shoulders'].append({
    'Exercise': 'Military Press',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Shoulders'].append({
    'Exercise': 'Dumbbell Press',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Shoulders'].append({
    'Exercise': 'Barbell Shrug',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Shoulders'].append({
    'Exercise': 'Cable Lateral Raise',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Chest'] = []
workout['Chest'].append({
    'Exercise': 'Bench Press',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Chest'].append({
    'Exercise': 'Incline Dumbbell Press',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Chest'].append({
    'Exercise': 'Cable Fly',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Chest'].append({
    'Exercise': 'Weighted Dip',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Arms'] = []
workout['Arms'].append({
    'Exercise': 'Close-grip Bench Press',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Arms'].append({
    'Exercise': 'Barbell Curl',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Arms'].append({
    'Exercise': 'Triceps Push-down',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Arms'].append({
    'Exercise': 'Hammer Curl',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Abs'] = []
workout['Abs'].append({
    'Exercise': 'Reverse Crunch',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Abs'].append({
    'Exercise': 'Bicycle Crunch',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Abs'].append({
    'Exercise': 'Weighted Sit-Up',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})
workout['Abs'].append({
    'Exercise': 'Hanging Leg Raise',
    'Sets' : 4,
    'Reps' : 8,
    'Weight': '',
    'Percentage of 1RM': 75
})

def programming():
    group = easygui.choicebox(msg="Select your workout?", choices=["Legs", "Back", "Chest", "Arms", "Abs", "Shoulders", "Custom Workout"])
    group = group.title()
    if group == "Custom Workout":
        group = easygui.enterbox(msg="Enter a muscle group: ")
        workout[group]=[]
        # # print(workout_log)
        # value = easygui.multenterbox(msg='type in your stuff', fields=[{workout[group]}, 'Number of Sets', 'Number of Reps', 'What is your one rep max?', 'Enter yourworking weight?', 'Enter the Percentage of your 1RM'])
        # easygui.msgbox(msg=value)
        choice = easygui.choicebox("Select \"Add New\" to enter another exercise or \"Done\".", choices=["Add New", "Done"])
        while choice != 'Done':
            workout[group].append({ #user inputs exercise information
                'Exercise': easygui.enterbox(msg="Enter the exercise: "),
                'Sets' : easygui.integerbox(msg="How many sets? "),
                'Reps' : easygui.integerbox(msg="How many reps? "),
                '1RM' : easygui.integerbox(msg="What is your one rep max? "),
                'Weight': easygui.integerbox(msg="Enter your working weight: "),
                'Percentage of 1RM' : easygui.integerbox(msg="Enter the percentage of your 1RM: ")
            })
            choice = easygui.choicebox("Select \"Add New\" to enter another exercise or \"Done\".", choices=["Add New", "Done"])

    count = 0
    exercise_num = 1
    exercises = ""
    for exercise in workout[group]: #display all exercises in workout
        exercises += f"#{exercise_num} {exercise['Exercise']} | Sets: {exercise['Sets']} | Reps: {exercise['Reps']}\n"
        exercise_num += 1
    easygui.msgbox(msg=f"Your {group} workout for today:\n{exercises}")
    exercise_num = 1
    for exercise in workout[group]:
        max_weight = easygui.integerbox(msg=f"#{exercise_num} {exercise['Exercise']} | Sets: {exercise['Sets']} | Reps: {exercise['Reps']}\nEnter your one rep max on {workout[group][count]['Exercise']}: ", upperbound=1000)
        workout[group][count]['Weight'] =round(((workout[group][count]['Percentage of 1RM'] / 100) * max_weight), 0) #calculate working weight based on percentage and 1RM and inputs it into ['Weight']

        exercise_num += 1
        # workout_log.append(workout[group][count]) # appending the entire workout list to workout_log multiple times
        print(workout_log)
        set_count = 0 # set counter to keep track of number of sets
        log = ""

        while set_count < workout[group][count]['Sets']:

            for i in range(workout[group][count]['Sets']):
                
                set_count += 1
                # print(f"Set: {set_count} / {workout[group][count]['Sets']}") #display set count
                # workout_log[group].append(workout[group][count]['Sets'])

                #display set information
                # print(f"Exercise: {exercise['Exercise']} | Sets: {exercise['Sets']} | Reps: {exercise['Reps']} | Weight: {exercise['Weight']} | Percentage of 1RM: {exercise['Percentage of 1RM']}%")

                user_reps = easygui.integerbox(msg=f"Exercise: {exercise['Exercise']} | Sets: {exercise['Sets']} | Reps: {exercise['Reps']} | Weight: {exercise['Weight']} | Percentage of 1RM: {exercise['Percentage of 1RM']}%\nSet: {set_count} / {workout[group][count]['Sets']}\nHow many reps did you complete? ", title=f"Exercise: {exercise['Exercise']} | Sets: {exercise['Sets']}", upperbound=1000)

                print(workout[group], "a")
                print(workout[group][count], "b")
                print(count)
                workout_log.append(workout[group][count])

                """Adjusting to lower weight"""
                if user_reps < workout[group][count]['Reps']:
                    new_one_rep_max = round(workout[group][count]['Weight'] * (36 / (37 - user_reps) ),0) 
                    workout[group][count]['Weight'] = ((workout[group][count]['Percentage of 1RM'] / 100) * new_one_rep_max)

                    answer.append(workout[group][count])
                    answer.append("**************************************************************************")
                else:
                    answer.append(workout[group][count])
                    answer.append("**************************************************************************")
            
            print(answer,"bbbbbbb")
            for line in answer:
                print(line,"abcdef")
                log += f"{line}\n"
        easygui.msgbox(msg=log, title="Workout Recap")           
        count += 1
        print(count,"count")   
programming()
# print(workout_log, "aaaaaaaa")



# for group in workout_log:
#     for exercise in group:
#         print(exercise)

# with open('workout.json', 'w') as f:
#     json.dump(workout, f)
#     f.write('workout.json')
# # df = pd.DataFrame(workout)
# # gui = show('df')
    

# with open('workout.json') as json_file:
#     workout = json.load(json_file)
#     for exercise in workout['Legs']:
#         print(f"Exercise: {exercise['Exercise']}, Sets: {exercise['Sets']}, Reps: {exercise['Reps']}aaaa")                    
            

# with open('workout.json', 'w') as outfile:
#     json.dump(workout, outfile)

# with open('workout.json') as json_file:
#     workout = json.load(json_file)
#     for exercise in workout['Legs']:
#         print(f"Exercise: {exercise['Exercise']}, Sets: {exercise['Sets']}, Reps: {exercise['Reps']}")
# print(workout)
# df = pd.read_json(params = {'path' : workout})
# print(df)
# df = pd.io.json.read_json('workout.json')
# df = pd.read_json('workout.txt')

# print(df.to_string()) 

# show(workout)