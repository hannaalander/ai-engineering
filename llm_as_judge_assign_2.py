import ollama
import unittest

def ask_capital(country, model="qwen2.5"):
    prompt = f"What is the capital of {country}?"
    try:
        response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}], options={"temperature": 1.0}, stream=False)
        content = response["message"]["content"]
        print(f"[DEBUG ask_capital ({country}, {model})): {content}") # Syns direkt i terminalen!
        return content
    except Exception as e:
        print(f"[DEBUG ERROR]: {e}")
        return "Failure."

def llm_as_a_judge_agrees(country, answer, expected):
    prompt = (f"Question: What is the capital of {country}?\n"
              f"Expected answer: {expected}\n"
              f"Given answer: {answer}\n\n"
              f"Does the given answer agree with the expected answer? "
              f"Extra details are fine as long as they do not contradict it. Reply with only YES or NO.")
    try:
        verdict = ollama.chat(model="qwen2.5", messages=[{"role": "user", "content": prompt}], options={"temperature": 1.0}, stream=False)['message']['content']
        return verdict.strip().upper().startswith("YES")
    except Exception:
        return False

class TestApp(unittest.TestCase):

    # WRONG MODEL
    def test_unknown_model_returns_failure(self):
        response = ask_capital("Sweden", "no-such-model")
        self.assertEqual(response, "Failure.")

    # CONSISTENCY TEST
    def test_knows_capital_of_sweden(self):
        correct = 0
        for i in range(3):
            answer = ask_capital("Sweden")
            if "Stockholm" in answer:
                correct += 1
        self.assertGreaterEqual(correct, 2)

    # LLM AS JUDGE
    def test_judge_accepts_right_capital(self):
        answer = "The capital of Sweden is Stockholm."
        self.assertTrue(llm_as_a_judge_agrees("Sweden", answer, "Stockholm"))

    # HALLUCINATIONS
    def test_judge_rejects_invented_capital(self):
        answer = "The capital of Bealandia is Bea City."
        self.assertFalse(llm_as_a_judge_agrees("Bealandia", answer, "There is no such country, so it has no capital.")) 

    # CONSISTENCY TEST FOR NORWAY
    def test_knows_capital_of_norway(self):
        correct = 0
        for i in range(3):
            answer = ask_capital("Norway")
            if "Oslo" in answer:
                correct += 1
        self.assertGreaterEqual(correct, 2)


    # LLM AS JUDGE FOR NORWAY
    def test_judge_accepts_right_capital_norway(self):        
            answer = "The capital of Norway is Oslo."        
            self.assertTrue(llm_as_a_judge_agrees("Norway", answer, "Oslo"))    

            
    def test_judge_rejects_wrong_capital_norway(self):        
            answer = "The capital of Norway is Trondheim."        
            self.assertFalse(llm_as_a_judge_agrees("Norway", answer, "Oslo"))


    # Consistency test där judge bedömer modellens svar    
    def test_norway_with_judge(self):        
        correct = 0        
        for i in range(3):            
            answer = ask_capital("Norway")            
            if llm_as_a_judge_agrees("Norway", answer, "Oslo"):                
                correct += 1        
        self.assertGreaterEqual(correct, 2)


if __name__ == "__main__":
    unittest.main()
