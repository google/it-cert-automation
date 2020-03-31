#!/usr/bin/env python3
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# This application displays a purplebox.
# It has a bug: it fails if the config directory doesn't exist.
# But it fails silently, without telling the user why it crashed.

# To run this, you need to install:
#   python3-pyside2.qtwidgets
#   python3-pyside2.qtgui
#   qt5-style-plugins

import os
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget


class PurpleBox(QMainWindow):

    def __init__(self):
        self.read_config()
        QMainWindow.__init__(self)
        self.setGeometry(0, 0, 640, 480)
        self.createMenus()
        self.widget = QWidget(self)
        self.setStyleSheet(
            """
QWidget { background-color: MediumPurple; }
QMenuBar { background: SlateBlue; }
""")
        self.setCentralWidget(self.widget)
        self.centralWidget().setObjectName("centralwidget")
        self.setAutoFillBackground = True

    def read_config(self):
        config_dir = os.path.expanduser('~/.config/purplebox')
        # TODO: process the config files
        try:
            config_files = []
            for filename in os.listdir(config_dir):
                if filename.endswith('.conf') and os.path.isfile(filename):
                    config_files.append(filename)
        except Exception:
            sys.exit(1)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.helpMenu = self.menuBar().addMenu("&Help")


if __name__ == "__main__":
    app = QApplication([])
    window = PurpleBox()
    window.show()
    sys.exit(app.exec_())
