import librosa
import os
import audio_utils


class Routines(object):
    def __init__(self, config):
        self.workspace = config['DEFAULT']['workspace']
        self.mfcc_dir = config['DEFAULT']['mfcc_dir']
        self.original_mp3_dir = config['DEFAULT']['original_mp3_dir']
        self.filtered_mp3_dir = config['DEFAULT']['filtered_mp3_dir']
        self.clipped_mp3_dir = config['DEFAULT']['clipped_mp3_dir']
        self.cqt_dir = config['DEFAULT']['cqt_dir']
        self.utils = audio_utils.AudioUtils()

    def to_spectrogram(self, skip=0):
        print("Generating spectrograms for clipped mp3s.")
        print("skipping {} lines".format(skip))
        count = 0
        with open(self.clipped_mp3_dir+'/all.list', 'r') as f:
            for l in f:
                count += 1
                if count <= skip:
                    continue
                l = l.strip()
                output_path = l.replace('mp3s-clipped', 'mp3s-cqt').replace('wav', 'png')
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                self.utils.save_spectrogram(l, output_path)
                print("Line {}: CQT generated to {}".format(count, output_path))

    def slice(self, skip=0):
        print("Slicing audios into 30s intervals")
        print("skipping {} lines".format(skip))
        count = 0
        with open(self.original_mp3_dir+'/all.list', 'r') as f1, \
                open(self.clipped_mp3_dir+'/all.list', 'a' if skip > 0 else 'w') as f2:
            for l in f1:
                count += 1
                if count <= skip:
                    continue
                l = '/' + l.strip()
                input_path = self.original_mp3_dir+l+'.mp3'
                output_prefix = self.clipped_mp3_dir+l
                os.makedirs(os.path.dirname(output_prefix), exist_ok=True)
                slices = self.utils.save_sliced_audio(input_path, output_prefix, 30)
                for sl in slices:
                    f2.write(sl + '\n')
                print("Line {}: Song {} has been sliced to {}".format(count, l, len(slices)))

    def filter(self, skip=0):
        print("skipping {} lines".format(skip))
        count = 0
        with open(self.original_mp3_dir+'/all.list', 'r') as f:
            for l in f:
                count += 1
                if count <= skip:
                    continue
                l = '/'+l.strip()
                input_path = self.original_mp3_dir+l+'.mp3'
                output_path = self.filtered_mp3_dir+l+'.wav'
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                self.utils.save_processed_audio(input_path, output_path)
                print("line {}, complete song {}".format(count, l))

    # TODO
    def generate_dataset(self, nsamples: int):
        X = []
        y = []
        with open(self.original_mp3_dir+'/all.list', 'r') as f:
            for l in f:
                l = '/'+l.strip()
                label = l.split('/')[0]
                htk_path = self.mfcc_dir+l+'.htk'
                data = self.utils.read_mfcc(htk_path)