import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import os

class YouTubeDownloaderGUI:
    def __init__(self, master):
        self.master = master
        master.title("YouTube Downloader")
        master.geometry('400x250')
        master.resizable(False, False)
        master.configure(bg='#ECECEC')

        self.url_label = tk.Label(master, text="Enter YouTube video URL:", bg='#ECECEC', font=("Helvetica", 12))
        self.url_label.pack(pady=10)

        self.url_entry = tk.Entry(master, width=40)
        self.url_entry.pack()

        self.mp4_button = tk.Button(master, text="Download MP4", bg='#008CBA', fg='white', font=("Helvetica", 12), command=self.download_mp4)
        self.mp4_button.pack(pady=10)

        self.mp3_button = tk.Button(master, text="Download MP3", bg='#008CBA', fg='white', font=("Helvetica", 12), command=self.download_mp3)
        self.mp3_button.pack(pady=10)

        self.directory_frame = tk.Frame(master, bg='#ECECEC')
        self.directory_frame.pack(pady=10)

        self.directory_label = tk.Label(self.directory_frame, text="Save to:", bg='#ECECEC', font=("Helvetica", 10))
        self.directory_label.pack(side=tk.LEFT, padx=10)

        self.directory_entry = tk.Entry(self.directory_frame, width=30)
        self.directory_entry.pack(side=tk.LEFT)

        self.directory_button = tk.Button(self.directory_frame, text="Browse", bg='#008CBA', fg='white', font=("Helvetica", 10), command=self.choose_directory)
        self.directory_button.pack(side=tk.LEFT, padx=10)

        self.status_label = tk.Label(master, text="", bg='#ECECEC', font=("Helvetica", 12))
        self.status_label.pack(pady=10)

        self.directory = ""

    def download_mp4(self):
        url = self.url_entry.get()
        if self.directory == "":
            self.status_label.config(text="Please choose a directory.")
            return
        try:
            video = YouTube(url)
            stream = video.streams.get_highest_resolution()
            filename = stream.default_filename
            stream.download(output_path=self.directory, filename=filename)
            self.status_label.config(text="Download successful!", fg='green')
        except:
            self.status_label.config(text="Download failed.", fg='red')

    def download_mp3(self):
        url = self.url_entry.get()
        if self.directory == "":
            self.status_label.config(text="Please choose a directory.")
            return
        try:
            video = YouTube(url)
            stream = video.streams.get_highest_resolution()
            filename = stream.default_filename
            stream.download(output_path=self.directory, filename=filename)
            video = VideoFileClip(os.path.join(self.directory, filename))
            audio = video.audio
            audio.write_audiofile(os.path.join(self.directory, filename[:-4] + '.mp3'))
            self.status_label.config(text="Download successful!", fg='green')
        except:
            self.status_label.config(text="Download failed.", fg='red')

    def choose_directory(self):
        self.directory = filedialog.askdirectory()
        if self.directory != "":
            self.directory_entry.delete(0, tk.END)
            self.directory_entry.insert(0, self.directory)
            self.status_label.config(text="Directory selected.", fg='green')
        else:
            self.status_label.config(text="Directory selection cancelled.", fg='red')


root = tk.Tk()
youtube_downloader = YouTubeDownloaderGUI(root)
root.mainloop()

