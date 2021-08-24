import csv
import json
from os import path
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
        QDialog, QFileDialog, QGridLayout, QGroupBox, QHBoxLayout, 
        QProgressBar, QPushButton, QTextEdit,
        QVBoxLayout
        )


class New_Subject_Display(QDialog):
    def __init__(self, parent=None):
        super(New_Subject_Display, self).__init__(parent)
        self.resize(1000,800)
        self.new_subject_title = ''
        self.path = None

        self.card_font = self.font()
        self.card_font.setPointSize(12)

        self.create_subject_box()
        self.create_import_file_and_return_button()
        self.create_create_new_subject_button()
        self.create_return_to_main_button()


        main_layout = QGridLayout()
        main_layout.addWidget(self.subject_box, 0, 0, 1, 1)
        main_layout.addWidget(self.new_subject_button_box, 2, 0, 1, 1)
        main_layout.addWidget(self.import_file_button_box, 1, 0, 1, 1)
        main_layout.addWidget(self.return_button_box, 3,0,1,1)

        main_layout.setRowStretch(1, 1)
        main_layout.setColumnStretch(0, 1)
        self.setLayout(main_layout)

    def create_subject_box(self):
        self.subject_box = QGroupBox("New Subject Title: ")
        self.subject_box.setFont(self.card_font)

        self.subject_title = QTextEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.subject_title)
        self.subject_box.setLayout(layout)    

    def create_import_file_and_return_button(self):
        self.import_file_button_box = QGroupBox("Select CSV file with questions and answers?")
        self.import_file_button_box.setFont(self.card_font)

        self.import_file_button = QPushButton("Select File")
        self.import_file_button.clicked.connect(self.select_file)

        layout = QHBoxLayout()
        layout.addWidget(self.import_file_button)
        self.import_file_button_box.setLayout(layout)

    def create_create_new_subject_button(self):
        self.new_subject_button_box = QGroupBox("Create New Subject: ")
        self.new_subject_button_box.setFont(self.card_font)

        self.new_subject_button = QPushButton("Create")
        self.new_subject_button.clicked.connect(self.create_new_subject_import_and_save)


        layout = QHBoxLayout()
        layout.addWidget(self.new_subject_button)
        self.new_subject_button_box.setLayout(layout)

    def create_return_to_main_button(self):
        self.return_button_box = QGroupBox()
        self.return_button_box.setFont(self.card_font)

        return_button = QPushButton("Return to Main")
        return_button.setDefault(True)
        return_button.clicked.connect(self.accept) 

        layout = QHBoxLayout()
        layout.addWidget(return_button)
        self.return_button_box.setLayout(layout)

    
    def select_file(self):
        self.path = QFileDialog.getOpenFileName(filter="*.csv")[0]
    
    def import_subject_csv(self):
        """Opens the subject csv file with a saved list of questions and answers.  Returns the list except the last line which is blank"""
        with open(self.path, 'r', encoding='utf8') as file:
            lines = file.read().split('\n')
            for i in range(len(lines)):
                lines[i] = lines[i].split('","')
        return lines

    def create_new_subject_import_and_save(self):
        """Used to create a new subject. Used to name the new subject and import questions and answers via a csv file.  
        Returns a dictionary of questions and answers."""
        subject_dict = {}
        subject_dict['name'] = self.subject_title.toPlainText()
        if self.path != None:
            list_of_questions_and_answers = self.import_subject_csv()
            for item in list_of_questions_and_answers:
                subject_dict[item[0]] = item[1]
        self.save_subject_dictionary(subject_dict)
        self.read_subject_list()

    def save_subject_dictionary(self, subject_dict):
        """Takes in a dictionary and saves it with the name of the subject as a json file.  Removes the name key from the saved json"""
        with open(f"{subject_dict['name']}.json", 'w') as file:
            subject_dict.pop('name')
            json.dump(subject_dict, file, indent=4)

    def save_subject_list(self, subject_list, subject_path):
        """Takes in a list of subjects and a file path for the subject list save location.  Writes the list to a csv file"""
        with open(subject_path, 'w') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(subject_list)

    def read_subject_list(self, subject_path='subject_list.csv'):
        """Takes in a file path for a csv with a list of subjects and returns the list"""
        with open(subject_path, 'r') as file:
            lines = file.read().rstrip()
            lines = lines.split(',')
            lines.append(self.subject_title.toPlainText())
        self.save_subject_list(lines, subject_path)

        


