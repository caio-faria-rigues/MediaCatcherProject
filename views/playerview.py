import flet as ft
from source.tools import pallete
from os import listdir


class PlayerView:
    def __init__(self) -> None:
        self.dirDialog = None
        self.filePath = ft.Text(value=r'C:\Users\Cliente\Documents\MediaCatcher\Audio', size=15)
        self.fileWidget = ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            spacing=20,
            height=300,
            width=765
        )

        for i in range(0, len(listdir(self.filePath.value))):
            self.fileWidget.controls.append(ft.Text(value=listdir(self.filePath.value)[i]))    


        self.currentTime = ft.Text("00:00")
        self.endTime = ft.Text("00:00")
        self.musicSlider = ft.Slider(
            width=500,
            min=0,
            max=100,
            divisions=100,
            label="{value}",
            active_color=pallete[0],
        )

        self.playButton = ft.IconButton(icon=ft.icons.PLAY_ARROW_ROUNDED, icon_size=50, on_click=self.playClickEvent)
        self.previousButton = ft.IconButton(icon=ft.icons.SKIP_PREVIOUS_ROUNDED, icon_size=50)
        self.nextButton = ft.IconButton(icon=ft.icons.SKIP_NEXT_ROUNDED, icon_size=50)
        self.modeButton = ft.IconButton(icon=ft.icons.REPEAT_ROUNDED, icon_size=50, on_click=self.modeClickEvent)
        self.folderButton = ft.IconButton(icon=ft.icons.FOLDER_ROUNDED, icon_size=50, on_click= lambda _:self.dirDialog.get_directory_path(initial_directory=r'C:\Users\Cliente\Documents\MediaCatcher\Audio'))

    
    def getFilePath(self, e: ft.FilePickerResultEvent):
        self.filePath.value = e.path if e.path else r'C:\Users\Cliente\Documents\MediaCatcher\Audio'
        self.filePath.update()
        self.fileWidget.controls.clear()
        for i in range(0, len(listdir(self.filePath.value))):
            self.fileWidget.controls.append(ft.Text(value=listdir(self.filePath.value)[i]))    
        self.fileWidget.update()

    def playClickEvent(self, e):
        e.control.icon = ft.icons.PAUSE_ROUNDED if e.control.icon == ft.icons.PLAY_ARROW_ROUNDED else ft.icons.PLAY_ARROW_ROUNDED
        e.control.update()
        self.fileWidget.update()

    def modeClickEvent(self, e):
        match e.control.icon:
            case ft.icons.REPEAT_ROUNDED: e.control.icon = ft.icons.REPEAT_ONE_ROUNDED
            case ft.icons.REPEAT_ONE_ROUNDED: e.control.icon = ft.icons.SHUFFLE_ROUNDED
            case ft.icons.SHUFFLE_ROUNDED: e.control.icon = ft.icons.REPEAT_ROUNDED
        e.control.update()

    def returnView(self, playerDialog):
        self.dirDialog = playerDialog
        return ft.Column(
            [
            #files widget
            ft.Container(
                bgcolor=ft.colors.TRANSPARENT,
                width=765,
                height=350,
                content=ft.Column(
                    [
                    self.filePath,
                    self.fileWidget
                    ]
                )
            ),
            #time slider widget
            ft.Container(
                bgcolor=ft.colors.TRANSPARENT,
                width=765,
                height=30,
                content=ft.Row(
                    [
                    self.currentTime,
                    self.musicSlider,
                    self.endTime
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ),
            #buttons widget
            ft.Container(
                bgcolor=ft.colors.TRANSPARENT,
                width=765,
                height=60,
                content=ft.Row(
                    [
                    self.modeButton,
                    self.previousButton,
                    self.playButton,
                    self.nextButton,
                    self.folderButton,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )
            ],
            spacing=5
        )
