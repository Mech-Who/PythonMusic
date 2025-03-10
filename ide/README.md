# musicpy_editor
This is an easy-to-use musicpy editor and IDE.

## Installation
Firstly,  make sure you have installed python (version >= 3.7) in your computer first.

Secondly, download the PyQt5-sip wheel from this site: https://pypi.tuna.tsinghua.edu.cn/simple/pyqt5-sip/ (choose the version which matches your python version and system, for example, your python is 3.7.9 32bit, your system is Windows 10, then download "PyQt5_sip-12.12.2-cp37-cp37m-win32.whl")

Thirdly, put the wheel file in a location, then use `pip install PyQt5_sip-12.12.2-cp37-cp37m-win32.whl` to install PyQt5-sip.

Then run this line in cmd/terminal:
```
pip install musicpy pyglet==1.5.11 yapf PyQt5==5.15.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

**Note: In Linux, you need to install freepats in order to make the play function works, in Ubuntu, you can run `sudo apt-get install freepats`, and you also need to make sure the installed version of pygame is older than 2.0.3 on Linux in order to make the play function works, you can run `pip install pygame==2.0.2` to install pygame 2.0.2 or any version that is older than 2.0.3.**

Then download the source codes from [here](https://github.com/Rainbow-Dreamer/musicpy_editor/archive/refs/heads/main.zip), extract the folder `musicpy editor` from the zip file, go to the `musicpy editor` folder, open the file `musicpy editor.pyw` to use musicpy editor. You can change language by change `language` parameter in the settings, currently supported languages are json files in `languages` folder, you can make your own language's json file and change to your language.

For more details including abilities and usages of this musicpy editor, see the [documentation](https://github.com/Rainbow-Dreamer/musicpy/wiki/Useful-functionality#i-wrote-an-ide-specifically-for-musicpy-for-everyone-to-use) here.



## Previews

![image](previews/1.jpg)

