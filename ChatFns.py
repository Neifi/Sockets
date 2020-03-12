from Tkinter import *
from socket import *
import urllib
import re
import pygame
import base64
import time
#import win32gui

HOST = 'localhost'



def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan
def initMixer():
    BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)
def playsound(soundfile):
    """Play sound through default mixer channel in blocking manner.
       This will load the whole sound into memory before playback
    """
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(soundfile)
    clock = pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
        clock.tick(1000)
def playmusic(soundfile):
    """Stream music with mixer.music module in blocking manner.
       This will stream the sound from disk while playing.
    """
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(soundfile)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(1000)
def stopmusic():
    """stop currently playing music"""
    pygame.mixer.music.stop()

#HOW TO PLAY SONG:
initMixer()
#playmusic(filename)



def FlashMyWindow(title):
    pass
    #ID = win32gui.FindWindow(None, title)
    #win32gui.FlashWindow(ID,True)

def FlashMyWindow2(title2):
    ID2 = win32gui.FindWindow(None, title2)
    win32gui.FlashWindow(ID2,True)

def GetExternalIP():
    url = "http://checkip.dyndns.org"
    request = urllib.urlopen(url).read()
    return str(re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request))

def GetInternalIP():
    return str(gethostbyname(getfqdn()))

def FilteredMessage(EntryText):
    """
    Filter out all useless white lines at the end of a string,
    returns a new, beautifully filtered string.
    """
    EndFiltered = ''
    for i in range(len(EntryText)-1,-1,-1):
        if EntryText[i]!='\n':
            EndFiltered = EntryText[0:i+1]
            break
    for i in range(0,len(EndFiltered), 1):
            if EndFiltered[i] != "\n":
                    return EndFiltered[i:]+'\n'
    return ''

def LoadConnectionInfo(ChatLog, EntryText):
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            ChatLog.insert(END, EntryText+'\n')
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)

def LoadMyEntry(ChatLog, EntryText):
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            LineNumber = float(ChatLog.index('end'))-1.0
            ChatLog.insert(END, "You: " + EntryText)
            ChatLog.tag_add("You", LineNumber, LineNumber+0.4)
            ChatLog.tag_config("You", foreground="#FF8000", font=("Arial", 12, "bold"))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)


def LoadOtherEntry(ChatLog, EntryText):
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            try:
                LineNumber = float(ChatLog.index('end'))-1.0
            except:
                pass
            text = EntryText.split(':',1)
            ChatLog.insert(END, text[0] + ": " + text[1])
            ChatLog.tag_add(text[0] + ": ", LineNumber, LineNumber+float('0.' + str(len(text[0] + ":"))))
            ChatLog.tag_config(text[0] + ": ", foreground="#04B404", font=("Arial", 12, "bold"))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)


def sendImg(s, path):
    print(s)
    img = open(path, 'rb')
    data = img.read()
    c_data = data.encode('base64')
    size = len(c_data)
    print "path es "+path+" Size " +str(size)
    s.sendall('/img '+str(size)+ " "+c_data)
    #time.sleep(1)
    #s.sendall('/img '+c_data)
    


def reciveImg(s,size):
    img = open('/home/neifi/Imatges/android-logo_server.png', 'wb')

    t = s.recv(409600)
    datos = t.split(" ")
    size = int(datos[1])
    enconded_img = datos[2]
    r_size = 0
    print size
     
    dt = enconded_img.decode()
    print "[INFO] IMAGEN es esto: "+enconded_img
    img.write(dt)


PORT = 6009


#/home/neifi/Imatges/android-logo.png
