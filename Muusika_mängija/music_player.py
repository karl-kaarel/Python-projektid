from easygui import*
import winsound
import random
import wave

# this function puts different song files into one singular file
# pm - you can change the directory in which songs are first and last
def audio_start():
    muusika_list = ["Can't Feel My Brain Neon Greed.wav", "Warframe OST - Corpus Ship Ambience Extended.wav"]
    sorteeritud_muusika_list = random.sample(muusika_list, len(muusika_list))
    uus_fail = "corpus_tunes.wav"
    
    uus_fail_andmed = []
    for k in sorteeritud_muusika_list:
        fail = wave.open(k, 'rb')
        v = [fail.getparams(), fail.readframes(fail.getnframes())]
        uus_fail_andmed.append(v)
        fail.close()
    tulemus = wave.open(uus_fail, 'wb')
    tulemus.setparams(uus_fail_andmed[0][0])
    for i in range(len(uus_fail_andmed)):
        tulemus.writeframes(uus_fail_andmed[i][1])
    tulemus.close()
    
    winsound.PlaySound(uus_fail, winsound.SND_ASYNC)
    
def audio_stop():
    winsound.PlaySound(None, winsound.SND_ASYNC)
    
def nupud():
    msgbox('end it')

audio_start()
nupud()
audio_stop()
