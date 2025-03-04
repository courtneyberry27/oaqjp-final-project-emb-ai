from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        key = 'dominant_emotion'

        test1 = emotion_detector("I am glad this happened")
        self.assertEqual(test1[key], 'joy')

        test2 = emotion_detector("I am really mad about this")
        self.assertEqual(test2[key], 'anger')

        test3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test3[key], 'disgust')

        test4 = emotion_detector("I am so sad about this")
        self.assertEqual(test4[key], 'sadness')

        test5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test5[key], 'fear')
unittest.main()