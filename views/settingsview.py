import flet as ft
import toml
from source.tools import updateTOML

class SettingsView:
    def __init__(self) -> None:
        self.audioPath = ft.Text(value=r'C:\Users\Cliente\Documents\MediaCatcher\Audio', size=15)
        self.videoPath = ft.Text(value=r'C:\Users\Cliente\Documents\MediaCatcher\Video', size=15)
        self.optionalPath = ft.Text(value=r'C:\Users\Cliente\Documents\MediaCatcher', size=15)
        
    def getAudioDir(self, e: ft.FilePickerResultEvent):
        self.audioPath.value = e.path if e.path else r'C:\Users\Cliente\Documents\MediaCatcher\Audio'
        self.audioPath.update()
        updateTOML(e, 'audio', 'default', 'path')

    def getVideoDir(self, e: ft.FilePickerResultEvent):
        self.videoPath.value = e.path if e.path else r'C:\Users\Cliente\Documents\MediaCatcher\Video'
        self.videoPath.update()
        updateTOML(e, 'video', 'default', 'path')

    def getOptionalDir(self, e: ft.FilePickerResultEvent):
        self.optionalPath.value = e.path if e.path else r'C:\Users\Cliente\Documents\MediaCatcher'
        self.optionalPath.update()
        updateTOML(e, 'optional', 'default', 'path')

    def returnView(self, audioDirDialog, videoDirDialog, optionalDirDialog):
        return ft.Column(
        [
        ft.Text(value="Pasta dos Áudios:"),
        ft.Row(
            [
            ft.IconButton(icon=ft.icons.AUDIO_FILE_ROUNDED, icon_size=30, on_click= lambda _:audioDirDialog.get_directory_path(initial_directory=r'C:\Users\Cliente\Documents\MediaCatcher\Audio')),
            self.audioPath,
            ]
        ),
        ft.Text(value="Pasta dos Vídeos:"),
        ft.Row(
            [
            ft.IconButton(icon=ft.icons.VIDEO_FILE_ROUNDED, icon_size=30, on_click= lambda _:videoDirDialog.get_directory_path(initial_directory=r'C:\Users\Cliente\Documents\MediaCatcher\Audio')),
            self.videoPath,
            ]
        ),
        ft.Text(value="Pasta do ffmpeg:"),
        ft.Text(value="Necessário para algumas opções para download, como salvar o áudio com imagem de capa e alguns outros metadados. Visite https://www.ffmpeg.org/download.html", size=10, selectable=True),
        ft.Row(
            [
            ft.IconButton(icon=ft.icons.INSERT_DRIVE_FILE_ROUNDED, icon_size=30, on_click= lambda _:optionalDirDialog.get_directory_path(initial_directory=r'C:\Users\Cliente\Documents\MediaCatcher')),
            self.optionalPath,
            ]
        ),
        ]
    )
