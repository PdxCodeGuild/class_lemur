import csv
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QGridLayout, QGroupBox, QHBoxLayout, QListWidget, QPushButton, QTextEdit, QVBoxLayout
from card_display import Card_Display
from add_subject_display import New_Subject_Display
from add_card_display import New_Card_Display
import sys
import json


class Main_Window(QDialog):
    def __init__(self, subject='python', parent=None):
        super(Main_Window, self).__init__(parent)
        self.resize(1000,800)
        self.row = 0
        self.subject = subject
        self.list_of_subjects = None
        self.subject_path='subject_list.csv'

        self.main_font = self.font()
        self.main_font.setPointSize(14)


        self.create_list_widget()
        self.create_study_button()
        self.create_subject_and_card_add_buttons()
        self.read_subject_list()

        main_layout = QGridLayout()
        main_layout.addWidget(self.list_box, 0, 0, 2, 2)
        main_layout.addWidget(self.study_button_box, 2, 0, 2, 1)
        main_layout.addWidget(self.quit_button_box, 2, 1, 2, 1)
        main_layout.setRowStretch(1, 1)
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 1)
        self.setLayout(main_layout)

    def create_list_widget(self):
        self.list_box = QGroupBox("Available Subjects")
        self.list_box.setFont(self.main_font)

        self.subjects_list = QListWidget()
        self.subjects_list.clicked.connect(self.selectionChanged)
        layout = QVBoxLayout()
        layout.addWidget(self.subjects_list)
        self.list_box.setLayout(layout)

    def create_study_button(self):
        self.study_button_box = QGroupBox()
        self.study_button_box.setFont(self.main_font)

        study_button = QPushButton("Study")
        study_button.clicked.connect(self.open_card_display)

        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(QApplication.quit)

        layout = QVBoxLayout()
        layout.addWidget(study_button)
        layout.addWidget(quit_button)
        self.study_button_box.setLayout(layout)

    def create_subject_and_card_add_buttons(self):
        self.quit_button_box = QGroupBox()
        self.quit_button_box.setFont(self.main_font)

        add_subject_button = QPushButton("Add Subject")
        add_subject_button.clicked.connect(self.new_subject)

        refresh_subject_list_button = QPushButton("Refresh List")
        refresh_subject_list_button.clicked.connect(self.read_subject_list)

        add_card_button = QPushButton("Add Card")
        add_card_button.clicked.connect(self.add_card)

        layout = QVBoxLayout()
        layout.addWidget(add_subject_button)
        layout.addWidget(refresh_subject_list_button)
        layout.addWidget(add_card_button)
        self.quit_button_box.setLayout(layout)

    def add_item_to_list(self):
        """Adds item to subject list in list window."""
        self.subjects_list.clear()
        for item in self.list_of_subjects:
            self.subjects_list.addItem(item)

    def selectionChanged(self):
        """For the subject selection list.  Sets the current row number of the subject selected in the list window."""
        row = self.subjects_list.currentRow()
        self.subject = self.list_of_subjects[row]
        
    def open_card_display(self):
        """Opens a new window for going the questions and answers."""
        self.w = Card_Display(self.subject)
        self.w.show()

    def close_application(self):
        QtWidgets.QApplication.quit()

    def add_card(self):
        """NOT IMPLEMENTED YET"""
        """Add a new question and answer card to the subject"""
        self.add_card_display = New_Card_Display(self.subject)
        self.add_card_display.show()

    def save_subject_list(self, subject_list):
        """Takes in a list of subjects and a file path for the subject list save location.  Writes the list to a csv file"""
        with open(self.subject_path, 'w') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(subject_list)

    def read_subject_list(self):
        """Takes in a file path for a csv with a list of subjects and returns the list"""
        self.subjects_list.clear()
        with open(self.subject_path, 'r') as file:
            lines = file.read().rstrip()
            self.list_of_subjects = lines.split(',')
        self.add_item_to_list()


    def open_subject_dict(self, subject):
        """Takes in a subject name and attempts to open the subjects corresponding json file with questions and answers"""
        try:
            with open(f"{subject}.json") as file:
                subject_dict = json.load(file)
            return subject_dict
        except:
            print("Unable to locate file.  Please try again.")

    def new_subject(self):
        """Takes in a file path for a csv with the questions and answers.  Creates the end result json file."""
        self.new_subject_display = New_Subject_Display()
        self.new_subject_display.show()

# def start_window(list_of_subjects):
def start_window():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    """ -------------MOST IMPORTANT FEATURE - Creates Dark Mode--------------"""
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    """-------------------Dark Mode created.  The world is safe--------------"""

    main_window = Main_Window()
    # for subject in list_of_subjects:
    #     main_window.add_item_to_list(subject)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    path = 'python_subject.csv'
    subject_path = 'subject_list.csv'
    start_window()
    # create_load_save_subject(path)