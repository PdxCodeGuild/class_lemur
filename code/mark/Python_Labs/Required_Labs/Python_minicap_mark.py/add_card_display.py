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
        self.path = f"{subject}.json"
        self.subject = subject

        self.card_font = self.font()
        self.card_font.setPointSize(12)
        self.label_font = self.font()
        self.label_font.setPointSize(20)
        self.label_font.setCapitalization(True)

        self.import_card_database()
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
        self.import_file_button.clicked.connect(self.add_new_card_to_dictionary)

        self.return_button = QPushButton("Return")
        self.return_button.clicked.connect(self.save_subject_dictionary)

        layout = QHBoxLayout()
        layout.addWidget(self.import_file_button)
        layout.addWidget(self.return_button)
        self.submit_and_return_button_box.setLayout(layout)

    def save_subject_dictionary(self):
        """Takes in a dictionary and saves it with the name of the subject as a json file.  Removes the name key from the saved json"""
        with open(self.path, 'w') as file:
            json.dump(self.subject_dict, file, indent=4)
        self.close()


    def import_card_database(self):
        """Using the name of the file path, it will import all the cards from a json file.  
        File must be set up in {question: answer} format"""
        with open(self.path, 'r') as file:
            self.subject_dict = json.load(file)

    def add_new_card_to_dictionary(self):
        """Adds the new card to the dictionary"""
        self.subject_dict[f"{self.new_question.toPlainText()}"] = f"{self.new_answer.toPlainText()}"
        self.new_question.clear()
        self.new_answer.clear()
        
