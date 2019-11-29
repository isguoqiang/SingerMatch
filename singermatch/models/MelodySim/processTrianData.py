# reading mp3 files, extract melody bags of music, write to the file
from melodyCount import audio_to_midi_melodia

count = 0
for line in open("/Users/mac126/19fall/cs258/assign2/data/artist20/mp3s-32k/all.list"):
    path = "/Users/mac126/19fall/cs258/assign2/data/artist20/mp3s-32k/" + line.strip("\n") + ".mp3"
    f = open(path)
    f.close()
    count += 1
    print("All files exits!")

dataSet = []
fwrite = open("dataSet.txt", 'w')
for line in open("/Users/mac126/19fall/cs258/assign2/data/artist20/mp3s-32k/all.list"):
    artist, album, music = line.strip('\n').split("/")
    print(music)

    feature = audio_to_midi_melodia("/Users/mac126/19fall/cs258/assign2/data/artist20/mp3s-32k/"
                                    + artist + "/" + album + "/" + music + ".mp3")
    feature.append(album)
    feature.append(artist)
    dataSet.append(feature)
    featureString = ",".join(feature)
    print(featureString)
    fwrite.write(featureString + "\n")
    count -= 1
    print(count)
fwrite.close()

