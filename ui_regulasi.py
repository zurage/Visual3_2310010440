# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regulasi.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(418, 548)
        self.gridLayoutWidget_2 = QWidget(Form)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 20, 341, 381))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 5, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.editNama = QLineEdit(self.gridLayoutWidget_2)
        self.editNama.setObjectName(u"editNama")

        self.gridLayout_3.addWidget(self.editNama, 1, 1, 1, 1)

        self.tabelRegulasi = QTableWidget(self.gridLayoutWidget_2)
        if (self.tabelRegulasi.columnCount() < 5):
            self.tabelRegulasi.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelRegulasi.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelRegulasi.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelRegulasi.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelRegulasi.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelRegulasi.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelRegulasi.setObjectName(u"tabelRegulasi")

        self.gridLayout_3.addWidget(self.tabelRegulasi, 7, 0, 1, 2)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.editNomor = QLineEdit(self.gridLayoutWidget_2)
        self.editNomor.setObjectName(u"editNomor")

        self.gridLayout_3.addWidget(self.editNomor, 2, 1, 1, 1)

        self.editID = QLineEdit(self.gridLayoutWidget_2)
        self.editID.setObjectName(u"editID")

        self.gridLayout_3.addWidget(self.editID, 0, 1, 1, 1)

        self.editDeskripsi = QTextEdit(self.gridLayoutWidget_2)
        self.editDeskripsi.setObjectName(u"editDeskripsi")

        self.gridLayout_3.addWidget(self.editDeskripsi, 3, 1, 1, 1)

        self.editTahun = QDateEdit(self.gridLayoutWidget_2)
        self.editTahun.setObjectName(u"editTahun")

        self.gridLayout_3.addWidget(self.editTahun, 5, 1, 1, 1)

        self.editCari = QLineEdit(self.gridLayoutWidget_2)
        self.editCari.setObjectName(u"editCari")

        self.gridLayout_3.addWidget(self.editCari, 6, 0, 1, 2)

        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(270, 420, 90, 29))
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(10, 420, 90, 29))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(140, 420, 90, 29))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Nama Regulasi", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Tahun ", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Nomor", None))
        ___qtablewidgetitem = self.tabelRegulasi.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"IDRegulasi", None));
        ___qtablewidgetitem1 = self.tabelRegulasi.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama", None));
        ___qtablewidgetitem2 = self.tabelRegulasi.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Nomor", None));
        ___qtablewidgetitem3 = self.tabelRegulasi.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Tahun", None));
        ___qtablewidgetitem4 = self.tabelRegulasi.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Deskripsi", None));
        self.label_10.setText(QCoreApplication.translate("Form", u"Deskripsi", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"ID Regulasi", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
    # retranslateUi

