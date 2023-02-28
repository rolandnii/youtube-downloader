import tkinter
import customtkinter
from pytube import YouTube

# Sytem Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.geometry("720x360")
app.title("Yotube Downloader")

# Adding ui 
title = customtkinter.CTkLabel(app, text = "Insert a youtube link")
title.pack(padx=10,pady=10)


# Run app
app.mainloop()