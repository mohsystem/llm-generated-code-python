# from output.claude.Task29_CLAUDE_claude_3_5_sonnet_20240620 import two_sum as two_sum
# from output.codestral.Task29_MISTRAL_codestral_latest import two_sum as two_sum
# from output.gemini.Task29_GEMINI_gemini_1_5_pro_001 import two_sum as two_sum
# from output.gtp4o.Task29_OPENAI_gpt_4o import two_sum as two_sum
# from output.llama3.Task29_PERPLEXITY_llama_3_sonar_large_32k_chat import two_sum as two_sum
import unittest
#  todo : need to update cases !

class TestTwoSum(unittest.TestCase):

    def test_case1(self):
        numbers = [1, 2, 3]
        target = 4
        expected = (0, 2)  # Changed to tuple
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case2(self):
        numbers = [3, 2, 4]
        target = 6
        expected = (1, 2)  # Changed to tuple
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case3(self):
        numbers = [1, -2, 3, 4]
        target = 7
        expected = (2, 3)  # Changed to tuple
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case4(self):
        numbers = [0, 1, 2]
        target = 3
        expected = (1, 2)  # Changed to tuple
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case5(self):
        numbers = [2, 2, 3]
        target = 4
        expected = (0, 1)  # Changed to tuple
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case6(self):
        numbers = [5, 7, 3, 9]
        target = 12
        expected = (0, 1)  # Changed to tuple
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case7(self):
        numbers = [-5, -2, -3, 1]
        target = -7
        expected = (0, 1)  # Changed to tuple
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case8(self):
        numbers = [10, 20, 30, 40]
        target = 50
        expected = (1, 2)  # Changed to tuple
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case9(self):
        numbers = [1, 2, 5, 9]
        target = 14
        expected = (2, 3)  # Changed to tuple
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case10(self):
        numbers = [7, 14, 21, 28]
        target = 35
        expected = (1, 2)  # Changed to tuple
        self.assertEqual(two_sum(numbers, target), expected)

if __name__ == '__main__':
    unittest.main()