from whatsapp_api import Whatsapp

what = Whatsapp()


what.go_to("phonenumber")
what.send_message("Hello world")

what.quit()