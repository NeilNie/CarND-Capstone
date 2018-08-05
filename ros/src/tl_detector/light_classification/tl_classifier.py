from styx_msgs.msg import TrafficLight
import cv2
from keras.models import load_model
import numpy as np


class TLClassifier(object):
    def __init__(self):
        self.model = load_model('./model.h5')

        pass

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        image = cv2.resize(image,(400,400))
        image = image.astype(float)
        image = image / 255.0
        image = image[np.newaxis,:,:,:]
        pred = self.model.predict(image)
        light = np.argmax(preds,axis=1)[0]
        if(light == 1):
            return TrafficLight.RED
        else:
            return TrafficLight.GREEN
        return TrafficLight.UNKNOWN
