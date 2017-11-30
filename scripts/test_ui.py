from PyQt5 import QtCore, QtGui, QtWidgets
from toplog import Ui_MainWindow
import sys

class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
	def __init__(self, parent = None):
		QtWidgets.QMainWindow.__init__(self, parent = parent)
		self.setupUi(self)
		self.comboBox.addItems(['ROVER', 'IMU'])
		self.roverIPText.show()
		self.imuIPText.hide()
		self.navState = 'OFF'
		self.gpsState = 'OFF'
		self.armState = 'OFF'
		self.imuState = 'OFF'
		self.navigationButton.setStyleSheet("background-color:red")
		self.gpsButton.setStyleSheet("background-color:red")
		self.armButton.setStyleSheet("background-color:red")
		self.imuButton.setStyleSheet("background-color:red")
		#palette = self.palette()
		#palette.setColor(self.backgroundRole(), QtCore.Qt.black)
		#self.speedLabel.setStyleSheet("color:green")
		#self.setPalette(palette)
		self.comboBox.currentTextChanged.connect(lambda: self.changeComboText())
		self.setIPButton.clicked.connect(lambda: self.printToLog('IP'))
		self.navigationButton.clicked.connect(lambda: self.printToLog('NAV'))
		self.gpsButton.clicked.connect(lambda: self.printToLog('GPS'))
		self.armButton.clicked.connect(lambda: self.printToLog('ARM'))
		self.imuButton.clicked.connect(lambda: self.printToLog('IMU'))
		#self.infoText.setStyleSheet("background-color: black; color:green")
		self.show()

	def printToLog(self,button):
		if button == 'IP':
			if self.comboBox.currentText() == 'ROVER':
				self.infoText.append('ROVER IP SET TO :' + self.roverIPText.text())
			else:
				self.infoText.append('IMU IP SET TO :' + self.imuIPText.text())

		if button == 'NAV':
			if self.navState == 'OFF':
				self.infoText.append('NAVIGATION MODULE ACTIVE')
				self.navState = 'ON'
				self.navigationButton.setStyleSheet("background-color:green")
			else:
				self.infoText.append('NAVIGATION MODULE DISABLED')
				self.navState = 'OFF'
				self.navigationButton.setStyleSheet("background-color:red")

		if button == 'GPS':
			if self.gpsState == 'OFF':
				self.infoText.append('GPS MODULE ACTIVE')
				self.gpsState = 'ON'
				self.gpsButton.setStyleSheet("background-color:green")
			else:
				self.infoText.append('GPS MODULE DISABLED')
				self.gpsState = 'OFF'
				self.gpsButton.setStyleSheet("background-color:red")

		if button == 'ARM':
			if self.armState == 'OFF':
				self.infoText.append('ARM MODULE ACTIVE')
				self.armState = 'ON'
				self.armButton.setStyleSheet("background-color:green")
			else:
				self.infoText.append('ARM MODULE DISABLED')
				self.armState = 'OFF'
				self.armButton.setStyleSheet("background-color:red")

		if button == 'IMU':
			if self.imuState == 'OFF':
				self.infoText.append('IMU MODULE ACTIVE')
				self.imuState = 'ON'
				self.imuButton.setStyleSheet("background-color:green")
			else:
				self.infoText.append('IMU MODULE DISABLED')
				self.imuState = 'OFF'
				self.imuButton.setStyleSheet("background-color:red")



	def changeComboText(self):
		if self.comboBox.currentText() == 'ROVER':
			self.roverIPText.show()
			self.imuIPText.hide()
		else:
			self.imuIPText.show()
			self.roverIPText.hide()

	def keyPressEvent(self,event):
		if event.key() == QtCore.Qt.Key_Plus:
			self.speedBar.setValue(self.speedBar.value() + 1)
		elif event.key() == QtCore.Qt.Key_Minus:
			self.speedBar.setValue(self.speedBar.value() - 1)

		if event.key() == QtCore.Qt.Key_A:
			self.infoText.append('ROVER MOVING LEFT')
		if event.key() == QtCore.Qt.Key_D:
			self.infoText.append('ROVER MOVING RIGHT')
		if self.speedBar.value() < 20:
			self.speedBar.setStyleSheet("""QProgressBar::chunk { background-color:red;} QProgressBar{text-align:center;} """)
		else:
			self.speedBar.setStyleSheet("""QProgressBar::chunk { background-color:green;} QProgressBar{text-align:center;} """)



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()
