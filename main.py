from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import sys
import os 
import cv2
import random
import numpy as np
import main_ui
from image import ImageHandler
import logging 
from logging import debug as log


class MainWindow(QMainWindow,main_ui.Ui_MainWindow):

    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.openVideoAction.triggered.connect(self.openVideo)
        self.openImageAction.triggered.connect(self.openImageFolder)
        self.actionNext.triggered.connect(self.next)
        self.actionNext.setDisabled(True)
        self.fname = None
        self.Images = None
        log('Application started')

    def openVideo(self):
        self.fname,_ = QFileDialog.getOpenFileName(self, "Open file", "", "Video Files (*.avi);All files (*.*)")

        pass

    def next(self):
        if self.Images is not None:
            self.setCurrentImage(self.Images.next_img())
    
    def setCurrentImage(self,image):
        pixmap = QtGui.QPixmap.fromImage(image)
        self.ImLabel.setPixmap(pixmap)

    def openImageFolder(self):
        dirname = QFileDialog.getExistingDirectory(self, "Select Directory")
        
        fnames = [os.path.join(dirname,name) for name in os.listdir(dirname) if name.endswith('.jpg') or name.endswith('.png')]
        self.Images = ImageHandler(fnames)
        
        self.setCurrentImage(self.Images.getCurrent())
        self.actionNext.setDisabled(False)
        
        

if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1]=='-d':
        logging.basicConfig(level=logging.DEBUG)
        log(sys.argv)

    app = QApplication(sys.argv)
    app.setApplicationName("T200")

    window = MainWindow()
    window.show()
    app.exec_()
    