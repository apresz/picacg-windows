# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gameinfo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .qtlistwidget import QtBookList


class Ui_GameInfo(object):
    def setupUi(self, GameInfo):
        if not GameInfo.objectName():
            GameInfo.setObjectName(u"GameInfo")
        GameInfo.resize(900, 963)
        self.gridLayout_2 = QGridLayout(GameInfo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(GameInfo)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.picture = QLabel(self.page)
        self.picture.setObjectName(u"picture")
        self.picture.setMinimumSize(QSize(320, 320))

        self.horizontalLayout.addWidget(self.picture)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 16777215))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_3.addWidget(self.label)

        self.title = QLabel(self.page)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_3.addWidget(self.title)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon_1 = QLabel(self.page)
        self.icon_1.setObjectName(u"icon_1")
        self.icon_1.setEnabled(True)
        self.icon_1.setMaximumSize(QSize(60, 60))

        self.horizontalLayout_4.addWidget(self.icon_1)

        self.icon_2 = QLabel(self.page)
        self.icon_2.setObjectName(u"icon_2")
        self.icon_2.setMinimumSize(QSize(60, 60))
        self.icon_2.setMaximumSize(QSize(60, 60))

        self.horizontalLayout_4.addWidget(self.icon_2)

        self.icon_3 = QLabel(self.page)
        self.icon_3.setObjectName(u"icon_3")
        self.icon_3.setMinimumSize(QSize(60, 60))
        self.icon_3.setMaximumSize(QSize(60, 60))

        self.horizontalLayout_4.addWidget(self.icon_3)

        self.icon_4 = QLabel(self.page)
        self.icon_4.setObjectName(u"icon_4")
        self.icon_4.setMinimumSize(QSize(60, 60))
        self.icon_4.setMaximumSize(QSize(60, 60))

        self.horizontalLayout_4.addWidget(self.icon_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(40, 16777215))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.description = QLabel(self.page)
        self.description.setObjectName(u"description")
        self.description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_5.addWidget(self.description)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.updateTick = QLabel(self.page)
        self.updateTick.setObjectName(u"updateTick")
        self.updateTick.setEnabled(True)
        self.updateTick.setMinimumSize(QSize(80, 40))
        self.updateTick.setMaximumSize(QSize(80, 40))

        self.horizontalLayout_2.addWidget(self.updateTick)

        self.androidButton = QPushButton(self.page)
        self.androidButton.setObjectName(u"androidButton")
        self.androidButton.setMinimumSize(QSize(0, 40))
        self.androidButton.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_2.addWidget(self.androidButton)

        self.iosButton = QPushButton(self.page)
        self.iosButton.setObjectName(u"iosButton")
        self.iosButton.setMinimumSize(QSize(0, 40))
        self.iosButton.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_2.addWidget(self.iosButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.tabWidget = QTabWidget(self.page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget:pane {border-top:0px solid #e8f3f9;background:  transparent; }")
        self.epsWidget = QWidget()
        self.epsWidget.setObjectName(u"epsWidget")
        self.epsLayout = QGridLayout(self.epsWidget)
        self.epsLayout.setObjectName(u"epsLayout")
        self.epsListWidget = QListWidget(self.epsWidget)
        self.epsListWidget.setObjectName(u"epsListWidget")
        self.epsListWidget.setStyleSheet(u"QListWidget {background-color:transparent;}\n"
"")
        self.epsListWidget.setTextElideMode(Qt.ElideRight)
        self.epsListWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.epsListWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.epsListWidget.setSpacing(6)

        self.epsLayout.addWidget(self.epsListWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.epsWidget, "")
        self.commentWidget = QWidget()
        self.commentWidget.setObjectName(u"commentWidget")
        self.commentLayout = QGridLayout(self.commentWidget)
        self.commentLayout.setObjectName(u"commentLayout")
        self.listWidget = QtBookList(self.commentWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"QListWidget {background-color:transparent;}\n"
"QListWidget::item { border-bottom: 1px solid black; }")

        self.commentLayout.addWidget(self.listWidget, 0, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.commentLine = QLineEdit(self.commentWidget)
        self.commentLine.setObjectName(u"commentLine")
        self.commentLine.setStyleSheet(u"background-color:transparent;")

        self.horizontalLayout_10.addWidget(self.commentLine)

        self.commentButton = QPushButton(self.commentWidget)
        self.commentButton.setObjectName(u"commentButton")

        self.horizontalLayout_10.addWidget(self.commentButton)


        self.commentLayout.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)

        self.tabWidget.addTab(self.commentWidget, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(GameInfo)
        self.iosButton.clicked.connect(GameInfo.CopyIos)
        self.androidButton.clicked.connect(GameInfo.CopyAndroid)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(GameInfo)
    # setupUi

    def retranslateUi(self, GameInfo):
        GameInfo.setWindowTitle(QCoreApplication.translate("GameInfo", u"Form", None))
        self.picture.setText(QCoreApplication.translate("GameInfo", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("GameInfo", u"\u6807\u9898\uff1a", None))
        self.title.setText(QCoreApplication.translate("GameInfo", u"\u6807\u9898", None))
        self.icon_1.setText(QCoreApplication.translate("GameInfo", u"TextLabel", None))
        self.icon_2.setText(QCoreApplication.translate("GameInfo", u"TextLabel", None))
        self.icon_3.setText(QCoreApplication.translate("GameInfo", u"TextLabel", None))
        self.icon_4.setText(QCoreApplication.translate("GameInfo", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("GameInfo", u"\u63cf\u8ff0\uff1a", None))
        self.description.setText(QCoreApplication.translate("GameInfo", u"\u63cf\u8ff0", None))
        self.updateTick.setText(QCoreApplication.translate("GameInfo", u"TextLabel", None))
        self.androidButton.setText(QCoreApplication.translate("GameInfo", u"\u590d\u5236\u5b89\u5353\u4e0b\u8f7d\u5730\u5740", None))
        self.iosButton.setText(QCoreApplication.translate("GameInfo", u"\u590d\u5236IOS\u4e0b\u8f7d\u5730\u5740", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.epsWidget), QCoreApplication.translate("GameInfo", u"\u7ae0\u8282", None))
        self.commentButton.setText(QCoreApplication.translate("GameInfo", u"\u53d1\u9001\u8bc4\u8bba", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.commentWidget), QCoreApplication.translate("GameInfo", u"\u8bc4\u8bba", None))
    # retranslateUi

