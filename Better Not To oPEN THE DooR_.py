from roboid import*    

import smtplib

from email.mime.text import MIMEText

dev = Hamster()


import time
time.time()




    ###############delete##############3
info= {"ID":"YOUR@gmail.com","PW":"YOUR_PW"} #delete
    ###############delete##############3
#class=str

info2= {"MS1":"SOMEONE BROKE INTO YOUR ROOM or it was you...","MS2":"TAKE IMMEDIATE ACTION"}





def sett():
    print("You decided to make change on your 'email'")
    nid=str(input("Gmail account: "))
    npw=str(input("Gmail password: "))
    nopen_ms=str(input("open message: "))
    nremove_ms=str(input("remove message: "))
    info.update({"ID":nid,"PW":npw})
    info2.update({"MS1":nopen_ms,"MS2":nremove_ms})


def send_open():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(info["ID"], info["PW"])

    mail = MIMEText(info2["MS1"])
    mail['Subject'] = 'THE DOOR IS OPEN'


    s.sendmail(info["ID"], info["ID"], mail.as_string())

    s.quit()

def send_remove():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(info["ID"], info["PW"])

    mail = MIMEText(info2["MS2"])
    mail['Subject'] = 'THE DEVICE IS BEING REMOVED'


    s.sendmail(info["ID"],info["ID"], mail.as_string())

    s.quit()

def det_alarm():
    dev.leds(2,4)
    dev.note(Hamster.NOTE_E_4, .2)
    dev.leds(4,2)
    dev.note(Hamster.NOTE_E_4, .2)
    dev.leds(2,4)
    dev.note(Hamster.NOTE_E_4, .4)
    dev.leds(4,2)
    dev.note(Hamster.NOTE_E_4, .2)
    dev.leds(2,4)
    dev.note(Hamster.NOTE_E_4, .2)
    dev.leds(4,2)
    dev.note(Hamster.NOTE_E_4, .4)
    dev.leds(2,4)
    dev.note(Hamster.NOTE_E_4, .2)
    dev.leds(4,2)
    dev.note(Hamster.NOTE_G_4, .2)
    dev.leds(2,4)
    dev.note(Hamster.NOTE_C_4, .2)
    dev.leds(4,2)
    dev.note(Hamster.NOTE_D_4, .2)
    dev.leds(2,4)
    dev.note(Hamster.NOTE_E_4, .4)
    
    

def remove_alarm():
    dev.leds(Hamster.LED_YELLOW)
    dev.note(Hamster.NOTE_C_4, .2)
    dev.note(Hamster.NOTE_B_3, .2)
    dev.note(Hamster.NOTE_A_3, .2)
    dev.note(Hamster.NOTE_G_5, .8)
    dev.note(Hamster.NOTE_D_5, .4)
    dev.note(Hamster.NOTE_C_4, .2)
    dev.note(Hamster.NOTE_B_3, .2)
    dev.note(Hamster.NOTE_A_3, .2)
    dev.note(Hamster.NOTE_G_5, .8)
    dev.note(Hamster.NOTE_D_5, .4)
    dev.note(Hamster.NOTE_C_4, .2)
    dev.note(Hamster.NOTE_B_3, .2)
    dev.note(Hamster.NOTE_C_4, .2)
    dev.note(Hamster.NOTE_A_3, .4)

def operation():

    print("History of ", time.strftime('%Y-%m-%d', time.localtime(time.time())))
    while True:
        l_prox=dev.left_proximity()
        r_prox=dev.right_proximity()
        if l_prox < 15 or r_prox < 15:
            
            dev.note(Hamster.NOTE_OFF)
            dev.leds(Hamster.LED_BLUE)
            if dev.left_floor() > 70 or dev.right_floor() > 70:
                dev.note(Hamster.NOTE_OFF)
                dev.leds(Hamster.LED_BLUE)
            else:
                det_alarm()
                send_open()
                print("OPEN TIME: ",time.strftime('%c', time.localtime(time.time())))
            
        else:
            remove_alarm()
            send_remove()
            print("REMOVE TIME: ",time.strftime('%c', time.localtime(time.time())))

        wait(10)

def main():
    cnt=0
    print("Better not to open the door")
    print("Need to Sign in first")
    while True:
        inputid=input("ID: ")
        inputpw=input("PW: ")
        if inputid == "door" and inputpw == "entry":
            print("SIGNED IN SUCCESSFUL")
            todo=input("ACTIVATE or SETTING: ")
            if todo=="ACTIVATE":
                operation()
            elif todo=="SETTING":
                sett()
                operation()
        else:
            cnt +=1
            print("Wrong ID or PW.","Log in Attempts:",cnt,"time(s)")
        if cnt > 3:
            print("LOG IN FAILED. GOOD BYE ")
            break
        
main()
