# Lab 02 — Python Fundamentals for Problem Solving

**Course:** AI-216: Programming for Artificial Intelligence  
**Semester:** Fall 2026  
**Week:** 02

## Concepts Practiced

- Variables and data types
- Arithmetic, comparison, and logical operators
- Conditional statements
- `for` loops
- Counters and accumulators
- Functions and return values
- Problem decomposition
- Boundary testing

## Tasks Completed

1. Daily Expense Tracker
2. Internet Package Advisor
3. Temperature Monitoring
4. Model Score Analysis
5. Applicant Eligibility
6. Functions
7. Problem Decomposition Challenge

## Task 7 Choice

I selected **Option C — AI Service Request Monitor** because it is related to AI applications and uses response-time classification.

## Boundary / Test Cases

| Task | Input | Expected | Actual | Pass? |
|---|---|---|---|---|
| 1 | 450, 200, 150, 1000 | Within budget | Within budget | Yes |
| 1 | 500, 300, 200, 1000 | Exactly at budget | Exactly at budget | Yes |
| 1 | 600, 300, 250, 1000 | Over budget | Over budget | Yes |
| 2 | 5 GB | Basic | Basic | Yes |
| 2 | 5.1 GB | Standard | Standard | Yes |
| 2 | 15 GB | Standard | Standard | Yes |
| 2 | 15.1 GB | Premium | Premium | Yes |
| 2 | -1 GB | Invalid | Invalid | Yes |
| 3 | 14.0°C | Below Normal | Below Normal | Yes |
| 3 | 15.0°C | Normal | Normal | Yes |
| 3 | 30.0°C | Normal | Normal | Yes |
| 3 | 35.2°C | High | High | Yes |
| 4 | 0.85 | Meeting target | Meeting target | Yes |
| 5 | 18, 60, True | Eligible | Eligible | Yes |
| 5 | 17, 55, False | Not eligible | Not eligible | Yes |
| 6 | 50, 50 | True | True | Yes |
| 7 | 300 ms | Fast | Fast | Yes |
| 7 | 700 ms | Acceptable | Acceptable | Yes |
| 7 | 701 ms | Slow | Slow | Yes |

## Expected Fixed-Data Results

### Task 1
- Total expense: 800
- Remaining budget: 200
- Status: Within budget

### Task 3
- Below Normal: 1
- Normal: 4
- High: 2

### Task 4
- Meeting target (>= 0.85): 3
- Below target: 4
- Average score: 0.81
- Percentage meeting target: 42.86%

### Task 7
- Fast: 3
- Acceptable: 2
- Slow: 2

## What I Found Difficult

Understanding the boundary conditions was the main difficult part. For example, I had to make sure that exactly 5 GB is Basic, while 5.1 GB is Standard.

## What I Learned

I learned how to convert a problem statement into input, processing, and output. I also practiced loops, counters, conditions, and simple reusable functions.

## AI Engineering Relevance

### Data Processing
Loops and conditions can be used to process data one value at a time.

### Validation
Conditions can check whether input values meet required rules before an AI application uses them.

### Model Evaluation
The score-analysis task can be used to count model results above a target and calculate an average.

### AI Application Code
The response-time monitor shows how an AI service can classify requests as Fast, Acceptable, or Slow.

## AI Usage Log

### Tool Used
ChatGPT

### What I Asked
I asked for help solving the Week 2 AI-216 lab tasks and preparing the files for my GitHub repository.

### What I Used
I used the generated Python solutions and README structure as a starting point.

### What I Verified or Changed Myself
I checked the required rules, boundary cases, expected results, and file names against the lab handout before submission.

## Repository Structure

```text
labs/week02/
├── task01_expense_tracker.py
├── task02_package_advisor.py
├── task03_temperature_monitor.py
├── task04_score_analysis.py
├── task05_eligibility.py
├── task06_functions.py
├── task07_decomposition.py
└── README.md
```

## How to Run

From the repository root:

```bash
python labs/week02/task01_expense_tracker.py
python labs/week02/task02_package_advisor.py
python labs/week02/task03_temperature_monitor.py
python labs/week02/task04_score_analysis.py
python labs/week02/task05_eligibility.py
python labs/week02/task06_functions.py
python labs/week02/task07_decomposition.py
```
