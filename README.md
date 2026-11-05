Assignment 1 - Ollama

Models used:
- gemma:2b
- llama3.2:1b
- qwen2.5 (swapped gemma:2b with this)

How we ran the code:
- downloaded the models with the terminal
- created a new local project folder with an app.py-file
- opened the project folder in VS Code
- asked gemini ai for example on code for our purpose and wrote it down in the app.py-file.
  the code includes executing a question, same question for both models and then code for saving the answer in a result.csv-file.
- first question asked was "Kan man läsa Mittuniversitetets utbildning "informatik med inriktning systemutveckling" på distans?"
- second question asked was "Vad har Sveriges flagga för färger?", this one we then changed into english.

Observations:
- gemma:2b took a long time at answering our question about the program on Mittuniversitetet.
  it gave us an answer in a mix of swedish/norweigan, and the short answer was correct but the details about the answer were not entirely correct.
  we chose to swap this model after that, to another.
- llama3.2:1b did not take as long time as gemma:2b to answer. it answered in swedish and gave the correct overall answer but the details hint about that the model did not interpret the question as we intended.
  we thought about "study at distance" to be studying from home, while the answer gave details about things to think about if studying from another country.
  when asked about the colors of the swedish flag the answer were totaly wrong, not even close to correct.
  when we swapped the question about the flag into english it gave a way faster answer, though still incorrect.
- qwen2.5 was a little bit bigger of a model than the other two models, and only got asked the question about the swedish flag in english but it was fast in answering and gave a correct answer.
- conclusion is that a bigger model seems to give better answers and they answered faster when the question was written in english, probably because it was easier to match with the tokens.
