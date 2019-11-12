# SingerMatch  
The project is to explore ML approaches to match singers (Or find singer) for audio files.   
This classification task is also known as Artist Identification in Music Information Retrieval field and Voice Recognition in Speech Recognition field.


## Dataset  
We will be using the [artist20](https://labrosa.ee.columbia.edu/projects/artistid/) dataset provided by LabROSA. This is a dataset of six albums by each of 20 artists, making a total of 1,413 tracks (~100 hours).   
Here are a few interesting findings about the dataset and the artists:  
*TODO*

## Predictive Task
The task is straightforward: Given a song audio, we want to predict its artist. 

Average accuracy and F1 score from 6-fold testing are used to evaluate our models. Guessing the most common class gives a baseline accuracy of 6%. Our results are also compared to [a better baseline](http://www.ee.columbia.edu/~dpwe/pubs/Ellis07-timbrechroma.pdf) provided by the LabROSA group. In the future, we are considering to develop an even stronger baseline using [Microsoft Speaker Recognition API](https://azure.microsoft.com/en-us/services/cognitive-services/speaker-recognition/).

## Feature Extraction
The major difficulty of this task lies in extracting features from the audio that best represents the nature of a singer's voice. One useful thing we can intuitively think of is a singer's vocal range, which is effective in distinguishing male singers and female singers. The vocal range of John Lennon(The Beatles) is B1-A5, Thom York(Radiohead)'s is E2-E6, Freddie Mercury(Queen) is F2-E6, more artists' vocal ranges can be found [here](https://www.concerthotels.com/worlds-greatest-vocal-ranges). If we know the distribution of a song's notes, maybe we can infer the artist better than random guess.

But what is the nature of a singer's voice? Traditional ML approaches usually consider two aspects: The timbre information (such as MFCC coeffiecients) and pitch profiles (a.k.a. Chroma features).  Modern ML models, however, tend to treat audio as images and let neural networks extract features. In a recent research[1] on the same dataset, the authors train the neural network using [spectrogram](https://en.wikipedia.org/wiki/Spectrogram) images of the songs. Raw wave images are also considered for similar tasks. Paper [2] even find out that wave images perform better than spectrograms in large dataset.

\* The main aim of this project is to explore different learning models, so our primary focus is on MFCC and Chroma features. We will also look into image processing field to see if we can come up with a better model. If time permits, we will train a CNN model.

## Models
One major difference of this project compared to other papers is that we make an assumption that only vocal melody should be used to identify an artist. This assumption appeals to common sense: A singer can try out different genres and play different instruments, but we always know it's him/her because of the unique voice. One can argue that this assumption ignores the play-style preferences of singers, but it brings greater benefits, which we will verify later, by erasing the non-vocal noises in timbre and pitch features. More importantly, this assumption transforms the task into the voice recognition problem, which has been studied for decades.   
To realize this assumption, we will do the following pre-process to the MP3 files:
1. Use REPET-SIM (see [8]) method to separate vocals. See tutorial [here](https://librosa.github.io/librosa_gallery/auto_examples/plot_vocal_separation.html).
2. Use [Melodia Algorithm](https://www.upf.edu/web/mtg/melodia) to find frames where melody is present (a.k.a. voicing detection). Frames without melody are discarded.   

After preprocessing, the mp3 file will contain only vocal sounds and no pause.

In this project, different features and different models in order to find the best model for this task. 
### Similarity model based on Chroma features and Bag of Pitches
TODO
### GMM model based on foreground MFCC features
TODO
### SVM model based on foreground MFCC features
TODO
### *TODO*

## Results
TODO
## References
1. [Music Artist Classification with Convolutional Recurrent Neural Networks](https://arxiv.org/pdf/1901.04555.pdf).
2. [End-to-End Learning for Music Audio Tagging](http://ismir2018.ircam.fr/doc/pdfs/191_Paper.pdf).
3. [Detecting Music Genre Using Extreme Gradient Boosting](https://dbis.uibk.ac.at/sites/default/files/2018-04/music_genre_detection.pdf).
4. [Borderline: How to train a ConvNet to classify sounds](https://github.com/jerpint/Borderline).
5. [An overview of automatic speaker recognition technology](https://ieeexplore.ieee.org/abstract/document/5745552).
6. [A hands-on tutorial on identifying speakers with voice recognition](https://subscription.packtpub.com/book/big_data_and_business_intelligence/9781787125193/9/ch09lvl1sec61/identifying-speakers-with-voice-recognition).
7. [Support vector machines for speaker and language recognition](https://www.sciencedirect.com/science/article/pii/S0885230805000318).
8. [Music-Voice Separation using the Similarity Matrix](https://users.cs.northwestern.edu/~zra446/doc/Rafii-Pardo%20-%20Music-Voice%20Separation%20using%20the%20Similarity%20Matrix%20-%20ISMIR%202012.pdf).
9. [Melody Extraction From Polyphonic Music Signals Using Pitch Contour Characteristics](https://ieeexplore.ieee.org/abstract/document/6155601).