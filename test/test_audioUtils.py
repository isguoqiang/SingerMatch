from unittest import TestCase
from singermatch.audio_utils import AudioUtils
import os


class TestAudioUtils(TestCase):
    def setUp(self) -> None:
        self.utils = AudioUtils()

    def test_save_spectrogram(self):
        self.utils.save_spectrogram('resources/test.mp3', 'resources/test.png')
        self.assertTrue(os.path.exists('resources/test.png'))

    def test_save_vocal_audio(self):
        # self.utils.save_vocal_audio('resources/test.mp3', 'resources/test_vocal.wav')
        self.utils.save_vocal_audio('resources/ImYours.mp3', 'resources/test_vocal.wav')
        self.assertTrue(os.path.exists('resources/test_vocal.wav'))