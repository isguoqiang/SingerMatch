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
        self.utils = audio_utils.AudioUtils()

    def slice(self, interval=30):
        print("Slicing audios into {}s intervals".format(interval))
        with open(self.original_mp3_dir+'/all.list', 'r') as f1, open(self.clipped_mp3_dir+'/all.list', 'w') as f2:
            for l in f1:
                l = '/' + l.strip()
                input_path = self.original_mp3_dir+l+'.mp3'
                output_prefix = self.clipped_mp3_dir+l
                os.makedirs(os.path.dirname(output_prefix), exist_ok=True)
                slices = self.utils.save_sliced_audio(input_path, output_prefix, interval)
                for sl in slices:
                    f2.write(sl + '\n')
                print("Song {} has been sliced to {}".format(l, len(slices)))

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
