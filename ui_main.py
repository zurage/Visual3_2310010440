# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 600)
        self.actionAdmin = QAction(Main)
        self.actionAdmin.setObjectName(u"actionAdmin")
        self.actionLembaga = QAction(Main)
        self.actionLembaga.setObjectName(u"actionLembaga")
        self.actionStrategi = QAction(Main)
        self.actionStrategi.setObjectName(u"actionStrategi")
        self.actionProgram = QAction(Main)
        self.actionProgram.setObjectName(u"actionProgram")
        self.actionRegulasi = QAction(Main)
        self.actionRegulasi.setObjectName(u"actionRegulasi")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuHalaman = QMenu(self.menubar)
        self.menuHalaman.setObjectName(u"menuHalaman")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHalaman.menuAction())
        self.menuHalaman.addAction(self.actionAdmin)
        self.menuHalaman.addAction(self.actionProgram)
        self.menuHalaman.addAction(self.actionStrategi)
        self.menuHalaman.addAction(self.actionLembaga)
        self.menuHalaman.addAction(self.actionRegulasi)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.actionAdmin.setText(QCoreApplication.translate("Main", u"Admin", None))
        self.actionLembaga.setText(QCoreApplication.translate("Main", u"Lembaga", None))
        self.actionStrategi.setText(QCoreApplication.translate("Main", u"Strategi", None))
        self.actionProgram.setText(QCoreApplication.translate("Main", u"Program", None))
        self.actionRegulasi.setText(QCoreApplication.translate("Main", u"Regulasi", None))
        self.menuHalaman.setTitle(QCoreApplication.translate("Main", u"Halaman", None))
    # retranslateUi

