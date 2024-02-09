import flet as ft

debug = True

youtubeTextField = ft.TextField(hint_text="link do YouTube", width=600, border_radius=15,bgcolor=ft.colors.INDIGO_400)
nameTextField = ft.TextField(hint_text="Nome do vídeo", width=600, border_radius=15,bgcolor=ft.colors.INDIGO_400)

def textFieldReturnerYoutube(e):
    global globalLink
    globalLink = youtubeTextField.value
    print(globalLink) if debug else None


def textFieldReturnerName(e):
    pass

def textFieldReturnerGeneric(e):
    pass

audioFormatDropdown = ft.Dropdown(
    label="Formato", 
    width=108, 
    height=60,
    scale=0.9, 
    border_color=ft.colors.TRANSPARENT,
    options=[ft.dropdown.Option("mp3"), 
             ft.dropdown.Option("etc")],
    )

videoFormatDropdown = ft.Dropdown(label="Formato", 
    width=108, 
    height=60,
    scale=0.9, 
    border_color=ft.colors.TRANSPARENT,
    options=[ft.dropdown.Option("mp4"), 
             ft.dropdown.Option("mwa"),
             ft.dropdown.Option("etc")],
    )

videoResolutionDropdown = ft.Dropdown(label="Resolução", 
    width=120, 
    height=60,
    scale=0.9, 
    border_color=ft.colors.TRANSPARENT,
    options=[ft.dropdown.Option("240p"), 
             ft.dropdown.Option("360p"),
             ft.dropdown.Option("480p"),
             ft.dropdown.Option("720p"),
             ft.dropdown.Option("1080p")],
    )