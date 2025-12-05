from whatsapp_api import Whatsapp

what = Whatsapp()


what.go_to("6xxxxxxxxxx")
what.send_message("Hello world")

what.quit()