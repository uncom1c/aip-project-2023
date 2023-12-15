import unittest

from notebook import pseudo_random, twobit, encoding, decoder, force_attack_16, attack_rashivrovka, nums



class notebooktest(unittest.TestCase):
    def test_pseudo_random1(self):
        self.assertEqual(pseudo_random(1), 10)

    
    def test_pseudo_random2(self):
        self.assertEqual(pseudo_random(-1), 4)

    def test_twobit(self):
        self.assertMultiLineEqual(twobit([1, 2, 3, 4]), "11011100")
    
    def test_twobit2(self):
        self.assertMultiLineEqual(twobit([1, 3, 5, 7, 9, 10, 11, 12]), "1111011111001101010111100")
    
    def test_twobit3(self):
        self.assertMultiLineEqual(twobit([2, 2, 4, 6, 10, 16, 26]), "101010011010101000011010")
    
    def test_twobit4(self):
        self.assertMultiLineEqual(twobit([106793]), "11010000100101001")


    '''
    Тесты на правильность закодирования проверить нельзя по причине кодирования по секундам, потому ключи и шифровки динамичны
    '''
    # def test_encoding_1(self):
    #     self.assertEqual(encoding('Hello'), ())    
    
    # def test_encoding_2(self):
    #     self.assertEqual(encoding('aip'), )    
    
    def test_decoder_1(self):
        self.assertEqual(decoder('0011011100011010000100110001001100010000', '1111111111111111111111111111111111111111'), 'Hello')

    def test_decoder_2(self):
        self.assertEqual(decoder('010010110100001101011010', '101010101010101010101010'), 'aip')
    
    


if __name__ == "__main__":
    unittest.main()