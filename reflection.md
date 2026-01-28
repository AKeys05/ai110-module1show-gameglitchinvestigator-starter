# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The first time I ran it, the game had an input box, a submit guess button, a new game button, and a show hint checkbox. The instructions beneath the header tells me to guess a number between 1 and 100 and it lists my number of remaining attempts. The 'Developer Debug Info' dropdown box can also be publicly seen above the guess. One core bug I noticed was that the hints do not correspond with my guess and the secret (it was reversed). For example, when I made guesses between 50 and 90, it continued to display a 'Go Higher' hint when the secret was actually 26. Another noticeable bug was that after the game finished, it wouldn't allow me to start a new game of the same or different difficulty mode. It continued to display 'Game Over' and I had to refresh to play again. I also noticed other small bugs/inconsistencies involving the score, number of attempts left, switching difficulty modes, and the range values.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion you accepted and why.
- Give one example of an AI suggestion you changed or rejected and why.

I used VS Code's built-in agent to find the location of specific bugs in my code, get suggestions for how to fix them, and to write tests for them. One example of an AI suggestion I accepted was for the first bug I described above where the hints used the wrong logic. This was a clear-cut issue with a simple fix, so I accpeted it because it was easy to verify and test. The only thing I had to edit was an emoji/symbol that wasn't pasted over or rendered properly. One example of an AI suggestion I rejected was when I was trying to get the input box to automatically clear after a user submits a guess. It gave two suggestions that ultimately did not work and raised Streamlit errors, so I discarded them.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed when it could no longer be found in the game and when it successfully passed all of the pytests. A few tests that helped me learn about my code were the three original tests written in test_game_logic.py that tested the check_guess function. While I knew the hints and wins were working in the real game, those three function were not passing the tests due to an AssertionError. Looking deeper at the code showed me that check_guess returns a tuple, where the tests were looking for a single string. This helped me to know that I had to extract the 0th index of the tuple in order for it to work. I was then able to use the agent to help me generate a bunch of additional tests on parsing, updating the score, initializing the game and attempts, session and secret number persistence, and changing difficulty modes.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

While I never ran into the issue of the secret number changing after each guess, I still learned about Streamlit's session state through other bugs. Notably, when the new game button was clicked, it was set so that the attempts and secret were reset but not the status. I had to make sure that after each game, the status check was reset to "playing" instead of "won" or "lost" so that a new game could be created. Another problem involving session state was that when the difficulty mode was changed mid-game, it used the same secret number and attempts as the previous game. Again I had to set a check for a change in difficulty mode so Streamlit knew to create a new game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I will definitely reuse in the future is using VS Code's built-in agent feature. I have frequently uesd AI as a collaboration tool for programming, but it's always an external resource that doesn't have context of my code. Being able to highlight specific lines or reference certain files made it incredibly easy to get to the root of my bugs and fix them. One thing I will do differently next time is use the explain feature more to get a better understanding of existing or unfamiliar code. This project changed the way I think about AI-generated code because when the agent is given proper context, references to files/code, and detailed instructions, it can make solving simple problems way less of a headache.