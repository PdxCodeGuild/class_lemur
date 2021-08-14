# import json
# import pandas as pd
# import pandasgui as pd
# from pandasgui import show

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
    group = input("Which body part would you like to work: Legs, Back, Chest, Arms, Abs, Shoulders? Enter 'New' to input your own workout.\n")
    group = group.title()
    if group == "New":
        group = input("Enter a muscle group: ")
        workout[group] = []
        choice = input("Press 'enter' to enter workout information or enter 'done' to exit: ")
        while choice != 'done':
            workout[group].append({ #user inputs exercise information
                'Exercise': input("Enter the exercise: "),
                'Sets' : int(input("How many sets? ")),
                'Reps' : int(input("How many reps? ")),
                '1RM' : int(input("What is your one rep max? ")),
                'Weight': int(input("Enter your working weight: ")),
                'Percentage of 1RM' : int(input("Enter the percentage of your 1RM: "))
            })
            choice = input("Press 'enter' to enter workout information or enter 'done' to exit: ")

        

    print(f"Your {group} workout for today:")
    count = 0
    exercise_num = 1
    for exercise in workout[group]: #display all exercises in workout
        print(f"#{exercise_num} {exercise['Exercise']} | Sets: {exercise['Sets']} | Reps: {exercise['Reps']}")
        exercise_num += 1
    
    exercise_num = 1
    for exercise in workout[group]:
        print(f"\n\n#{exercise_num} {exercise['Exercise']} | Sets: {exercise['Sets']} | Reps: {exercise['Reps']}")
        max_weight = int(input(f"Enter your one rep max on {workout[group][count]['Exercise']}: "))
        workout[group][count]['Weight'] =round(((workout[group][count]['Percentage of 1RM'] / 100) * max_weight), 0) #calculate working weight based on percentage and 1RM and inputs it into ['Weight']
        print(workout[group][count]['Weight']) 
        exercise_num += 1

        set_count = 0 # set counter to keep track of number of sets
        while set_count < workout[group][count]['Sets']:
            for i in range(workout[group][count]['Sets']):
                    set_count += 1
                    print(f"Set: {set_count} / {workout[group][count]['Sets']}") #display set count
                    
                    #display set information
                    print(f"Exercise: {exercise['Exercise']} | Sets: {exercise['Sets']} | Reps: {exercise['Reps']} | Weight: {exercise['Weight']} | Percentage of 1RM: {exercise['Percentage of 1RM']}%")


                    user_reps = int(input("How many reps did you complete? "))

                    """Adjusting to lower weight"""
                    if user_reps < workout[group][count]['Reps']:
                        new_one_rep_max = round(workout[group][count]['Weight'] * (36 / (37 - user_reps) ),0) 
                        # if set_count < (workout[group][count]['Sets'] -1):
                            # print(f"Your adjusted weight is {new_one_rep_max}")
                        workout[group][count]['Weight'] = ((workout[group][count]['Percentage of 1RM'] / 100) * new_one_rep_max)
                    
                    """adjusting to higher weight"""
                    # if user_reps > workout[group][count]['Reps']:
                    #     new_one_rep_max = round(workout[group][count]['Weight'] * (36 / (37 - user_reps) ),0) 
                    #     workout[group][count]['Weight'] = ((workout[group][count]['Percentage of 1RM'] / 100) * new_one_rep_max)
                        # print(workout[group][count], "a")
        count += 1
            # break    
        

    
programming()

# with open('workout.json', 'w') as f:
#     json.dump(workout, f)
    # f.write(workout)
# df = pd.DataFrame(workout)
# gui = show('df')
    

# with open('workout.json') as json_file:
#     workout = json.load(json_file)
#     for exercise in workout['Legs']:
#         print(f"Exercise: {exercise['Exercise']}, Sets: {exercise['Sets']}, Reps: {exercise['Reps']}")                    
            

