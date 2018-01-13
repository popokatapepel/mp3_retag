# -*- coding: utf-8 -*-
import os
from os.path import join, getsize
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.mp3 import MPEGInfo
from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC, TRCK, TPOS

from time import sleep

path="/home/janniklas/Musik/Marc-Uwe Kling/QualityLand"
ext=".mp3"
output=[]
print (os.listdir(path))
for file in os.listdir(path):
    if file.endswith(ext):
        output.append(os.path.join(path, file))

filearray=[]
i=1
for filePath in output:
    mp3file = MP3(filePath)
    trk=str(mp3file["TRCK"]).split("/")[0]
    key=int(str(mp3file["TPOS"])+str(trk).zfill(3))
    filearray.append((key,mp3file,filePath))

filearray.sort()
trk=1
for f in filearray:
    f[1]["TCON"] = TCON(encoding=3, text=u'Audiobook')
    f[1]["TPOS"]=TPOS(encoding=3, text=u'')
    f[1]["TRCK"] = TRCK(encoding=3, text=str(trk))
    f[1].save()

    print(os.path.basename(f[2]))
    newfilename=os.path.join(os.path.dirname(f[2]),str(trk).zfill(2)+os.path.basename(f[2])[2:])
    print(newfilename)
    print(trk,f[0],f[1]["TRCK"])
    os.rename(f[2],newfilename)
    trk+=1


print(filearray)