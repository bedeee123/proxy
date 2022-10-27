from proxy import *
import unittest

class testProxy(unittest.TestCase):
    def test_when_calling_proxy_class_output_should_be_request_method_details(self):
        #Arrange
        real_subject = RealSubject()
        PROX = Proxy(real_subject)
        prox = PROX.request()
        #Act
        output = prox
        #Assert
        self.assertEqual(output, "RealSubject: Handling Request.")

    def test_when_calling_main_class_output_should_be_request_method_details(self):
        #Arrange
        real_subject = RealSubject()
        real = real_subject.request()
        #Act
        output2 = real
        #Assert
        self.assertEqual(output2, "RealSubject: Handling Request.")

if __name__ == "__main__":
    unittest.main()