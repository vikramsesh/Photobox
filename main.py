#!/usr/bin/env python3

"""

Camera controls
Vikram Seshadri
September 24, 2019

v3 Edit: November 08, 2019
Live view integrated into the GUI

Update: November 25, 2019
Adding Error Pop-up screen

Update: December 4,2019
Fixed Other screen pop up and Live view close

Update: January 8,2020
Added Photo Grid in LiveView for Centering Objects

Update: January 27,2020
Filename check and fixed LiveView crashing issue

"""

import logging
import os
import re
import subprocess
import time

import gphoto2 as gp
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
# GUI
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

# variables
flag = 0
foodflag = 0
filename = ""
pic_dir = ""
name_dir = ""
new_dir = ""
bashCommand = """gphoto2 --capture-movie --stdout> fifo.mjpg & omxplayer -o hdmi --win "840 525 1680 1050" --alpha 230 fifo.mjpg & python /home/pi/Desktop/Photobox/liveview.py"""

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        self.do_init = QtCore.QEvent.registerEventType()
        QtWidgets.QMainWindow.__init__(self)
        super(MainWindow, self).__init__()
        uiFiles = os.path.join(parent_dir, "uiFiles")
        mainUI = os.path.join(uiFiles, "cameracontrols.ui")
        self.ui = uic.loadUi(mainUI, self)
        self.move(0, 40)

        # defer full initialisation (slow operation) until gui is visible
        self.camera = gp.Camera()
        QtWidgets.QApplication.postEvent(
            self, QtCore.QEvent(self.do_init), Qt.LowEventPriority - 1)

        # Quit button and shortcut
        quit_action = QtWidgets.QAction('Quit', self)
        quit_action.setShortcuts(['Ctrl+Q', 'Ctrl+W'])
        quit_action.triggered.connect(QtWidgets.qApp.closeAllWindows)
        self.addAction(quit_action)
        self.pushButton_quit.clicked.connect(QtWidgets.qApp.closeAllWindows)

        # Toggle Other lineEdit based on foodload
        self.ui.comboBox_foodload.activated[str].connect(self.other_food)

        # Connect to Camera button - Checks if camera is connected
        self.pushButton_camerastatus.clicked.connect(self.camera_summary)

        # Live View
        self.pushButton_liveView.clicked.connect(self.live_view)

        # Capture button
        self.pushButton_capture.clicked.connect(self.initialise)

    def image_settings(self):

        # adjust camera configuratiuon
        cfg = self.camera.get_config()

        # Artist
        artist_cfg = cfg.get_child_by_name('artist')
        artist_cfg.set_value(self.name)

        # Copyright
        copyright_cfg = cfg.get_child_by_name('copyright')
        copyright_cfg.set_value('NinjaTestTeam')

        # capure target - Internal Ram or Memory card
        capturetarget_cfg = cfg.get_child_by_name('capturetarget')
        capturetarget_cfg.set_value('Internal Ram')

        # camera dependent - 'imageformat' is 'imagequality' on some
        imageformat_cfg = cfg.get_child_by_name('imageformat')
        imageformat_cfg.set_value('Large Normal JPEG')  # 6000x4000

        # whitebalance
        whitebalance_cfg = cfg.get_child_by_name('whitebalance')
        whitebalance_cfg.set_value('Daylight')

        # meteringmode
        metering_cfg = cfg.get_child_by_name('meteringmode')
        metering_cfg.set_value('Center-weighted average')

        # drive mode
        drive_cfg = cfg.get_child_by_name('drivemode')
        drive_cfg.set_value('Single')

        # colorspace
        colorspace_cfg = cfg.get_child_by_name('colorspace')
        colorspace_cfg.set_value('sRGB')

        # focusmode
        focusmode_cfg = cfg.get_child_by_name('focusmode')
        focusmode_cfg.set_value('AI Focus')

        # Canon Auto Exposure mode
        autoexposure_cfg = cfg.get_child_by_name('autoexposuremode')
        autoexposure_cfg.set_value('Manual')

        # Shutterspeed
        shutter_cfg = cfg.get_child_by_name('shutterspeed')

        # aperture
        aperture_cfg = cfg.get_child_by_name('aperture')

        # iso
        iso_cfg = cfg.get_child_by_name('iso')

        # Set values
        iso_cfg.set_value('100')
        aperture_cfg.set_value('4.5')
        shutter_cfg.set_value('1/40')

        self.camera.set_config(cfg)

    def camera_capture(self):
        global filename, pic_dir, name_dir, new_dir
        self.camera = gp.Camera()
        new_message = ""

        try:
            self.camera.init()
            logging.info("Camera initialized")

            # Camera parameters
            self.image_settings()
            logging.info("Camera parameters set")

            # Checking if duplicate image exists
            i = 1
            new_dir = os.path.join(pic_dir, filename + "_" + str(i) + '.jpg')
            while os.path.exists(new_dir):
                i += 1
                new_dir = os.path.join(pic_dir, filename + "_" + str(i) + '.jpg')

            path = self.camera.capture(gp.GP_CAPTURE_IMAGE)
            camera_file = self.camera.file_get(
                path.folder, path.name, gp.GP_FILE_TYPE_NORMAL)

            # Save Image
            camera_file.save(new_dir)

            # free camera
            self.camera.exit()

            if os.path.exists(new_dir):
                self.textEdit_message.setText(
                    str(new_message) + "Picture Captured and Stored in‣ \n" + pic_dir)

                # Display Image
                img = mpimg.imread(new_dir)
                plt.imshow(img)
                plt.show()

                QMessageBox.information(
                    None,
                    "Capture successful",
                    str(new_message) +
                    "Picture Captured and Stored in‣ \n" +
                    pic_dir)


            else:
                self.textEdit_message.setText("Image not Captured")
                logging.error("Image not captured")
                QMessageBox.critical(
                    None,
                    "Image not captured",
                    "Image not Captured‣\n➊Turn off the camera and turn it back on.\n➋Check USB cable")

        except BaseException:
            self.textEdit_message.setText(
                "➊Check if camera is powered on.\n➋Remove lens cover.\n➌Turn off the camera and turn it back on.\n"
                "➍Replace Battery.\n➎Place an object in front of the camera.\n❻Free up storage.")
            QMessageBox.critical(
                None,
                "Lens Error",
                "➊Check if camera is powered on.\n➋Remove lens cover.\n➌Turn off the camera and turn it back on.\n"
                "➍Replace Battery.\n➎Place an object in front of the camera.\n❻Free up storage.")

        filename = ""

    def initialise(self):
        global flag, foodflag
        self.gui_setup()
        if flag == 0 and foodflag == 0:
            self.camera_capture()
            flag = 1

    def gui_setup(self):
        global flag, foodflag, filename, pic_dir, name_dir

        filename = ""
        flag = 0
        foodflag = 0
        messageString = ""

        # User input data
        # name*
        self.name = str(self.ui.lineEdit_name.text())

        if self.name == "" or self.name.lower() == "your name here":
            messageString = "Enter Name\n"
            flag = 1

        else:
            flag = 0

        self.name = re.sub(r"([^\w])", "", self.name)

        foodcount = 0

        # food load
        self.foodload = str(self.ui.comboBox_foodload.currentText())

        if self.foodload == "Other":

            # Other*
            self.foodload = str(self.ui.lineEdit_other.text())
            if self.foodload.lower() == "other in food load dropdown" or self.foodload.lower() == "":
                messageString += "Enter a Valid Food load\n"
                foodflag = 1

            if foodflag == 0:
                for i in range(0, len(self.comboBox_foodload)):
                    if self.ui.comboBox_foodload.itemText(
                            i).lower() == self.foodload.lower():
                        foodcount += 1

                if foodcount >= 1:
                    messageString += "Food load already present"
                    foodflag = 1

                elif foodcount == 0:
                    self.foodload = str(self.ui.lineEdit_other.text())
                    foodflag = 0

        # sku
        self.sku = str(self.ui.lineEdit_sku.text())

        # software
        self.software = str(self.ui.lineEdit_software.text())

        # build
        self.build = str(self.ui.lineEdit_build.text())

        # other
        self.filenameextra = str(self.ui.lineEdit_FilenameExtra.text())

        if not messageString == "":
            self.textEdit_message.setText(messageString)
            QMessageBox.critical(None, "*Important info", messageString)

        if flag == 0 and foodflag == 0:
            name_dir = os.path.join(data_dir, str(self.name))
            if not os.path.exists(name_dir):
                os.makedirs(name_dir)

            pic_dir = os.path.join(name_dir, str(self.foodload) + " " + str(time.strftime("%m.%d.%Y")))
            if not os.path.exists(pic_dir):
                os.makedirs(pic_dir)

            filename += str(self.name)

            if not self.sku == "":
                filename += "_" + str(self.sku)
            if not self.build == "":
                filename += "_" + str(self.build)
            if not self.software == "":
                filename += "_" + str(self.software)
            if not self.filenameextra == "":
                filename += "_" + str(self.filenameextra)

            filename += "_" + str(time.strftime("%m.%d.%Y"))
            filename = re.sub(r"([^\w])", "_", filename)

    def other_food(self):
        if str(self.ui.comboBox_foodload.currentText()) == "Other":
            self.label_other.setEnabled(True)
            self.lineEdit_other.setEnabled(True)
        else:
            self.label_other.setEnabled(False)
            self.lineEdit_other.setEnabled(False)

    def live_view(self):
        global bashCommand, process
        makefile = """ mkfifo fifo.mjpg """
        fifofile_dir = os.path.join(os.path.abspath(os.curdir), "fifo.mjpg")
        print (fifofile_dir)

        try:
            self.textEdit_message.setText(
                "If LiveView is not visible:\n‣Check if camera is powered on.\n‣Unplug and replug the Camera USB.")
            if not os.path.exists(fifofile_dir):
                time.sleep(1)
                process1 = subprocess.Popen(
                    makefile,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    close_fds=False)

            process = subprocess.Popen(
                bashCommand,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                close_fds=False)
            try:
                output, error = process.communicate()
                logging.info('liveView output:{}, error:{}'.format(output, error))
            except BaseException:
                logging.exception("Exception occurred", exc_info=True)
                self.textEdit_message.setText(
                    "‣Check Camera Connection.\n➊Close the application.\n➋Unplug and re plug the camera USB cable.")
                QMessageBox.critical(
                    None,
                    "LiveView Error",
                    "‣Check Camera Connection.\n➊Close the application.\n➋Unplug and re plug the camera USB cable.")

        except BaseException:
            logging.exception("Exception occurred", exc_info=True)
            self.textEdit_message.setText(
                "‣Check Camera Connection.\n➊Close the application.\n➋Unplug and re plug the camera USB cable.")
            QMessageBox.critical(
                None,
                "LiveView Error",
                "‣Check Camera Connection.\n➊Close the application.\n➋Unplug and re plug the camera USB cable.")

    def camera_summary(self):
        self.camera = gp.Camera()
        try:
            self.camera.init()

            # Battery percentage
            batterycfg = self.camera.get_config()
            text = self.camera.get_summary()
            self.textEdit_message.setText(
                "Camera connected successfully\n‣Click Away")

            # battery level
            battery_cfg = batterycfg.get_child_by_name('batterylevel')
            battery = battery_cfg.get_value()

            try:
                battery = int(battery.replace('%', ''))
            except BaseException:
                if battery == "Low":
                    battery = 0

            if int(battery) == 0:
                self.textEdit_message.setText("Recharge the Battery")
                QMessageBox.warning(
                    None, "Battery info", "Recharge the Battery")

            self.progressBar_battery.setProperty("value", int(battery))

            print('Camera Summary')
            print('=============')
            print(str(text))
            self.textEdit_camstatus.setText(str(""))
            self.textEdit_camstatus.setText(
                "Camera Summary\n==============\n" + str(text))

            # enable functions
            self.enable_toggle(True)
            self.camera.exit()

        except BaseException:
            self.textEdit_camstatus.setText("‣Could not detect any camera")
            logging.error("Could not detect camera")
            self.textEdit_message.setText(
                "No Camera detected - Check the following:\n➊Camera is ON.\n➋Battery is present and charged.\n"
                "➌USB is connected.")
            QMessageBox.warning(
                None,
                "No Camera detected",
                "Check the following:\n➊Camera is ON.\n➋Battery is present and charged.\n➌USB is connected.")
            self.progressBar_battery.setProperty("value", 0)

            # disable functions
            self.enable_toggle(False)
            self.label_other.setEnabled(False)
            self.lineEdit_other.setEnabled(False)

    def enable_toggle(self, toggle_status):
        # ComboBox
        self.comboBox_foodload.setEnabled(toggle_status)

        # Progress Bar
        self.progressBar_battery.setEnabled(toggle_status)

        # Push Button
        self.pushButton_liveView.setEnabled(toggle_status)
        self.pushButton_capture.setEnabled(toggle_status)

        # Labels
        self.label_name.setEnabled(toggle_status)
        self.label_foodload.setEnabled(toggle_status)
        self.label_sku.setEnabled(toggle_status)
        self.label_software.setEnabled(toggle_status)
        self.label_build.setEnabled(toggle_status)
        self.label_FilenameExtra.setEnabled(toggle_status)
        self.label_battery.setEnabled(toggle_status)
        self.label_capture.setEnabled(toggle_status)

        # Line Edits
        self.lineEdit_name.setEnabled(toggle_status)
        self.lineEdit_sku.setEnabled(toggle_status)
        self.lineEdit_software.setEnabled(toggle_status)
        self.lineEdit_build.setEnabled(toggle_status)
        self.lineEdit_FilenameExtra.setEnabled(toggle_status)


if __name__ == "__main__":
    import sys

    if (sys.flags.interactive != 1):
        parent_dir = os.path.dirname(__file__)  # Current directory
        data_dir = os.path.join(os.path.abspath(os.curdir), "Pictures")  # Pictures folder
        log_dir = os.path.join(os.path.abspath(os.curdir), "Logs")  # Log files folder

        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Logging
        log_file = os.path.join(log_dir, "log" + str(time.strftime("-%m-%d-%Y--%I-%M-%S %p")) + ".log")

        logging.basicConfig(filename=log_file, filemode='w', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        logging.getLogger().addHandler(logging.StreamHandler())

        callback_obj = gp.check_result(gp.use_python_logging())
        app = QtWidgets.QApplication(sys.argv)
        app.processEvents()
        app.setStyle('gtk2')
        program = MainWindow()
        program.show()
        app.exec_()
