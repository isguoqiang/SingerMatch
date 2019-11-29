# This code is referring below github repo:
# https://github.com/justinsalamon/audio_to_midi_melodia/blob/master/audio_to_midi_melodia.py
#
from collections import defaultdict

import soundfile
import resampy
import vamp
import argparse
import os
import numpy as np
from midiutil.MidiFile import MIDIFile
from scipy.signal import medfilt
import ext
import librosa
import audioread



'''
Extract the melody from an audio file and count the frequency of different melody of each file.

The script extracts the melody from an audio file using the Melodia algorithm,
and then segments the continuous pitch sequence into a series of quantized
notes

Note: Melodia can work pretty well and is the result of several years of
research. The note segmentation/quantization code was hacked in about 30
minutes. Proceed at your own risk... :)

usage: audio_to_midi_melodia.py [-h] [--smooth SMOOTH]
                                [--minduration MINDURATION] [--jams]
                                infile outfile bpm


Examples:
python audio_to_midi_melodia.py --smooth 0.25 --minduration 0.1 --jams
                                ~/song.wav ~/song.mid 60
'''


def midi_to_notes(midi, fs, hop, smooth, minduration):

    # smooth midi pitch sequence first
    if (smooth > 0):
        filter_duration = smooth  # in seconds
        filter_size = int(filter_duration * fs / float(hop))
        if filter_size % 2 == 0:
            filter_size += 1
        midi_filt = medfilt(midi, filter_size)
    else:
        midi_filt = midi
    # print(len(midi),len(midi_filt))

    notes = []
    p_prev = None
    duration = 0
    onset = 0
    for n, p in enumerate(midi_filt):
        if p == p_prev:
            duration += 1
        else:
            # treat 0 as silence
            if p_prev > 0:
                # add note
                duration_sec = duration * hop / float(fs)
                # only add notes that are long enough
                if duration_sec >= minduration:
                    onset_sec = onset * hop / float(fs)
                    notes.append((onset_sec, duration_sec, p_prev))

            # start new note
            onset = n
            duration = 1
            p_prev = p

    # add last note
    if p_prev > 0:
        # add note
        duration_sec = duration * hop / float(fs)
        onset_sec = onset * hop / float(fs)
        notes.append((onset_sec, duration_sec, p_prev))

    return notes


def hz2midi(hz):

    # convert from Hz to midi note
    hz_nonneg = hz.copy()
    idx = hz_nonneg <= 0
    hz_nonneg[idx] = 1
    midi = 69 + 12*np.log2(hz_nonneg/440.)
    midi[idx] = 0

    # round
    midi = np.round(midi)

    return midi


def audio_to_midi_melodia(infile):

    # define analysis parameters
    fs = 44100
    hop = 128

    # load audio using librosa
    print("Loading audio...")
    data, sr = librosa.load(infile)
    # data, sr = soundfile.read(infile)
    # mixdown to mono if needed
    if len(data.shape) > 1 and data.shape[1] > 1:
        data = data.mean(axis=1)
    # resample to 44100 if needed
    if sr != fs:
        data = resampy.resample(data, sr, fs)
        sr = fs

    # extract melody using melodia vamp plugin
    print("Extracting melody f0 with MELODIA...")
    melody = vamp.collect(data, sr, "mtg-melodia:melodia",
                          parameters={"voicing": 0.2})

    # hop = melody['vector'][0]
    pitch = melody['vector'][1]

    # impute missing 0's to compensate for starting timestamp
    pitch = np.insert(pitch, 0, [0]*8)

    # debug
    # np.asarray(pitch).dump('f0.npy')
    # print(len(pitch))

    # convert f0 to midi notes
    print("Converting Hz to MIDI notes...")
    midi_pitch = hz2midi(pitch)

    # convert midi_pitch list to midi_pitch count bag
    pitch_bag = [0] * 130
    for p in midi_pitch:
        pitch_bag[int(p)] += 1
    # pitch_bag = defaultdict(int)
    # for p in midi_pitch:
    #     pitch_bag[p] += 1
    # print(pitch_bag)
    pitch_bag_str = [str(i) for i in pitch_bag]
    return pitch_bag_str


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="Path to input audio file.")
    args = parser.parse_args()
    audio_to_midi_melodia(args.infile)