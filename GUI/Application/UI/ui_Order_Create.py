# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Order_Create.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTableView, QVBoxLayout, QWidget)

class Ui_Create_Order_Form(object):
    def setupUi(self, Create_Order_Form):
        if not Create_Order_Form.objectName():
            Create_Order_Form.setObjectName(u"Create_Order_Form")
        Create_Order_Form.resize(756, 527)
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        Create_Order_Form.setFont(font)
        Create_Order_Form.setWindowTitle(u"Create Order")
        self.verticalLayout = QVBoxLayout(Create_Order_Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Create_Order_Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_name = QLineEdit(Create_Order_Form)
        self.le_name.setObjectName(u"le_name")

        self.horizontalLayout_2.addWidget(self.le_name)

        self.label_3 = QLabel(Create_Order_Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.le_address = QLineEdit(Create_Order_Form)
        self.le_address.setObjectName(u"le_address")

        self.horizontalLayout_2.addWidget(self.le_address)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tv_product = QTableView(Create_Order_Form)
        self.tv_product.setObjectName(u"tv_product")

        self.horizontalLayout.addWidget(self.tv_product)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.p_add = QPushButton(Create_Order_Form)
        self.p_add.setObjectName(u"p_add")
        self.p_add.setEnabled(False)

        self.verticalLayout_2.addWidget(self.p_add)

        self.pb_remove = QPushButton(Create_Order_Form)
        self.pb_remove.setObjectName(u"pb_remove")
        self.pb_remove.setEnabled(False)

        self.verticalLayout_2.addWidget(self.pb_remove)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Create_Order_Form)
        self.label.setObjectName(u"label")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label.setIndent(-1)

        self.horizontalLayout_3.addWidget(self.label)

        self.sb_quantity = QSpinBox(Create_Order_Form)
        self.sb_quantity.setObjectName(u"sb_quantity")
        self.sb_quantity.setMaximum(999999999)

        self.horizontalLayout_3.addWidget(self.sb_quantity)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.tv_orderproducts = QTableView(Create_Order_Form)
        self.tv_orderproducts.setObjectName(u"tv_orderproducts")

        self.horizontalLayout.addWidget(self.tv_orderproducts)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pb_ok = QPushButton(Create_Order_Form)
        self.pb_ok.setObjectName(u"pb_ok")

        self.horizontalLayout_4.addWidget(self.pb_ok)

        self.pb_cancel = QPushButton(Create_Order_Form)
        self.pb_cancel.setObjectName(u"pb_cancel")

        self.horizontalLayout_4.addWidget(self.pb_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        QWidget.setTabOrder(self.le_name, self.le_address)
        QWidget.setTabOrder(self.le_address, self.tv_product)
        QWidget.setTabOrder(self.tv_product, self.tv_orderproducts)
        QWidget.setTabOrder(self.tv_orderproducts, self.p_add)
        QWidget.setTabOrder(self.p_add, self.pb_remove)
        QWidget.setTabOrder(self.pb_remove, self.sb_quantity)
        QWidget.setTabOrder(self.sb_quantity, self.pb_ok)
        QWidget.setTabOrder(self.pb_ok, self.pb_cancel)

        self.retranslateUi(Create_Order_Form)

        QMetaObject.connectSlotsByName(Create_Order_Form)
    # setupUi

    def retranslateUi(self, Create_Order_Form):
#if QT_CONFIG(tooltip)
        Create_Order_Form.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Create_Order_Form", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("Create_Order_Form", u"Address", None))
        self.p_add.setText(QCoreApplication.translate("Create_Order_Form", u"Add", None))
        self.pb_remove.setText(QCoreApplication.translate("Create_Order_Form", u"Remove", None))
        self.label.setText(QCoreApplication.translate("Create_Order_Form", u"Quantity", None))
        self.pb_ok.setText(QCoreApplication.translate("Create_Order_Form", u"Ok", None))
        self.pb_cancel.setText(QCoreApplication.translate("Create_Order_Form", u"Cancel", None))
    # retranslateUi

