# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/actualizar_insertar.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(305, 424)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Iconos/Icons/fatcow/Principal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineTitulo = QtWidgets.QLineEdit(Dialog)
        self.lineTitulo.setObjectName("lineTitulo")
        self.gridLayout.addWidget(self.lineTitulo, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BoxTemporada = QtWidgets.QComboBox(Dialog)
        self.BoxTemporada.setObjectName("BoxTemporada")
        self.horizontalLayout_2.addWidget(self.BoxTemporada)
        self.lineTemp = QtWidgets.QLineEdit(Dialog)
        self.lineTemp.setEnabled(True)
        self.lineTemp.setObjectName("lineTemp")
        self.horizontalLayout_2.addWidget(self.lineTemp, 0, QtCore.Qt.AlignLeft)
        spacerItem = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BoxCapitulo = QtWidgets.QComboBox(Dialog)
        self.BoxCapitulo.setObjectName("BoxCapitulo")
        self.horizontalLayout.addWidget(self.BoxCapitulo)
        self.lineCapitulo = QtWidgets.QLineEdit(Dialog)
        self.lineCapitulo.setEnabled(True)
        self.lineCapitulo.setObjectName("lineCapitulo")
        self.horizontalLayout.addWidget(self.lineCapitulo, 0, QtCore.Qt.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.widget_5 = QtWidgets.QWidget(Dialog)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.radioSeguirSi = QtWidgets.QRadioButton(self.widget_5)
        self.radioSeguirSi.setChecked(True)
        self.radioSeguirSi.setObjectName("radioSeguirSi")
        self.gridLayout_4.addWidget(self.radioSeguirSi, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 2, 1, 1)
        self.radioSeguirNo = QtWidgets.QRadioButton(self.widget_5)
        self.radioSeguirNo.setObjectName("radioSeguirNo")
        self.gridLayout_4.addWidget(self.radioSeguirNo, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.widget_5, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.BoxEmision = QtWidgets.QComboBox(Dialog)
        self.BoxEmision.setObjectName("BoxEmision")
        self.BoxEmision.addItem("")
        self.BoxEmision.addItem("")
        self.BoxEmision.addItem("")
        self.BoxEmision.addItem("")
        self.BoxEmision.addItem("")
        self.BoxEmision.addItem("")
        self.BoxEmision.addItem("")
        self.BoxEmision.addItem("")
        self.gridLayout.addWidget(self.BoxEmision, 4, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioVOSE_Si = QtWidgets.QRadioButton(self.widget_3)
        self.radioVOSE_Si.setChecked(False)
        self.radioVOSE_Si.setObjectName("radioVOSE_Si")
        self.gridLayout_2.addWidget(self.radioVOSE_Si, 0, 0, 1, 1)
        self.radioVOSE_No = QtWidgets.QRadioButton(self.widget_3)
        self.radioVOSE_No.setChecked(True)
        self.radioVOSE_No.setObjectName("radioVOSE_No")
        self.gridLayout_2.addWidget(self.radioVOSE_No, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.widget_3, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioAcabadaSi = QtWidgets.QRadioButton(self.widget_2)
        self.radioAcabadaSi.setObjectName("radioAcabadaSi")
        self.gridLayout_3.addWidget(self.radioAcabadaSi, 0, 0, 1, 1)
        self.radioAcabadaNo = QtWidgets.QRadioButton(self.widget_2)
        self.radioAcabadaNo.setChecked(True)
        self.radioAcabadaNo.setObjectName("radioAcabadaNo")
        self.gridLayout_3.addWidget(self.radioAcabadaNo, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 6, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BoxEstado = QtWidgets.QComboBox(self.widget)
        self.BoxEstado.setObjectName("BoxEstado")
        self.horizontalLayout_3.addWidget(self.BoxEstado)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.gridLayout.addWidget(self.widget, 7, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.lineImdb = QtWidgets.QLineEdit(Dialog)
        self.lineImdb.setObjectName("lineImdb")
        self.gridLayout.addWidget(self.lineImdb, 8, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(Dialog)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radioImdbNo = QtWidgets.QRadioButton(self.widget_4)
        self.radioImdbNo.setObjectName("radioImdbNo")
        self.gridLayout_5.addWidget(self.radioImdbNo, 0, 2, 1, 1)
        self.radioImdbSi = QtWidgets.QRadioButton(self.widget_4)
        self.radioImdbSi.setChecked(True)
        self.radioImdbSi.setObjectName("radioImdbSi")
        self.gridLayout_5.addWidget(self.radioImdbSi, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.widget_4, 9, 1, 1, 1)
        self.WidgetBotones = QtWidgets.QWidget(Dialog)
        self.WidgetBotones.setObjectName("WidgetBotones")
        self.LayoutBotones = QtWidgets.QHBoxLayout(self.WidgetBotones)
        self.LayoutBotones.setContentsMargins(0, 0, 0, 0)
        self.LayoutBotones.setObjectName("LayoutBotones")
        self.label_Info = QtWidgets.QLabel(self.WidgetBotones)
        self.label_Info.setText("")
        self.label_Info.setObjectName("label_Info")
        self.LayoutBotones.addWidget(self.label_Info)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LayoutBotones.addItem(spacerItem7)
        self.pushButtonAplicar = QtWidgets.QPushButton(self.WidgetBotones)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Iconos/Icons/fatcow/accept_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAplicar.setIcon(icon1)
        self.pushButtonAplicar.setObjectName("pushButtonAplicar")
        self.LayoutBotones.addWidget(self.pushButtonAplicar)
        self.pushButtonCerrar = QtWidgets.QPushButton(self.WidgetBotones)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Iconos/Icons/fatcow/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCerrar.setIcon(icon2)
        self.pushButtonCerrar.setObjectName("pushButtonCerrar")
        self.LayoutBotones.addWidget(self.pushButtonCerrar)
        self.pushButtonAceptar = QtWidgets.QPushButton(self.WidgetBotones)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Iconos/Icons/fatcow/file_save_as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAceptar.setIcon(icon3)
        self.pushButtonAceptar.setObjectName("pushButtonAceptar")
        self.LayoutBotones.addWidget(self.pushButtonAceptar)
        self.gridLayout.addWidget(self.WidgetBotones, 10, 0, 1, 2)
        self.widget_2.raise_()
        self.widget_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.widget_5.raise_()
        self.lineTitulo.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineImdb.raise_()
        self.label_8.raise_()
        self.BoxEmision.raise_()
        self.label_9.raise_()
        self.widget_4.raise_()
        self.label_10.raise_()
        self.widget.raise_()
        self.label.setBuddy(self.lineTitulo)
        self.label_6.setBuddy(self.radioSeguirSi)
        self.label_3.setBuddy(self.BoxEmision)
        self.label_8.setBuddy(self.lineImdb)

        self.retranslateUi(Dialog)
        self.BoxTemporada.activated['QString'].connect(self.lineTemp.setText)
        self.BoxCapitulo.activated['QString'].connect(self.lineCapitulo.setText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Titulo"))
        self.label_5.setText(_translate("Dialog", "Temporada"))
        self.label_2.setText(_translate("Dialog", "Capitulo"))
        self.label_6.setText(_translate("Dialog", "Siguiendo"))
        self.radioSeguirSi.setText(_translate("Dialog", "Si"))
        self.radioSeguirNo.setText(_translate("Dialog", "No"))
        self.label_3.setText(_translate("Dialog", "Dia de Emision"))
        self.BoxEmision.setItemText(0, _translate("Dialog", "None"))
        self.BoxEmision.setItemText(1, _translate("Dialog", "Lunes"))
        self.BoxEmision.setItemText(2, _translate("Dialog", "Martes"))
        self.BoxEmision.setItemText(3, _translate("Dialog", "Miercoles"))
        self.BoxEmision.setItemText(4, _translate("Dialog", "Jueves"))
        self.BoxEmision.setItemText(5, _translate("Dialog", "Viernes"))
        self.BoxEmision.setItemText(6, _translate("Dialog", "Sabado"))
        self.BoxEmision.setItemText(7, _translate("Dialog", "Domingo"))
        self.label_4.setText(_translate("Dialog", "V.O.S.E."))
        self.radioVOSE_Si.setText(_translate("Dialog", "Si"))
        self.radioVOSE_No.setText(_translate("Dialog", "No"))
        self.label_7.setText(_translate("Dialog", "Acabada"))
        self.radioAcabadaSi.setText(_translate("Dialog", "Si"))
        self.radioAcabadaNo.setText(_translate("Dialog", "No"))
        self.label_10.setText(_translate("Dialog", "Estado"))
        self.label_8.setText(_translate("Dialog", "Id Idmd"))
        self.label_9.setText(_translate("Dialog", "lanzar imdb"))
        self.radioImdbNo.setText(_translate("Dialog", "No"))
        self.radioImdbSi.setText(_translate("Dialog", "Si"))
        self.pushButtonAplicar.setText(_translate("Dialog", "Aplicar"))
        self.pushButtonCerrar.setText(_translate("Dialog", "Cerrar"))
        self.pushButtonAceptar.setText(_translate("Dialog", "Aceptar"))


import app.views.ui.fatcow_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
