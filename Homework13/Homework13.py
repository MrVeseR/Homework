import os
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *


class MainApplication(QtWidgets.QMainWindow, "Homework13\TextEditor.ui"):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.directory = os.getcwd()
        self.data = None



def main():
  app = QtWidgets.QApplication(sys.argv)
  window = MainApplication()
  window.show()
  app.exec()


if __name__ == '__main__':
  main()