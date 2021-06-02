# sound libs
from sounddevice import rec as _record_audio
from sounddevice import wait as _wait_for_interupt
from sounddevice import stop as _stop_audio_recording
from scipy.io.wavfile import write as _write_audio
# input
import keyboard
# timing
from time import time
# store audio in an np.ndarray
import numpy as np


# test
from sounddevice import play as _play


class AudioManager:
    """ Used to record, stop and write a .wav audio file """

    # test
    def play(self):
        _play(self.audio, self.fs)

    def __init__(self):
        self.fs = 44100
        self.channels = 1
        self.MAX_SECONDS = 120
        self.path = None
        self.name = None
        self.extension = None
        self.full_path = None  # used if set
        self.audio = None  # acts kinda like a Global

    def config(self, **kwargs):  # example .config(name="new")
        for key, value in kwargs.items():
            if key not in self.__dict__:
                raise AttributeError(
                    "Can not add nonexistent atribute '" + str(key) + "'")
            setattr(self, key, value)

    def record(self):
        # start recording
        # print("Recording...")
        start_time = time()  # for calculating new numpy array size

        self.audio = _record_audio(  # start recording
            int(self.MAX_SECONDS * self.fs),
            samplerate=self.fs,
            channels=self.channels
        )
        _wait_for_interupt()  # stopped by self.stop()
        #print("Stopped Recording")

        # get amount of seconds elapsed
        end_time = time()
        time_difference = -start_time + end_time
        audio_length = int(time_difference * self.fs)

        # edit np.ndarray here
        self.audio = self.audio[int(self.fs/5):audio_length]

    def stop(self):
        _stop_audio_recording()

    def save(self):  # needs config or else will use defaults
        # try use full_path when saving audio
        if self.full_path:
            _write_audio(self.full_path, self.fs, self.audio)

        else:  # get full path form path, name and extension summed
            path = self.path if self.path else "./Out"
            name = self.name if self.name else "new_audio_file"
            extension = self.extension if self.extension else ".wav"
            # save audio
            _write_audio(
                # example output: "Output/output.wav",
                "/".join([path, name]) + extension,
                self.fs,
                self.audio
            )


"""
('System', 'Terminal', 'Fixedsys', 'Modern', 'Roman', 'Script', 'Courier'MS Sans Serif', 'Small Fonts', 'TeamViewer15', 'Marlett', 'Arial', 'Arabi 'Arial Baltic', 'Arial CE', 'Arial CYR', 'Arial Greek', 'Arial TUR', 'Arhnschrift Light', 'Bahnschrift SemiLight', 'Bahnschrift', 'Bahnschrift Sechrift Light SemiCondensed', 'Bahnschrift SemiLight SemiConde', 'Bahnschred', 'Bahnschrift SemiBold SemiConden', 'Bahnschrift Light Condensed', 'BLight Condensed', 'Bahnschrift Condensed', 'Bahnschrift SemiBold Condense
'Calibri Light', 'Cambria', 'Cambria Math', 'Candara', 'Candara Light', ' 'Consolas', 'Constantia', 'Corbel', 'Corbel Light', 'Courier New', 'Cour, 'Courier New CE', 'Courier New CYR', 'Courier New Greek', 'Courier New  'Franklin Gothic Medium', 'Gabriola', 'Gadugi', 'Georgia', 'Impact', 'Inese Text', 'Leelawadee UI', 'Leelawadee UI Semilight', 'Lucida Console', icode', 'Malgun Gothic', '@Malgun Gothic', 'Malgun Gothic Semilight', '@Mmilight', 'Microsoft Himalaya', 'Microsoft JhengHei', '@Microsoft JhengHe
JhengHei UI', '@Microsoft JhengHei UI', 'Microsoft JhengHei Light', '@Mic Light', 'Microsoft JhengHei UI Light', '@Microsoft JhengHei UI Light', 'ai Lue', 'Microsoft PhagsPa', 'Microsoft Sans Serif', 'Microsoft Tai Le',ei', '@Microsoft YaHei', 'Microsoft YaHei UI', '@Microsoft YaHei UI', 'Miight', '@Microsoft YaHei Light', 'Microsoft YaHei UI Light', '@Microsoft , 'Microsoft Yi Baiti', 'MingLiU-ExtB', '@MingLiU-ExtB', 'PMingLiU-ExtB',B', 'MingLiU_HKSCS-ExtB', '@MingLiU_HKSCS-ExtB', 'Mongolian Baiti', 'MS Gthic', 'MS UI Gothic', '@MS UI Gothic', 'MS PGothic', '@MS PGothic', 'MV  Text', 'Nirmala UI', 'Nirmala UI Semilight', 'Palatino Linotype', 'Segoe
'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Black', 'Segoe UI Em Historic', 'Segoe UI Light', 'Segoe UI Semibold', 'Segoe UI Semilight', l', 'SimSun', '@SimSun', 'NSimSun', '@NSimSun', 'SimSun-ExtB', '@SimSun-Ehic UI Semibold', '@Yu Gothic UI Semibold', 'Yu Gothic Light', '@Yu Gothic Light', 'Yu Gothic UI Light', '@Yu Gothic UI Light', 'Yu Gothic Medium', '@Yu Gothic Medium', 'Yu Gothic UI Semilight', '@Yu Gothic UI Semilight')
"""
