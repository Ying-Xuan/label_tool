# from PyQt5 import QtWidgets
# from PyQt5.QtCore import Qt
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
# import cv2
from cv2 import imread, resize, INTER_AREA
from utils import all_filepaths, get_initial_idx, csv_to_jason
from pandas import read_csv, DataFrame

class MainWindow_controller(QMainWindow):
    def __init__(self):
        super(MainWindow_controller, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        self.img_label = 'invalid'

    def setup_control(self):
        # TODO
        self.ui.open_folder_buttom.clicked.connect(self.open_folder)
        self.ui.open_csv_buttom.clicked.connect(self.open_csv)
        self.ui.left_buttom.clicked.connect(self.left)
        self.ui.right_buttom.clicked.connect(self.right)
        self.ui.invalid_buttom.clicked.connect(self.invalid)
        # self.ui.sent_label_buttom.clicked.connect(self.sent_label)
        self.ui.last_buttom.clicked.connect(self.last_img)
        self.ui.next_buttom.clicked.connect(self.next_img)

    def open_csv(self):
        self.csv_path, filetype = QFileDialog.getOpenFileName(self, "Open file", "./") 
        df = read_csv(self.csv_path)
        self.paths = df.path.tolist()
        self.labels = df.label.tolist()
        # print(self.paths[-1])

    # def open_file(self):
    #     filename, filetype = QFileDialog.getOpenFileName(self, "Open file", "./")
    #     self.ui.img_path_label.setText(filename)
    #     self.display_img(filename)
    
    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Open file", "./")
        self.ui.img_path_label.setText(folder_path)
        
        self.img_paths = all_filepaths(folder_path)
        # print(self.img_paths[0])
        self.idx = get_initial_idx(self.img_paths, self.paths)+1
        self.display_img()

    def display_img(self):
        self.ui.img_path_label.setText(self.img_paths[self.idx])
        # print(self.img_paths[self.idx])
        self.img = imread(self.img_paths[self.idx])
        height, width, channel = self.img.shape
        height, width = int(height/5), int(width/5)
        self.img = resize(self.img, (width, height), interpolation=INTER_AREA)
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.ui.img_label.setPixmap(QPixmap.fromImage(self.qimg))

    def left(self):
        self.img_label = 'left'
    def right(self):
        self.img_label = 'right'
    def invalid(self):
        self.img_label = 'invalid'

    # def sent_label(self):
    #     self.paths.append(self.img_paths[self.idx])
    #     self.labels.append(self.img_label)
    #     df = DataFrame({'path':self.paths, 'label':self.labels})
    #     df.to_csv(self.csv_path)
    #     csv_to_jason(self.csv_path)

    def last_img(self):
        self.idx  = self.idx - 1 
        self.paths.pop()
        self.labels.pop()
        self.display_img()

    def next_img(self):
        print(self.img_paths[self.idx], self.img_label, sep='\t')
        self.paths.append(self.img_paths[self.idx])
        self.labels.append(self.img_label)
        df = DataFrame({'path':self.paths, 'label':self.labels})
        df.to_csv(self.csv_path)
        csv_to_jason(self.csv_path)

        self.idx  = self.idx + 1 
        if self.idx < len(self.img_paths):
            self.display_img()
        else:
            self.ui.img_label.setText('End!')
            self.ui.img_path_label.setText('Empty')

    # def keyPressEvent(self, event):
    #     key = event.key()

    #     if key == Qt.Key_Left:  # left
    #         self.left()
    #     elif key == Qt.Key_Right:  # right
    #         self.right()
    #     elif key == Qt.Key_Space:  # space
    #         self.invalid()
    #     elif key == Qt.Key_down:  # down
    #         self.next_img()
    #     elif key == Qt.Key_Up:  #up
    #         self.last_img()
