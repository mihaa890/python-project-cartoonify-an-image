# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cartoonify_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 908)
        MainWindow.setMinimumSize(QtCore.QSize(844, 0))
        MainWindow.setStyleSheet("background-color:#fff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setMaximumSize(QtCore.QSize(16777215, 80))
        self.logo.setStyleSheet("background-color:#fff;")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("resources/logo.png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo)
        self.browse_box = QtWidgets.QGroupBox(self.centralwidget)
        self.browse_box.setMinimumSize(QtCore.QSize(0, 65))
        self.browse_box.setMaximumSize(QtCore.QSize(16777215, 65))
        self.browse_box.setStyleSheet("background-color:#fff;")
        self.browse_box.setObjectName("browse_box")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.browse_box)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.file_input_field = QtWidgets.QLineEdit(self.browse_box)
        self.file_input_field.setObjectName("file_input_field")
        self.horizontalLayout_2.addWidget(self.file_input_field)
        self.browse_button = QtWidgets.QPushButton(self.browse_box)
        self.browse_button.setMinimumSize(QtCore.QSize(0, 20))
        self.browse_button.setMaximumSize(QtCore.QSize(80, 30))
        self.browse_button.setStyleSheet("background-color: #0078d7;\n"
"border : 0;\n"
"color : #fff;\n"
"font-weight : bold;\n"
"width : 70px;\n"
"height  : 70px;\n"
"border-radius:5px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.browse_button.setObjectName("browse_button")
        self.horizontalLayout_2.addWidget(self.browse_button)
        self.verticalLayout.addWidget(self.browse_box)
        self.build_parameters_box = QtWidgets.QGroupBox(self.centralwidget)
        self.build_parameters_box.setMinimumSize(QtCore.QSize(0, 230))
        self.build_parameters_box.setMaximumSize(QtCore.QSize(16777215, 200))
        self.build_parameters_box.setStyleSheet("background-color:#fff;")
        self.build_parameters_box.setObjectName("build_parameters_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.build_parameters_box)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.threshold_parameters_box = QtWidgets.QGroupBox(self.build_parameters_box)
        self.threshold_parameters_box.setMinimumSize(QtCore.QSize(200, 85))
        self.threshold_parameters_box.setStyleSheet("padding : 0;")
        self.threshold_parameters_box.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.threshold_parameters_box.setObjectName("threshold_parameters_box")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.threshold_parameters_box)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.threshold_adaptive_method_widget = QtWidgets.QWidget(self.threshold_parameters_box)
        self.threshold_adaptive_method_widget.setMinimumSize(QtCore.QSize(100, 60))
        self.threshold_adaptive_method_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.threshold_adaptive_method_widget.setStyleSheet("padding : 0;")
        self.threshold_adaptive_method_widget.setObjectName("threshold_adaptive_method_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.threshold_adaptive_method_widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.threshold_adaptive_method_label = QtWidgets.QLabel(self.threshold_adaptive_method_widget)
        self.threshold_adaptive_method_label.setObjectName("threshold_adaptive_method_label")
        self.verticalLayout_5.addWidget(self.threshold_adaptive_method_label)
        self.threshold_adaptive_method_dropdown = QtWidgets.QComboBox(self.threshold_adaptive_method_widget)
        self.threshold_adaptive_method_dropdown.setMinimumSize(QtCore.QSize(0, 20))
        self.threshold_adaptive_method_dropdown.setObjectName("threshold_adaptive_method_dropdown")
        self.verticalLayout_5.addWidget(self.threshold_adaptive_method_dropdown)
        self.horizontalLayout_5.addWidget(self.threshold_adaptive_method_widget)
        self.threshold_type_widget = QtWidgets.QWidget(self.threshold_parameters_box)
        self.threshold_type_widget.setMinimumSize(QtCore.QSize(100, 60))
        self.threshold_type_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.threshold_type_widget.setObjectName("threshold_type_widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.threshold_type_widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.threshold_type_label = QtWidgets.QLabel(self.threshold_type_widget)
        self.threshold_type_label.setMinimumSize(QtCore.QSize(0, 0))
        self.threshold_type_label.setLineWidth(1)
        self.threshold_type_label.setIndent(-1)
        self.threshold_type_label.setObjectName("threshold_type_label")
        self.verticalLayout_6.addWidget(self.threshold_type_label)
        self.threshold_type_dropdown = QtWidgets.QComboBox(self.threshold_type_widget)
        self.threshold_type_dropdown.setMinimumSize(QtCore.QSize(0, 20))
        self.threshold_type_dropdown.setObjectName("threshold_type_dropdown")
        self.verticalLayout_6.addWidget(self.threshold_type_dropdown)
        self.horizontalLayout_5.addWidget(self.threshold_type_widget)
        self.threshold_max_size_widget = QtWidgets.QWidget(self.threshold_parameters_box)
        self.threshold_max_size_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.threshold_max_size_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.threshold_max_size_widget.setStyleSheet("")
        self.threshold_max_size_widget.setObjectName("threshold_max_size_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.threshold_max_size_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.threshold_block_size_label = QtWidgets.QLabel(self.threshold_max_size_widget)
        self.threshold_block_size_label.setObjectName("threshold_block_size_label")
        self.verticalLayout_3.addWidget(self.threshold_block_size_label)
        self.threshold_block_size_slider = QtWidgets.QSlider(self.threshold_max_size_widget)
        self.threshold_block_size_slider.setMinimumSize(QtCore.QSize(0, 20))
        self.threshold_block_size_slider.setStyleSheet("")
        self.threshold_block_size_slider.setMinimum(1)
        self.threshold_block_size_slider.setMaximum(7)
        self.threshold_block_size_slider.setSingleStep(1)
        self.threshold_block_size_slider.setPageStep(10)
        self.threshold_block_size_slider.setProperty("value", 1)
        self.threshold_block_size_slider.setOrientation(QtCore.Qt.Horizontal)
        self.threshold_block_size_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.threshold_block_size_slider.setTickInterval(1)
        self.threshold_block_size_slider.setObjectName("threshold_block_size_slider")
        self.verticalLayout_3.addWidget(self.threshold_block_size_slider)
        self.horizontalLayout_5.addWidget(self.threshold_max_size_widget)
        self.threshold_distance_widget = QtWidgets.QWidget(self.threshold_parameters_box)
        self.threshold_distance_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.threshold_distance_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.threshold_distance_widget.setObjectName("threshold_distance_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.threshold_distance_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.threshold_distance_label_ = QtWidgets.QLabel(self.threshold_distance_widget)
        self.threshold_distance_label_.setObjectName("threshold_distance_label_")
        self.verticalLayout_4.addWidget(self.threshold_distance_label_)
        self.threshold_distance_slider = QtWidgets.QSlider(self.threshold_distance_widget)
        self.threshold_distance_slider.setMinimumSize(QtCore.QSize(0, 20))
        self.threshold_distance_slider.setMinimum(1)
        self.threshold_distance_slider.setMaximum(15)
        self.threshold_distance_slider.setProperty("value", 9)
        self.threshold_distance_slider.setOrientation(QtCore.Qt.Horizontal)
        self.threshold_distance_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.threshold_distance_slider.setTickInterval(1)
        self.threshold_distance_slider.setObjectName("threshold_distance_slider")
        self.verticalLayout_4.addWidget(self.threshold_distance_slider)
        self.horizontalLayout_5.addWidget(self.threshold_distance_widget)
        self.verticalLayout_2.addWidget(self.threshold_parameters_box)
        self.bilateral_filter_box = QtWidgets.QGroupBox(self.build_parameters_box)
        self.bilateral_filter_box.setMinimumSize(QtCore.QSize(0, 0))
        self.bilateral_filter_box.setObjectName("bilateral_filter_box")
        self.gridLayout = QtWidgets.QGridLayout(self.bilateral_filter_box)
        self.gridLayout.setObjectName("gridLayout")
        self.bilateral_filter_sigma_color_widget = QtWidgets.QWidget(self.bilateral_filter_box)
        self.bilateral_filter_sigma_color_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.bilateral_filter_sigma_color_widget.setObjectName("bilateral_filter_sigma_color_widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.bilateral_filter_sigma_color_widget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.bilateral_filter_sigma_color_label = QtWidgets.QLabel(self.bilateral_filter_sigma_color_widget)
        self.bilateral_filter_sigma_color_label.setMinimumSize(QtCore.QSize(0, 20))
        self.bilateral_filter_sigma_color_label.setObjectName("bilateral_filter_sigma_color_label")
        self.verticalLayout_9.addWidget(self.bilateral_filter_sigma_color_label)
        self.bilateral_filter_sigma_color_slider = QtWidgets.QSlider(self.bilateral_filter_sigma_color_widget)
        self.bilateral_filter_sigma_color_slider.setMinimumSize(QtCore.QSize(0, 20))
        self.bilateral_filter_sigma_color_slider.setMinimum(1)
        self.bilateral_filter_sigma_color_slider.setMaximum(255)
        self.bilateral_filter_sigma_color_slider.setProperty("value", 250)
        self.bilateral_filter_sigma_color_slider.setOrientation(QtCore.Qt.Horizontal)
        self.bilateral_filter_sigma_color_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.bilateral_filter_sigma_color_slider.setTickInterval(5)
        self.bilateral_filter_sigma_color_slider.setObjectName("bilateral_filter_sigma_color_slider")
        self.verticalLayout_9.addWidget(self.bilateral_filter_sigma_color_slider)
        self.gridLayout.addWidget(self.bilateral_filter_sigma_color_widget, 0, 2, 1, 1)
        self.bilateral_filter_distance_widget = QtWidgets.QWidget(self.bilateral_filter_box)
        self.bilateral_filter_distance_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.bilateral_filter_distance_widget.setObjectName("bilateral_filter_distance_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.bilateral_filter_distance_widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.bilateral_filter_distance_label = QtWidgets.QLabel(self.bilateral_filter_distance_widget)
        self.bilateral_filter_distance_label.setMinimumSize(QtCore.QSize(0, 20))
        self.bilateral_filter_distance_label.setObjectName("bilateral_filter_distance_label")
        self.gridLayout_2.addWidget(self.bilateral_filter_distance_label, 0, 0, 1, 1)
        self.bilateral_filter_distance_slider = QtWidgets.QSlider(self.bilateral_filter_distance_widget)
        self.bilateral_filter_distance_slider.setMinimumSize(QtCore.QSize(0, 20))
        self.bilateral_filter_distance_slider.setMinimum(1)
        self.bilateral_filter_distance_slider.setMaximum(15)
        self.bilateral_filter_distance_slider.setProperty("value", 9)
        self.bilateral_filter_distance_slider.setOrientation(QtCore.Qt.Horizontal)
        self.bilateral_filter_distance_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.bilateral_filter_distance_slider.setTickInterval(1)
        self.bilateral_filter_distance_slider.setObjectName("bilateral_filter_distance_slider")
        self.gridLayout_2.addWidget(self.bilateral_filter_distance_slider, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.bilateral_filter_distance_widget, 0, 0, 1, 1)
        self.bilateral_filter_sigma_space_widget = QtWidgets.QWidget(self.bilateral_filter_box)
        self.bilateral_filter_sigma_space_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.bilateral_filter_sigma_space_widget.setObjectName("bilateral_filter_sigma_space_widget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.bilateral_filter_sigma_space_widget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.bilateral_filter_sigma_space_label = QtWidgets.QLabel(self.bilateral_filter_sigma_space_widget)
        self.bilateral_filter_sigma_space_label.setMinimumSize(QtCore.QSize(0, 20))
        self.bilateral_filter_sigma_space_label.setObjectName("bilateral_filter_sigma_space_label")
        self.verticalLayout_10.addWidget(self.bilateral_filter_sigma_space_label)
        self.bilateral_filter_sigma_space_slider = QtWidgets.QSlider(self.bilateral_filter_sigma_space_widget)
        self.bilateral_filter_sigma_space_slider.setMinimumSize(QtCore.QSize(0, 20))
        self.bilateral_filter_sigma_space_slider.setToolTipDuration(-1)
        self.bilateral_filter_sigma_space_slider.setMinimum(1)
        self.bilateral_filter_sigma_space_slider.setMaximum(255)
        self.bilateral_filter_sigma_space_slider.setProperty("value", 250)
        self.bilateral_filter_sigma_space_slider.setOrientation(QtCore.Qt.Horizontal)
        self.bilateral_filter_sigma_space_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.bilateral_filter_sigma_space_slider.setTickInterval(5)
        self.bilateral_filter_sigma_space_slider.setObjectName("bilateral_filter_sigma_space_slider")
        self.verticalLayout_10.addWidget(self.bilateral_filter_sigma_space_slider)
        self.gridLayout.addWidget(self.bilateral_filter_sigma_space_widget, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.bilateral_filter_box)
        self.verticalLayout.addWidget(self.build_parameters_box)
        self.result_box = QtWidgets.QGroupBox(self.centralwidget)
        self.result_box.setMinimumSize(QtCore.QSize(0, 400))
        self.result_box.setMaximumSize(QtCore.QSize(16777215, 450))
        self.result_box.setStyleSheet("background-color:#fff;")
        self.result_box.setObjectName("result_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.result_box)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.before_box = QtWidgets.QGroupBox(self.result_box)
        self.before_box.setMaximumSize(QtCore.QSize(16777215, 400))
        self.before_box.setObjectName("before_box")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.before_box)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.before_img = QtWidgets.QLabel(self.before_box)
        self.before_img.setText("")
        self.before_img.setPixmap(QtGui.QPixmap("resources/no_preview.jpg"))
        self.before_img.setScaledContents(True)
        self.before_img.setObjectName("before_img")
        self.horizontalLayout_3.addWidget(self.before_img)
        self.horizontalLayout.addWidget(self.before_box)
        self.after_box = QtWidgets.QGroupBox(self.result_box)
        self.after_box.setMaximumSize(QtCore.QSize(16777215, 400))
        self.after_box.setObjectName("after_box")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.after_box)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.after_img = QtWidgets.QLabel(self.after_box)
        self.after_img.setText("")
        self.after_img.setPixmap(QtGui.QPixmap("resources/no_preview.jpg"))
        self.after_img.setScaledContents(True)
        self.after_img.setObjectName("after_img")
        self.horizontalLayout_4.addWidget(self.after_img)
        self.horizontalLayout.addWidget(self.after_box)
        self.verticalLayout.addWidget(self.result_box)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setStyleSheet("padding: 0;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.download_button = QtWidgets.QPushButton(self.frame)
        self.download_button.setMinimumSize(QtCore.QSize(0, 20))
        self.download_button.setMaximumSize(QtCore.QSize(80, 30))
        self.download_button.setStyleSheet("QPushButton {\n"
"background-color: #0078d7;\n"
"border : 0;\n"
"color : #fff;\n"
"font-weight : bold;\n"
"width : 70px;\n"
"height  : 70px;\n"
"border-radius:5px;\n"
"margin : 0;\n"
"}\n"
"QPushButton:disabled{\n"
"background-color:#d0d0d0;\n"
"}\n"
"")
        self.download_button.setObjectName("download_button")
        self.horizontalLayout_6.addWidget(self.download_button)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cartoonify"))
        self.browse_box.setTitle(_translate("MainWindow", "Browse"))
        self.browse_button.setText(_translate("MainWindow", "Browse"))
        self.build_parameters_box.setTitle(_translate("MainWindow", "Build Parameters"))
        self.threshold_parameters_box.setTitle(_translate("MainWindow", "Adaptive Threshold"))
        self.threshold_adaptive_method_label.setText(_translate("MainWindow", "Adaptive Method"))
        self.threshold_type_label.setText(_translate("MainWindow", "Threshold type"))
        self.threshold_block_size_label.setText(_translate("MainWindow", "BlockSize: 3"))
        self.threshold_distance_label_.setText(_translate("MainWindow", "Distance: 9"))
        self.bilateral_filter_box.setTitle(_translate("MainWindow", "Bilateral Filter"))
        self.bilateral_filter_sigma_color_label.setText(_translate("MainWindow", "Sigma Color"))
        self.bilateral_filter_distance_label.setText(_translate("MainWindow", "Distance"))
        self.bilateral_filter_sigma_space_label.setText(_translate("MainWindow", "Sigma Space"))
        self.result_box.setTitle(_translate("MainWindow", "Result"))
        self.before_box.setTitle(_translate("MainWindow", "Before"))
        self.after_box.setTitle(_translate("MainWindow", "After"))
        self.download_button.setText(_translate("MainWindow", "Download"))
