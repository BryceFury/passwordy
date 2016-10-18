from stylesheet import set_stylesheet

from PyQt5 import QtCore, QtGui, QtWidgets

def CreateMainUI(self):

        # Set window size
        self.resize(500, 50)

        # Set window stylesheet
        get_stylesheet = set_stylesheet()
        self.setStyleSheet(get_stylesheet)

        # Main window setting
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName('centralWidget')

        # Set main widget layout (centralWidget)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName('verticalLayout_10')

         # Create top frame
        self.top_frame = QtWidgets.QFrame(self.centralWidget)
        self.top_frame.setObjectName('top_frame')
        self.horizontallayout_10 = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontallayout_10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontallayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_10.setSpacing(0)
        self.horizontallayout_10.setObjectName('horizontallayout_10')

        # Add top frame to layout
        self.verticalLayout_10.addWidget(self.top_frame)
        

        # Create frame for menu button and title
        self.menu_frame = QtWidgets.QFrame(self.top_frame)

        # Set frame size
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_frame.sizePolicy().hasHeightForWidth())
        self.menu_frame.setSizePolicy(sizePolicy)
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName('menu_frame')

        # Set menu frames layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.menu_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName('horizontalLayout')

        # Create menubutton
        self.menu_button = QtWidgets.QPushButton(self.menu_frame)
        self.menu_button.setObjectName('menu_button')
        self.menu_button.setText('☰')

        # Add menubutton widget to layout
        self.horizontalLayout.addWidget(self.menu_button)

        # Connect menu button to open_menu function
        self.menu_button.clicked.connect(self.open_menu)

        # Create title label
        self.title_label = QtWidgets.QLabel(self.menu_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setObjectName('title_label')
        self.title_label.setText('passwordy')

        # Add title label to layout
        self.horizontalLayout.addWidget(self.title_label)
        self.horizontallayout_10.addWidget(self.menu_frame)

        # Create frame for middle spacer
        self.spacer_frame = QtWidgets.QFrame(self.top_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spacer_frame.sizePolicy().hasHeightForWidth())     
        self.spacer_frame.setSizePolicy(sizePolicy)
        self.spacer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spacer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spacer_frame.setObjectName('spacer_frame')

        # Create layout for spacer frame
        self.verticalLayout = QtWidgets.QVBoxLayout(self.spacer_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName('verticalLayout')

        # Create horizontal spacer
        spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacer)

        # Add spacer to layout
        self.horizontallayout_10.addWidget(self.spacer_frame)
        
        # Create frame for generate button
        self.generate_frame = QtWidgets.QFrame(self.top_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_frame.sizePolicy().hasHeightForWidth())
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_button.sizePolicy().hasHeightForWidth())
        self.generate_button.setSizePolicy(sizePolicy)
        self.generate_button.setObjectName('generate_button')

        # Add generate button to layout
        self.verticalLayout_3.addWidget(self.generate_button)

        # Add generate frame to layout
        self.horizontallayout_10.addWidget(self.generate_frame)

        # Connect generate button to generate_passwords function
        self.generate_button.clicked.connect(self.password_ui)
        self.generate_button.clicked.connect(self.generate_passwords)
        
        # Set central widget
        self.setCentralWidget(self.centralWidget)

        # Hide OS' default window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Connect slots
        #QtCore.QMetaObject.connectSlotsByName(self)

if __name__ == '__main__':
    main()