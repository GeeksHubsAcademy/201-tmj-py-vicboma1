import pytest
import unittest   # The test framework

from kata import apply

class Test_kata(unittest.TestCase):

    def test_apply_1(self):
        expected = [0]
        result = apply([0], 0)
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 
    
    def test_apply_2(self):
        expected = [6, 6, 0, 5, 6]
        result = apply([0, 5, 6, 6, 6],  3)
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 
    
    def test_apply_3(self):
        expected = [ 6, 0, 5, 6, 6]
        result = apply([6, 6, 0, 5, 6],  1)
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_4(self):
        expected = [ 5, 6, 6, 6, 0]
        result = apply([ 6, 0, 5, 6, 6],  2)
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_5(self):
        expected = [2, 1, 5]
        result = apply([1, 5, 2],  2)
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_6(self):
        expected = [9, 5, 2, 4, 0]
        result = apply([0, 9, 5, 2, 4],  1)
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 
    
    def test_apply_7(self):
        expected = [3, 4, 0, 1, 2]
        result = apply([0, 1, 2, 3, 4],  3)
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_8(self):
        expected = [0, 1, 2, 3, 4]
        result = apply([0, 1, 2, 3, 4],  0)
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 
    

    def test_apply_9(self):
        expected = [0]
        result = apply([0, 0, 0, 0, 0], 0)
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 
    

if __name__ == '__main__':
	unittest.main()