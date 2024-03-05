import flet as ft
import flet.canvas as ftc
import math

from views.downloaderview import DownloaderView
from views.playerview import PlayerView
from views.settingsview import SettingsView

class MediaCatcher(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.page.title = "Media Catcher"
        self.page.window_width = 1000
        self.page.window_height = 600
        self.page.window_resizable = False
        self.page.window_maximizable = False
        self.mainContainer = 0
        self.prevIndex = 3

        self.downloaderView = DownloaderView()
        self.settingsView = SettingsView()
        self.playerView = PlayerView()

        self.audioDirDialog = ft.FilePicker(on_result=self.settingsView.getAudioDir)
        self.videoDirDialog = ft.FilePicker(on_result=self.settingsView.getVideoDir)
        self.customDirDialog = ft.FilePicker(on_result=self.downloaderView.getCustomDir)
        self.playerDirDialog = ft.FilePicker(on_result=self.playerView.getFilePath)
        self.optionalDirDialog = ft.FilePicker(on_result=self.settingsView.getOptionalDir)
        self.page.overlay.append(self.audioDirDialog)
        self.page.overlay.append(self.videoDirDialog)
        self.page.overlay.append(self.customDirDialog)
        self.page.overlay.append(self.playerDirDialog)
        self.page.overlay.append(self.optionalDirDialog)

        self.audio = ft.Audio(src=r'../source/blank.mp3', on_loaded=lambda _: print("Loaded"))

        self.page.overlay.append(self.audio)
        print(self.page.overlay)
        

        self.mainContainer = ft.Container(
                expand=False,
                alignment=ft.alignment.top_left,
                padding=25,
                content=self.downloaderView.returnView(self.customDirDialog)
                )
        
        self.page.add(
            ft.Container(
                alignment=ft.alignment.center,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.bottom_left,
                    end=ft.alignment.top_right,
                    colors=
                        [
                        "#001147",
                        "#180837",
                        "#180837"
                        ],
                    tile_mode=ft.GradientTileMode.MIRROR,
                    rotation=math.pi / 3
                ),
                width=1000,
                height=600,
                margin=-10,
                content=ft.Row(
                    [
                    ft.Container( #widget da esquerda
                        expand=False,
                        alignment=ft.alignment.center,
                        gradient=ft.LinearGradient(
                            colors=
                                [
                                "#010e38",
                                "#2b194d"
                                #"#180837"
                                ],
                            begin=ft.alignment.top_left,
                            end=ft.alignment.bottom_right
                        ),
                        width=150,
                        height=500,
                        border_radius=20,
                        margin=15,
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=10,
                            color=ft.colors.BLACK45,
                            offset=ft.Offset(0, 0),
                            blur_style=ft.ShadowBlurStyle.OUTER,
                        ),
                        content=ft.Column(
                            [
                            ft.NavigationRail(
                                selected_index=0,
                                label_type=ft.NavigationRailLabelType.ALL,
                                min_width=100,
                                min_extended_width=400,
                                height=500,
                                bgcolor=ft.colors.with_opacity(0, '#ff6666'),
                                indicator_color=ft.colors.with_opacity(0.5, '#808080'),
                                leading=ft.Image(src=r"../source/images/logo.png", width=100, height=100), #logo
                                group_alignment=-1,
                                destinations=
                                    [
                                    ft.NavigationRailDestination(
                                        icon=ft.icons.DOWNLOAD, 
                                        selected_icon=ft.icons.DOWNLOAD, 
                                        label="Downloader"
                                    ),
                                    ft.NavigationRailDestination(
                                        icon_content=ft.Icon(ft.icons.PLAY_CIRCLE_FILLED_ROUNDED),
                                        selected_icon_content=ft.Icon(ft.icons.PLAY_CIRCLE_FILLED_ROUNDED),
                                        label="Player",
                                    ),
                                    ft.NavigationRailDestination(
                                        icon=ft.icons.SETTINGS_OUTLINED,
                                        selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                                        label_content=ft.Text("Settings"),
                                    ),
                                    ],
                                on_change=self.changeView,
                            )
                            ]
                        )
                    ),
                    ft.Container( #widgeSt da direita
                        expand=False,
                        alignment=ft.alignment.center,
                        gradient=ft.LinearGradient(
                            colors=
                                [
                                "#001147",
                                "#2b194d"
                                ],
                            begin=ft.alignment.top_right,
                            end=ft.alignment.bottom_left
                        ),
                        width=765,
                        height=500,
                        border_radius=20,
                        margin=15,
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.colors.BLACK45,
                            offset=ft.Offset(0, 0),
                            blur_style=ft.ShadowBlurStyle.OUTER,
                        ),
                        content=self.mainContainer
                    )
                    ],
                    alignment=ft.alignment.center
                )
            )
        )

        self.page.update()


    def changeView(self, e):
        if e.control.selected_index != self.prevIndex:
            print("Selected destination:", e.control.selected_index)
            match e.control.selected_index:
                case 0: self.mainContainer.content = self.downloaderView.returnView(self.customDirDialog)
                case 1: self.mainContainer.content = self.playerView.returnView(self.playerDirDialog, self.audio)
                case 2: self.mainContainer.content = self.settingsView.returnView(self.audioDirDialog, self.videoDirDialog, self.optionalDirDialog)
            self.mainContainer.update()
        print(self.page.overlay)

        self.prevIndex = e.control.selected_index

