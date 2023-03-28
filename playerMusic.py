import tkinter as tk
import tkinter.filedialog as fd
import pygame
import os

class LecteurAudio:
    def __init__(self, master):
        self.master = master
        master.title("Lecteur audio")

        self.playlist = []
        self.current_track = None
        self.paused = False
        self.loop = False  
        self.volume = 50  

        
        self.label = tk.Label(master, text="Lecteur audio")
        self.label.pack()

        self.listbox = tk.Listbox(master, selectmode=tk.MULTIPLE)
        self.listbox.pack()

        self.play_button = tk.Button(master, text="Play", command=self.play)
        self.play_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(master, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)

        self.volume_scale = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.set(self.volume)
        self.volume_scale.pack(side=tk.LEFT)

        self.loop_button = tk.Checkbutton(master, text="Loop", command=self.toggle_loop)
        self.loop_button.pack(side=tk.LEFT)

        self.add_button = tk.Button(master, text="Add", command=self.add_tracks)
        self.add_button.pack(side=tk.LEFT)

        self.remove_button = tk.Button(master, text="Remove", command=self.remove_tracks)
        self.remove_button.pack(side=tk.LEFT)

        pygame.mixer.init()

    def add_tracks(self):

        filenames = fd.askopenfilenames(title="Ajouter des pistes audio")
        for filename in filenames:
            self.playlist.append(filename)
            self.listbox.insert(tk.END, os.path.basename(filename))

    def remove_tracks(self):
        
        selection = self.listbox.curselection()
        for i in reversed(selection):
            self.playlist.pop(i)
            self.listbox.delete(i)

    def play(self):

        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            if self.current_track is None:
                self.current_track = self.playlist[0]
            pygame.mixer.music.load(self.current_track)
            pygame.mixer.music.play()
        self.label.config(text="Lecture en cours : " + os.path.basename(self.current_track))

    def pause(self):
        
        pygame.mixer.music.pause()
        self.paused = True

    def stop(self):
        
        pygame.mixer.music.stop()
        self.current_track = None
        self.paused = False

    def set_volume(self, val):
        
        self.volume = int(val)
        pygame.mixer.music.set_volume(self.volume / 100)

    def toggle_loop(self):

        self.loop = not self.loop
        if self.loop:
            pygame.mixer.music.set_endevent(pygame.USEREVENT)
        else:
            pygame.mixer.music.set_endevent()
    
