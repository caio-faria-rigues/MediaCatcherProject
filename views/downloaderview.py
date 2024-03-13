import flet as ft
from source.tools import pallete, readTOML
from app.ddl import *

debug = True

class DownloaderView:
    def __init__(self) -> None:
        self.customPath = ft.Text(value=r'C:\Users\Cliente\Documents\MediaCatcher\Audio', size=15)
        self.urlInput = ft.TextField(hint_text="link", width=600, border_radius=15,bgcolor=pallete[0])
        self.nameInput = ft.TextField(hint_text="Nome do arquivo", width=600, border_radius=15,bgcolor=pallete[0])
        self.downloadUrl = self.urlInput.value
        self.dirDialog = None

        self.requestContainer = ft.Container(width=50, height=50)

        self.searchButton = ft.IconButton(
            icon=ft.icons.SEARCH_ROUNDED, 
            icon_size=40, 
            on_click=self.textFieldReturnerYoutube, 
            icon_color=pallete[0]
        )
        self.downloadButton = ft.IconButton(
            icon=ft.icons.DOWNLOAD, 
            icon_size=40,
            on_click=self.download,
            icon_color=pallete[0]
        )

        self.downloadProgress = ft.ProgressRing(
            height=40, 
            width=40, 
            bgcolor=pallete[0],
            color=pallete[4],
            value=0.0,
            visible=False,
        )

        self.optionsSwitch = ft.Switch(
            label="Baixar Áudio", 
            on_change=self.changeOptions, 
            track_color=pallete[3], 
            thumb_icon={
                ft.MaterialState.SELECTED: ft.icons.VIDEOCAM_ROUNDED,
                ft.MaterialState.DEFAULT: ft.icons.MUSIC_NOTE_ROUNDED
            },
            thumb_color={
                ft.MaterialState.SELECTED: pallete[5],
                ft.MaterialState.DEFAULT: pallete[0],
            }
        )

        self.audioOptions = ft.Row(
            [
            ft.Dropdown(
                label="Formato",
                value="m4a",
                width=108, 
                height=65,
                scale=0.9, 
                border_color=ft.colors.TRANSPARENT,
                options=
                    [
                    ft.dropdown.Option("m4a"), 
                    ft.dropdown.Option("webm")
                    ],
            ),
            ft.Checkbox(
                label="Incluir Thumbnail",
                value=True,
                check_color=pallete[4]
            )
            ]
        )
        self.videoOptions = ft.Row(
            [
            ft.Dropdown(
                label="Formato", 
                value="mp4",
                width=108, 
                height=65,
                scale=0.9, 
                border_color=ft.colors.TRANSPARENT,
                options=
                    [
                    ft.dropdown.Option("mp4"), 
                    ft.dropdown.Option("webm"),
                    ],
            ),
            ft.Dropdown(
                label="Resolução", 
                value="1080",
                width=120, 
                height=65,
                scale=0.9, 
                border_color=ft.colors.TRANSPARENT,
                options=
                    [
                    ft.dropdown.Option("144"),
                    ft.dropdown.Option("240"), 
                    ft.dropdown.Option("360"),
                    ft.dropdown.Option("480"),
                    ft.dropdown.Option("720"),
                    ft.dropdown.Option("1080")
                    ],
                )
            ]
        )
        self.currentOptions = ft.Container(content=self.audioOptions)

        self.timeSlider = ft.RangeSlider(
            min=0, 
            max=100, 
            label="{value}", 
            start_value=0, 
            end_value=100, 
            width=550, 
            divisions=100,
            on_change_end=self.timeSliderSubmit,
            active_color=pallete[0],
        )

        self.timeStartInput = ft.TextField(
            value=0,
            bgcolor=pallete[0],
            width=50, 
            height=30,
            text_size=14,
            multiline=False,
            text_align=ft.alignment.center,
            content_padding=2,
            border_radius=10,
            selection_color=pallete[5],
            input_filter=ft.InputFilter(
                            allow=True, 
                            regex_string=r"[0-9]", 
            ),
            on_submit=self.timeStartSubmit
        )

        self.timeEndInput = ft.TextField(
            value=0,
            bgcolor=pallete[0],
            width=50, 
            height=30,
            text_size=14,
            multiline=False,
            text_align=ft.alignment.center,
            content_padding=2,
            border_radius=10,
            input_filter=ft.InputFilter(
                            allow=True, 
                            regex_string=r"[0-9]", 
            ),
            on_submit=self.timeEndSubmit
        )

        self.advancedOptions = ft.Container(
            visible=False,
            content=ft.Column(
                [
                ft.Text("Caminho Personalizado:", size=13),
                ft.Row(
                    [
                    ft.IconButton(icon=ft.icons.FOLDER_ROUNDED, icon_size=30, on_click= lambda _:self.dirDialog.get_directory_path(initial_directory=r'C:\Users\Cliente\Documents\MediaCatcher')),
                    self.customPath,
                    ]
                ),
                ft.Text("Cortar arquivo:", size=13),
                ft.Row(
                    [
                    self.timeSlider,
                    self.timeStartInput,
                    self.timeEndInput
                    ]
                )
                ]
            )
        )


    def changeOptions(self, e):
        if self.currentOptions.content == self.audioOptions:
            self.currentOptions.content = self.videoOptions
            self.customPath.value = readTOML("video", "default", "path")
            self.optionsSwitch.label = "Baixar Vídeo"
        else:
            self.currentOptions.content = self.audioOptions
            self.customPath.value = readTOML("audio", "default", "path")
            self.optionsSwitch.label = "Baixar Áudio"
        self.currentOptions.update()
        self.optionsSwitch.update()
        self.customPath.update()

    def getCustomDir(self, e: ft.FilePickerResultEvent):
        self.customPath.value = e.path if e.path else r'C:\Users\Cliente\Documents\MediaCatcher\Audio'
        self.customPath.update()

    def textFieldReturnerYoutube(self, e):
        self.requestContainer.content = ft.ProgressRing(height=50, width=40, bgcolor=pallete[0], color=pallete[4])
        self.requestContainer.update()
        self.downloadUrl = self.urlInput.value
        title, duration, thumb = requestSourceInfo(self.downloadUrl)
        self.nameInput.hint_text = title
        self.timeEndInput.value = duration
        self.timeSlider.max = self.timeSlider.end_value = self.timeSlider.divisions = duration
        self.requestContainer.content = ft.Image(src=thumb)
        self.requestContainer.update()
        self.timeSlider.update()
        self.nameInput.update()
        self.timeEndInput.update()

    def download(self, e):
        if self.optionsSwitch.label == "Baixar Áudio":
            audioDownloader(
                url=self.downloadUrl, 
                name=self.nameInput.hint_text if self.nameInput.value == "" else self.nameInput.value, 
                ext=self.audioOptions.controls[0].value, 
                thumb=self.audioOptions.controls[1].value, 
                timeStart=float(self.timeStartInput.value),
                timeEnd=float(self.timeEndInput.value),
                ring=self.downloadProgress,
                path=self.customPath.value
            )
        elif self.optionsSwitch.label == "Baixar Vídeo":
            videoDownloader(
                url=self.downloadUrl, 
                name=self.nameInput.hint_text if self.nameInput.value == "" else self.nameInput.value, 
                ext=self.videoOptions.controls[0].value, 
                res=self.videoOptions.controls[1].value,
                timeStart=float(self.timeStartInput.value),
                timeEnd=float(self.timeEndInput.value), 
                ring=self.downloadProgress
            )
    
    def hideAdvancedOptions(self, e):
        self.advancedOptions.visible = True if self.advancedOptions.visible == False else False
        self.advancedOptions.update()

    def timeSliderSubmit(self, e):
        self.timeStartInput.value = e.control.start_value
        self.timeEndInput.value = e.control.end_value
        self.timeStartInput.update()
        self.timeEndInput.update()

    def timeStartSubmit(self, e):
        self.timeSlider.start_value = e.control.value
        self.timeSlider.update()

    def timeEndSubmit(self, e):
        self.timeSlider.end_value = e.control.value
        self.timeSlider.update()

    def returnView(self, customDirDialog):
        self.dirDialog = customDirDialog
        return ft.Column(
            [
            ft.Text(value="URL:", width=500, text_align="LEFT", size=15),
            ft.Row(
                [
                self.urlInput,
                self.searchButton,
                self.requestContainer,
                ]
            ),
            ft.Text(value="Nome do Arquivo:", width=500, text_align="LEFT", size=15),
            ft.Row(
                [
                self.nameInput,
                self.downloadButton,
                self.downloadProgress,
                ]
            ),
            ft.Row(
                [
                self.optionsSwitch,
                self.currentOptions
                ],
                height=60
            ),
            ft.TextButton(
                content=ft.Text("Opções Avançadas", size=10, text_align=ft.alignment.center_left, italic=True),
                on_click=self.hideAdvancedOptions, 
                width=115, 
                height=20,
            ),
            self.advancedOptions,
            ]
    )
