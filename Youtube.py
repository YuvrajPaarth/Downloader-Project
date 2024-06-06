from pytube import YouTube
import tkinter as tk
from tkinter import filedialog, messagebox

def download_video():
    video_url = url_entry.get()
    selected_res = resolution_var.get()
    save_path = open_file_dialog()
    if video_url and save_path:
        try:
            yt = YouTube(video_url)
            streams = yt.streams.filter(progressive=True, file_extension="mp4")
            if selected_res == "Highest":
                selected_stream = streams.get_highest_resolution()

            else:
                selected_stream = streams.filter(res=selected_res).first()

            if selected_stream:
                selected_stream.download(output_path=save_path)
                messagebox.showinfo("Success", "Video is successfully downloaded :)")


            else:
                messagebox.showerror("Error", f"No stream found with resolution {selected_res}")


        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Invalid URL or save path")


def open_file_dialog():
    initial_folder = "/Users/yuvrajpaarth/Movies/Videos"  # Replace this with the path to your default folder
    folder = filedialog.askdirectory(initialdir=initial_folder)
    if folder:
        print(f"Selected folder: {folder}")
        return folder
    else:
        return None


if __name__ =="__main__":
    root = tk.Tk()
    root.geometry("300x200")
    root.title("Youtube downloader")


    url_label = tk.Label(root, text="Enter YouTube URL:")
    url_label.pack()

    url_entry = tk.Entry(root, width=50)
    url_entry.pack()


    #Resolution selection
    resolution_var = tk.StringVar(root)
    resolution_var.set("Highest")
    resolution = ["Highest", "1080p", "720p", "480p", "360p"]
    resolution_label = tk.Label(root, text="Select Resolution")
    resolution_label.pack()
    resolution_menu = tk.OptionMenu(root, resolution_var, *resolution)
    resolution_menu.pack()

    
    browse_button = tk.Button(root, text="Browse", command=download_video)
    browse_button.pack()

    root.mainloop()




#url = "https://youtu.be/NpmFbWO6HPU"
#save_path = "/Users/yuvrajpaarth/Documents/Downloader Project"

#download_video(url, save_path)