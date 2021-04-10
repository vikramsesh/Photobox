# PhotoBox fixture

The program helps users control the capture images and removes the guesswork of the camera settings for specific food loads used. It was designed to keep the camera settings and the file naming metrics consistent across multiple fixtures. This project was designed to aid personel with minimum technical knowledge about programming or camera operations.

[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

## Logo
<img src="https://github.com/vikramsesh/Photobox/blob/master/Photobox%20Logo.png" width="300" height="300">

### Built With

* [PyQt](https://riverbankcomputing.com/software/pyqt/intro)
* [Python](https://www.python.org/)

<!-- GETTING STARTED -->
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
* [matplotlib](https://matplotlib.org) - To view images

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

* Matplotlib
```
$ pip install matplotlib
```

Update and Upgrade the libraries
```
$sudo apt-get update
$sudo apt-get upgrade
```

### Installation

Copy the uiFiles folder to the location you want to run the program from.
Depending on the features you need, copy v1,v2 or v3 to the same folder.
For v3, also copy liveview.py to the same folder.

```
chmod +x main.py
```

## Tests

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
$chmod +x main.py
```
You are all set to enjoy the program. CLICK AWAY!

## What to do if you have a problem

If you find a problem in the UI or with any dependencies or general bug reports, then please report it on the GitHub "issues" page (https://github.com/vikramsesh/Photobox/issues)

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE`](https://github.com/vikramsesh/Photobox/blob/master/LICENSE.txt) for more information.

<!-- CONTACT -->
## Contact

[Vikram Seshadri](https://www.linkedin.com/in/vikramseshadri/)
Project Link: [https://github.com/vikramsesh/Photobox](https://github.com/vikramsesh/Photobox)

## Acknowledgments

* [jim-easterbrook](https://github.com/jim-easterbrook/python-gphoto2) - best examples on gphoto2
* Raspberry Pi community
* Python community
* Co-workers
* [Img Shields](https://shields.io)
* [Microsoft PowerToys](https://github.com/microsoft/PowerToys)
* [Choose an Open Source License](https://choosealicense.com)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/vikramsesh/Serial-output-data-parser?color=%230093FF
[contributors-url]: https://github.com/vikramsesh/Serial-output-data-parser/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/vikramsesh/Photobox
[forks-url]: https://github.com/vikramsesh/Photobox/network/members
[issues-shield]: https://img.shields.io/github/issues/vikramsesh/Serial-output-data-parser
[issues-url]: https://github.com/vikramsesh/Photobox/issues
[license-shield]: https://img.shields.io/github/license/vikramsesh/Serial-output-data-parser
[license-url]: https://github.com/vikramsesh/Photobox/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/vikramseshadri/
