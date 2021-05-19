from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import QtGui, QtCore
import gui
import sys
import cv2
from debounce import debounce
from constants import Constants


class GUI(QMainWindow, gui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.movie = QMovie("resources/loading.gif")
        self.timer = QTimer()
        self.setupUi(self)
        self.constants = Constants()

        self.final_image = None
        self.current_path = None
        self.current_threshold_adaptive_method = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
        self.current_threshold_type = cv2.THRESH_BINARY
        self.current_threshold_block_size = 3
        self.current_threshold_distance = 9
        self.current_bilateral_filter_distance = 9
        self.current_sigma_color = 250
        self.current_sigma_space = 250

        self.buildDropdowns()
        self.buildSliders()
        self.browse_button.clicked.connect(self.browse)
        self.download_button.clicked.connect(self.download)

        if (self.current_path is None):
            self.build_parameters_box.setEnabled(False)
            self.result_box.setEnabled(False)
            self.download_button.setEnabled(False)


    def buildDropdowns(self):
        self.threshold_adaptive_method_dropdown.clear()
        self.threshold_type_dropdown.clear()

        self.threshold_adaptive_method_dropdown.addItems(self.constants.THRESHOLD_ADAPTIVE_METHODS._all())
        self.threshold_adaptive_method_dropdown.activated[str].connect(
            lambda value: self.on_dropdown_change(self.constants.DROPDOWN_TYPES.ADAPTIVE_METHOD, value))

        self.threshold_type_dropdown.addItems(self.constants.THRESHOLD_TYPES._all())
        self.threshold_type_dropdown.activated[str].connect(
            lambda value: self.on_dropdown_change(self.constants.DROPDOWN_TYPES.THRESHOLD_TYPE, value))

    def buildSliders(self):
        self.threshold_block_size_slider.valueChanged.connect(
            lambda value: self.on_slider_change(self.constants.SLIDERS_TYPES.THRESHOLD_BLOCK_SIZE_SLIDER, value))

        self.threshold_distance_slider.valueChanged.connect(
            lambda value: self.on_slider_change(self.constants.SLIDERS_TYPES.THRESHOLD_DISTANCE_SLIDER, value))

        self.bilateral_filter_distance_slider.valueChanged.connect(
            lambda value: self.on_slider_change(self.constants.SLIDERS_TYPES.BILATERAL_FILTER_DISTANCE_SLIDER, value))

        self.bilateral_filter_sigma_color_slider.valueChanged.connect(
            lambda value: self.on_slider_change(self.constants.SLIDERS_TYPES.BILATERAL_FILTER_SIGMA_COLOR_SLIDER,
                                                value))

        self.bilateral_filter_sigma_space_slider.valueChanged.connect(
            lambda value: self.on_slider_change(self.constants.SLIDERS_TYPES.BILATERAL_FILTER_SIGMA_SPACE_SLIDER,
                                                value))

    def on_dropdown_change(self, dropdown_type, value):
        if dropdown_type == self.constants.DROPDOWN_TYPES.ADAPTIVE_METHOD:
            if value == self.constants.THRESHOLD_ADAPTIVE_METHODS.ADAPTIVE_THRESH_GAUSSIAN_C:
                self.current_threshold_adaptive_method = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
            elif value == self.constants.THRESHOLD_ADAPTIVE_METHODS.ADAPTIVE_THRESH_MEAN_C:
                self.current_threshold_adaptive_method = cv2.ADAPTIVE_THRESH_MEAN_C
        elif dropdown_type == self.constants.DROPDOWN_TYPES.THRESHOLD_TYPE:
            if value == self.constants.THRESHOLD_TYPES.THRESH_BINARY:
                self.current_threshold_type = cv2.THRESH_BINARY
            elif value == self.constants.THRESHOLD_TYPES.THRESH_BINARY_INV:
                self.current_threshold_type = cv2.THRESH_BINARY_INV

        self.debouncedProcess()

    def on_slider_change(self, slider_type, value):
        self.after_img.setMovie(self.movie)
        timer = QTimer()
        self.startAnimation()
        timer.singleShot(1000, self.processCv2Image)
        if slider_type == self.constants.SLIDERS_TYPES.THRESHOLD_BLOCK_SIZE_SLIDER:
            actual_value = (value*2) + 1
            self.threshold_block_size_label.setText('BlockSize: {}'.format(actual_value))
            self.current_threshold_block_size = actual_value
        elif slider_type == self.constants.SLIDERS_TYPES.THRESHOLD_DISTANCE_SLIDER:
            self.threshold_distance_label_.setText('Distance: {}'.format(value))
            self.current_threshold_distance = value
        elif slider_type == self.constants.SLIDERS_TYPES.BILATERAL_FILTER_DISTANCE_SLIDER:
            self.current_bilateral_filter_distance = value
        elif slider_type == self.constants.SLIDERS_TYPES.BILATERAL_FILTER_SIGMA_COLOR_SLIDER:
            self.current_sigma_color = value
        elif slider_type == self.constants.SLIDERS_TYPES.BILATERAL_FILTER_SIGMA_SPACE_SLIDER:
            self.current_sigma_space = value

        self.debouncedProcess()

    def browse(self):
        qFileDialog = QFileDialog()
        filter = "Images (*.png *.jpg)"
        file_names = QFileDialog.getOpenFileName(qFileDialog, "Select an image", None, filter)
        self.current_path = file_names[0]

        if (self.current_path):
            self.file_input_field.setText(self.current_path)
            self.before_img.setPixmap(
                QtGui.QPixmap(self.file_input_field.text()).scaled(511, 431, QtCore.Qt.AspectRatioMode.KeepAspectRatio))
            self.processCv2Image()
            self.build_parameters_box.setEnabled(True)
            self.result_box.setEnabled(True)
            self.download_button.setEnabled(True)
        else:
            print('Please select an image...')

    def download(self):
        filter = "Images (*.png *.jpg)"
        name = QFileDialog.getSaveFileName(self, 'Save File',None, filter)
        path = name[0]
        cv2.imwrite(path, cv2.cvtColor(self.final_image, cv2.COLOR_RGB2BGR))

    @debounce(0.35)
    def debouncedProcess(self):
        self.processCv2Image()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()

    def processCv2Image(self):
        cv2_image = cv2.imread(self.current_path)
        cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)

        print(
            self.current_threshold_block_size,
            self.current_threshold_distance,
            self.current_bilateral_filter_distance,
            self.current_sigma_color,
            self.current_sigma_space)

        gray = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
        edged = cv2.adaptiveThreshold(
            gray,
            255,
            self.current_threshold_adaptive_method,
            self.current_threshold_type,
            self.current_threshold_block_size,
            self.current_threshold_distance
        )

        color = cv2.bilateralFilter(
            cv2_image,
            self.current_bilateral_filter_distance,
            self.current_sigma_color,
            self.current_sigma_space)

        self.final_image = cv2.bitwise_and(color, color, mask=edged)

        height, width, channel = self.final_image.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(self.final_image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)

        self.after_img.setPixmap(
            QtGui.QPixmap.fromImage(qImg).scaled(511, 431, QtCore.Qt.AspectRatioMode.KeepAspectRatio))


def main():
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    app.exec_()


if __name__ == '__main__':
    main()
