from send_telegram_msg import send_msg
import time
import schedule

# time of sending message
sending_time = "00:30"  #24hours clock
schedule.every().day.at(sending_time).do(send_msg)

while True:
    schedule.run_pending()
    time.sleep(1)