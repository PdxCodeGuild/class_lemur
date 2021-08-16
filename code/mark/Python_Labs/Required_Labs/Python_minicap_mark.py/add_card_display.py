import csv
import json
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
        QDialog, QFileDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, 
        QProgressBar, QPushButton, QTextEdit,
        QVBoxLayout
        )


class New_Card_Display(QDialog):
    def __init__(self, subject, parent=None):
        super(New_Card_Display, self).__init__(parent)
        self.resize(1000,800)
        self.path = None
        self.subject = subject

        self.card_font = self.font()
        self.card_font.setPointSize(12)
        self.label_font = self.font()
        self.label_font.setPointSize(20)
        self.label_font.setCapitalization(True)

        self.create_label_for_subject()
        self.create_card_question_box()
        self.create_card_answer_box()
        self.create_submit_and_return_button_box()

        main_layout = QGridLayout()
        main_layout.addWidget(self.subject_label, 0,0,1,1)
        main_layout.addWidget(self.new_question_box, 1, 0, 1, 1)
        main_layout.addWidget(self.new_answer_box, 2, 0, 1, 1)
        main_layout.addWidget(self.submit_and_return_button_box, 3, 0, 1, 1)


        main_layout.setRowStretch(1, 1)
        main_layout.setColumnStretch(0, 1)
        self.setLayout(main_layout)

    def create_label_for_subject(self):
        self.subject_label = QLabel(f"{self.subject}")
        self.subject_label.setFont(self.label_font)
        self.subject_label.setAlignment(QtCore.Qt.AlignCenter)

    def create_card_question_box(self):
        self.new_question_box = QGroupBox("New Question: ")
        self.new_question_box.setFont(self.card_font)

        self.new_question = QTextEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.new_question)
        self.new_question_box.setLayout(layout)    
    
    def create_card_answer_box(self):
        self.new_answer_box = QGroupBox("New Answer: ")
        self.new_answer_box.setFont(self.card_font)

        self.new_answer = QTextEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.new_answer)
        self.new_answer_box.setLayout(layout) 

    def create_submit_and_return_button_box(self):
        self.submit_and_return_button_box = QGroupBox()
        self.submit_and_return_button_box.setFont(self.card_font)

        self.import_file_button = QPushButton("Submit")
        self.import_file_button.clicked.connect(self.select_file)

        self.return_button = QPushButton("Return")
        self.return_button.clicked.connect(self.close)

        layout = QHBoxLayout()
        layout.addWidget(self.import_file_button)
        layout.addWidget(self.return_button)
        self.submit_and_return_button_box.setLayout(layout)
    
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
        subject_dict['name'] = self.new_question.toPlainText()
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
            lines.append(self.new_question.toPlainText())
        self.save_subject_list(lines, subject_path)

        


