import librosa
import librosa.display
import soundfile
from matplotlib import pyplot as plt
import numpy as np

class AudioUtils(object):
    def __init__(self):
        pass

    def save_spectrogram(self, mp3_path: str, img_path: str):
        y, sr = librosa.load(mp3_path)
        cqt = librosa.amplitude_to_db(np.abs(librosa.cqt(y, sr=sr)), ref=np.max)
        plt.figure(figsize=(6, 4))
        librosa.display.specshow(cqt)
        plt.axis('off')
        plt.savefig(img_path, bbox_inches='tight', pad_inches=0)

    #
    # extract vocal from mp3 file and save to mp3 file
    # https://librosa.github.io/librosa_gallery/auto_examples/plot_vocal_separation.html
    #
    def save_vocal_audio(self, input_path: str, output_path: str):
        y, sr = librosa.load(input_path)
        S_full, phase = librosa.magphase(librosa.stft(y))
        S_filter = librosa.decompose.nn_filter(S_full,
                                               aggregate=np.median,
                                               metric='cosine',
                                               width=int(librosa.time_to_frames(2, sr=sr)))
        S_filter = np.minimum(S_full, S_filter)
        margin_i, margin_v = 2, 10
        power = 2
        mask_v = librosa.util.softmask(S_full - S_filter,
                                       margin_v * S_filter,
                                       power=power)
        S_foreground = mask_v * S_full
        output_data = librosa.griffinlim(S_foreground)
        soundfile.write(output_path, output_data, sr)