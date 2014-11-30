pixelsort.py
============

Pixel sorting experiments written in Python (2.7)

## Dependencies
I would highly recommend creating a virtualenv and installing the following depenencies on that
* [NumPy](http://www.numpy.org/): Install NumPy through Pip with
```
pip install numpy
```
* [OpenCV](http://opencv.org/): There are different methods for installing OpenCV. If you're on OSX use Homebrew to install:
```
brew tap homebrew/science
brew install opencv

```
Then link the Python files
```
ln -s /usr/local/Cellar/opencv/2.4.9/lib/python2.7/site-packages/cv.py cv.py
ln -s /usr/local/Cellar/opencv/2.4.9/lib/python2.7/site-packages/cv2.so cv2.so
```
Make sure to change the symlink above if you're linking OpenCV to a virtualenv!
