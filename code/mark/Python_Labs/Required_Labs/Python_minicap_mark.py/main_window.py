from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
import sys
from PyQt5.QtWidgets import QApplication, QBoxLayout, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QListWidget, QMainWindow, QPushButton, QVBoxLayout
from card_display import Card_Display


class Main_Window(QDialog):
    def __init__(self, subject='python', parent=None):
        super(Main_Window, self).__init__(parent)
        self.resize(800,600)
        self.row = 0
        self.subject = subject

        self.main_font = self.font()
        self.main_font.setPointSize(20)

        self.create_list_widget()
        self.create_study_button()
        self.create_quit_button()
        self.create_add_card_button()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.list_box, 0, 0, 1, 2)
        mainLayout.addWidget(self.study_button_box, 1, 0, 1, 1)
        mainLayout.addWidget(self.quit_button_box, 1, 1, 1, 1)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

    def create_list_widget(self):
        self.list_box = QGroupBox("Available Subjects")
        self.list_box.setFont(self.main_font)
        self.available_subjects = QListWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.available_subjects)
        self.list_box.setLayout(layout)

    def create_study_button(self):
        self.study_button_box = QGroupBox()
        self.study_button_box.setFont(self.main_font)

        study_button = QPushButton("Study")
        study_button.clicked.connect(self.open_card_display)

        layout = QHBoxLayout()
        layout.addWidget(study_button)
        self.study_button_box.setLayout(layout)

    def create_quit_button(self):
        self.quit_button_box = QGroupBox()
        self.quit_button_box.setFont(self.main_font)

        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(QApplication.quit)

        layout = QHBoxLayout()
        layout.addWidget(quit_button)
        self.quit_button_box.setLayout(layout)

    def create_add_card_button(self):
        self.add_card_button_box = QGroupBox()
        self.add_card_button_box.setFont(self.main_font)

        add_card_button = QPushButton("Add Card")
        add_card_button.clicked.connect()

        layout = QHBoxLayout()
        layout.addWidget(add_card_button)
        self.add_card_button_box.setLayout(layout)
    
    def create_add_subject_button(self):
        self.add_subject_button_box = QGroupBox()
        self.add_subject_button_box.setFont(self.main_font)

        add_subject_button = QPushButton("Add Subject")
        add_subject_button.clicked.connect()

        layout = QHBoxLayout()
        layout.addWidget(add_subject_button)
        self.add_card_button_box.setLayout(layout)

    def add_item_to_list(self, item):
        """Adds item to subject list in list window."""
        self.available_subjects.addItem(item)

    def selectionChanged(self):
        """For the subject selection list.  Sets the current row number of the subject selected in the list window."""
        self.row = self.available_subjects.currentRow()
        
    def open_card_display(self):
        """Opens a new window for going the questions and answers."""
        self.w = Card_Display(self.subject)
        self.w.show()

    def close_application(self):
        QtWidgets.QApplication.quit()

    def add_subject(self):
        ...
    
    def add_card(self):
        ...


def start_window(list_of_subjects, subject_dict):
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

    main_window = Main_Window(subject_dict)
    for subject in list_of_subjects:
        main_window.add_item_to_list(subject)
    main_window.show()
    sys.exit(app.exec_())

