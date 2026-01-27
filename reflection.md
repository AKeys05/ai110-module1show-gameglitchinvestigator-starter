# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The first time I ran it, the game had an input box, a submit guess button, a new game button, and a show hint checkbox. The instructions beneath the header tells me to guess a number between 1 and 100 and it lists my number of remaining attempts. The developer debug info dropdown box can also be publicly seen above the guess. One core bug I noticed was that the hints do not correspond with my guess and the secret (it was reversed). For example, when I made guesses between 50 and 90, it continued to display a 'Go Higher' hint when the secret was actually 26. Another noticeable bug was that after the game finished, it wouldn't allow me to start a new game of the same or different difficulty mode. It continued to display 'Game Over' and I had to refresh to play again. I also noticed that:
- the score displayed in the 'Game Over' message differs from the score listed in the developer debug info (overall unpredictable scoring system)
- for each mode played it gives you one less attempt than you're supposed to have
- sometimes no hint is displayed at all when a guess is submitted
- when you change modes, the updated range is listed in settings but not in the instructions (still says 1-100) 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion you accepted and why.
- Give one example of an AI suggestion you changed or rejected and why.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
