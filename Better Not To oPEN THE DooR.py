from roboid import*    

import smtplib

from email.mime.text import MIMEText

dev = Hamster()


def send_open():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('youremail@gmail.com', 'password') #delete the PASSWORD

    mail = MIMEText('SOMEONE BROKE INTO YOUR ROOM or it was you...')
    mail['Subject'] = 'THE DOOR IS OPEN'


    s.sendmail("youremail@gmail.com", "youremail@gmail.com", mail.as_string())

    s.quit()

def send_remove():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('youremail@gmail.com', 'password') #delete the PASSWORD

    mail = MIMEText('TAKE IMMEDIATE ACTION')
    mail['Subject'] = 'THE DEVICE IS REMOVED'


    s.sendmail("youremail@gmail.com", "youremail@gmail.com", mail.as_string())

    s.quit()

def det_alarm():
    dev.leds(Hamster.LED_RED)
    dev.note(Hamster.NOTE_E_4, .2)
    dev.note(Hamster.NOTE_E_4, .2)
    dev.note(Hamster.NOTE_E_4, .4)
    dev.note(Hamster.NOTE_E_4, .2)
    dev.note(Hamster.NOTE_E_4, .2)
    dev.note(Hamster.NOTE_E_4, .4)
    dev.note(Hamster.NOTE_E_4, .2)
    dev.note(Hamster.NOTE_G_4, .2)
    dev.note(Hamster.NOTE_C_4, .2)
    dev.note(Hamster.NOTE_D_4, .2)
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

def main():
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
        else:
            remove_alarm()
            send_remove()
        wait(10)    
main()
