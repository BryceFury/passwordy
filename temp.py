import random
import string
import sys


from PyQt5 import QtGui, QtWidgets

class Passwordy(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Passwordy, self).__init__(parent)

        QtWidgets.QWidget.__init__(self)

        tabWidget = QtWidgets.QTabWidget()
        tabWidget.addTab(generate_tab(), 'General')
        tabWidget.addTab(manage_tab(), 'Permissions')
        tabWidget.addTab(settings_tab(), 'Settings')
        tabWidget.setStyleSheet('background: #FFFFFF')

        # Set main layout, add tab widget
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        self.setLayout(mainLayout)

        self.setWindowTitle('Passwordy')


class generate_tab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(generate_tab, self).__init__(parent)

        QtWidgets.QWidget.__init__(self)

        # Create Labels
        # Choices
        self.numbers_label = QtWidgets.QLabel('Numbers')
        self.lowercase_label_label = QtWidgets.QLabel('Lowercase letters')
        self.uppercase_label = QtWidgets.QLabel('Uppercase letters')
        self.special_characters_label = QtWidgets.QLabel('Special Characters')
        # Input
        self.number_of_characters_label = QtWidgets.QLabel('Number of Characters')
        self.number_of_passwords_label = QtWidgets.QLabel('Number of Passwords')
        # Output
        self.generated_passwords_label = QtWidgets.QLabel('Generated Passwords :')

        # Create checkboxes
        self.numbers_checkbox = QtWidgets.QCheckBox()
        self.lowercase_checkbox = QtWidgets.QCheckBox()
        self.uppercase_checkbox = QtWidgets.QCheckBox()
        self.special_characters_checkbox = QtWidgets.QCheckBox()

        # Create number boxes
        self.number_of_passwords = QtWidgets.QSpinBox()
        self.number_of_passwords.setMinimum(1)
        self.number_of_passwords.setMaximum(64)

        self.number_of_characters = QtWidgets.QSpinBox()
        self.number_of_characters.setMinimum(1)
        self.number_of_characters.setMaximum(64)

        # Create output box
        self.password_output = QtWidgets.QTextEdit()
        self.password_output.setReadOnly(True)
        self.password_output.setSizePolicy(QtWidgets.QSizePolicy.Preferred, 
                                           QtWidgets.QSizePolicy.Expanding)
        self.password_output.setStyleSheet('font: bold 12px;'
                                           'background: #FFFFFF; '
                                           'border: 1px solid #272727')

        # Create password generate button
        self.generate_password_button = QtWidgets.QPushButton('Generate Password')
        self.generate_password_button.setStyleSheet('font: 12px; background-color:#FFFFFF; border: 1px solid #272727')

        # Create layout, add widgets
        self.grid = QtWidgets.QGridLayout()
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
        self.setWindowIcon(QtGui.QIcon('../assets/padlock.png'))
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
            informer = QtWidgets.QMessageBox()
            #informer.setWindowTitle('Passwordy - Error')
            informer.setStandardButtons(QtWidgets.QMessageBox.Ok)
            informer.setDefaultButton(QtWidgets.QMessageBox.Ok)
                # Warning text
            informer.setText('Error: ' + '\n' + 'You must make a selection using one of the checkboxes, please try again...')
            informer.exec_()

        # Add each password in the password list to the output box
        for i in final_password_list:
            self.password_output.append(i)
  

class manage_tab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(manage_tab, self).__init__(parent)
        self.layout = QtWidgets.QFormLayout()
        self.box = QtWidgets.QHBoxLayout()
        self.box.addWidget(QtWidgets.QRadioButton('Manage'))
        self.box.addWidget(QtWidgets.QRadioButton('Passwords'))
        #self.layout.addRow(QtWidgets.QLabel('Test'),sex) 
        self.layout.addRow('Testy',QtWidgets.QLineEdit())
        #self.setTabText(1,'Test test')
        self.setStyleSheet('background: #FFFFFF;')
        self.setLayout(self.layout)


class settings_tab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(settings_tab, self).__init__(parent)
        self.layout = QtWidgets.QFormLayout()
        self.box = QtWidgets.QHBoxLayout()
        self.box.addWidget(QtWidgets.QRadioButton('Manage'))
        self.box.addWidget(QtWidgets.QRadioButton('Passwords'))
        #self.layout.addRow(QtWidgets.QLabel('Test'),sex)
        self.layout.addRow('Testy',QtWidgets.QLineEdit())
        #self.setTabText(1,'Test test')
        self.setStyleSheet('background: #FFFFFF;')
        self.setLayout(self.layout)

            
# The usual
def main():
    app = QtWidgets.QApplication(sys.argv)

    ex = Passwordy()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
