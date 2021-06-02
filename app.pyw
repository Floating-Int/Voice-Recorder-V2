from package import *
from record import AudioManager
from threading import Thread
from tkinter.filedialog import asksaveasfilename as ask_save_as_filename
from tkinter.font import Font, NORMAL, BOLD, ITALIC, ROMAN


class App(Engine):

    def _ready(self):
        Engine.set_target_fps(120)
        self.recording = False
        self.audio_manager = AudioManager()

        # window and canvas style
        div = Canvas(self.window)  # button container - centered
        div.place(relx=0.5, rely=0.5, anchor=CENTER,
                  relheight=0.17, relwidth=0.6)
        div.configure(bg="#ffffff")
        self.window.configure(bg="#252525")

        # main button font
        btn_font = Font(family="Helvetica", size=12, weight=NORMAL)

        # record btn callback
        def toggle(btn):
            self.recording = not self.recording
            if self.recording:
                btn["text"] = "Recording..."
                Thread(target=self.audio_manager.record).start()
            else:
                btn["text"] = "Record"
                self.audio_manager.stop()

        # play btn callback
        def play_sound():
            if type(self.audio_manager.audio) == type(None):
                return  # needs audio
            self.audio_manager.play()

        # save btn callback
        def save_audio_file(btn):
            if type(self.audio_manager.audio) == type(None):
                return  # needs audio
            btn["text"] = "Saving..."
            files = [('All Files', '*.*'),
                     ('Wave File', ".wav"),
                     ('Python Files', '*.py'),
                     ('Text Document', '*.txt')]
            # get path
            full_path = ask_save_as_filename(
                filetypes=files, defaultextension=files
            )  # + ".wav"
            self.audio_manager.config(full_path=full_path)
            self.audio_manager.save()
            btn["text"] = "Save"

        # record btn
        record_btn = Button(master=div, text="Record", bg="#fff")
        record_btn["command"] = lambda: toggle(btn=record_btn)
        record_btn["font"] = btn_font
        record_btn.configure(relief="flat", borderwidth=0,
                             activebackground='#ffffff')
        record_btn.pack()
        # play btn
        play_btn = Button(master=div, text="Play", bg="#fff")
        play_btn["command"] = lambda: play_sound()
        play_btn["font"] = btn_font
        play_btn.configure(relief="flat", borderwidth=0,
                           activebackground='#ffffff')
        play_btn.pack()
        # save btn
        save_btn = Button(master=div, text="Save", bg="#fff")
        save_btn["command"] = lambda: save_audio_file(btn=save_btn)
        save_btn["font"] = btn_font
        save_btn.configure(relief="flat", borderwidth=0,
                           activebackground='#ffffff')
        save_btn.pack()

    def _process(self):
        if Input.is_action_pressed("space"):
            Engine.stop(self.window)  # pass Tk window


# read me:
# https://www.reddit.com/r/Python/comments/7rp4xj/threading_a_tkinter_gui_is_hell_my_least_favorite/

def main():
    # init App
    app = App(title="Voice Recorder V2", favicon="./favicon.ico")


if __name__ == "__main__":
    main()
