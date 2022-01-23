import winsound
import time
import random
import wave
from easygui import*

#Autor: Karl Mathias Fenske

#Paul on 17. aastane õpilane, kes käib gümnaasiumis ja on endale palju
#asju ette plaaninud. 
#Kuid covid - 19 tõttu on koolid läinud üle koduõppele ja poisi
#koormus on kahekordistunud. Sealhulgas on Paul otsustanud
#teha 1 tunnise tööplaani, hommikul kella 8-st kuni 6-ni õhtul,
#kus 45 minuti jooksul võiks tööd teha ja 15 
#minutit puhata. 
#Ta on otsustanud programmeerida endale taimeri. Paul veel tahab
#pausi ajal oma lemmik muusikat kuulata. 
#Koosta programm mis teeb järgmist:

#1)loeb sekundeid 45 minuti vältel ja väljastab iga sekundi koos
#minutitega.(siin saab kasutada time moodulit)

#2)iga kord, kui taimer lõpeb(jõuab 45 minutini), siis segab
#programm muusikapalad suvalises järjekorras. 
      #!kasutama peab winsound moodulit, et muusikat mängida.
        #-) fail peaks olema .wav formaadiga
        #-) faili mängimist saab alustada järgmise koodiga: winsound.PlaySound(\.wav\, winsound.SND_ASYNC)
        #-) faili saab sulgeda järgmise koodiga: winsound.PlaySound(None, winsound.SND_ASYNC)

#3)kui taimer on jõudnud 45 minuti juurde tegutseb programm easygui-ga
#järgmiselt, sellises järjekorras:
        
#!muusikat peab koos kastiga mängima. Kuna programm jääb seisma sellel ajal kui kast ekraanile kuvatakse, 
#siis saab tehniliselt kastiga koos mängida ühest failist. See tähendab, et kuna meil on mitu muusikapala, 
#tuleb kõik ühte faili tõsta. (siin saab kasutada moodulit wave)
    
   # 1. ütleb, et on pausi aeg ja küsib kasutajalt kas ta soovib muusika peatada.
            #1.1 kui kasutaja soovib, siis muusika peatub ja programm
                #liigub edasi.
            #1.2 kui kasutaja ei soovi, siis küsib programm uuesti,
                #kas kasutaja on kindel et EI soovi muusikat peatada.
                    #1.2.1 kui kasutaja valib 'jah', et on nõus, siis
                          #muusika EI peatu ja programm liigub edasi.
                    #1.2.2 kui ei, siis muusika peatub.
    #2. küsib kasutajalt, kas ta soovib taimerit uuesti alustada.

#funktsioon paneb muusika mangima ja segab mangimise jarjekorra. Tahaks siin veel viidata jargmisi: Tom10, Ardweaden 
def audio_start():
    muusika_list = ['Beneath the Mask.wav', 'Heaven.wav', 'Take Over.wav', 'When Mother Was There.wav', 'With the Stars _ Us(no vocal).wav']
    sorteeritud_muusika_list = random.sample(muusika_list, len(muusika_list))
    uus_fail = 'koik_muusikad'
    
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

#funktsioon lopetab muusika mangimise
def audio_stop():
    winsound.PlaySound(None, winsound.SND_ASYNC)

#funktsioon toob esile esimese ja teise easygui kasti, mis otsustab muusika lopetamise voi edasimangimise
def kast1():
    nupp = ['Jah', 'Ei']
    v = buttonbox('Aeg teha paus. Kas soovite muusika lõpetada?', choices = nupp)
    if v == nupp[0]:
        audio_stop()
    elif v == nupp[1]:
        v1 = buttonbox('Kas olete kindel? Kui vajutate nupule EI, siis muusika peatub', choices = nupp)
        if v1 == nupp[1]:
            audio_stop()

#funktsioon toob esile viimase easygui kasti, mis otsustab kas taimer loppeb voi mitte
def kast2():
    nupp = ['Jah', 'Ei']
    v = buttonbox('Soovite taimeriga jätkata?', choices = nupp)
    if not v == nupp[0]:
        return 1
    else:
        return None

END = 5 #See muutuja defineerib taimeri lopu
s = 0 #sekundid
m = 0 #minutid

#terve programm tootab pohiliselt siin, kus koik eelnevad funktsioonid ja muutujad esinevad
loop = True
while loop:
    s += 1
    print(m, 'minutit', s, 'sekundit')
    time.sleep(1)
    if s == 60:
        m += 1
        s = 0
    if s == END:
        print()
        print("Alustamine")
        s = 0
        m = 0
        audio_start()
        kast1()
        vastus = kast2()
        if vastus == 1:
            loop = False
            audio_stop()
