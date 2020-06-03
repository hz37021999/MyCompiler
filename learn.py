import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

# class first(QMainWindow):
#     def __init__(self):
#         super(first,self).__init__()
#
#         self.setWindowTitle('first app')
#         self.resize(400,300)
#         self.status = self.statusBar()
#         self.status.showMessage('5s',5000)
#
# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     app.setWindowIcon(QIcon())
#     main=first()
#     main.show()
#
#     sys.exit(app.exec_())

class first(QMainWindow):
    def __init__(self):
        super(first,self).__init__()

        self.resize(300,120)
        self.setWindowTitle('退出')

        #添加Button
        self.button1 = QPushButton('退出程序')
        self.button1.clicked.connect(self.onClick_Button)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)


    #单击事件的方法
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text()+'按钮被按下')
        app = QApplication.instance()
        #退出应用
        app.quit()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=first()
    main.show()

    sys.exit(app.exec_())