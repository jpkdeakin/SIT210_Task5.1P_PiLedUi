import RPi.GPIO as GPIO
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# Setting up class for the GUI Window.
class MyWindow(QMainWindow):

	# Constructor
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100,100,300,150)
        self.setWindowTitle("SIT Task 5.1P")
        self.initUI()
        self.initGPIO()
    
	# Setup GPIO's and PWMs
    def initGPIO(self):
		# General GPIO Stuff
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
		
		# Setting up Outputs
        GPIO.setup(2,GPIO.OUT)
        GPIO.setup(3,GPIO.OUT)
        GPIO.setup(4,GPIO.OUT)
        GPIO.output(2,False)
        GPIO.output(3,False)
        GPIO.output(4,False)
        
    
    # Setup User Interface Devices
    def initUI(self):
	
		# Text Labels
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("LED Red : 0")
        self.label1.move(120,20)
 
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("LED Orange : 0")
        self.label2.move(120,60)
        
        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("LED Green : 0")
        self.label3.move(120,100)
		
        # Update label sizes to match text
        self.update()
		
		# Toggle Buttons
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText("Toggle 1 ")
        self.btn1.move(10,20)
        self.btn1.clicked.connect(self.btn1_Clicked)
        
        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText("Toggle 2")
        self.btn2.move(10,60)
        self.btn2.clicked.connect(self.btn2_Clicked)
        
        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setText("Toggle 3")
        self.btn3.move(10,100)
        self.btn3.clicked.connect(self.btn3_Clicked)

    # Toggle red LED
    def btn1_Clicked(self):
        GPIO.output(2,not GPIO.input(2))
        self.label1.setText("LED Red : " + str(GPIO.input(2)))
        self.update()

	# Toggle orange LED
    def btn2_Clicked(self):
        GPIO.output(3,not GPIO.input(3))
        self.label2.setText("LED Orange : " + str(GPIO.input(3)))
        self.update()

	# Toggle green LED
    def btn3_Clicked(self):
        GPIO.output(4,not GPIO.input(4))
        self.label3.setText("LED Green : " + str(GPIO.input(4)))
        self.update()

    def update(self):
        self.label1.adjustSize()
        self.label2.adjustSize()
        self.label3.adjustSize()

# Create window MyWindow object
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
 
# Run the window! 
window()
                                

