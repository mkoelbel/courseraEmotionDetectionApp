from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        joy_stmt = emotion_detector("I am glad this happened.")["dominant_emotion"]
        anger_stmt = emotion_detector("I am really mad about this.")["dominant_emotion"]
        disgust_stmt = emotion_detector("I feel disgusted just hearing about this.")["dominant_emotion"]
        sadness_stmt = emotion_detector("I am so sad about this.")["dominant_emotion"]
        fear_stmt = emotion_detector("I am really afraid that this will happen.")["dominant_emotion"]

        self.assertEqual(joy_stmt, "joy")
        self.assertEqual(anger_stmt, "anger")
        self.assertEqual(disgust_stmt, "disgust")
        self.assertEqual(sadness_stmt, "sadness")
        self.assertEqual(fear_stmt, "fear")

unittest.main()