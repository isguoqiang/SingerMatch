from unittest import TestCase
from singermatch.audio_utils import AudioUtils
import librosa
import os


class TestAudioUtils(TestCase):
    def setUp(self) -> None:
        self.utils = AudioUtils()
    #
    # def test_save_spectrogram(self):
    #     self.utils.save_spectrogram('resources/test.mp3', 'resources/test.png')
    #     self.assertTrue(os.path.exists('resources/test.png'))

    # def test_load_vocal_audio(self):
    #     y, sr = librosa.load('resources/test.mp3')
    #     y, sr = self.utils.load_vocal_audio(y, sr)
    #     self.assertTrue(len(y) > 0)

    def test_save_processed_audio(self):
        self.utils.save_processed_audio('resources/test.mp3', 'resources/test_vocal.wav')
        self.assertTrue(os.path.exists('resources/test_vocal.wav'))

    def test_save_sliced_audio(self):
        self.utils.save_sliced_audio('resources/test.mp3', 'resources/test', 30)
        self.assertTrue(os.path.exists('resources/test_0.wav'))
        self.assertTrue(os.path.exists('resources/test_1.wav'))
        self.assertTrue(os.path.exists('resources/test_2.wav'))
        self.assertTrue(os.path.exists('resources/test_3.wav'))
        self.assertTrue(os.path.exists('resources/test_4.wav'))
