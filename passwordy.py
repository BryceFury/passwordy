# coding=UTF-8

import random
import string
import sys

from stylesheet import set_stylesheet


from PyQt5 import QtCore, QtGui, QtWidgets


# Create main canvas
class Passwordy(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        # Call function to create UI
        self.create_main_ui()

    def create_main_ui(self):

        # Set window stylesheet
        get_stylesheet = set_stylesheet()
        self.setStyleSheet(get_stylesheet)

        # Main window setting
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName('centralWidget')

        # Set main widget layout (centralWidget)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_10.setSizeConstraint(QtWidgets
                                                 .QLayout
                                                 .SetDefaultConstraint)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName('verticalLayout_10')

        # Create top frame
        self.top_frame = QtWidgets.QFrame(self.centralWidget)
        self.top_frame.setObjectName('top_frame')
        self.horizontallayout_10 = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontallayout_10.setSizeConstraint(QtWidgets
                                                   .QLayout
                                                   .SetDefaultConstraint)
        self.horizontallayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_10.setSpacing(-1)
        self.horizontallayout_10.setObjectName('horizontallayout_10')

        # Add top frame to layout
        self.verticalLayout_10.addWidget(self.top_frame)

        # Create frame for menu button and title
        self.menu_frame = QtWidgets.QFrame(self.top_frame)

        # Set frame size
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_frame
                                     .sizePolicy()
                                     .hasHeightForWidth())
        self.menu_frame.setSizePolicy(sizePolicy)
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName('menu_frame')

        # Set menu frames layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.menu_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(-1)
        self.horizontalLayout.setObjectName('horizontalLayout')

        # Create title label
        self.title_label = QtWidgets.QLabel(self.menu_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label
                                     .sizePolicy()
                                     .hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setObjectName('title_label')
        self.title_label.setText('passwordy')

        # Add title label to layout
        self.horizontalLayout.addWidget(self.title_label)

        # Create menubutton
        self.menu_button = QtWidgets.QPushButton(self.menu_frame)
        self.menu_button.setObjectName('menu_button')
        self.menu_button.setText('☰')

        # Add menubutton widget to layout
        self.horizontalLayout.addWidget(self.menu_button)

        # Connect menu button to open_menu function
        self.menu_button.clicked.connect(self.open_menu)

        # Add menu frame to layout
        self.horizontallayout_10.addWidget(self.menu_frame)

        # Create frame for generate button
        self.generate_frame = QtWidgets.QFrame(self.top_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_frame
                                     .sizePolicy()
                                     .hasHeightForWidth())
        self.generate_frame.setSizePolicy(sizePolicy)
        self.generate_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.generate_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.generate_frame.setObjectName('generate_frame')

        # Create layout for generate button frame
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.generate_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName('verticalLayout_3')

        # Create generate button
        self.generate_button = QtWidgets.QPushButton(self.generate_frame)
        self.generate_button.setText('generate')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_button
                                     .sizePolicy()
                                     .hasHeightForWidth())
        self.generate_button.setSizePolicy(sizePolicy)
        self.generate_button.setObjectName('generate_button')

        # Add generate button to layout
        self.verticalLayout_3.addWidget(self.generate_button)

        # Add generate frame to layout
        self.horizontallayout_10.addWidget(self.generate_frame)

        # Connect generate button to generate_pass function
        self.generate_button.clicked.connect(self.open_password_ouput)

        # Create frame for exit button
        self.exit_frame = QtWidgets.QFrame(self.top_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_frame
                                     .sizePolicy()
                                     .hasHeightForWidth())
        self.exit_frame.setSizePolicy(sizePolicy)
        self.exit_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exit_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exit_frame.setObjectName('exit_frame')

        # Create layout for exit button frame
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.exit_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName('verticalLayout_3')

        # Create exit button
        self.exit_button = QtWidgets.QPushButton(self.exit_frame)
        self.exit_button.setText('exit')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_button
                                     .sizePolicy()
                                     .hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy)
        self.exit_button.setObjectName('exit_button')

        # Add exit button to layout
        self.verticalLayout_3.addWidget(self.exit_button)

        # Add exit frame to layout
        self.horizontallayout_10.addWidget(self.exit_frame)

        # Connect exit button to close function
        self.exit_button.clicked.connect(self.close)

        # Set central widget
        self.setCentralWidget(self.centralWidget)

        # Hide OS' default window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Call menu ui to set options and immediately hide
        self.menu_ui()
        self.options_frame.hide()

        # Reset menu button icon
        self.menu_button.setText('☰')

        # Set password output open flag
        self.password_output_open = False

        # Set menu open flag
        self.menu_open = False

        # Reset window size
        if not self.password_output_open:
            self.resize(500, 50)
        else:
            self.setFixedSize(500, 200)

    def menu_ui(self):

        # Set open flag
        self.menu_open = True

        # Change menu button to 'open'
        self.menu_button.setText('☷')

        # Create options frame
        self.options_frame = QtWidgets.QFrame(self.centralWidget)
        self.options_frame.setObjectName('options_frame')
        self.horizontallayout_4 = QtWidgets.QHBoxLayout(self.options_frame)
        self.horizontallayout_4.setSizeConstraint(QtWidgets
                                                  .QLayout
                                                  .SetDefaultConstraint)
        self.horizontallayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_4.setSpacing(0)
        self.horizontallayout_4.setObjectName('horizontallayout_4')

        # Add options frame to layout
        self.verticalLayout_10.addWidget(self.options_frame)

        # Add checkboxes frame
        self.checks_frame = QtWidgets.QFrame(self.options_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checks_frame
                                     .sizePolicy()
                                     .hasHeightForWidth())
        self.checks_frame.setSizePolicy(sizePolicy)
        self.checks_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.checks_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.checks_frame.setObjectName('checks_frame')
        self.horizontallayout_3 = QtWidgets.QHBoxLayout(self.checks_frame)
        self.horizontallayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_3.setSpacing(0)
        self.horizontallayout_3.setObjectName('horizontallayout_3')
        self.chars_frame = QtWidgets.QFrame(self.checks_frame)
        self.chars_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chars_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chars_frame.setObjectName('chars_frame')
        self.verticallayout_6 = QtWidgets.QVBoxLayout(self.chars_frame)
        self.verticallayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticallayout_6.setSpacing(6)
        self.verticallayout_6.setObjectName('verticallayout_6')
        self.nums_checkbox = QtWidgets.QCheckBox(self.chars_frame)
        self.nums_checkbox.setChecked(True)
        self.nums_checkbox.setObjectName('nums_checkbox')
        self.verticallayout_6.addWidget(self.nums_checkbox)
        self.s_chars_checkbox = QtWidgets.QCheckBox(self.chars_frame)
        self.s_chars_checkbox.setChecked(True)
        self.s_chars_checkbox.setObjectName('s_chars_checkbox')
        self.verticallayout_6.addWidget(self.s_chars_checkbox)
        self.horizontallayout_3.addWidget(self.chars_frame)
        self.case_frame = QtWidgets.QFrame(self.checks_frame)
        self.case_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.case_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.case_frame.setObjectName('case_frame')
        self.verticallayout_7 = QtWidgets.QVBoxLayout(self.case_frame)
        self.verticallayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticallayout_7.setSpacing(6)
        self.verticallayout_7.setObjectName('verticallayout_7')
        self.lower_checkbox = QtWidgets.QCheckBox(self.case_frame)
        self.lower_checkbox.setChecked(True)
        self.lower_checkbox.setObjectName('lower_checkbox')
        self.verticallayout_7.addWidget(self.lower_checkbox)
        self.upper_checkbox = QtWidgets.QCheckBox(self.case_frame)
        self.upper_checkbox.setChecked(True)
        self.upper_checkbox.setObjectName('upper_checkbox')
        self.verticallayout_7.addWidget(self.upper_checkbox)
        self.horizontallayout_3.addWidget(self.case_frame)
        self.horizontallayout_4.addWidget(self.checks_frame)
        self.spins_frame = QtWidgets.QFrame(self.options_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spins_frame
                                     .sizePolicy()
                                     .hasHeightForWidth())

        self.nums_checkbox.setText('nums')
        self.s_chars_checkbox.setText('Specials')
        self.lower_checkbox.setText('lower')
        self.upper_checkbox.setText('upper')

        self.spins_frame.setSizePolicy(sizePolicy)
        self.spins_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spins_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spins_frame.setObjectName('spins_frame')
        self.verticallayout_3 = QtWidgets.QVBoxLayout(self.spins_frame)
        self.verticallayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticallayout_3.setSpacing(0)
        self.verticallayout_3.setObjectName('verticallayout_3')
        self.labels_frame = QtWidgets.QFrame(self.spins_frame)
        self.labels_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labels_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labels_frame.setObjectName('labels_frame')
        self.horizontallayout_6 = QtWidgets.QHBoxLayout(self.labels_frame)
        self.horizontallayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_6.setSpacing(0)
        self.horizontallayout_6.setObjectName('horizontallayout_6')
        self.chars_label_frame = QtWidgets.QFrame(self.labels_frame)
        self.chars_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chars_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chars_label_frame.setObjectName('chars_label_frame')
        self.verticallayout_5 = QtWidgets.QVBoxLayout(self.chars_label_frame)
        self.verticallayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticallayout_5.setSpacing(0)
        self.verticallayout_5.setObjectName('verticallayout_5')
        self.chars_label = QtWidgets.QLabel(self.chars_label_frame)
        self.chars_label.setObjectName('chars_label')
        self.verticallayout_5.addWidget(self.chars_label)
        self.horizontallayout_6.addWidget(self.chars_label_frame)
        self.pass_label_frame = QtWidgets.QFrame(self.labels_frame)
        self.pass_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pass_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pass_label_frame.setObjectName('pass_label_frame')
        self.horizontallayout_7 = QtWidgets.QHBoxLayout(self.pass_label_frame)
        self.horizontallayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_7.setSpacing(0)
        self.horizontallayout_7.setObjectName('horizontallayout_7')
        self.pass_label = QtWidgets.QLabel(self.pass_label_frame)
        self.pass_label.setObjectName('pass_label')
        self.horizontallayout_7.addWidget(self.pass_label)
        self.horizontallayout_6.addWidget(self.pass_label_frame)
        self.verticallayout_3.addWidget(self.labels_frame)
        self.spin_boxes_frame = QtWidgets.QFrame(self.spins_frame)
        self.spin_boxes_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spin_boxes_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spin_boxes_frame.setObjectName('spin_boxes_frame')
        self.horizontallayout_5 = QtWidgets.QHBoxLayout(self.spin_boxes_frame)
        self.horizontallayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_5.setSpacing(0)
        self.horizontallayout_5.setObjectName('horizontallayout_5')
        self.number_of_chars = QtWidgets.QSpinBox(self.spin_boxes_frame)
        self.number_of_chars.setMinimum(1)
        self.number_of_chars.setMaximum(64)
        self.number_of_chars.setObjectName('number_of_chars')
        self.horizontallayout_5.addWidget(self.number_of_chars)
        self.number_of_pass = QtWidgets.QSpinBox(self.spin_boxes_frame)
        self.number_of_pass.setMinimum(1)
        self.number_of_pass.setObjectName('number_of_pass')
        self.horizontallayout_5.addWidget(self.number_of_pass)
        self.verticallayout_3.addWidget(self.spin_boxes_frame)
        self.horizontallayout_4.addWidget(self.spins_frame)

        self.chars_label.setText('Number of chars')
        self.pass_label.setText('Number of pass')

        self.close_button_frame = QtWidgets.QFrame(self.options_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_button_frame
                                     .sizePolicy()
                                     .hasHeightForWidth())

        self.close_button_frame.setSizePolicy(sizePolicy)
        self.close_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.close_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.close_button_frame.setObjectName('close_button_frame')
        self.verticallayout_4 = QtWidgets.QVBoxLayout(self.close_button_frame)
        self.verticallayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticallayout_4.setSpacing(0)
        self.verticallayout_4.setObjectName('verticallayout_4')
        self.close_opts_button = QtWidgets.QPushButton(self.close_button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_opts_button
                                     .sizePolicy()
                                     .hasHeightForWidth())
        self.close_opts_button.setSizePolicy(sizePolicy)
        self.close_opts_button.setObjectName('close_opts_button')
        self.verticallayout_4.addWidget(self.close_opts_button)
        self.horizontallayout_4.addWidget(self.close_button_frame)
        self.close_opts_button.setText('⇪')

        # Connect options close button to options_close function
        self.close_opts_button.clicked.connect(self.close_menu)

    def open_menu(self):
        if not self.menu_open:
            if not self.password_output_open:
                self.setFixedSize(500, 100)
            else:
                self.setFixedSize(500, 200)
            self.menu_ui()
        else:
            self.close_menu()

    def close_menu(self):

        # Hide menu
        self.options_frame.hide()

        # Reset window size
        if not self.password_output_open:
            self.resize(500, 50)
        else:
            self.setFixedSize(500, 200)

        # Reset menu button icon
        self.menu_button.setText('☰')

        # Set menu open flag
        self.menu_open = False

    def open_password_ouput(self):
        if not self.password_output_open:
            self.setFixedSize(500, 200)
            self.password_ui()
            self.generate_pass()
        else:
            self.generate_pass()

    def password_ui(self):

        # Set open flag
        self.password_output_open = True

        # Change menu button to 'open'
        self.menu_button.setText('☷')

        # Create output frame
        self.output_frame = QtWidgets.QFrame(self.centralWidget)
        self.output_frame.setObjectName('output_frame')
        self.horizontallayout_14 = QtWidgets.QHBoxLayout(self.output_frame)
        self.horizontallayout_14.setSizeConstraint(QtWidgets
                                                   .QLayout
                                                   .SetDefaultConstraint)
        self.horizontallayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_14.setSpacing(0)
        self.horizontallayout_14.setObjectName('horizontallayout_14')

        # Add output frame to layout
        self.verticalLayout_10.addWidget(self.output_frame)

        # Create output box
        self.password_output = QtWidgets.QTextEdit(self.output_frame)
        self.password_output.setReadOnly(True)
        self.password_output.setSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Expanding)
        self.password_output.setStyleSheet('font: bold 12px;'
                                           'background: #FFFFFF; '
                                           'border: 1px solid #272727')

        self.horizontallayout_14.addWidget(self.password_output)

    def generate_pass(self):

        # Clear the output box
        self.password_output.setText('')

        # Set strings to get chars from
        nums = string.digits
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        s_chars = '!@#$%^&*()\{\}[]?,.'

        # Init output character string
        output_chars = ''

        # Init empty password list
        final_password_list = []

        # Add chars from strings relative to checkboxes
        output_chars = (nums * self.nums_checkbox.isChecked() +
                        lower * self.lower_checkbox.isChecked() +
                        upper * self.upper_checkbox.isChecked() +
                        s_chars * self.s_chars_checkbox.isChecked())

        # Generate for that amount in the number of pass input
        for i in range(0, self.number_of_pass.value()):
            password = ''

            for i in range(self.number_of_chars.value()):
                password += random.choice(output_chars)

            # Add generated password to the password lisr
            final_password_list.append(password)

        # Add each password in the password list to the output box
        for i in final_password_list:
            self.password_output.append(i)

    ''' Window handling '''

    # Listen for mouse click and move window when dragged
    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)


''' Run '''


def main():

    app = QtWidgets.QApplication(sys.argv)

    main = Passwordy()
    main.show()

    sys.exit(app.exec_())

if __name__ == '__main__':

    main()
