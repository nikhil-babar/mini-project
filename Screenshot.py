import threading

from handtracking import HandTracking
from threading import Thread
import os
import pyautogui
from uuid import uuid4 as uid

tracker = HandTracking()
tips = [4, 8, 12, 16, 20]
fingerStatus = []
isThreeFingerGesture = False


class Screenshot(threading.Thread):
    def __init__(self, tracker):
        Thread.__init__(self)
        self.tracker = tracker
        self.RUN = threading.Event()

    def takeScreenShot(self):
        try:
            parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
            screenshot_dir = os.path.join(parent_dir, 'screenshot')

            print(screenshot_dir)

            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)

            img = pyautogui.screenshot()
            img.save(os.path.join(screenshot_dir, f'{uid()}.png'))

        except UnboundLocalError:
            print('error while taking screenshot')

    def run(self):
        isThreeFingerGesture = False
        fingerStatus = []

        while self.RUN.is_set() is not True:
            landmarks = self.tracker.getLandmarks()

            if len(landmarks) != 0:
                if landmarks[tips[0]][0] > landmarks[tips[0] - 1][0]:
                    fingerStatus.append(1)
                else:
                    fingerStatus.append(0)

                for i in range(1, 5):
                    if landmarks[tips[i]][1] < landmarks[tips[i] - 2][1]:
                        fingerStatus.append(1)
                    else:
                        fingerStatus.append(0)

                if fingerStatus[1:4].count(1) == 3 and fingerStatus[0] == 0 and fingerStatus[4] == 0:
                    print("Three finger gesture..")
                    isThreeFingerGesture = True

                elif isThreeFingerGesture and fingerStatus.count(0) == len(fingerStatus):
                    print("Take screenshot..")
                    isThreeFingerGesture = False
                    self.takeScreenShot()

            fingerStatus = []

    def stop(self):
        self.RUN.set()