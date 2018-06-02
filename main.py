from PyQt5 import uic, QtWidgets
import sys
 
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()

def showOutput():
    window.output.setText(window.input.text()) 

def clearOutput():
    window.input.setText("")
    window.output.setText("")
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.pushButton.clicked.connect(showOutput)
    window.btnClearOutput.clicked.connect(clearOutput)
    sys.exit(app.exec_())