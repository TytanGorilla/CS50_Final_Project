# Spontaneous Training Split Creator
## Video Demo:  <URL HERE>
### Description: A prompt selection questionnaire that quickly generates a training split entry point with a training template recommendation for those too busy to consider their training needs. Use this application to synthesis the most likely to be most productive route for getting on with your fitness rather than being halted in a guagmire of self doubting questions.

#### TODO
Spec Project needs, find appropriate libraries for use within projects.py -> to be injected via: `pip freeze > requirements.txt`
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
In .md file use Markdown to style, enrich & embbed useful info to learn how.

Libraries to potentially use due to needs/usecase:
1) Pytest - testing my own code, and guiding me to code defensively.
2) mypy - catch errors earlier by using type hints.
3) tabulate - print esay to read tables
4) cowsay for some character interaction.

**Rough concept of logic with problem at hand**

A person has a need to do the most productive training they can possibly do, but they do not know or desire to solve for what that would be if their goal was to
illict a robust grow stimulus to them, and perhaps in a very specific way. They also need that answer 5 minutes ago, as they now have x time left to accomplish said specific goal.

The app aims to understand the user's position quite literally, so it can acquire markers/constraints and recommend most productive recommended course of action, and the steps there after. Would be cool to implement a 30s barrage of questions, the more the merrier, but no issue with less, just less clarity. So would need a timer to condense time of solution being presented.

6s per question, 30s total.

1) If you could improve one aspect of your body, what would it be? (Acquire inital heading)
A list of the general body parts (Neck, Traps, Shoulders, Arms, Chest, Abs, Back, Legs, Cardio, Composition)
You haven't trained that part of the body (except cardio, composition) in the past 2 days?

Further clarify the selected body part, and offer 2nd iteration of quick questions:
2)  Neck (Neck - go see Jeff Nipperd)
    Traps (Upper, Mid, Lower)
    Shoulders (Anterior, Lateral, Posterior)
    Arms (Bicep, Tricep, Brachialis, Forearms)
    Chest (Upper, Mid, Lower) -> (Inner, Mid, Outer)
    Abs (Upper, Lower, Obliques, Internal)
    Back (Upper, Mid, Lower)
    Legs (Upper, Lower) -> (Glutes, Hamstrings, Quads) / (Calves = Gastrocnemius, Solues, Tiialis Anterior)

3) Acquire time available for honest training today?
Anything lower than 10mins, might not be worth your effort.
!<10min and each exercise has its own amount of time needed or used, so a budget.
Perhaps some function/class that can apportion exercises according to their weighting and populate a session with x exercises, x sets per exercise.

