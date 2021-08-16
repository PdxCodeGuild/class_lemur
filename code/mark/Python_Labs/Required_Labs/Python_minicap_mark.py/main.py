import csv
import json
from card_display import Card_Display as card
import main_window as main
    
def import_subject_csv(path):
    """Opens the subject csv file with a saved list of questions and answers.  Returns the list except the last line which is blank"""
    with open(path, 'r', encoding='utf8') as file:
        lines = file.read().split('\n')
        for i in range(len(lines)):
            lines[i] = lines[i].split('","')
    return lines[:-1]

def create_subject(path):
    """Used to create a new subject. Used to name the new subject and import questions and answers via a csv file.  
    Returns a dictionary of questions and answers."""
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
            return subject_dict
        else:
            print("That is not a valid selection.")

def add_card():
    """NOT IMPLEMENTED YET"""
    """Add a new question and answer card to the subject"""
    question = input("What is the question for this card? ")
    answer = input("What is the answer for this card? ")
    return question, answer

def save_subject_dictionary(subject_dict):
    """Takes in a dictionary and saves it with the name of the subject as a json file.  Removes the name key from the saved json"""
    with open(f"{subject_dict['name']}.json", 'w') as file:
        subject_dict.pop('name')
        json.dump(subject_dict, file, indent=4)

def save_subject_list(subject_list, subject_path):
    """Takes in a list of subjects and a file path for the subject list save location.  Writes the list to a csv file"""
    with open(subject_path, 'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(subject_list)

def read_subject_list(subject_path):
    """Takes in a file path for a csv with a list of subjects and returns the list"""
    with open(subject_path, 'r') as file:
        lines = file.read().rstrip()
        lines = lines.split(',')
    return lines

def open_subject_dict(subject):
    """Takes in a subject name and attempts to open the subjects corresponding json file with questions and answers"""
    try:
        with open(f"{subject}.json") as file:
            subject_dict = json.load(file)
        return subject_dict
    except:
        print("Unable to locate file.  Please try again.")

def create_load_save_subject(path):
    """Takes in a file path for a csv with the questions and answers.  Creates the end result json file."""
    subject__dict = create_subject(path)
    save_subject_dictionary(subject__dict)

if __name__ == '__main__':
    path = 'python_subject.csv'
    subject_path = 'subject_list.csv'
    subject_dict = open_subject_dict('python')
    list_of_subjects = read_subject_list(subject_path)
    main.start_window(list_of_subjects, subject_dict)
    # create_load_save_subject(path)

 




