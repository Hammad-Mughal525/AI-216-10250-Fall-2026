# Lab 03 — Functions, Modules, Exceptions, Debugging & OOP

**Course:** AI-216: Programming for Artificial Intelligence  
**Semester:** Fall 2026  
**Week:** 03

## Concepts Practiced
- Functions and return values
- Scope and explicit parameters
- Modules and imports
- `__name__ == "__main__"`
- Exception handling
- Debugging
- Classes and objects
- Refactoring and separation of concerns

## Tasks Completed
1. Function Design & Reuse
2. Scope & Hidden State
3. Create and Use Your Own Module
4. Exception Handling
5. Debugging Challenge
6. Build a ScoreAnalyzer Class
7. Refactor a Procedural Script into Modules + Class

## Task 1 — Results
Scores: `[78, 85, 92, 67, 88]`
- Average: 82.00
- Highest: 92
- Scores >= 80: 3
- Classification: Good
- Empty list returns `None`.

## Task 2 — Scope
The `score = 70` inside `show_score()` is local. The `score = 90` outside the function is global. Passing `threshold` explicitly makes `is_qualified()` easier to reuse and test because it does not depend on hidden global state.

## Task 3 — Modules
`score_utils.py` contains reusable functions and `main.py` imports them. The main guard means demo code runs when `score_utils.py` is executed directly, but not when it is imported.

## Task 4 — Exception Test Cases
| Case | Input | Expected | Actual |
|---|---|---|---|
| Valid | 80, 100 | 80.00% | 80.00% |
| Negative | -5, 100 | Reject | Rejected |
| Too high | 120, 100 | Reject | Rejected |
| Zero total | 80, 0 | Reject | Rejected |
| Non-numeric | abc, 100 | Handle ValueError | Handled |

## Task 5 — Debugging Notes
**Bug 1:** `total = score` replaced the accumulated value each loop. It was fixed with `total += score`.

**Bug 2:** `average >= 50` came before `average >= 85`, so an excellent score could be classified as Pass. The higher condition must be checked first.

Correct output:
```text
Average: 75.0
Result: Pass
```

I located the bugs by tracing the accumulator through the loop and checking the conditions from top to bottom.

## Task 6 — OOP Results
Raw data: `[78, -5, 110, 67, 90, 88]`

After cleaning: `[78, 67, 90, 88]`

- Count: 4
- Average: 80.75
- Highest: 90
- Lowest: 67
- Count >= 80: 2

## Task 7 — Refactoring
The workflow is separated into:
- `preprocessing.py` — cleans raw scores.
- `analyzer.py` — contains the `ScoreAnalyzer` class and analysis methods.
- `main.py` — coordinates the workflow and prints the results.

Flow:
```text
Raw Data
   ↓
clean_scores()
   ↓
Clean Data
   ↓
ScoreAnalyzer()
   ↓
Summary
```

`main.py` does not contain the detailed cleaning or analysis logic.

## Design Decisions
Functions are used when no persistent state is required. A class is used when data and related behavior belong together. `main.py` is used to coordinate the workflow.

## What I Found Difficult
The most difficult part was dividing one program into separate responsibilities and understanding why the order of conditions matters during debugging.

## What I Learned
I learned how to create reusable functions, organize code into modules, handle predictable errors, debug logic errors, create classes, and refactor a procedural program.

## AI Engineering Relevance
- Functions can become reusable data-processing steps.
- Modules help organize larger AI projects.
- Exceptions help handle invalid input.
- Debugging is important for reliable AI code.
- Classes can keep model or analyzer state with related behavior.
- Refactoring makes AI applications easier to maintain and extend.

## AI Usage Log
### Tool Used
ChatGPT

### What I Asked
I asked for help solving the Week 3 AI-216 lab tasks and preparing the required GitHub repository files.

### What I Used
I used the generated solutions as a starting point for the required functions, modules, exceptions, debugging, OOP, and refactoring tasks.

### What I Verified or Changed Myself
I checked the requirements, file structure, boundary cases, expected behavior, and program outputs against the Week 3 lab handout.

## Repository Structure
```text
labs/week03/
├── task01_functions.py
├── task02_scope.py
├── task03_modules/
│   ├── main.py
│   └── score_utils.py
├── task04_exceptions.py
├── task05_debugging.py
├── task06_oop.py
├── task07_refactor/
│   ├── main.py
│   ├── preprocessing.py
│   └── analyzer.py
└── README.md
```

## How to Run
From `labs/week03`:
```bash
python task01_functions.py
python task02_scope.py
python task03_modules/score_utils.py
python task03_modules/main.py
python task04_exceptions.py
python task05_debugging.py
python task06_oop.py
python task07_refactor/main.py
```

## Suggested Git Commits
```bash
git add labs/week03/task01_functions.py
git commit -m "Lab03: add reusable score functions"

git add labs/week03/task03_modules/
git commit -m "Lab03: organize score utilities into module"

git add labs/week03/task04_exceptions.py
git commit -m "Lab03: add input validation and exception handling"

git add labs/week03/task06_oop.py
git commit -m "Lab03: add ScoreAnalyzer class"

git add labs/week03/task07_refactor/
git commit -m "Lab03: refactor analysis workflow into modules"
```
