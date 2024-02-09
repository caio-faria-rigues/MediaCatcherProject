import flet as ft
import flet.canvas as ftc
import math
from widgets import *

class MediaCatcher(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.page.title = "Media Catcher"
        self.page.window_width = 1000
        self.page.window_height = 600
        self.page.window_resizable = False
        self.page.window_maximizable = False

        self.page.add(
            ft.Container(
                alignment=ft.alignment.center,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.bottom_left,
                    end=ft.alignment.top_right,
                    colors=[
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
                                colors=[
                                    "#010e38",
                                    "#2b194d"
                                    #"#180837"
                                ],
                                begin=ft.alignment.top_left,
                                end=ft.alignment.bottom_right
                            ),
                            width=200,
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
                                    #indicator_color=ft.colors.with_opacity(0.5, '#808080'),
                                    leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"), #logo
                                    group_alignment=-0.9,
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
                                    on_change=lambda e: print("Selected destination:", e.control.selected_index),
                                    #on_change=change_body,
                                )
                                ]
                            )
                        ),
                        ft.Container( #widget da direita
                            expand=False,
                            alignment=ft.alignment.center,
                            gradient=ft.LinearGradient(
                                colors=[
                                    "#001147",
                                    "#2b194d"
                                ],
                                begin=ft.alignment.top_right,
                                end=ft.alignment.bottom_left
                            ),
                            width=715,
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
                            content=ft.Container(
                                expand=False,
                                alignment=ft.alignment.top_left,
                                padding=25,
                                content=ft.Column(
                                [
                                    ft.Text(value="Insira o link do vídeo do Youtube:", width=500, text_align="LEFT", size=15),
                                    ft.Row(
                                    [
                                        youtubeTextField,
                                        ft.IconButton(icon=ft.icons.SEARCH_ROUNDED, icon_size=40, on_click=textFieldReturnerYoutube)
                                    ]
                                    ),
                                    ft.Text(value="Modifique seu nome(opcional):", width=500, text_align="LEFT", size=15),
                                    nameTextField,
                                    ft.Row(
                                    [
                                        ft.ElevatedButton("Baixar Áudio", icon=ft.icons.MUSIC_NOTE_ROUNDED),
                                        audioFormatDropdown,
                                        ft.ElevatedButton("Baixar Vídeo", icon=ft.icons.VIDEO_FILE_ROUNDED),
                                    videoFormatDropdown,
                                    videoResolutionDropdown,
                            ]
                        )
                    ]
                )
            )
                        )
                    ],
                    alignment=ft.alignment.center
                )
            )
        )

        self.page.update()


def change_body(e):   
    pass