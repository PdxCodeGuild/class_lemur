import csv
import json
from gooey import Gooey, GooeyParser



path = 'python_subject.csv'
subject_path = 'subject_list.csv'


def user_select():
    while True:
        user_input = input("\nSelect an option number (1 Select Currrent Subject, 2 Add subject): ")
        if user_input == '1' or user_input == '2':
            return user_input
        else:
            print("That is not a valid selection.")

def select_subject(subject_list):
    while True:
        print("\nYour available subjects are: ")
        for subject in subject_list:
            print("\t" + subject)
        user_input = input("\nSelect a subject: ")
        if user_input in subject_list:
            return user_input
        else:
            print("That is not a valid selection.")

def add_or_study(subject):
    while True:
        user_input = input(f"\nSelect either (study or add cards) for {subject} ")
        if user_input == 'study' or 'add cards':
            return user_input
        else: 
            print("That is not a valid selection")
    
def import_subject_csv(path):
    with open(path, 'r', encoding='utf8') as file:
        lines = file.read().split('\n')
        for i in range(len(lines)):
            lines[i] = lines[i].split(',')
    return lines[:-1]

def create_subject(path):
    subject_dict = {}
    subject_name = input("What is the new subject's name? ")
    subject_dict['name'] = subject_name
    while True:
        import_or_not = input("Would you like to import a csv with questions and answers (yes/no)? ").lower()
        if import_or_not == 'yes':
            #path = input("Input the path to the csv to import. ")
            list_of_questions_and_answers = import_subject_csv(path)
            for item in list_of_questions_and_answers:
                print(item)
                subject_dict[item[0]] = item[1]
            return subject_dict
        elif import_or_not == 'no':
            break
        else:
            print("That is not a valid selection.")

def add_card():
    question = input("What is the question for this card? ")
    answer = input("What is the answer for this card? ")
    return question, answer

def save_subject_dictionary(subject_dict):
    with open(f"{subject_dict['name']}.json", 'w') as file:
        json.dump(subject_dict, file, indent=4)

def save_subject_list(subject_list, subject_path):
    with open(subject_path, 'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(subject_list)

def read_subject_list(subject_path):
    with open(subject_path, 'r') as file:
        lines = file.read().rstrip()
        lines = lines.split(',')
        print(lines)

def open_subject_dict(subject):
    with open(f"{subject}.json") as file:
        subject_dict = json.load(file)
    return subject_dict

subject_dict = create_subject(path)
save_subject_dictionary(subject_dict)

#question_answer_dict = import_subject_csv(path)
# subject_list = ['cats', 'dogs', 'chickens', 'python']
# # select_subject(subject_list)

# save_subject_list(subject_list, subject_path)
# read_subject_list(subject_path)

# @Gooey
# def main():
#   parser = GooeyParser(...)
#   subject_list = []