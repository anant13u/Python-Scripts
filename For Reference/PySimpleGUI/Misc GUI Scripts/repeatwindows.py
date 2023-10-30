import PySimpleGUI as psg
import time

psg.theme('darkamber')

def show_window():
    psg.Window(title='Hi AU, This is a GUI Program!',layout=[[psg.Text('Inside Text\n2nd Line')]],margins=(150,100)).read()
    time.sleep(3)

show_window()
show_window()