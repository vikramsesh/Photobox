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
