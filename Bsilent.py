import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest


from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest


from Config import STRING, SUDO, BIO_MESSAGE, ALIVE_NAME, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 , STRING22 , STRING23 , STRING24 , STRING25 , STRING26 , STRING27 , STRING28 , STRING29 , STRING30
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import مغادرهChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID


a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleve = STRING11
twelv = STRING12
thirt = STRING13
forte = STRING14
fifth = STRING15
sieee = STRING16
seeee = STRING17
eieee = STRING18
nieee = STRING19
gandu = STRING20
ekish = STRING21
baish = STRING22
teish = STRING23
tfour = STRING24
tfive = STRING25
tsix = STRING26
tseven = STRING27
teight = STRING28
tnine = STRING29
thirty = STRING30



idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""
vkk = ""
kkk = ""
lkk = ""
mkk = ""
sid = ""
shy = ""
aan = ""
ake = ""
eel = ""
khu = ""
shi = ""
yaa = ""
dav = ""
raj = ""
put = ""
eag = ""
gle = ""
wal = ""
aaa = ""
boy = ""



que = {}

SMEX_USERS = [1281418521, 431860002, 1018096414]
for x in SUDO: 
    SMEX_USERS.append(x)
    
async def start_flash():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    global vkk
    global kkk
    global lkk
    global mkk
    global sid
    global shy
    global aan
    global ake
    global eel
    global khu
    global shi
    global yaa
    global dav
    global raj
    global put
    global eag
    global gle
    global wal
    global aaa
    global boy
    
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            await idk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await idk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await idk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await idk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await idk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            await ydk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await ydk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await ydk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await ydk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await ydk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            await wdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await wdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await wdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await wdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await wdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            await hdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await hdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await hdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await hdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await hdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            await sdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await sdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await sdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await sdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await sdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            await adk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await adk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await adk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await adk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await adk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            await bdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await bdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await bdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await bdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await bdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            await cdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await cdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await cdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await cdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await cdk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            await ddk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await ddk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await ddk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await ddk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await ddk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            await edk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await edk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await edk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await edk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await edk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk.start()
        except Exception as e:
            pass 
        
    
    if eleve:
        session_name = str(eleve)
        print("String 11 Found")
        vkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await vkk.start()
            await vkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await vkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await vkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await vkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await vkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await vkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "startup"
        vkk = TelegramClient(session_name, a, b)
        try:
            await vkk.start()
        except Exception as e:
            pass
        
    
    if twelv:
        session_name = str(twelv)
        print("String 12 Found")
        kkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await kkk.start()
            await kkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await kkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await kkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await kkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await kkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await kkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        kkk = TelegramClient(session_name, a, b)
        try:
            await kkk.start()
        except Exception as e:
            pass   
    
  
    if thirt:
        session_name = str(thirt)
        print("String 13  Found")
        lkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await lkk.start()
            await lkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await lkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await lkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await lkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await lkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await lkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        lkk = TelegramClient(session_name, a, b)
        try:
            await lkk.start()
        except Exception as e:
            pass 
        
    
    if forte:
        session_name = str(forte)
        print("String 14 Found")
        mkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await mkk.start()
            await mkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await mkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await mkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await mkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await mkk(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await mkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        mkk = TelegramClient(session_name, a, b)
        try:
            await mkk.start()
        except Exception as e:
            pass
        
    
    if fifth:
        session_name = str(fifth)
        print("String 15 Found")
        sid = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await sid.start()
            await sid(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await sid(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await sid(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await sid(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await sid(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await sid.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        sid = TelegramClient(session_name, a, b)
        try:
            await sid.start()
        except Exception as e:
            pass


    if sieee:
        session_name = str(sieee)
        print("String 16 Found")
        shy = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 16")
            await shy.start()
            botme = await shy.get_me()
            await shy(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await shy(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await shy(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await shy(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await shy(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        shy = TelegramClient(session_name, a, b)
        try:
            await shy.start()
        except Exception as e:
            pass
   
    if seeee:
        session_name = str(seeee)
        print("String 17 Found")
        aan = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 17")
            await aan.start()
            botme = await aan.get_me()
            await aan(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await aan(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await aan(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await aan(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await aan(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        aan = TelegramClient(session_name, a, b)
        try:
            await aan.start()
        except Exception as e:
            pass
   
    if eieee:
        session_name = str(eieee)
        print("String 18 Found")
        ake = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 18")
            await ake.start()
            botme = await ake.get_me()
            await ake(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await ake(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await ake(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await ake(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await ake(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        ake = TelegramClient(session_name, a, b)
        try:
            await ake.start()
        except Exception as e:
            pass
   
    if nieee:
        session_name = str(nieee)
        print("String 19 Found")
        eel = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 19")
            await eel.start()
            botme = await eel.get_me()
            await eel(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await eel(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await eel(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await eel(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await eel(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        eel = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if gandu:
        session_name = str(gandu)
        print("String 20 Found")
        khu = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 20")
            await khu.start()
            botme = await khu.get_me()
            await khu(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await khu(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await khu(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await khu(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await khu(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        khu = TelegramClient(session_name, a, b)
        try:
            await khu.start()
        except Exception as e:
            pass
   
    if ekish:
        session_name = str(ekish)
        print("String 21 Found")
        shi = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 21")
            await shi.start()
            botme = await shi.get_me()
            await shi(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await shi(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await shi(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await shi(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await shi(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        shi = TelegramClient(session_name, a, b)
        try:
            await shi.start()
        except Exception as e:
            pass
   
    if baish:
        session_name = str(baish)
        print("String 22 Found")
        yaa = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 22")
            await yaa.start()
            botme = await yaa.get_me()
            await yaa(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await yaa(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await yaa(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await yaa(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await yaa(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "startup"
        yaa = TelegramClient(session_name, a, b)
        try:
            await yaa.start()
        except Exception as e:
            pass
   
    if teish:
        session_name = str(teish)
        print("String 23 Found")
        dav = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 23")
            await dav.start()
            botme = await dav.get_me()
            await dav(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await dav(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await dav(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await dav(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await dav(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "startup"
        dav = TelegramClient(session_name, a, b)
        try:
            await dav.start()
        except Exception as e:
            pass
   
    if tfour:
        session_name = str(tfour)
        print("String 24 Found")
        raj = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 24")
            await raj.start()
            botme = await raj.get_me()
            await raj(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await raj(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await raj(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await raj(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await raj(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "startup"
        raj = TelegramClient(session_name, a, b)
        try:
            await raj.start()
        except Exception as e:
            pass
   
    if tfive:
        session_name = str(tfive)
        print("String 25 Found")
        put = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 25")
            await put.start()
            botme = await put.get_me()
            await put(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await put(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await put(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await put(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await put(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "startup"
        put = TelegramClient(session_name, a, b)
        try:
            await put.start()
        except Exception as e:
            pass
   
    if tsix:
        session_name = str(tsix)
        print("String 26 Found")
        eag = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 26")
            await eag.start()
            botme = await eag.get_me()
            await eag(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await eag(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await eag(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await eag(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await eag(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        session_name = "startup"
        eag = TelegramClient(session_name, a, b)
        try:
            await eag.start()
        except Exception as e:
            pass
   
    if tseven:
        session_name = str(tseven)
        print("String 27 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 27")
            await gle.start()
            await gle(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await gle(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await gle(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await gle(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await gle(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await gle.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "startup"
        gle = TelegramClient(session_name, a, b)
        try:
            await gle.start()
        except Exception as e:
            pass

    if teight:
        session_name = str(teight)
        print("String 28 Found")
        wal = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 28")
            await wal.start()
            await wal(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await wal(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await wal(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await wal(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await wal(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await wal.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "startup"
        wal = TelegramClient(session_name, a, b)
        try:
            await wal.start()
        except Exception as e:
            pass

    if tnine:
        session_name = str(tnine)
        print("String 29 Found")
        aaa = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 29")
            await aaa.start()
            await aaa(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await aaa(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await aaa(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await aaa(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await aaa(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await aaa.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "startup"
        aaa = TelegramClient(session_name, a, b)
        try:
            await aaa.start()
        except Exception as e:
            pass

    if thirty:
        session_name = str(thirty)
        print("String 30 Found")
        boy = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 30")
            await boy.start()
            await boy(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await boy(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await boy(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await boy(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            await boy(functions.channels.JoinChannelRequest(channel="@Bsilent_spam"))
            botme = await boy.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "startup"
        boy = TelegramClient(session_name, a, b)
        try:
            await boy.start()
        except Exception as e:
            pass
                  
   
loop = asyncio.get_event_loop()
loop.run_until_complete(start_flash())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass


@idk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(flash) == 2:
            message = str(flash[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(flash[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(flash[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
            
            
@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@adk.on(events.NewMessage(incoming=True))
@bdk.on(events.NewMessage(incoming=True))
@cdk.on(events.NewMessage(incoming=True))
@edk.on(events.NewMessage(incoming=True))
@ddk.on(events.NewMessage(incoming=True))
@vkk.on(events.NewMessage(incoming=True))
@kkk.on(events.NewMessage(incoming=True))
@lkk.on(events.NewMessage(incoming=True))
@mkk.on(events.NewMessage(incoming=True))
@sid.on(events.NewMessage(incoming=True))
@shy.on(events.NewMessage(incoming=True))
@aan.on(events.NewMessage(incoming=True))
@ake.on(events.NewMessage(incoming=True))
@eel.on(events.NewMessage(incoming=True))
@khu.on(events.NewMessage(incoming=True))
@shi.on(events.NewMessage(incoming=True))
@yaa.on(events.NewMessage(incoming=True))
@dav.on(events.NewMessage(incoming=True))
@raj.on(events.NewMessage(incoming=True))
@put.on(events.NewMessage(incoming=True))
@eag.on(events.NewMessage(incoming=True))
@gle.on(events.NewMessage(incoming=True))
@wal.on(events.NewMessage(incoming=True))
@aaa.on(events.NewMessage(incoming=True))
@boy.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )
        

@idk.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.سبام")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.سبام")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.سبام")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.سبام")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.سبام")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.سبام"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.سبام <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use سبام ضخم."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(flash) == 2:
            message = str(flash[1])
            counter = int(flash[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(flash[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(flash[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.انضمام"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.انضمام <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = flash[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.اشتموه"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.اشتموه <Username of User>\n\n.اشتموه <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(flash[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid")) 
@ake.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(flash[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك")) 
@ake.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.انضمام لينك"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.انضمام لينك <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.انضمام لينك HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = flash[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@idk.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.مغادره"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.مغادره <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = flash[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(مغادرهChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
           
         

@idk.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.سبام ضخم"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.سبام ضخم <count> <message to spam>\n\n.سبام ضخم <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(flash) == 2:
            message = str(flash[1])
            counter = int(flash[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(flash[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(flash[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@idk.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.بينغ"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f" انا حي!\n`{ms}` 𝗺𝘀\n           ⚔️ 𝐁𝐒𝐈𝐋𝐄𝐍𝐓 𝙎𝙋𝘼𝙈𝘽𝙊𝙏 ⚔️")
       


@idk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.setname")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.setname")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.setname")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.setname")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.setname")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
async def setname(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗖𝗛𝗔𝗡𝗚𝗘 𝗡𝗔𝗠𝗘\n\nCommand:\n\n.setname <Message to change name of spam ids>"
    if e.sender_id in SMEX_USERS:
        names = e.text.split(" ", 1)
        flash = names[1]
        if len(e.text) > 5:
            firstname = flash
            text = "Changing Name..."
            try:
                await e.client(functions.account.UpdateProfileRequest(first_name=firstname))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await event.edit("Changed name successfully! ✅")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))            
async def setbio(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗖𝗛𝗔𝗡𝗚𝗘 𝗕𝗜𝗢\n\nCommand:\n\n.setbio <Message to change name of spam ids>"
    if e.sender_id in SMEX_USERS:
        flash = e.text.split(" ", 1)
        message = flash[1]
        if len(e.text) > 5:
            bio = message
            text = "Changing Bio..."
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await asyncio.sleep(0.7)
                await event.edit("Changed bio successfully! ✅")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


#INVITEALL


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info
   

@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await adk.disconnect()
        except Exception as e:
            pass
        try:
            await bdk.disconnect()
        except Exception as e:
            pass
        try:
            await cdk.disconnect()
        except Exception as e:
            pass
        try:
            await ddk.disconnect()
        except Exception as e:
            pass
        try:
            await edk.disconnect()
        except Exception as e:
            pass
        try:
            await vkk.disconnect()
        except Exception as e:
            pass
        try:
            await kkk.disconnect()
        except Exception as e:
            pass
        try:
            await lkk.disconnect()
        except Exception as e:
            pass
        try:
            await mkk.disconnect()
        except Exception as e:
            pass
        try:
            await sid.disconnect()
        except Exception as e:
            pass
        try:
            await shy.disconnect()
        except Exception as e:
            pass
        try:
            await aan.disconnect()
        except Exception as e:
            pass
        try:
            await ake.disconnect()
        except Exception as e:
            pass
        try:
            await eel.disconnect()
        except Exception as e:
            pass
        try:
            await khu.disconnect()
        except Exception as e:
            pass
        try:
            await shi.disconnect()
        except Exception as e:
            pass
        try:
            await yaa.disconnect()
        except Exception as e:
            pass
        try:
            await dav.disconnect()
        except Exception as e:
            pass
        try:
            await raj.disconnect()
        except Exception as e:
            pass
        try:
            await put.disconnect()
        except Exception as e:
            pass
        try:
            await eag.disconnect()
        except Exception as e:
            pass
        try:
            await gle.disconnect()
        except Exception as e:
            pass
        try:
            await wal.disconnect()
        except Exception as e:
            pass
        try:
            await aaa.disconnect()
        except Exception as e:
            pass
        try:
            await boy.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.help"))

async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 ☠️☠️\n►Pɪɴɢ\n►Rᴇsᴛᴀʀᴛ\n►Jᴏɪɴ\n►Lᴇᴀᴠᴇ\n►Pᴊᴏɪɴ\n►Bɪɢsᴘᴀᴍ\n►Rᴀɪᴅ\n\n\n\n       "
       await e.reply(text, parse_mode=None, link_preview=None )

 

    
        
text = """
 𝙂𝙤 𝘿𝙤 .𝙥𝙞𝙣𝙜 𝙖𝙩 @Bsilent_spam
𝗕𝗬 @ahmed15basher """

print(text)
print("")
print("𝗦𝗣𝗔𝗠 𝗕𝗢𝗧 𝗥𝗘𝗔𝗗𝗬 𝗙𝗢𝗥 𝗨𝗦𝗘")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
    try:
        adk.disconnect()
    except Exception as e:
        pass
    try:
        bdk.disconnect()
    except Exception as e:
        pass
    try:
        cdk.disconnect()
    except Exception as e:
        pass
    try:
        edk.disconnect()
    except Exception as e:
        pass
    try:
        ddk.disconnect()
    except Exception as e:
        pass
    try:
        vkk.disconnect()
    except Exception as e:
        pass 
    try:
        kkk.disconnect()
    except Exception as e:
        pass
    try:
        lkk.disconnect()
    except Exception as e:
        pass 
    try:
        mkk.disconnect()
    except Exception as e:
        pass
    try:
        sid.disconnect()
    except Exception as e:
        pass
    try:
        shy.disconnect()
    except Exception as e:
        pass
    try:
        aan.disconnect()
    except Exception as e:
        pass
    try:
        ake.disconnect()
    except Exception as e:
        pass
    try:
        eel.disconnect()
    except Exception as e:
        pass
    try:
        khu.disconnect()
    except Exception as e:
        pass
    try:
        shi.disconnect()
    except Exception as e:
        pass
    try:
        yaa.disconnect()
    except Exception as e:
        pass
    try:
        dav.disconnect()
    except Exception as e:
        pass
    try:
        raj.disconnect()
    except Exception as e:
        pass
    try:
        put.disconnect()
    except Exception as e:
        pass
    try:
        eag.disconnect()
    except Exception as e:
        pass
    try:
        gle.disconnect()
    except Exception as e:
        pass
    try:
        wal.disconnect()
    except Exception as e:
        pass
    try:
        aaa.disconnect()
    except Exception as e:
        pass
    try:
        boy.disconnect()
    except Exception as e:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        adk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        edk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        vkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        kkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        lkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        mkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sid.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shy.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aan.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ake.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eel.run_until_disconnected()
    except Exception as e:
        pass
    try:
        khu.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shi.run_until_disconnected()
    except Exception as e:
        pass
    try:
        yaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        dav.run_until_disconnected()
    except Exception as e:
        pass
    try:
        raj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        put.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eag.run_until_disconnected()
    except Exception as e:
        pass
    try:
        gle.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wal.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        boy.run_until_disconnected()
    except Exception as e:
        pass
