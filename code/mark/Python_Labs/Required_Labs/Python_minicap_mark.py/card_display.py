import json
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, 
        QProgressBar, QPushButton, QTextEdit,
        QVBoxLayout
        )


class Card_Display(QDialog):
    def __init__(self, subject, parent=None):
        super(Card_Display, self).__init__(parent)
        self.resize(1000,800)
        self.subject_dict = {}
        self.subject = subject
        self.question_num = -1
        self.import_card_database(f"{subject}.json")
        self.restudy_dict = {}

        self.card_font = self.font()
        self.card_font.setPointSize(12)

        self.create_question_box()
        self.create_answer_box()
        self.create_next_and_show_answer_buttons()
        self.create_correct_incorrect_buttons()
        self.create_progress_bar()


        main_layout = QGridLayout()
        main_layout.addWidget(self.question_box, 0, 0, 1, 2)
        main_layout.addWidget(self.answer_box, 1, 0, 1, 2)
        main_layout.addWidget(self.correct_incorrect_buttons, 2, 0, 1, 2)
        main_layout.addWidget(self.next_and_show_answer_buttons, 3, 0, 1, 2)
        main_layout.addWidget(self.progress_bar, 4, 0, 1, 2)
        main_layout.setRowStretch(1, 1)
        main_layout.setRowStretch(2, 1)
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 1)
        self.setLayout(main_layout)



    def create_question_box(self):
        self.question_box = QGroupBox("Question: ")
        self.question_box.setFont(self.card_font)

        self.question_text = QTextEdit()
        self.question_text.setReadOnly(True)
        self.question_text.textCursor().insertHtml("<b>Click Next Question to Start</b>")

        layout = QVBoxLayout()
        layout.addWidget(self.question_text)
        self.question_box.setLayout(layout)    

    def create_answer_box(self):
        self.answer_box = QGroupBox("Answer: ")
        self.answer_box.setFont(self.card_font)

        self.answer_text = QTextEdit()
        self.answer_text.setReadOnly(True)
        self.answer_text.textCursor().insertHtml("Try to answer the question, then hit show answer button to check.")

        layout = QVBoxLayout()
        layout.addWidget(self.answer_text)
        self.answer_box.setLayout(layout)

    def create_next_and_show_answer_buttons(self):
        self.next_and_show_answer_buttons = QGroupBox()
        self.next_and_show_answer_buttons.setFont(self.card_font)

        self.next_question_button = QPushButton("Next Question")
        self.next_question_button.clicked.connect(self.show_next_question)

        self.show_answer_button = QPushButton("Show Answer")
        self.show_answer_button.setDisabled(True)
        self.show_answer_button.clicked.connect(self.show_answer)

        return_button = QPushButton("Return to Main")
        return_button.setDefault(True)
        return_button.clicked.connect(self.close)

        layout = QHBoxLayout()
        layout.addWidget(self.next_question_button)
        layout.addWidget(self.show_answer_button)
        layout.addWidget(return_button)
        self.next_and_show_answer_buttons.setLayout(layout)

    def create_correct_incorrect_buttons(self):
        self.correct_incorrect_buttons = QGroupBox()
        self.correct_incorrect_buttons.setFont(self.card_font)

        self.correct_button = QPushButton("Correct")
        self.correct_button.setDisabled(True)
        self.correct_button.clicked.connect(self.correct_selected)

        self.incorrect_button = QPushButton("Incorrect")
        self.incorrect_button.setDisabled(True)
        self.incorrect_button.clicked.connect(self.incorrect_selected)

        layout = QHBoxLayout()
        layout.addWidget(self.correct_button)
        layout.addWidget(self.incorrect_button)
        self.correct_incorrect_buttons.setLayout(layout)

    def create_progress_bar(self):
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, len(self.subject_dict))
        self.progress_bar.setValue(0)

    def increase_progress_bar(self):
        """Sets the current and max progress bar points and increases it when called."""
        current_value = self.question_num + 1
        max_value = self.progress_bar.maximum()
        self.progress_bar.setValue(current_value + (max_value - current_value) // 100)

    def show_next_question(self):
        """Shows the next question and clears the answer text box.  If last question and it is called again, it will
        move all the missed questions into the subject dictionary to be run through again. Disables next question 
        button until current answer has been shown and marked correct or incorrect."""
        self.next_question_button.setDisabled(True)
        self.keys = list(self.subject_dict.keys())
        if self.question_num < len(self.keys)-1:
            self.question_num += 1
            self.question_text.clear()
            self.answer_text.clear()
            self.question_text.insertHtml(self.keys[self.question_num].strip("\""))

        else:
            self.question_text.clear()
            self.answer_text.clear()
            self.question_text.insertHtml(f"<b>That was the last question. You missed {len(self.restudy_dict)} questions.\n\nSelect Next Question to restudy the ones you got wrong.</b>")
            if len(self.restudy_dict) > 0:
                self.subject_dict = self.restudy_dict.copy()
                self.restudy_dict.clear()
                self.progress_bar.setRange(0, len(self.subject_dict))
            else:
                self.import_card_database()
                self.progress_bar.setRange(0, len(self.subject_dict))
            self.question_num = -1
            self.increase_progress_bar()

            self.next_question_button.setDisabled(False)
        self.show_answer_button.setDisabled(False)

    def show_answer(self):
        """Shows the answer in the answer text box"""
        self.answer_text.clear()
        keys = list(self.subject_dict.keys())
        self.answer_text.insertHtml(self.subject_dict[keys[self.question_num]].strip("\""))
        self.correct_button.setDisabled(False)
        self.incorrect_button.setDisabled(False)

    def import_card_database(self, path='python.json'):
        """Using the name of the file path, it will import all the cards from a json file.  
        File must be set up in {question: answer} format"""
        with open(path, 'r') as file:
            self.subject_dict = json.load(file)

    def correct_selected(self):
        """Enables the next question button after the current question has been marked correct.  Also increases progress bar"""
        self.next_question_button.setDisabled(False)
        self.increase_progress_bar()

    def incorrect_selected(self):
        """Enables the next question button after the current question has been marked incorrect. 
        Adds the missed question to the restudy list.  Also increases progress bar."""
        self.next_question_button.setDisabled(False)
        self.restudy_dict[self.keys[self.question_num]] = self.subject_dict[self.keys[self.question_num]]
        self.increase_progress_bar()

