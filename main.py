# -*- coding: utf-8 -*-
import os
from os.path import join, getsize
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.mp3 import MPEGInfo
from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC, TRCK

from time import sleep

path="/media/win/temp/Die drei Fragezeichen"
ext=".mp3"
output=[]
print (os.listdir(path))
for file in os.listdir(path):
    if file.endswith(ext):
        output.append(os.path.join(path, file))

output.sort()
i=1
for filePath in output:
    fname=os.path.splitext(os.path.basename(filePath))[0]
    info=fname.replace(" - Die drei Fragezeichen","")
    trk=int(info[0:3])
    tit=info[6:]
    print(trk, tit)

    mp3file = MP3(filePath)
    print(filePath)
    #mp3file["TPE1"] = TPE1(encoding=3, text=u'J.K. Rowling')
    mp3file["TCON"] = TCON(encoding=3, text=u'Audiobook')
    mp3file["TRCK"] = TRCK(encoding=3, text=str(trk))
    mp3file["TALB"] = TALB(encoding=3, text=u'Die drei Fragezeichen')
    #mp3file.save()
    i=i+1
    print(mp3file.pprint())
    print('############################')
