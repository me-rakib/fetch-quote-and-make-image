from send_tel import send_msg
import time
import schedule

# schedule.every().day.at("00:30").do(send_msg)

while True:
    # schedule.run_pending()
    send_msg()
    time.sleep(100)