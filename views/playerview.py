import flet as ft
from source.widgets import pallete
from os import listdir


class PlayerView:
    def __init__(self) -> None:
        self.fileWidget = ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            spacing=20,
        )

        for i in range(0, len(listdir(r'C:\Users\Cliente\Pictures\Saved Pictures'))):
            self.fileWidget.controls.append(ft.Text(value=listdir(r'C:\Users\Cliente\Pictures\Saved Pictures')[i]))


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
        self.folderButton = ft.IconButton(icon=ft.icons.FOLDER_ROUNDED, icon_size=50)

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

    def returnView(self):
        return ft.Column(
            [
            ft.Container(
                bgcolor=ft.colors.TRANSPARENT,
                width=765,
                height=350,
                content=self.fileWidget
            ),
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

def playerView():
    view = ft.Column(
        [
            ft.Text(value="aqui eh player"),
            
        ]
    )

    return view