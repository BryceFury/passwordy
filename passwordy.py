import random
import string
import sys


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QIcon, QPalette, QPixmap
from PyQt5.QtWidgets import QApplication, QCheckBox, QComboBox
from PyQt5.QtWidgets import QDesktopWidget, QFormLayout, QGridLayout
from PyQt5.QtWidgets import QHBoxLayout, QInputDialog, QLabel, QLineEdit
from PyQt5.QtWidgets import QMessageBox, QTabWidget, QPushButton
from PyQt5.QtWidgets import QRadioButton, QSizePolicy, QSpinBox
from PyQt5.QtWidgets import QTextEdit, QVBoxLayout, QWidget


class Passwordy(QWidget):
    def __init__(self, parent=None):
        super(Passwordy, self).__init__(parent)

        QWidget.__init__(self)

        tabWidget = QTabWidget()
        tabWidget.addTab(generate_tab(), 'General')
        tabWidget.addTab(manage_tab(), 'Permissions')
        tabWidget.addTab(settings_tab(), 'Settings')
        tabWidget.setStyleSheet('background: #FFFFFF')

        # Set main layout, add tab widget
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        self.setLayout(mainLayout)

        self.setWindowTitle('Passwordy')


class generate_tab(QWidget):
    def __init__(self, parent=None):
        super(generate_tab, self).__init__(parent)

        QWidget.__init__(self)

        # Create Labels
        # Choices
        self.numbers_label = QLabel('Numbers')
        self.lowercase_label_label = QLabel('Lowercase letters')
        self.uppercase_label = QLabel('Uppercase letters')
        self.special_characters_label = QLabel('Special Characters')
        # Input
        self.number_of_characters_label = QLabel('Number of Characters')
        self.number_of_passwords_label = QLabel('Number of Passwords')
        # Output
        self.generated_passwords_label = QLabel('Generated Passwords :')

        # Create checkboxes
        self.numbers_checkbox = QCheckBox()
        self.lowercase_checkbox = QCheckBox()
        self.uppercase_checkbox = QCheckBox()
        self.special_characters_checkbox = QCheckBox()

        # Create number boxes
        self.number_of_passwords = QSpinBox()
        self.number_of_passwords.setMinimum(1)
        self.number_of_passwords.setMaximum(64)

        self.number_of_characters = QSpinBox()
        self.number_of_characters.setMinimum(1)
        self.number_of_characters.setMaximum(64)

        # Create output box
        self.password_output = QTextEdit()
        self.password_output.setReadOnly(True)
        self.password_output.setSizePolicy(QSizePolicy.Preferred, 
                                           QSizePolicy.Expanding)
        self.password_output.setStyleSheet('font: bold 12px;'
                                           'background: #FFFFFF; '
                                           'border: 1px solid #272727')

        # Create password generate button
        self.generate_password_button = QPushButton('Generate Password')
        self.generate_password_button.setStyleSheet('font: 12px; background-color:#FFFFFF; border: 1px solid #272727')

        # Create layout, add widgets
        self.grid = QGridLayout()
            # Add widget to row, label to same row, next column
        self.grid.addWidget(self.numbers_checkbox, 0, 0)
        self.grid.addWidget(self.numbers_label, 0, 1)
        self.grid.addWidget(self.lowercase_checkbox, 1, 0)
        self.grid.addWidget(self.lowercase_label_label, 1, 1)
        self.grid.addWidget(self.uppercase_checkbox, 2, 0)
        self.grid.addWidget(self.uppercase_label, 2, 1)
        self.grid.addWidget(self.special_characters_checkbox, 3, 0)
        self.grid.addWidget(self.special_characters_label, 3, 1)
        self.grid.addWidget(self.number_of_characters, 4, 0)
        self.grid.addWidget(self.number_of_characters_label, 4, 1)
        self.grid.addWidget(self.number_of_passwords, 5, 0)
        self.grid.addWidget(self.number_of_passwords_label, 5, 1)
        # Add these to next column
        self.grid.addWidget(self.generated_passwords_label, 0, 2)
        self.grid.addWidget(self.password_output, 1, 2, 4, 1)
        self.grid.addWidget(self.generate_password_button, 5, 2)

        # Set layout
        self.setLayout(self.grid)

        # Connect password generate button to password generate functions
        self.generate_password_button.clicked.connect(self.generate_passwords)

        # Set window
        self.setFixedSize(500, 250)
        self.setWindowTitle('Passwordy')
        self.setWindowIcon(QIcon('../assets/padlock.png'))
        self.setStyleSheet('background: #FFFFFF;')

    def generate_passwords(self):
        # Clear the output box
        self.password_output.setText('')

        # Set strings to get characters from
        # Numbers
        numbers = string.digits
        # Letters
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        # Special Characters
        special_characters = '!@#$%^&*()\{\}[]?,.'

        # Init output character string
        output_characters = ''

        # Init empty password list
        final_password_list = []

        # Check user has used a checkbox, add characters from strings relative to checkboxes, generate password
        if True in [self.numbers_checkbox.isChecked(), 
                    self.lowercase_checkbox.isChecked(), 
                    self.uppercase_checkbox.isChecked(),
                    self.special_characters_checkbox.isChecked()]:

            output_characters = (numbers * self.numbers_checkbox.isChecked() 
                                  + lowercase * self.lowercase_checkbox.isChecked() 
                                  + uppercase * self.uppercase_checkbox.isChecked() 
                                  + special_characters * self.special_characters_checkbox.isChecked())
            # Check how many passwords the user requires, generate for that amount
            for i in range(0, self.number_of_passwords.value()):

                password = ''.join(random.choice(output_characters) for i in range(self.number_of_characters.value()))

                final_password_list.append(password)

        # If user hasn't selected a checkbox, inform them in a popup
        else:
            informer = QMessageBox()
            #informer.setWindowTitle('Passwordy - Error')
            informer.setStandardButtons(QMessageBox.Ok)
            informer.setDefaultButton(QMessageBox.Ok)
                # Warning text
            informer.setText('Error: ' + '\n' + 'You must make a selection using one of the checkboxes, please try again...')
            informer.exec_()

        # Add each password in the password list to the output box
        for i in final_password_list:
            self.password_output.append(i)
  

class manage_tab(QWidget):
    def __init__(self, parent=None):
        super(manage_tab, self).__init__(parent)
        self.layout = QFormLayout()
        self.box = QHBoxLayout()
        self.box.addWidget(QRadioButton('Manage'))
        self.box.addWidget(QRadioButton('Passwords'))
        #self.layout.addRow(QLabel('Test'),sex) 
        self.layout.addRow('Testy',QLineEdit())
        #self.setTabText(1,'Test test')
        self.setStyleSheet('background: #FFFFFF;')
        self.setLayout(self.layout)


class settings_tab(QWidget):
    def __init__(self, parent=None):
        super(settings_tab, self).__init__(parent)
        self.layout = QFormLayout()
        self.box = QHBoxLayout()
        self.box.addWidget(QRadioButton('Manage'))
        self.box.addWidget(QRadioButton('Passwords'))
        #self.layout.addRow(QLabel('Test'),sex)
        self.layout.addRow('Testy',QLineEdit())
        #self.setTabText(1,'Test test')
        self.setStyleSheet('background: #FFFFFF;')
        self.setLayout(self.layout)

            
# The usual
def main():
    app = QApplication(sys.argv)

    ex = Passwordy()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
