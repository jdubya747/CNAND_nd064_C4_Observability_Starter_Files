import time
import random
import threading

import requests

endpoints = ('8083/', '8082/trace', '8081/', '8081/api', '8082/')


def run():
    while True:
        try:
            target = random.choice(endpoints)
            requests.get("http://localhost:%s" % target, timeout=3)
            time.sleep(1)
        except:
            pass

def run_post():
    while True:
        try:
            target = '8081/star'
            sleep_time = random.randint(1000, 3000) / 1000
            time.sleep(sleep_time)
            myobj = {'name':'John White','distance':10000}
            requests.post("http://localhost:%s" % target,  data = myobj, timeout=3)
        except:
            pass


if __name__ == '__main__':
    for _ in range(4):
        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()

    thread = threading.Thread(target=run_post)
    thread.daemon = True
    thread.start()

    while True:
        time.sleep(1)

