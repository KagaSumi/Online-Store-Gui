# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Product_Form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QWidget)

class Ui_W_Product_Form(object):
    def setupUi(self, W_Product_Form):
        if not W_Product_Form.objectName():
            W_Product_Form.setObjectName(u"W_Product_Form")
        W_Product_Form.resize(532, 244)
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        W_Product_Form.setFont(font)
        self.gridLayout = QGridLayout(W_Product_Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_cancel = QPushButton(W_Product_Form)
        self.pb_cancel.setObjectName(u"pb_cancel")

        self.gridLayout.addWidget(self.pb_cancel, 3, 1, 1, 1)

        self.pb_ok = QPushButton(W_Product_Form)
        self.pb_ok.setObjectName(u"pb_ok")

        self.gridLayout.addWidget(self.pb_ok, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 2)

        self.le_message = QLabel(W_Product_Form)
        self.le_message.setObjectName(u"le_message")

        self.gridLayout.addWidget(self.le_message, 4, 0, 1, 2)

        self.gb = QGroupBox(W_Product_Form)
        self.gb.setObjectName(u"gb")
        self.gb.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.gb)
        self.formLayout.setObjectName(u"formLayout")
        self.lb_1 = QLabel(self.gb)
        self.lb_1.setObjectName(u"lb_1")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lb_1)

        self.le_1 = QLineEdit(self.gb)
        self.le_1.setObjectName(u"le_1")
        self.le_1.setEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_1)

        self.lb_2 = QLabel(self.gb)
        self.lb_2.setObjectName(u"lb_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lb_2)

        self.lb_price = QLabel(self.gb)
        self.lb_price.setObjectName(u"lb_price")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lb_price)

        self.sb_price = QDoubleSpinBox(self.gb)
        self.sb_price.setObjectName(u"sb_price")
        self.sb_price.setMinimum(0.010000000000000)
        self.sb_price.setMaximum(999999999999999.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.sb_price)

        self.sb_quantity = QSpinBox(self.gb)
        self.sb_quantity.setObjectName(u"sb_quantity")
        self.sb_quantity.setMaximum(999999999)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sb_quantity)


        self.gridLayout.addWidget(self.gb, 1, 0, 1, 2)

        QWidget.setTabOrder(self.le_1, self.sb_quantity)
        QWidget.setTabOrder(self.sb_quantity, self.sb_price)
        QWidget.setTabOrder(self.sb_price, self.pb_ok)
        QWidget.setTabOrder(self.pb_ok, self.pb_cancel)

        self.retranslateUi(W_Product_Form)

        QMetaObject.connectSlotsByName(W_Product_Form)
    # setupUi

    def retranslateUi(self, W_Product_Form):
        W_Product_Form.setWindowTitle(QCoreApplication.translate("W_Product_Form", u"Form", None))
        self.pb_cancel.setText(QCoreApplication.translate("W_Product_Form", u"Cancel", None))
        self.pb_ok.setText(QCoreApplication.translate("W_Product_Form", u"Ok", None))
        self.le_message.setText("")
        self.gb.setTitle(QCoreApplication.translate("W_Product_Form", u"PlaceHolder", None))
        self.lb_1.setText(QCoreApplication.translate("W_Product_Form", u"Name", None))
        self.lb_2.setText(QCoreApplication.translate("W_Product_Form", u"Quantity", None))
        self.lb_price.setText(QCoreApplication.translate("W_Product_Form", u"Price", None))
    # retranslateUi

