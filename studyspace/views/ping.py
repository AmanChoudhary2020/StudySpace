import os
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def ping(ip_address_range):
    print("Pinging...")
    os.system(f'nmap -sn {ip_address_range} | grep "Nmap scan report for " > temp')
    os.system("sed -n 's/Nmap scan report for //p' temp > out")
    os.remove("temp")

scheduler = BlockingScheduler()
scheduler.add_job(lambda: ping("10.0.0.1-255"), 'interval', seconds=600, next_run_time=datetime.now())
scheduler.start()