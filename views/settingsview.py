import flet as ft

class SettingsView:
    def __init__(self) -> None:
        self.audioPath = ft.Text(value=r'C:\Users\Cliente\Documents\MediaCatcher\Audio', size=15)
        self.videoPath = ft.Text(value=r'C:\Users\Cliente\Documents\MediaCatcher\Video', size=15)
        #self.dirDialog = ft.FilePicker(on_result=self.getAudioDir)

    #def dirDialog(self):
    #    return ft.FilePicker(on_result=self.getAudioDir)
        
    def getAudioDir(self, e: ft.FilePickerResultEvent):
        self.audioPath.value = e.path if e.path else r'C:\Users\Cliente\Documents\MediaCatcher\Audio'
        self.audioPath.update()

    def getVideoDir(self, e: ft.FilePickerResultEvent):
        self.videoPath.value = e.path if e.path else r'C:\Users\Cliente\Documents\MediaCatcher\Video'
        self.videoPath.update()

    def returnView(self, audioDirDialog, videoDirDialog):
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
        )
        ]
    )
