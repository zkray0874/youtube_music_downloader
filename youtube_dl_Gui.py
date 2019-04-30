import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class youtube_dl_Gui(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint)
        QToolTip.setFont(QFont('SanSerif', 10))

        self.setToolTip('This is <b>ZK-youtube-downloader</b>')

        label = QLabel('Download complete', self)
        label.setFont(QFont('SanSerif', 70))
        label.setAlignment(Qt.AlignCenter)

        btn = QPushButton('Got it', self)
        btn.setFont(QFont('SanSerif', 22))
        btn.clicked.connect(QApplication.instance().quit)
        btn.setToolTip('<b>Game over</b>')
        btn.resize(btn.sizeHint())

        h_layout = QVBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(btn)

        self.setLayout(h_layout)
        self.setGeometry(0, 0, 1300, 300)
        self.setWindowTitle('ZK youtube Downloader')
        self.setWindowIcon(QIcon('web.png'))
        self.center()

        self.show()

    def center(self):

        gr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        gr.moveCenter(cp)
        self.move(gr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = youtube_dl_Gui()
    sys.exit(app.exec_())
