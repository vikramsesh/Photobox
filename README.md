# PhotoBox fixture

The program helps users control the capture images and removes the guesswork of the camera settings for specific food loads used. It was designed to keep the camera settings and the file naming metrics consistent across multiple fixtures. It also removes the tedious process of sharing the images with multiple users by sending the image to the user's email address once the image is captured. This software was created to aid personel with minimum technical knowledge about programming or camera operations.

## Logo
<img src="https://github.com/vikramsesh/Photobox/blob/master/Photobox%20Logo.png" width="300" height="300">

## Getting Started

```
$sudo apt-get update
$sudo apt-get upgrade
```
Check python version using the following command in the terminal
```
$python --version
```
If version is not python3 or above, follow instructions on [Python3 default](https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux) to change default python to Python3 if its not already version 3.

### Prerequisites

What things you need to install the software and how to install them

* [Python 3 or greater](https://www.python.org/) - Python 3 installation if it's not already present
* [gPhoto2 & libgphoto2](http://www.gphoto.org/) - Library used to control the camera parameters and retrieve image from the DSLR
* [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5) - GUI for the python script
* [omxplayer](https://github.com/popcornmix/omxplayer) - Camera LiveView

A small library that aims at hiding the various difficulties of dlopening libraries from programmers. It is a system independent dlopen wrapper for GNU libtool.
```
$sudo apt-get install libltdl-dev
```

* gphoto2 - Download gphoto latest version from [gphoto2](http://gphoto.org/)
Extract the .tar file in Downloads
```
$cd <extracted file location>
$./configure
$make
$sudo make install
```
```
$cd
$sudo apt-get install gphoto2
$pip install gphoto2
```
* qt5 and QtCreator
```
$sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
$sudo apt-get install qtcreator
```
* Omxplayer python wrapper
```
$ pip install omxplayer-wrapper
```
* validate_email and py3DNS module
```
$pip install validate_email
$pip install py3DNS
```

Update and Upgrade the libraries
```
$sudo apt-get update
$sudo apt-get upgrade
```

### Installing

* cameraui_v1.py - Basic software for capturing an image and storing it. 
* cameraui_v2.py - Email addition for Image capture and email feature.
* cameraui_v3.py - LiveView addition to preview the image before capture.

Copy the uiFiles folder to the location you want to run the program from.
Depending on the features you need, copy v1,v2 or v3 to the same folder.
For v3, also copy liveview.py to the same folder.

```
chmod +x cameraui_v<x>.py
```

## Running the tests

Testing gphoto2 and camera interaction
```
$gphoto2 --auto-detect
$gphoto2 --capture-image-and-download
```
Testing Live View - Setting resolution using --win. Ctrl+c or q to quit omxplayer
```
$mkfifo fifo.mjpg
$gphoto2 --capture-movie --stdout> fifo.mjpg & omxplayer -o hdmi --win "0 0 820 525" fifo.mjpg
```

## Deployment

* Make sure all the prerequisites are installed. 
* Python3 should be the default.
* Make the script executable
Open the terminal Ctrl+Alt+T and follow the steps listed below
```
$cd <folder to execute scripts from> (eg.$cd /home/pi/Desktop)
$chmod +x cameraui_v<x>.py
```
You are all set to enjoy the program. CLICK AWAY!

## What to do if you have a problem

If you find a problem in the UI or with any dependencies or general bug reports, then please report it on the GitHub "issues" page (https://github.com/vikramsesh/Photobox/issues)

## Authors

**[Vikram Seshadri](https://github.com/vikramsesh)**

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE v3 - see the [LICENSE.txt](https://github.com/vikramsesh/Photobox/blob/master/LICENSE.txt) file for details

## Acknowledgments

* [jim-easterbrook](https://github.com/jim-easterbrook/python-gphoto2) - best examples on gphoto2
* Raspberry Pi community
* Python community
* Co-workers
