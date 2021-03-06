from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QVariant

from app.Controller import Controller
from model import SchemaGraph

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

btnTranslate = None
choiceBox = None
queryInputText = None
btnConfirmChoice = None
treeChoice = None
btnTreeConfirm = None
label = None
display = None


class Ui_MainWindow(object):
    stage = None
    app = None
    ctrl = None
    nlInput = ""
    userView = None
    choiceList = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnTranslate = QtGui.QPushButton(self.centralwidget)
        self.btnTranslate.setGeometry(QtCore.QRect(140, 190, 117, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnTranslate.setFont(font)
        self.btnTranslate.setObjectName(_fromUtf8("btnTranslate"))
        self.btnTranslate.clicked.connect(lambda: self.startTranslation())

        self.queryInputText = QtGui.QPlainTextEdit(self.centralwidget)
        self.queryInputText.setGeometry(QtCore.QRect(40, 40, 341, 141))
        self.queryInputText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.queryInputText.setObjectName(_fromUtf8("plainTextEdit"))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setItalic(False)
        self.queryInputText.setFont(font)
        self.queryInputText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.queryInputText.setObjectName(_fromUtf8("plainTextEdit"))

        self.choiceBox = QtGui.QComboBox(self.centralwidget)
        self.choiceBox.setGeometry(QtCore.QRect(470, 230, 241, 32))
        self.choiceBox.setVisible(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choiceBox.sizePolicy().hasHeightForWidth())
        self.choiceBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.choiceBox.setFont(font)
        self.choiceBox.setObjectName(_fromUtf8("choiceBox"))

        self.btnConfirmChoice = QtGui.QPushButton(self.centralwidget)
        self.btnConfirmChoice.setGeometry(QtCore.QRect(520, 270, 141, 32))
        self.btnConfirmChoice.clicked.connect(lambda: self.btnConfirmChoiceClick(self.btnConfirmChoice, self.choiceBox))
        self.btnConfirmChoice.setVisible(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnConfirmChoice.setFont(font)
        self.btnConfirmChoice.setObjectName(_fromUtf8("btnConfirmChoice"))

        self.treeChoice = QtGui.QComboBox(self.centralwidget)
        self.treeChoice.setGeometry(QtCore.QRect(540, 360, 81, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.treeChoice.setFont(font)
        self.treeChoice.setObjectName(_fromUtf8("treeChoice"))
        self.treeChoice.setVisible(False)

        self.btnTreeConfirm = QtGui.QPushButton(self.centralwidget)
        self.btnTreeConfirm.setGeometry(QtCore.QRect(520, 400, 131, 32))
        self.btnTreeConfirm.setVisible(False)
        self.btnTreeConfirm.clicked.connect(lambda: self.btnTreeConfirmClick(self.treeChoice))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnTreeConfirm.setFont(font)
        self.btnTreeConfirm.setObjectName(_fromUtf8("btnTreeConfirm"))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 0, 261, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.display = QtGui.QTextEdit(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(410, 40, 381, 171))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.display.setFont(font)
        self.display.setObjectName(_fromUtf8("display"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnTranslate.setText(_translate("MainWindow", "Translate", None))
        self.queryInputText.setPlainText(_translate("MainWindow", self.nlInput, None))
        self.btnConfirmChoice.setText(_translate("MainWindow", "Confirm Choice ", None))
        self.btnTreeConfirm.setText(_translate("MainWindow", "Confirm Tree", None))
        self.label.setText(_translate("MainWindow", "Welcome to NLIDB ", None))


    def __init__(self):
        self.userView = self
        self.ctrl = Controller(self.userView)
        # self.nlInput = raw_input("Enter Natural Language Input:\n")
        self.nlInput = "Return number of authors who published theory papers before 1980 ."
        #self.nlInput = "Return the conference in each area whose papers have the most total citations ."
        self.choiceList =[]

    def setDisplay(self, text):
        self.display.setText(text)

    def appendDisplay(self, text):
        self.display.setText(self.display.toPlainText()+text)

    def showNodesChoice(self):
        self.choiceBox.show()
        self.btnConfirmChoice.show()

    def removeChoiceBoxButton(self):
        self.choiceBox.hide()
        self.btnConfirmChoice.hide()

    def btnConfirmChoiceClick(self, btn, chBox):
        self.ctrl.chooseNode(self.getNodeInfoObject(self.getChoice()))

    def getNodeInfoObject(self, string):
        nodeInfo = string.split(' ')
        type = nodeInfo[0]
        value = nodeInfo[2]
        return self.findNodeInfo(type, value)

    def findNodeInfo(self, type, value):
        for nodeInfo in self.choiceList:
            if nodeInfo.getType() == type and nodeInfo.getValue() == value:
                return nodeInfo

    def setChoices(self, choices):
        self.choiceList = choices
        self.choiceBox.clear()
        for choice in choices:
            self.choiceBox.addItem(self.userView.createOptionMsg(choice.getType(), choice.getValue(), choice.getScore()))
        self.choiceBox.setCurrentIndex(0)
        self.choiceBox.show()
        self.btnConfirmChoice.show()

    def createOptionMsg(self, type, value, score):
        sb = []
        sb.append(type)
        sb.append(" : ")
        sb.append(value)
        str = ''.join(sb)
        return str

    def getChoice(self):
        return self.choiceBox.currentText()

    def showTreesChoice(self):
        self.treeChoice.addItem("select")
        self.treeChoice.addItem("0")
        self.treeChoice.addItem("1")
        self.treeChoice.addItem("2")
        self.btnTreeConfirm.show()
        self.treeChoice.show()

    def removeTreesChoices(self):
        self.treeChoice.clear()
        self.btnConfirmChoice.hide()
        self.btnTreeConfirm.hide()
        self.treeChoice.hide()

    def startTranslation(self):
        self.ctrl.processNaturalLanguage(str(self.queryInputText.toPlainText()))

    def btnTreeConfirmClick(self, treeChoice):
        if(treeChoice.currentText() == "select"):
            return
        self.ctrl.chooseTree(int(treeChoice.currentText()))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
#     ROOT Return number authors papers before 1980
