import random
import string
import sys


from PyQt5 import QtCore, QtGui, QtWidgets


# Create main canvas
class Passwordy(QtWidgets.QMainWindow):
 
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self,parent)
 
        # Default filename

        self.create_ui()

 
    def create_ui(self):
 
        self.setObjectName('self')
        self.resize(500, 61)
        self.setStyleSheet('#centralWidget {\n'
                           'background: #232532;\n'
                           'border: None;\n'
                           '}\n'
                           '\n'
                           '#menu_frame {\n'
                           'border: None;\n'
                           '}\n'
                           '\n'
                           '#menu_button {\n'
                           'text-align:center;\n'
                           'font: 18px;\n'
                           'color: #FFFFFF;\n'
                           'background-color: #232532;\n'
                           'border-style: solid;\n'
                           'border-width: 0px;\n'
                           'max-width:40px;\n'
                           'max-height:40px;\n'
                           'min-width:40px;\n'
                           'min-height:40px;\n'
                           '}\n'
                           '\n'
                           '#menu_frame QPushButton:hover {\n'
                           'color: #59F3D7;\n'
                           '}\n'
                           '\n'
                           '#generate_frame {\n'
                           'border: None;\n'
                           '}\n'
                           '\n'
                           '#generate_button {\n'
                           'text-align:center;\n'
                           'font: 18px;\n'
                           'color: #FFFFFF;\n'
                           'border-style: solid;\n'
                           'border-width: 0px;\n'
                           'border-radius: 25px;\n'
                           'max-width:100px;\n'
                           'max-height:50px;\n'
                           'min-width:100px;\n'
                           'min-height:50px;\n'
                           '}\n'
                           '\n'
                           '#generate_button:hover {\n'
                           'color: #59F3D7;\n'
                           '}\n'
                           '\n'
                           '#spacer_frame {\n'
                           'border: None;\n'
                           'max-width:250px;\n'
                           'max-height:50px;\n'
                           'min-width:225px;\n'
                           'min-height:50px;\n'
                           '}\n'
                           '\n'
                           'QLabel {\n'
                           'color: #FFFFFF;\n'
                           'font: 18px;\n'
                           'max-height:20px;\n'
                           'min-height:20px;\n'
                           '}\n'
                           '\n'
                           '\n'
                           '')

        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName('centralWidget')
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.menu_frame = QtWidgets.QFrame(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_frame.sizePolicy().hasHeightForWidth())
        self.menu_frame.setSizePolicy(sizePolicy)
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName('menu_frame')
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.menu_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.menu_button = QtWidgets.QPushButton(self.menu_frame)
        self.menu_button.setObjectName('menu_button')
        self.horizontalLayout.addWidget(self.menu_button)
        self.title_label = QtWidgets.QLabel(self.menu_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setObjectName('title_label')
        self.horizontalLayout.addWidget(self.title_label)
        self.horizontalLayout_2.addWidget(self.menu_frame)
        self.spacer_frame = QtWidgets.QFrame(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spacer_frame.sizePolicy().hasHeightForWidth())
        self.spacer_frame.setSizePolicy(sizePolicy)
        self.spacer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spacer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spacer_frame.setObjectName('spacer_frame')
        self.verticalLayout = QtWidgets.QVBoxLayout(self.spacer_frame)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName('verticalLayout')
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.spacer_frame)
        self.generate_frame = QtWidgets.QFrame(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_frame.sizePolicy().hasHeightForWidth())
        self.generate_frame.setSizePolicy(sizePolicy)
        self.generate_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.generate_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.generate_frame.setObjectName('generate_frame')
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.generate_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.generate_button = QtWidgets.QPushButton(self.generate_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_button.sizePolicy().hasHeightForWidth())
        self.generate_button.setSizePolicy(sizePolicy)
        self.generate_button.setObjectName('generate_button')
        self.verticalLayout_2.addWidget(self.generate_button)
        self.horizontalLayout_2.addWidget(self.generate_frame)
        self.setCentralWidget(self.centralWidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate('self', 'self'))
        self.menu_button.setText(_translate('self', '☰'))
        self.title_label.setText(_translate('self', 'passwordy'))
        self.generate_button.setText(_translate('self', 'generate'))


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

 
# Run App
def main():
 
    app = QtWidgets.QApplication(sys.argv)
 
    main = Passwordy()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    
    main()
