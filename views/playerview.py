import flet as ft
from source.tools import DEBUG, pallete
from os import listdir
from random import randint


class PlayerView:
    def __init__(self) -> None:
        self.currentAudio = r'../source/blank.mp3'
        self.currentAudioControl = None
        self.timeUpdating = False
        self.previousFile = ""
        self.currentVolume = 0
        self.dirDialog = None
        self.filePath = ft.Text(value=r'C:\Users\Cliente\Documents\MediaCatcher\Audio', size=15)
        self.nameDisplayed = ft.Text(size=15, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS)
        self.thumb = ft.Image(src=r'../source/images/generic_thumb.png', width=100, height=100)
        self.fileWidget = ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            spacing=5,
            height=250,
            width=765
        )


        for i in listdir(self.filePath.value):
            if i.endswith(('.mp3', '.m4a', '.webm')):
                self.fileWidget.controls.append(ft.TextButton(text=i, on_click=self.fileClickEvent))

        self.currentTime = ft.Text("0:00")
        self.endTime = ft.Text("0:00")
        self.musicSlider = ft.Slider(
            width=500,
            min=0,
            max=100,
            divisions=100,
            label="{value}",
            active_color=pallete[0],
            on_change_start=self.timeIsUpdating,
            on_change_end=self.timeUpdate,
        )
        self.volumeSlider = ft.Slider(
            width=140,
            height=20,
            min=0,
            max=10,
            value=10,
            divisions=10,
            label="{value}",
            active_color=pallete[0],
            on_change_end=self.changeVolume,
        )

        self.playButton = ft.IconButton(icon=ft.icons.PLAY_ARROW_ROUNDED, icon_size=50, on_click=self.playClickEvent, icon_color=pallete[0])
        self.previousButton = ft.IconButton(icon=ft.icons.SKIP_PREVIOUS_ROUNDED, icon_size=50, icon_color=pallete[0], on_click=self.previousClickEvent)
        self.nextButton = ft.IconButton(icon=ft.icons.SKIP_NEXT_ROUNDED, icon_size=50, icon_color=pallete[0], on_click=self.nextClickEvent)
        self.modeButton = ft.IconButton(icon=ft.icons.REPEAT_ROUNDED, icon_size=50, on_click=self.modeClickEvent, icon_color=pallete[0])
        self.folderButton = ft.IconButton(icon=ft.icons.FOLDER_ROUNDED, icon_size=50, on_click= lambda _:self.dirDialog.get_directory_path(initial_directory=r'C:\Users\Cliente\Documents\MediaCatcher\Audio'), icon_color=pallete[0])

    
    def getFilePath(self, e: ft.FilePickerResultEvent):
        self.filePath.value = e.path if e.path else r'C:\Users\Cliente\Documents\MediaCatcher\Audio'
        self.filePath.update()
        self.fileWidget.controls.clear()
        for i in listdir(self.filePath.value):
            if i.endswith(('.mp3', '.m4a', '.webm')):
                self.fileWidget.controls.append(ft.TextButton(text=i, on_click=self.fileClickEvent))
        self.fileWidget.update()

    def playClickEvent(self, e):
        if e.control.icon == ft.icons.PLAY_ARROW_ROUNDED:
            self.audio.resume()
            if DEBUG: print("tocando")
            e.control.icon = ft.icons.PAUSE_ROUNDED
        else:
            self.audio.pause()
            if DEBUG: print("pausado")
            e.control.icon = ft.icons.PLAY_ARROW_ROUNDED
        e.control.update()
        self.fileWidget.update()

    def nextClickEvent(self, e):
        match self.modeButton.icon:
            case ft.icons.REPEAT_ROUNDED: self.repeatDefaultNext()
            case ft.icons.REPEAT_ONE_ROUNDED: self.repeatLoop()
            case ft.icons.SHUFFLE_ROUNDED: e.control.icon = self.repeatRandom()
        if DEBUG: print("indice: ", self.index)

    def previousClickEvent(self, e):
        match self.modeButton.icon:
            case ft.icons.REPEAT_ROUNDED: self.repeatDefaultPrevious()
            case ft.icons.REPEAT_ONE_ROUNDED: self.repeatLoop()
            case ft.icons.SHUFFLE_ROUNDED: e.control.icon = self.repeatRandom()
        if DEBUG: print("indice: ", self.index)

    def modeClickEvent(self, e):
        match e.control.icon:
            case ft.icons.REPEAT_ROUNDED: e.control.icon = ft.icons.REPEAT_ONE_ROUNDED
            case ft.icons.REPEAT_ONE_ROUNDED: e.control.icon = ft.icons.SHUFFLE_ROUNDED
            case ft.icons.SHUFFLE_ROUNDED: e.control.icon = ft.icons.REPEAT_ROUNDED
        e.control.update()

    def fileClickEvent(self, e):
        if e.control.text == self.previousFile:
            self.audio.play()
            return
        self.audio.release()
        self.currentAudio = self.filePath.value + "\\" + e.control.text
        self.currentAudioControl = e.control
        self.index = self.fileWidget.controls.index(self.currentAudioControl)
        self.nameDisplayed.value = e.control.text
        self.audio.src = self.currentAudio
        if DEBUG: print(self.audio.src)
        self.audio.play()
        self.playButton.icon = ft.icons.PAUSE_ROUNDED
        self.playButton.update()
        self.audio.on_duration_changed=self.audioChange
        self.audio.on_position_changed=self.sliderChange
        self.audio.update()
        self.nameDisplayed.update()

        self.previousFile = e.control.text

    def sliderChange(self, e):
        if self.timeUpdating == False:
            self.seconds = int(int(e.data)/1000)
            self.musicSlider.value = self.seconds
            zero = 0 if self.seconds<10 else ""
            self.currentTime.value = f"{int(self.seconds/60)}:{zero}{int(self.seconds%60)}"
            self.currentTime.update()
            self.musicSlider.update()

        if self.currentTime.value == self.endTime.value:
            match self.modeButton.icon:
                case ft.icons.REPEAT_ROUNDED: self.repeatDefaultNext()
                case ft.icons.REPEAT_ONE_ROUNDED: self.repeatLoop()
                case ft.icons.SHUFFLE_ROUNDED: self.repeatRandom()

    def timeUpdate(self, e):
        zero = 0 if e.control.value<10 else ""
        self.currentTime.value = f"{int(e.control.value/60)}:{zero}{int(e.control.value%60)}"
        self.audio.seek(self.seconds*1000 + int(e.control.value-self.seconds)*1000)
        if DEBUG: print(self.seconds*1000 + int(e.control.value-self.seconds)*1000)
        self.seconds = 0
        self.currentTime.update()
        self.timeUpdating = False

    def timeIsUpdating(self, e):
        self.timeUpdating = True

    def audioChange(self, e):
        if DEBUG: print("DURATION:", e.data)
        seconds = int(int(e.data)/1000)
        zero = 0 if seconds<10 else ""
        self.endTime.value = f"{int(seconds/60)}:{zero}{int(seconds%60)}"
        self.musicSlider.max = seconds
        self.musicSlider.divisions = seconds
        self.endTime.update()
        self.musicSlider.update()

    def changeVolume(self, e):
        self.audio.volume = float(e.data)/10
        self.audio.update()

    def repeatDefaultNext(self):
        self.audio.release()
        name = self.fileWidget.controls[self.index+1].text
        if DEBUG: print(name)
        self.audio.src = self.filePath.value + "\\" + name
        self.audio.play()
        self.nameDisplayed.value = name
        self.nameDisplayed.update()
        self.audio.update()
        self.index = self.index+1 if self.index+2<len(self.fileWidget.controls) else self.index-len(self.fileWidget.controls)+1
        self.playButton.icon = ft.icons.PAUSE_ROUNDED
        self.playButton.update()

    def repeatDefaultPrevious(self):
        self.audio.release()
        name = self.fileWidget.controls[self.index-1].text
        if DEBUG: print(name)
        self.audio.src = self.filePath.value + "\\" + name
        self.audio.play()
        self.nameDisplayed.value = name
        self.nameDisplayed.update()
        self.audio.update()
        self.index = 0 if abs(self.index)+1==len(self.fileWidget.controls) else self.index-1
        if DEBUG: print("indice: ", self.index)
        self.playButton.icon = ft.icons.PAUSE_ROUNDED
        self.playButton.update()

    def repeatLoop(self):
        self.audio.play()
        self.playButton.icon = ft.icons.PAUSE_ROUNDED
        self.playButton.update()

    def repeatRandom(self):
        self.audio.release()
        lenght = len(self.fileWidget.controls)
        name = self.fileWidget.controls[randint(0, lenght-1)].text
        if DEBUG: print(name)
        self.audio.src = self.filePath.value + "\\" + name
        self.audio.play()
        self.nameDisplayed.value = name
        self.nameDisplayed.update()
        self.audio.update()
        self.playButton.icon = ft.icons.PAUSE_ROUNDED
        self.playButton.update()

    def returnView(self, playerDialog, audioOverlay):
        self.audio = audioOverlay
        self.dirDialog = playerDialog
        return ft.Column(
            [
            #files widget
            ft.Container(
                bgcolor=ft.colors.TRANSPARENT,
                width=765,
                height=325,
                content=ft.Column(
                    [
                    self.filePath,
                    self.fileWidget
                    ]
                )
            ),
            ft.Row(
                [
                self.thumb,
                ft.Column(
                    [
                    self.nameDisplayed,
                    #time slider widget
                    ft.Container(
                        bgcolor=ft.colors.TRANSPARENT,
                        width=500,
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
                        width=650,
                        height=60,
                        content=ft.Row(
                            [
                            self.modeButton,
                            self.previousButton,
                            self.playButton,
                            self.nextButton,
                            self.folderButton,
                            self.volumeSlider,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    )
                    ]
                )
                ],
                spacing=0
            ),
            
            #buttons widget
            
            ],
            spacing=5
        )
