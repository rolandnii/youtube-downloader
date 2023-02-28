import tkinter
import customtkinter
from pytube import YouTube
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink,on_progress_callback=on_progress)
        title.configure(text=ytObject.title,text_color='white')
        # video.download()
        finishLabel.configure(text="Downloaded")
        
    except:
        finishLabel.configure(text="Ops!, An internal error occured",text_color="red")
    
def on_progress():
    pass
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

#link input
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=300,height=35, textvariable=url)
link.pack()

#add text
finishLabel = customtkinter.CTkLabel(app,text="")
finishLabel.pack()

# download button
download = customtkinter.CTkButton(app,text="Download",command=startDownload)
download.pack(pady=10)

#progress
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=300)
progressBar.set(0.5)
progressBar.pack()


# Run app
app.mainloop()