# from output.claude.Task32_CLAUDE_claude_3_5_sonnet_20240620 import calculate_years as calculate_years
# from output.codestral.Task32_MISTRAL_codestral_latest import calculate_years as calculate_years
from output.gemini.Task32_GEMINI_gemini_1_5_pro_001 import calculate_years as calculate_years
# from output.gtp4o.Task32_OPENAI_gpt_4o import calculate_years as calculate_years
# from output.llama3.Task32_PERPLEXITY_llama_3_sonar_large_32k_chat import calculate_years as calculate_years
import unittest


class TestCalculateYears(unittest.TestCase):

    def test_exact_three_years(self):
        self.assertEqual(calculate_years(1000.00, 0.05, 0.18, 1100.00), 3)

    def test_zero_years(self):
        self.assertEqual(calculate_years(1000.00, 0.05, 0.18, 1000.00), 0)

    def test_small_increase_one_year(self):
        self.assertEqual(calculate_years(1000.00, 0.05, 0.18, 1040.00), 1)

    def test_long_term_investment(self):
        self.assertEqual(calculate_years(1000.00, 0.05, 0.18, 2000.00), 21)

    def test_no_tax(self):
        self.assertEqual(calculate_years(1000.00, 0.05, 0.00, 2000.00), 15)

    def test_high_tax(self):
        self.assertEqual(calculate_years(1000.00, 0.05, 0.50, 2000.00), 41)

    def test_high_interest_low_tax(self):
        self.assertEqual(calculate_years(1000.00, 0.10, 0.10, 2000.00), 7)

    def test_low_interest_high_tax(self):
        self.assertEqual(calculate_years(1000.00, 0.02, 0.50, 2000.00), 77)

    def test_minimal_interest(self):
        self.assertEqual(calculate_years(1000.00, 0.005, 0.18, 2000.00), 414)

    def test_high_principal_and_desired_sum(self):
        self.assertEqual(calculate_years(1000000.00, 0.05, 0.18, 2000000.00), 14)

if __name__ == '__main__':
    unittest.main()