import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from pytube import YouTube
from kivy.uix.filechooser import FileChooserListView

class YouTubeDownloader(GridLayout):
    def __init__(self, **kwargs):
        super(YouTubeDownloader, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Enter YouTube URL:"))
        self.url_input = TextInput(multiline=False)
        self.add_widget(self.url_input)

        self.add_widget(Label(text="Select Resolution:"))
        self.resolution_input = TextInput(multiline=False)
        self.add_widget(self.resolution_input)

        self.save_path_button = Button(text="Select Save Path")
        self.save_path_button.bind(on_press=self.select_save_path)
        self.add_widget(self.save_path_button)

        self.download_button = Button(text="Download")
        self.download_button.bind(on_press=self.download_video)
        self.add_widget(self.download_button)

    def select_save_path(self, instance):
        content = FileChooserListView()
        popup = Popup(title='Select Save Path', content=content, size_hint=(None, None), size=(400, 400))
        content.path = os.path.expanduser("~")
        content.bind(on_submit=self.update_save_path)
        popup.open()

    def update_save_path(self, instance, value):
        self.save_path = value[0]
        popup.dismiss()

    def download_video(self, instance):
        video_url = self.url_input.text
        selected_res = self.resolution_input.text
        if video_url and hasattr(self, 'save_path'):
            try:
                yt = YouTube(video_url)
                streams = yt.streams.filter(progressive=True, file_extension="mp4")
                if selected_res == "Highest":
                    selected_stream = streams.get_highest_resolution()
                else:
                    selected_stream = streams.filter(res=selected_res).first()

                if selected_stream:
                    selected_stream.download(output_path=self.save_path)
                    self.show_popup("Success", "Video is successfully downloaded :)")
                else:
                    self.show_popup("Error", f"No stream found with resolution {selected_res}")

            except Exception as e:
                self.show_popup("Error", str(e))
        else:
            self.show_popup("Error", "Invalid URL or save path")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()


class YouTubeDownloaderApp(App):
    def build(self):
        return YouTubeDownloader()


if __name__ == "__main__":
    YouTubeDownloaderApp().run()
