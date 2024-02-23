import flet as ft
from os import mkdir
from os.path import exists
from app.mainWindow import MediaCatcher

if __name__ == "__main__":
    if not exists(r'C:\Users\Cliente\Documents\MediaCatcher'):
        mkdir(r'C:\Users\Cliente\Documents\MediaCatcher')
        mkdir(r'C:\Users\Cliente\Documents\MediaCatcher\Audio')
        mkdir(r'C:\Users\Cliente\Documents\MediaCatcher\Video')
        mkdir(r'C:\Users\Cliente\Documents\MediaCatcher\.cache')

    ft.app(target=MediaCatcher)