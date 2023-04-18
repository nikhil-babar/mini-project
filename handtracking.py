import threading
import cv2 as cv
import mediapipe

class HandTracking(threading.Thread):
    def __init__(self):
        super().__init__()
        self.hands = mediapipe.solutions.hands.Hands()
        self.drawingModule = mediapipe.solutions.drawing_utils
        self.capture = cv.VideoCapture(0)
        self.results = None
        self.RUN = threading.Event()

    def run(self):
        while self.RUN.is_set() is not True:
            self.getHandsImage()
            cv.waitKey(1)


    def getHandsImage(self, draw=True):
        success, img = self.capture.read()
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        self.img = img

        if draw:
            if self.results.multi_hand_landmarks:
                for landmarks in self.results.multi_hand_landmarks:
                    self.drawingModule.draw_landmarks(img, landmarks, mediapipe.solutions.hands.HAND_CONNECTIONS)

        cv.imshow("Image", img)

        return img

    def getLandmarks(self, handNo = 0):
        endpoints = []
        if self.results is not None and self.results.multi_hand_landmarks:
            landmarks = self.results.multi_hand_landmarks[handNo]
            for index, landmark in enumerate(landmarks.landmark):
                height, width, c = self.img.shape

                px, py = int(landmark.x * width), int(landmark.y * height)
                endpoints.append([px, py])

        return endpoints

    def stop(self):
        self.RUN.set()









