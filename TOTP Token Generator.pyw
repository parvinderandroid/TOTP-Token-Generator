# Import pyotp for generating TOTP tokens and time for timing updates
# Import QtWidgets and QtCore for the GUI
import pyotp, time
from PyQt6 import QtWidgets, QtCore

# Define the style sheet for dark mode
dark_mode_style_sheet = """
* {
    font-size: 12pt;
}
QWidget {
    background-color: #333333;
    color: white;
}
QLineEdit {
    background-color: #444444;
}
QPushButton {
    background-color: #444444;
    color: white;
}
"""

# Define the style sheet for light mode
light_mode_style_sheet = """
* {
    font-size: 12pt;
}
"""


class TOTPWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.secrets = {
            "Issuer 1": "R233SCNY3FDNMWXN3O56RVLJFW533P46",
            "Issuer 2": "KAJC6U5ADSKRUZKIUATORJVE4EF7QG4I",
            "Issuer 3": "OZZYOMOU5F5BHL4WDA4JGEOWVE2Z333Y",
            "Issuer 4": "DMAN6Y6RUIGFDC4J6MJRFV3BX66AEHWT",
            "Issuer 5": "ADJYBHZ5ANKJXL62D5F7OPB2ZMYXYOHW",
            "Issuer 6": "6OVOWXYYLDLBK362XJJN2FAC2ZQW4HYV",
            "Issuer 7": "APGQVA2IAMTCLFWRMDYQICJ7NYMU5ETQ",
        }

        # Set the style sheet for the window
        self.setStyleSheet(light_mode_style_sheet)
        # Initialize the GUI
        self.initUI()

    def initUI(self):
        # Create a vertical layout to hold the user widgets
        layout = QtWidgets.QVBoxLayout()
        # Create a dictionary to hold the widgets for each issuer
        self.totp_widgets = {}
        # Find the length of the longest issuer name
        max_issuer_length = len(max(self.secrets, key=len))

        # Iterate over the secrets and create a widget for each issuer
        for n, s in self.secrets.items():
            # Create a label for the issuer name
            l = QtWidgets.QLabel(n)
            # Set the width to be as big as the longest issuer name
            l.setFixedWidth(max_issuer_length * 12)
            # Create a read-only line edit for the TOTP token
            le = QtWidgets.QLineEdit(pyotp.TOTP(s).now())
            le.setReadOnly(True)
            # Create a button to copy the TOTP token to the clipboard
            b = QtWidgets.QPushButton("Copy")
            # Set a property on the button to hold the secret
            b.setProperty("secret", s)
            # Connect the button's clicked signal to the copy_token method
            b.clicked.connect(self.copy_token)
            # Create a horizontal layout to hold the user widgets
            user_layout = QtWidgets.QHBoxLayout()
            # Add the user widgets to the layout
            user_layout.addWidget(l)
            user_layout.addWidget(le)
            user_layout.addWidget(b)
            # Add the user layout to the main layout
            layout.addLayout(user_layout)
            # Add the widgets to the totp_widgets dictionary
            self.totp_widgets[n] = (s, le)

        # Create a toggle button to switch between dark and light mode
        toggle_button = QtWidgets.QPushButton("Toggle Dark Mode")
        # Connect the toggle button's clicked signal to the toggle_dark_mode method
        toggle_button.clicked.connect(self.toggle_dark_mode)
        # Add the toggle button to the main layout
        layout.addWidget(toggle_button)
        # Set the main layout for the widget
        self.setLayout(layout)
        # Set the widget's geometry and window title
        # self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("TOTP Tokens")
        # Show the widget
        self.show()
        # Create a timer to update the TOTP tokens every 30 seconds
        self.timer = QtCore.QTimer(self)
        # Connect the timer's timeout signal to the update_tokens method
        self.timer.timeout.connect(self.update_tokens)
        # Start the timer with an initial delay to align with the 30 second time step
        self.timer.start((30 - int(time.time()) % 30) * 1000)

    def copy_token(self):
        # Get the button that was clicked
        s = self.sender()
        # Get the secret property from the button
        secret = s.property("secret")
        # Generate the TOTP token for the secret
        token = pyotp.TOTP(secret).now()
        # Get the clipboard object
        clipboard = QtWidgets.QApplication.clipboard()
        # Set the clipboard text to the TOTP token
        clipboard.setText(token)

    def update_tokens(self):
        # Iterate over the totp_widgets dictionary
        for name, (secret, line_edit) in self.totp_widgets.items():
            # Update the text of the line edit with the current TOTP token
            line_edit.setText(pyotp.TOTP(secret).now())

    def toggle_dark_mode(self):
        # If the widget's style sheet is set to light mode style sheet, set it to the dark mode style sheet
        if self.styleSheet() == light_mode_style_sheet:
            self.setStyleSheet(dark_mode_style_sheet)
        # Otherwise, set it to the light mode style sheet
        else:
            self.setStyleSheet(light_mode_style_sheet)


if __name__ == "__main__":
    # Create a QApplication object
    app = QtWidgets.QApplication([])
    # Create an instance of the TOTPWindow class
    w = TOTPWindow()
    # Run the application's event loop
    app.exec()
