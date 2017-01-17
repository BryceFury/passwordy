# coding=UTF-8

import random
import string
import sys

from stylesheet import set_stylesheet

from PyQt5 import QtCore, QtWidgets


# Create main canvas
class Passwordy(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        # Call function to create UI
        self.main_ui()

    ''' Initial window '''

    def main_ui(self):

        # Set window stylesheet
        get_stylesheet = set_stylesheet()
        self.setStyleSheet(get_stylesheet)

        # Set centralWidget
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName('centralWidget')

        # Set centralWidget layout
        self.main_layout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.main_layout.setSizeConstraint(QtWidgets
                                           .QLayout
                                           .SetDefaultConstraint)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName('main_layout')

        # Create top_frame
        self.top_frame = QtWidgets.QFrame(self.centralWidget)
        self.top_frame.setObjectName('top_frame')

        # Set top_frame layout
        self.top_frame_layout = QtWidgets.QHBoxLayout(self.top_frame)
        self.top_frame_layout.setSizeConstraint(QtWidgets
                                                .QLayout
                                                .SetDefaultConstraint)
        self.top_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.top_frame_layout.setSpacing(-1)

        # Set top_frame layout's name
        self.top_frame_layout.setObjectName('top_frame_layout')

        # Add top_frame to main_layout
        self.main_layout.addWidget(self.top_frame)

        # Create frame for menu button and title inside top_frame
        self.menu_frame = QtWidgets.QFrame(self.top_frame)

        # Set menu_frame's size
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

        # Set menu frame's name
        self.menu_frame.setObjectName('menu_frame')

        # Set menu frames layout
        self.menu_frame_layout = QtWidgets.QHBoxLayout(self.menu_frame)
        self.menu_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.menu_frame_layout.setSpacing(-1)
        self.menu_frame_layout.setObjectName('menu_frame_layout')

        # Create title label
        self.title_label = QtWidgets.QLabel(self.menu_frame)

        # Set title label's size
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label
                                     .sizePolicy()
                                     .hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)

        # Set title label's name
        self.title_label.setObjectName('title_label')

        # Set title label's text
        self.title_label.setText('passwordy')

        # Add title label to menu frame's layout
        self.menu_frame_layout.addWidget(self.title_label)

        # Create menubutton
        self.menu_button = QtWidgets.QPushButton(self.menu_frame)

        # Set menu button's name
        self.menu_button.setObjectName('menu_button')

        # Set menu button's text
        self.menu_button.setText('☰')

        # Add menu button widget to menu frame's layout
        self.menu_frame_layout.addWidget(self.menu_button)

        # Connect menu button to open_menu function
        self.menu_button.clicked.connect(self.open_menu)

        # Add menu frame to layout
        self.top_frame_layout.addWidget(self.menu_frame)

        # Create frame for generate button
        self.generate_frame = QtWidgets.QFrame(self.top_frame)

        # Set generate button's frame's size
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

        # Set generate button's frame's name
        self.generate_frame.setObjectName('generate_frame')

        # # Set generate button's frame's layout
        self.generate_frame_layout = QtWidgets.QVBoxLayout(self.generate_frame)
        self.generate_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.generate_frame_layout.setSpacing(0)
        self.generate_frame_layout.setObjectName('generate_frame_layout')

        # Create generate button
        self.generate_button = QtWidgets.QPushButton(self.generate_frame)

        # Set generate button's text
        self.generate_button.setText('generate')

        # Set generate button's size
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_button
                                     .sizePolicy()
                                     .hasHeightForWidth())
        self.generate_button.setSizePolicy(sizePolicy)

        # Set generate button's name
        self.generate_button.setObjectName('generate_button')

        # Add generate button to layout
        self.generate_frame_layout.addWidget(self.generate_button)

        # Add generate frame to layout
        self.top_frame_layout.addWidget(self.generate_frame)

        # Connect generate button to generate_pass function
        self.generate_button.clicked.connect(self.open_password_ouput)

        # Create frame for exit button
        self.exit_frame = QtWidgets.QFrame(self.top_frame)

        # Set exit button's frame's size
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

        # Set exit button's frame's name
        self.exit_frame.setObjectName('exit_frame')

        # Create layout for generate button frame
        self.generate_frame_layout = QtWidgets.QVBoxLayout(self.exit_frame)
        self.generate_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.generate_frame_layout.setSpacing(0)
        self.generate_frame_layout.setObjectName('generate_frame_layout')

        # Create exit button
        self.exit_button = QtWidgets.QPushButton(self.exit_frame)

        # Set exit button's text
        self.exit_button.setText('exit')

        # Set exit button's size
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_button
                                     .sizePolicy()
                                     .hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy)

        # Set exit button's name
        self.exit_button.setObjectName('exit_button')

        # Add exit button to layout
        self.generate_frame_layout.addWidget(self.exit_button)

        # Add exit frame to layout
        self.top_frame_layout.addWidget(self.exit_frame)

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

    ''' Options menu '''

    def menu_ui(self):

        # Set open flag
        self.menu_open = True

        # Change menu button to 'open'
        self.menu_button.setText('☷')

        # Create options frame
        self.options_frame = QtWidgets.QFrame(self.centralWidget)
        self.options_frame.setObjectName('options_frame')

        # Set layout for options frame
        self.options_frame_layout = QtWidgets.QHBoxLayout(self.options_frame)
        self.options_frame_layout.setSizeConstraint(QtWidgets
                                                    .QLayout
                                                    .SetDefaultConstraint)
        self.options_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.options_frame_layout.setSpacing(0)

        # Set options frame name
        self.options_frame_layout.setObjectName('options_frame_layout')

        # Add options frame to layout
        self.main_layout.addWidget(self.options_frame)

        # Create checkboxes frame
        self.checks_frame = QtWidgets.QFrame(self.options_frame)

        # Set checkboxes frame's size
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

        # Set checkboxes frame's name
        self.checks_frame.setObjectName('checks_frame')

        # Set checkboxes frame's layout
        self.checks_frame_layout = QtWidgets.QHBoxLayout(self.checks_frame)
        self.checks_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.checks_frame_layout.setSpacing(0)

        # Set checknoxes frame's layout's name
        self.checks_frame_layout.setObjectName('checks_frame_layout')

        # Create characters checkboxes' frame
        self.chars_frame = QtWidgets.QFrame(self.checks_frame)
        self.chars_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chars_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        # Create characters checkboxes' frame's name
        self.chars_frame.setObjectName('chars_frame')

        # Create characters checkboxes' frame's layout
        self.chars_frame_layout = QtWidgets.QVBoxLayout(self.chars_frame)
        self.chars_frame_layout.setContentsMargins(11, 11, 11, 11)
        self.chars_frame_layout.setSpacing(6)
        self.chars_frame_layout.setObjectName('chars_frame_layout')

        # Create numbers checkbox
        self.nums_checkbox = QtWidgets.QCheckBox(self.chars_frame)
        self.nums_checkbox.setChecked(True)

        # Set numbers' checkbox's name
        self.nums_checkbox.setObjectName('nums_checkbox')

        # Add numbers checkbox to characters frame
        self.chars_frame_layout.addWidget(self.nums_checkbox)

        # Create special characters checkbox
        self.s_chars_checkbox = QtWidgets.QCheckBox(self.chars_frame)
        self.s_chars_checkbox.setChecked(True)

        # Set special characters checkbox's name
        self.s_chars_checkbox.setObjectName('s_chars_checkbox')

        # Add special characters checkbox to characters frame
        self.chars_frame_layout.addWidget(self.s_chars_checkbox)

        # Add checkboxes frame to characters frame
        self.checks_frame_layout.addWidget(self.chars_frame)

        # Create case checboxes' frames
        self.case_frame = QtWidgets.QFrame(self.checks_frame)
        self.case_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.case_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        # Set case checboxes' frame's name
        self.case_frame.setObjectName('case_frame')

        # Set case checboxes' frame's layout
        self.case_frame_layout = QtWidgets.QVBoxLayout(self.case_frame)
        self.case_frame_layout.setContentsMargins(11, 11, 11, 11)
        self.case_frame_layout.setSpacing(6)

        # Set case checboxes' frame's name
        self.case_frame_layout.setObjectName('case_frame_layout')

        # Create lowercase checkbox
        self.lower_checkbox = QtWidgets.QCheckBox(self.case_frame)
        self.lower_checkbox.setChecked(True)

        # Set lowercase checkbox's name
        self.lower_checkbox.setObjectName('lower_checkbox')

        # Add lowercase checbox to layout
        self.case_frame_layout.addWidget(self.lower_checkbox)

        # Create uppercase checkbox
        self.upper_checkbox = QtWidgets.QCheckBox(self.case_frame)
        self.upper_checkbox.setChecked(True)

        # Set uppercase checkbox's name
        self.upper_checkbox.setObjectName('upper_checkbox')

        # Add uppercase checbox to case frame's layout
        self.case_frame_layout.addWidget(self.upper_checkbox)

        # Add case frame to checkboxes frame
        self.checks_frame_layout.addWidget(self.case_frame)

        # Set checkboxes labels
        self.nums_checkbox.setText('Numbers')
        self.s_chars_checkbox.setText('Specials')
        self.lower_checkbox.setText('Lowercase')
        self.upper_checkbox.setText('Uppercase')

        # Add checkboxes frame to options frame
        self.options_frame_layout.addWidget(self.checks_frame)

        # Create spinboxes frame
        self.spins_frame = QtWidgets.QFrame(self.options_frame)

        # Set spinboxes frame's size
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spins_frame
                                     .sizePolicy()
                                     .hasHeightForWidth())
        self.spins_frame.setSizePolicy(sizePolicy)
        self.spins_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spins_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        # Set spinboxes frame's name
        self.spins_frame.setObjectName('spins_frame')

        # Create generate_frame's layout
        self.generate_frame_layout = QtWidgets.QVBoxLayout(self.spins_frame)
        self.generate_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.generate_frame_layout.setSpacing(0)

        # Set generate_frame's name
        self.generate_frame_layout.setObjectName('generate_frame_layout')

        # Create labels frame's layout
        self.labels_frame = QtWidgets.QFrame(self.spins_frame)
        self.labels_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labels_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        # Set labels frame's name
        self.labels_frame.setObjectName('labels_frame')

        # Set labels layout's name
        self.labels_frame_layout = QtWidgets.QHBoxLayout(self.labels_frame)
        self.labels_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.labels_frame_layout.setSpacing(0)

        # Set labels layout's name
        self.labels_frame_layout.setObjectName('labels_frame_layout')

        # Create number of characters label's frame
        self.chars_label_frame = QtWidgets.QFrame(self.labels_frame)
        self.chars_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chars_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        # Create number of characters label's frame's name
        self.chars_label_frame.setObjectName('chars_label_frame')

        # Create number of characters label's frame's layout
        self.clbl_frame_layout = QtWidgets.QVBoxLayout(self.chars_label_frame)
        self.clbl_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.clbl_frame_layout.setSpacing(0)

        # Create number of characters label's frame's layout's name
        self.clbl_frame_layout.setObjectName('clbl_frame_layout')

        # Create number of characters label
        self.chars_label = QtWidgets.QLabel(self.chars_label_frame)

        # Set number of characters label's name
        self.chars_label.setObjectName('chars_label')

        # Add number of characters label to
        # number of characters label's frame's layout
        self.clbl_frame_layout.addWidget(self.chars_label)

        # Add labels frame to number of characters label's frame
        self.labels_frame_layout.addWidget(self.chars_label_frame)

        # Create number of passwords label's frame
        self.pass_label_frame = QtWidgets.QFrame(self.labels_frame)
        self.pass_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pass_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        # Set number of passwords label's frame's name
        self.pass_label_frame.setObjectName('pass_label_frame')

        # Set number of passwords label's frame's layout
        self.numpass_lbl_layout = QtWidgets.QHBoxLayout(self.pass_label_frame)
        self.numpass_lbl_layout.setContentsMargins(0, 0, 0, 0)
        self.numpass_lbl_layout.setSpacing(0)

        # Set number of passwords label's frame's layout's name
        self.numpass_lbl_layout.setObjectName('numpass_lbl_layout')

        # Create number of passwords label
        self.pass_label = QtWidgets.QLabel(self.pass_label_frame)

        # Set number of passwords label's name
        self.pass_label.setObjectName('pass_label')

        # Add number of passwords label to
        # number of passwords label's frame's layout
        self.numpass_lbl_layout.addWidget(self.pass_label)

        # Add number of passwords label's
        self.labels_frame_layout.addWidget(self.pass_label_frame)

        # Add labels frame to generate frame
        self.generate_frame_layout.addWidget(self.labels_frame)

        # Create spin boxes frame
        self.spin_boxes_frame = QtWidgets.QFrame(self.spins_frame)
        self.spin_boxes_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spin_boxes_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        # Set spin boxes' frame's name
        self.spin_boxes_frame.setObjectName('spin_boxes_frame')

        # Set spin boxes' frame's layout
        self.spin_frame_layout = QtWidgets.QHBoxLayout(self.spin_boxes_frame)
        self.spin_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.spin_frame_layout.setSpacing(0)

        # Set spin boxes' frame's layout's name
        self.spin_frame_layout.setObjectName('spin_frame_layout')

        # Create number of characters spinbox
        self.number_of_chars = QtWidgets.QSpinBox(self.spin_boxes_frame)

        # Set number of characters spinbox's default values
        self.number_of_chars.setMinimum(1)
        self.number_of_chars.setMaximum(64)

        # Set number of characters spinbox's name
        self.number_of_chars.setObjectName('number_of_chars')

        # Add number of characters spinbox to number of characters frame
        self.spin_frame_layout.addWidget(self.number_of_chars)

        # Create number of passwords spinbox
        self.number_of_pass = QtWidgets.QSpinBox(self.spin_boxes_frame)

        # Set number of passwords spinbox's default values
        self.number_of_pass.setMinimum(1)

        # Set number of passwords spinbox's name
        self.number_of_pass.setObjectName('number_of_pass')

        # Add spin boxes frame's layout to number of passwords frame
        self.spin_frame_layout.addWidget(self.number_of_pass)

        # Add spin boxes frame to generate frame's layout
        self.generate_frame_layout.addWidget(self.spin_boxes_frame)

        # Add spins frame to options frame's layout
        self.options_frame_layout.addWidget(self.spins_frame)

        # Set number of characters and passwords labels' text
        self.chars_label.setText('Number of chars')
        self.pass_label.setText('Number of pass')

        # Create close options button frame
        self.clsbt_frame = QtWidgets.QFrame(self.options_frame)

        # Set close options button's frame's size
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clsbt_frame
                                     .sizePolicy()
                                     .hasHeightForWidth())

        self.clsbt_frame.setSizePolicy(sizePolicy)
        self.clsbt_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.clsbt_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        # Set close options button's frame's name
        self.clsbt_frame.setObjectName('clsbt_frame')

        # Set close options button's frame's layout
        self.clsbt_frame_layout = QtWidgets.QVBoxLayout(self.clsbt_frame)
        self.clsbt_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.clsbt_frame_layout.setSpacing(0)

        # Set close options button's frame's layout's name
        self.clsbt_frame_layout.setObjectName('clsbt_frame_layout')

        # Create close options button
        self.close_opts_button = QtWidgets.QPushButton(self.clsbt_frame)

        # Set close options button's name
        self.close_opts_button.setObjectName('close_opts_button')

        # Add close options button to close options button's layout
        self.clsbt_frame_layout.addWidget(self.close_opts_button)

        # Add close options button's frame to options frame's layout
        self.options_frame_layout.addWidget(self.clsbt_frame)

        # Set close options button's text
        self.close_opts_button.setText('⇪')

        # Connect options close button to options_close function
        self.close_opts_button.clicked.connect(self.close_menu)

    def open_menu(self):
        # Check if menu is open and set size accordingly
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

        # Reset window size dependant on if password output or menu is open
        if not self.password_output_open:
            self.setFixedSize(500, 50)
        elif self.menu_open:
            self.setFixedSize(500, 200)

        # Reset menu button icon
        self.menu_button.setText('☰')

        # Set menu open flag
        self.menu_open = False

    ''' Password output '''

    def password_ui(self):

        # Set open flag
        self.password_output_open = True

        # Create output frame
        self.output_frame = QtWidgets.QFrame(self.centralWidget)
        self.output_frame.setObjectName('output_frame')
        self.output_frame_layout = QtWidgets.QHBoxLayout(self.output_frame)
        self.output_frame_layout.setSizeConstraint(QtWidgets
                                                   .QLayout
                                                   .SetDefaultConstraint)
        self.output_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.output_frame_layout.setSpacing(0)
        self.output_frame_layout.setObjectName('output_frame_layout')

        # Add output frame to layout
        self.main_layout.addWidget(self.output_frame)

        # Create output box
        self.password_output = QtWidgets.QTextEdit(self.output_frame)
        self.password_output.setReadOnly(True)
        self.password_output.setSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Expanding)
        self.password_output.setStyleSheet('font: bold 12px;'
                                           'background: #FFFFFF; '
                                           'border: 1px solid #272727')

        # Add password output to output frame's layout
        self.output_frame_layout.addWidget(self.password_output)

    def open_password_ouput(self):
        # Check if password output is open and call functions accordingly
        if not self.password_output_open:
            self.setFixedSize(500, 200)
            self.password_ui()
            self.generate_pass()
        else:
            self.generate_pass() 

    def generate_pass(self):

        # Check numbers checkbox if
        # user unchecks all boxes and tries to generate
        if not True in [self.nums_checkbox.isChecked() or
                        self.lower_checkbox.isChecked() or
                        self.upper_checkbox.isChecked() or
                        self.s_chars_checkbox.isChecked()]:

            self.nums_checkbox.setChecked(True)

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
