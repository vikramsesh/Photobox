# PhotoBox fixture

The program helps users control the capture images and removes the guesswork of the camera settings for specific food loads used. It was designed to keep the camera settings and the file naming metrics consistent across multiple fixtures. It also removes the tedious process of sharing the images with multiple users by sending the image to the user's email address once the image is captured. This software was created to aid personel with minimum technical knowledge about programming or camera operations.

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
$sudo apt-get install gphoto2
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

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
$sudo apt-get install --reinstall pcmanfm
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Authors

* **[Vikram Seshadri](https://github.com/vikramsesh) **  

## License

python-gphoto2 - Python interface to libgphoto2
https://github.com/vikramsesh/Photobox
Copyright (C) 2019  Vikram Seshadri

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.

## Acknowledgments

* [jim-easterbrook](https://github.com/jim-easterbrook/python-gphoto2) - best examples on gphoto2
* Raspberry Pi community
* Python community
* Co-workers
