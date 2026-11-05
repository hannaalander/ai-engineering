# The code has been written with help off Gemini AI

import csv
import ollama

prompt = "What color is the Swedish flag?"

models = ["qwen2.5", "llama3.2:1b"]

results = []

print("Kör modeller och samlar in svar...")
for model in models:
  print(f"-> Frågar {model}...")
  try:
    response = ollama.chat(
        model=model, messages=[{"role": "user", "content": prompt}]
    )
    answer = response["message"]["content"]
    results.append({"model": model, "prompt": prompt, "response": answer})
  except Exception as e:
    print(
        f"Kunde inte köra {model}. Har du kört 'ollama pull {model}' i"
        f" terminalen? Fel: {e}"
    )

csv_file = "results.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
  writer = csv.DictWriter(f, fieldnames=["model", "prompt", "response"])
  writer.writeheader()
  writer.writerows(results)

print(f"Klar! Resultaten har sparats till {csv_file}")