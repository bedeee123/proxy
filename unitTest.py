from proxy import *
import unittest

class testProxy(unittest.TestCase):
    def test_when_calling_proxy_class_output_should_call_realSubject(self):
        #Arrange
        real_subject = RealSubject()
        PROX = Proxy(real_subject)
        prox = PROX.request(0)
        #Act
        output = prox       
        #Assert
        self.assertEqual(output, PROX.request(0))

if __name__ == "__main__":
    unittest.main()