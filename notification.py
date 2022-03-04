# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 16:53:05 2022

@author: VAGUE
"""

from plyer import notification
import time

def drink_water():
    title = "Time to Get Hydrated !!"
    message = "Get up and drink a glass of water"
    while True:
        notification.notify(
            title = title,
            message = message,
            timeout = 5
        )
        time.sleep(1800)

if __name__ == "__main__":
    drink_water()