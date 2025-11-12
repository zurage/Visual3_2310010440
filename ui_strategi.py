# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'strategi.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(410, 499)
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(40, 350, 90, 29))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(280, 350, 90, 29))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(150, 350, 90, 29))
        self.gridLayoutWidget_2 = QWidget(Form)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(40, 20, 341, 319))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 1, 1, 1, 1)

        self.editID = QLineEdit(self.gridLayoutWidget_2)
        self.editID.setObjectName(u"editID")

        self.gridLayout_3.addWidget(self.editID, 0, 1, 1, 1)

        self.tabelStrategi = QTableWidget(self.gridLayoutWidget_2)
        if (self.tabelStrategi.columnCount() < 4):
            self.tabelStrategi.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelStrategi.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelStrategi.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelStrategi.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelStrategi.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelStrategi.setObjectName(u"tabelStrategi")

        self.gridLayout_3.addWidget(self.tabelStrategi, 5, 0, 1, 2)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)

        self.editDeskripsi = QTextEdit(self.gridLayoutWidget_2)
        self.editDeskripsi.setObjectName(u"editDeskripsi")

        self.gridLayout_3.addWidget(self.editDeskripsi, 3, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.editNomor = QLineEdit(self.gridLayoutWidget_2)
        self.editNomor.setObjectName(u"editNomor")

        self.gridLayout_3.addWidget(self.editNomor, 2, 1, 1, 1)

        self.editCari = QLineEdit(self.gridLayoutWidget_2)
        self.editCari.setObjectName(u"editCari")

        self.gridLayout_3.addWidget(self.editCari, 4, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"ID Regulasi", None))
        ___qtablewidgetitem = self.tabelStrategi.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"IDStrategi", None));
        ___qtablewidgetitem1 = self.tabelStrategi.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"IDRegulasi", None));
        ___qtablewidgetitem2 = self.tabelStrategi.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Judul", None));
        ___qtablewidgetitem3 = self.tabelStrategi.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Tujuan", None));
        self.label_6.setText(QCoreApplication.translate("Form", u"ID Strategi", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Tujuan", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Judul", None))
    # retranslateUi

