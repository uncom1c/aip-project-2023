import unittest

from notebook import pseudo_random, twobit, encoding, decoder, force_attack_16, attack_rashivrovka



class RunLengthEncodingTest(unittest.TestCase):
    def test_pseudo_random1(self):
        self.assertMultiLineEqual(pseudo_random(1), 10)

    
    def test_pseudo_random2(self):
        self.assertMultiLineEqual(pseudo_random(-1), 4)

    def test_twobit(self):
        self.assertMultiLineEqual(twobit([1, 2, 3, 4]), "11011100")

    


if __name__ == "__main__":
    unittest.main()