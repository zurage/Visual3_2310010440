# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(591, 408)
        self.gridLayoutWidget_2 = QWidget(Form)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(100, 50, 341, 192))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.editID = QLineEdit(self.gridLayoutWidget_2)
        self.editID.setObjectName(u"editID")

        self.gridLayout_3.addWidget(self.editID, 0, 2, 1, 1)

        self.editNama = QLineEdit(self.gridLayoutWidget_2)
        self.editNama.setObjectName(u"editNama")

        self.gridLayout_3.addWidget(self.editNama, 3, 2, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.editPassword = QLineEdit(self.gridLayoutWidget_2)
        self.editPassword.setObjectName(u"editPassword")

        self.gridLayout_3.addWidget(self.editPassword, 2, 2, 1, 1)

        self.editUser = QLineEdit(self.gridLayoutWidget_2)
        self.editUser.setObjectName(u"editUser")

        self.gridLayout_3.addWidget(self.editUser, 1, 2, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)

        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(220, 250, 90, 29))
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(100, 250, 90, 29))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(350, 250, 90, 29))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Password", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"ID Admin", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"User Name", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Nama Lengkap", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
    # retranslateUi

