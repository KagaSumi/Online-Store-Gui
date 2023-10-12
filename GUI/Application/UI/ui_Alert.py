# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Alert.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Alert(object):
    def setupUi(self, Alert):
        if not Alert.objectName():
            Alert.setObjectName(u"Alert")
        Alert.resize(373, 365)
        self.verticalLayout_2 = QVBoxLayout(Alert)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Alert)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_ok = QPushButton(Alert)
        self.pb_ok.setObjectName(u"pb_ok")

        self.horizontalLayout.addWidget(self.pb_ok)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Alert)

        QMetaObject.connectSlotsByName(Alert)
    # setupUi

    def retranslateUi(self, Alert):
        Alert.setWindowTitle(QCoreApplication.translate("Alert", u"Alert!!", None))
        self.label.setText(QCoreApplication.translate("Alert", u"Label", None))
        self.pb_ok.setText(QCoreApplication.translate("Alert", u"Ok", None))
    # retranslateUi

