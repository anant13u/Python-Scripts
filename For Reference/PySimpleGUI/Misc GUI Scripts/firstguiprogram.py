import PySimpleGUI as psg
import time

# Changing the theme of the GUI.
psg.theme('darkamber')
# Creating a window with a title, a layout, and margins.
psg.Window(title='Hi AU, This is a GUI Program!',layout=[[psg.Text('Inside Text\n2nd Line')]],margins=(150,100)).read()


