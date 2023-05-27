import customtkinter as ctk
import modules.create_frame as m_frame
import modules.full_path as path
import modules.image as image
import modules.button_function as functions
import pygame
import random



# Задаем ширину и высоту приложения
APP_WIDTH = 500
APP_HEIGHT = 500
# Клас настройки окна и характеристик фрейма
class App(ctk.CTk):
    def __init__(self, fg_color):
        super().__init__(fg_color)
        self.APP_WIDTH = APP_WIDTH
        self.APP_HEIGHT = APP_HEIGHT
        self.X = 200
        self.Y = 200
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.X}+{self.Y}")
        self.resizable(False,False)
        self.FRAME = m_frame.Frame(master = self, width = 275, height = 375, border_width = 2, fg_color = "white")
        self.FRAME.place(relx = 0.03, rely = 0.03)
        # self.LABEL = ctk.CTkLabel(self)
        # self.LABEL.place(relx = 0.2, rely = 0.2)
# Создаем окно и задаем ему цвет 
app = App(fg_color = "lightblue")

pygame.init()
pygame.mixer.init()
list_music = []








def add_music():
    music_file = ctk.filedialog.askopenfile(mode = "r", filetypes= [("MP3", "*.mp3")])
    print(111111111111)
    list_music.append(music_file)
    for name in list_music:
        print(name.name.split("/")[-1])
    print(1111111111)

    # print(list_music)
    pygame.mixer.music.load(music_file.name)
    pygame.mixer.music.queue(list_music[-1].name, loops = 1)
    def stop():
        label = ctk.CTkLabel(master= app, text = "аааaaaaaaaaaaaaaaa", text_color="lightblue")
        label.place(relx = 0.7, rely = 0.08)
        pygame.mixer.music.pause()
        button_big_play = ctk.CTkButton(master = app,
                           text = "",
                           width = 160,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_play,
                           command = play_music
                           )
        button_big_play.place(relx = 0.65, rely = 0.15)
    button_big_stop = ctk.CTkButton(master = app,
                           text = "",
                           width = 160,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_stop,
                           command = stop
                           )
    button_big_stop.place(relx = 0.65, rely = 0.6)
    def plus_volume():
        volume = pygame.mixer.music.get_volume()
        # print(volume)
        pygame.mixer.music.set_volume(volume + 0.1)
    button_small_sound_plus = ctk.CTkButton(master = app,
                           text = "",
                           width = 60,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_sound_plus,
                           command = plus_volume
                           )
    
    def minus_volume():
        volume = pygame.mixer.music.get_volume()
        # print(volume)
        pygame.mixer.music.set_volume(volume - 0.14)
    button_small_sound_minus = ctk.CTkButton(master = app,
                           text = "",
                           width = 60,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_sound_minus,
                           command = minus_volume
                           )
    
    def play_music():
        global label
        # pygame.mixer.music.unload()
        pygame.mixer.music.load(list_music[0].name)
        pygame.mixer.music.play()
        label = ctk.CTkLabel(master= app, text = str(list_music[0].name.split("/")[-1]), text_color="black")
        label.place(relx = 0.7, rely = 0.08)
        button_big_play = ctk.CTkButton(master = app,
                           text = "",
                           width = 160,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_play,
                           command = pygame.mixer.music.unpause
                           )
        button_big_play.place(relx = 0.65, rely = 0.15)
    button_big_play = ctk.CTkButton(master = app,
                           text = "",
                           width = 160,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_play,
                           command = play_music
                           )
    button_big_play.place(relx = 0.65, rely = 0.15)
     # def delete():
    #     global button1, label, list_music
    #     pygame.mixer.music.unload()
    #     button1 = ctk.CTkButton(master = app.FRAME,
    #                            text = "",
    #                            width = 250,
    #                            height = 350,
    #                            corner_radius = 15,
    #                            border_width = 3,
    #                            border_color = "white",
    #                            fg_color = "white",
    #                            hover_color="white",
    #                            image = None)
    #     button1.place(relx = 0.05, rely = 0.05)
    #     label = ctk.CTkLabel(master= app, text = "аааaaaaaaaaaaaaaaa", text_color="lightblue")
    #     label.place(relx = 0.7, rely = 0.08)
    #     list_music.clear()
    # button_trash = ctk.CTkButton(master = app,
    #                        text = "",
    #                        width = 60,
    #                        height = 60,
    #                        corner_radius = 15,
    #                        border_width = 3,
    #                        border_color = "black",
    #                        fg_color = "white",
    #                        hover_color="lightgreen",
    #                        image = image.image_button_delete,
    #                        command = delete
    #                        )
    # button_trash.place(relx = 0.24, rely = 0.85)
    def del_play1():
        def play():
            pygame.mixer.music.load(list_music[0].name)
            pygame.mixer.music.play()
            label = ctk.CTkLabel(master= app, text = "аааaaaaaaaaaaaaaaa", text_color="lightblue")
            label.place(relx = 0.7, rely = 0.08)
            label = ctk.CTkLabel(master= app, text = str(list_music[0].name.split("/")[-1]), text_color="black")
            label.place(relx = 0.7, rely = 0.08)
        button_big_play = ctk.CTkButton(master = app,
                           text = "",
                           width = 160,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_play,
                           command = play
                           )
        button_big_play.place(relx = 0.65, rely = 0.15)
        def del1():
            button1 = ctk.CTkButton(master = app.FRAME,
                               text = "",
                               width = 150,
                               height = 50,
                               corner_radius = 15,
                               border_width = 3,
                               border_color = "white",
                               fg_color = "white",
                               hover_color="white",
                               image = None)
            button1.place(relx = 0.05, rely = 0.05)
            label = ctk.CTkLabel(master= app, text = "аааaaaaaaaaaaaaaaa", text_color="lightblue")
            label.place(relx = 0.7, rely = 0.08)
            del list_music[0]
        button_trash = ctk.CTkButton(master = app,
                           text = "",
                           width = 60,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_delete,
                           command = del1
                           )
        button_trash.place(relx = 0.24, rely = 0.85)
    def del_play2():
        def play():
            pygame.mixer.music.load(list_music[1].name)
            pygame.mixer.music.play()
            label = ctk.CTkLabel(master= app, text = "аааaaaaaaaaaaaaaaa", text_color="lightblue")
            label.place(relx = 0.7, rely = 0.08)
            label = ctk.CTkLabel(master= app, text = str(list_music[1].name.split("/")[-1]), text_color="black")
            label.place(relx = 0.7, rely = 0.08)
        button_big_play = ctk.CTkButton(master = app,
                           text = "",
                           width = 160,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_play,
                           command = play
                           )
        button_big_play.place(relx = 0.65, rely = 0.15)
        def del2():
            button2 = ctk.CTkButton(master = app.FRAME,
                               text = "",
                               width = 150,
                               height = 50,
                               corner_radius = 15,
                               border_width = 3,
                               border_color = "white",
                               fg_color = "white",
                               hover_color="white",
                               image = None)
            button2.place(relx = 0.05, rely = 0.2)
            label = ctk.CTkLabel(master= app, text = "аааaaaaaaaaaaaaaaa", text_color="lightblue")
            label.place(relx = 0.7, rely = 0.08)
            try:
                del list_music[1]
            except:
                del list_music[0]
        button_trash = ctk.CTkButton(master = app,
                           text = "",
                           width = 60,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_delete,
                           command = del2
                           )
        button_trash.place(relx = 0.24, rely = 0.85)
    def del_play3():
        def play():
            pygame.mixer.music.load(list_music[2].name)
            pygame.mixer.music.play()
            label = ctk.CTkLabel(master= app, text = "аааaaaaaaaaaaaaaaa", text_color="lightblue")
            label.place(relx = 0.7, rely = 0.08)
            label = ctk.CTkLabel(master= app, text = str(list_music[2].name.split("/")[-1]), text_color="black")
            label.place(relx = 0.7, rely = 0.08)
        button_big_play = ctk.CTkButton(master = app,
                           text = "",
                           width = 160,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_play,
                           command = play
                           )
        button_big_play.place(relx = 0.65, rely = 0.15)
        def del3():
            button3 = ctk.CTkButton(master = app.FRAME,
                               text = "",
                               width = 150,
                               height = 50,
                               corner_radius = 15,
                               border_width = 3,
                               border_color = "white",
                               fg_color = "white",
                               hover_color="white",
                               image = None)
            button3.place(relx = 0.05, rely = 0.35)
            label = ctk.CTkLabel(master= app, text = "аааaaaaaaaaaaaaaaa", text_color="lightblue")
            label.place(relx = 0.7, rely = 0.08)
            try:
                del list_music[2]
            except:
                del list_music[1]
        button_trash = ctk.CTkButton(master = app,
                           text = "",
                           width = 60,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_delete,
                           command = del3
                           )
        button_trash.place(relx = 0.24, rely = 0.85)
    def del_play4():
        def play():
            pygame.mixer.music.load(list_music[3].name)
            pygame.mixer.music.play()
            label = ctk.CTkLabel(master= app, text = "аааaaaaaaaaaaaaaaa", text_color="lightblue")
            label.place(relx = 0.7, rely = 0.08)
            label = ctk.CTkLabel(master= app, text = str(list_music[3].name.split("/")[-1]), text_color="black")
            label.place(relx = 0.7, rely = 0.08)
        button_big_play = ctk.CTkButton(master = app,
                           text = "",
                           width = 160,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_play,
                           command = play
                           )
        button_big_play.place(relx = 0.65, rely = 0.15)
        def del4():
            button4 = ctk.CTkButton(master = app.FRAME,
                               text = "",
                               width = 150,
                               height = 50,
                               corner_radius = 15,
                               border_width = 3,
                               border_color = "white",
                               fg_color = "white",
                               hover_color="white",
                               image = None)
            button4.place(relx = 0.05, rely = 0.5)
            label = ctk.CTkLabel(master= app, text = "аааaaaaaaaaaaaaaaa", text_color="lightblue")
            label.place(relx = 0.7, rely = 0.08)
            try:
                del list_music[3]
            except:
                del list_music[2]
        button_trash = ctk.CTkButton(master = app,
                           text = "",
                           width = 60,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_delete,
                           command = del4
                           )
        button_trash.place(relx = 0.24, rely = 0.85)
    def del_play5():
        def play():
            pygame.mixer.music.load(list_music[4].name)
            pygame.mixer.music.play()
            label = ctk.CTkLabel(master= app, text = "аааaaaaaaaaaaaaaaa", text_color="lightblue")
            label.place(relx = 0.7, rely = 0.08)
            label = ctk.CTkLabel(master= app, text = str(list_music[4].name.split("/")[-1]), text_color="black")
            label.place(relx = 0.7, rely = 0.08)
        button_big_play = ctk.CTkButton(master = app,
                           text = "",
                           width = 160,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_play,
                           command = play
                           )
        button_big_play.place(relx = 0.65, rely = 0.15)
        def del5():
            button5 = ctk.CTkButton(master = app.FRAME,
                               text = "",
                               width = 150,
                               height = 50,
                               corner_radius = 15,
                               border_width = 3,
                               border_color = "white",
                               fg_color = "white",
                               hover_color="white",
                               image = None)
            button5.place(relx = 0.05, rely = 0.65)
            label = ctk.CTkLabel(master= app, text = "аааaaaaaaaaaaaaaaa", text_color="lightblue")
            label.place(relx = 0.7, rely = 0.08)
            try:
                del list_music[4]
            except:
                del list_music[3]
        button_trash = ctk.CTkButton(master = app,
                           text = "",
                           width = 60,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_delete,
                           command = del5
                           )
        button_trash.place(relx = 0.24, rely = 0.85)
    def del_play6():
        def play():
            pygame.mixer.music.load(list_music[5].name)
            pygame.mixer.music.play()
            label = ctk.CTkLabel(master= app, text = "аааaaaaaaaaaaaaaaa", text_color="lightblue")
            label.place(relx = 0.7, rely = 0.08)
            label = ctk.CTkLabel(master= app, text = str(list_music[5].name.split("/")[-1]), text_color="black")
            label.place(relx = 0.7, rely = 0.08)
        button_big_play = ctk.CTkButton(master = app,
                           text = "",
                           width = 160,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_play,
                           command = play
                           )
        button_big_play.place(relx = 0.65, rely = 0.15)
        def del6():
            button6 = ctk.CTkButton(master = app.FRAME,
                               text = "",
                               width = 150,
                               height = 50,
                               corner_radius = 15,
                               border_width = 3,
                               border_color = "white",
                               fg_color = "white",
                               hover_color="white",
                               image = None)
            button6.place(relx = 0.05, rely = 0.80)
            label = ctk.CTkLabel(master= app, text = "аааaaaaaaaaaaaaaaa", text_color="lightblue")
            label.place(relx = 0.7, rely = 0.08)
            del list_music[-1]
        button_trash = ctk.CTkButton(master = app,
                           text = "",
                           width = 60,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_delete,
                           command = del6
                           )
        button_trash.place(relx = 0.24, rely = 0.85)
    if len(list_music) == 1:
        button1 = ctk.CTkButton(master = app.FRAME,
                               text = str(music_file.name.split("/")[-1]),
                               text_color="black",
                               width = 100,
                               height = 40,
                               corner_radius = 15,
                               border_width = 3,
                               border_color = "black",
                               fg_color = "white",
                               hover_color="lightgreen",
                               image = None,
                               command = del_play1)
        button1.place(relx = 0.05, rely = 0.05)
    if len(list_music) == 2:
        button2 = ctk.CTkButton(master = app.FRAME,
                               text = str(music_file.name.split("/")[-1]),
                               text_color="black",
                               width = 100,
                               height = 40,
                               corner_radius = 15,
                               border_width = 3,
                               border_color = "black",
                               fg_color = "white",
                               hover_color="lightgreen",
                               image = None,
                               command = del_play2)
        button2.place(relx = 0.05, rely = 0.2)
    if len(list_music) == 3:
        button3 = ctk.CTkButton(master = app.FRAME,
                               text = str(music_file.name.split("/")[-1]),
                               text_color="black",
                               width = 100,
                               height = 40,
                               corner_radius = 15,
                               border_width = 3,
                               border_color = "black",
                               fg_color = "white",
                               hover_color="lightgreen",
                               image = None,
                               command = del_play3)
        button3.place(relx = 0.05, rely = 0.35)
    if len(list_music) == 4:
        button4 = ctk.CTkButton(master = app.FRAME,
                               text = str(music_file.name.split("/")[-1]),
                               text_color="black",
                               width = 100,
                               height = 40,
                               corner_radius = 15,
                               border_width = 3,
                               border_color = "black",
                               fg_color = "white",
                               hover_color="lightgreen",
                               image = None,
                               command = del_play4)
        button4.place(relx = 0.05, rely = 0.5)
    if len(list_music) == 5:
        button5 = ctk.CTkButton(master = app.FRAME,
                               text = str(music_file.name.split("/")[-1]),
                               text_color="black",
                               width = 100,
                               height = 40,
                               corner_radius = 15,
                               border_width = 3,
                               border_color = "black",
                               fg_color = "white",
                               hover_color="lightgreen",
                               image = None,
                               command = del_play5)
        button5.place(relx = 0.05, rely = 0.65)
    if len(list_music) == 6:
        button6 = ctk.CTkButton(master = app.FRAME,
                               text = str(music_file.name.split("/")[-1]),
                               text_color="black",
                               width = 100,
                               height = 40,
                               corner_radius = 15,
                               border_width = 3,
                               border_color = "black",
                               fg_color = "white",
                               hover_color="lightgreen",
                               image = None,
                               command = del_play6)
        button6.place(relx = 0.05, rely = 0.80)
    button_small_sound_plus.place(relx = 0.64, rely = 0.85)
    button_small_sound_minus.place(relx = 0.84, rely = 0.85)
   
    def mix():

        pygame.mixer.music.pause()
        # pygame.mixer.music.set_endevent()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(random.choice(list_music).name)
        pygame.mixer.music.play()
        label = ctk.CTkLabel(master= app, text = "aaaaaaaaaaaaaaaaaa", text_color="lightblue")
        label.place(relx = 0.7, rely = 0.08)
        label = ctk.CTkLabel(master= app, text = str(random.choice(list_music).name.split("/")[-1]), text_color="black")
        label.place(relx = 0.7, rely = 0.08)
    button_mix = ctk.CTkButton(master = app,
                           text = "",
                           width = 60,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_mix,
                           command = mix
                           )
    button_mix.place(relx = 0.44, rely = 0.85)
def unpause():
    pygame.mixer.music.unpause()
def pause():
    pygame.mixer.music.pause()
    button_big_play = ctk.CTkButton(master = app,
                           text = "",
                           width = 160,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image.image_button_play,
                           command = unpause
                           )
    button_big_play.place(relx = 0.65, rely = 0.15)


