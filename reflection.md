# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---
When I first ran the game, it appeared as a simple number guessing game in Streamlit with a title, input field for guesses, and display areas for hints and remaining attempts. However, the hints were completely backwards—for example, entering a number lower than 1 prompted "go lower," and entering one higher than 100 said "go higher." Additionally, when the secret number was 84 and I guessed higher, the hint incorrectly told me to go lower. The game also had only 7 attempts instead of the expected 8, and once the game ended, it became stuck without an option to start a new round.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude Code on this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One example of a good suggetion was when it suggested the hint logic was incorrect and hints were swapped to be the the opposite which was along the line of my thinking. I verified that the suggestion was right by running the app and visually checking for changes.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One example of a misleading suggestion it gave me was when it told me the ranges for Easy and Hard appear swapped relative to expected difficulty. It didnt take into consideration that hard only had 5 tries and had a bigger range so the suggestion was wrong. I verified this by playing both hard and easy mode on my own.
---


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I traced the logic manually and played the game again. For the attempts bug, I confirmed that initializing to 0 means attempt_limit - attempts correctly shows 8 on load 
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I ran a manual test by opening the app and checking the "Attempts left" display on load. It showed 8 for Normal difficulty, which confirmed that the off-by-one fix was working correctly. I also used the debug section on the app to ensure the rights hints were shown.
- Did AI help you design or understand any tests? How?
Yes, it helped me design the tests and understand what to look for in each bug to make sure all cases were covered.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every time you interact with a Streamlit app (like click a button) the entire Python script reruns from top to bottom. It's like refreshing the page, except it re-executes your code. Session state is like a dictionary that stores the values of your variables so that they can persist each time streamlit reruns. Without it, all your variables reset to their default values (go back to 0).

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

I like the strategy of having different chats for each bug it helps you stay organized and not have specific chats become be too convoluted.

- What is one thing you would do differently next time you work with AI on a coding task?

I would make sure I would attach context directly to every message so it can understand my problems better.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

I think this project helped me realize that while AI might think it knows what is best for your specific problem or project, you have to verify what it gives you, because certain things that get flagged by the AI might have actually been written intentionally by you.