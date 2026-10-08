# Lab 04 — Python Data Structures & Clean Code

**Course:** AI-216 — Programming for Artificial Intelligence  
**Semester:** Fall 2026  
**Week:** 04

## Concepts Practiced
- Lists
- Aliasing, shallow copy, and deep copy
- Tuples and tuple unpacking
- Tuples as dictionary keys and hashability
- Dictionaries and nested dictionaries
- Sets and set operations
- List, dictionary, and set comprehensions
- `enumerate()` and `zip()`
- Sorting and counting records
- Data structure selection
- Clean code and file organization

## Tasks Completed
1. Lists
2. Aliasing vs Copying
3. Tuples
4. Dictionaries
5. Sets
6. Comprehensions
7. `enumerate()` and `zip()`
8. Data Structure Selection
9. Prediction Analysis — Part A and Part B

## Task 8 — Data Structure Decisions
- **List:** model names in evaluation order because order matters.
- **Tuple:** fixed image size because the width/height pair is not meant to change.
- **Dictionary:** model configuration because each value has a meaningful field name.
- **Set:** unique labels and validation because duplicates are not needed.
- **List of dictionaries:** many prediction records because each record has multiple named fields.
- **Set comparison:** allowed and received labels because union/difference make validation clear.

## Aliasing vs Copying
With `processed_scores = original_scores`, both names refer to the same list, so changing one changes the other. `.copy()` creates a separate outer list, which fixes the simple list case.

For a list containing dictionaries, `.copy()` is only a shallow copy. The inner dictionaries are still shared, so changing a record can change the original data. `copy.deepcopy()` copies the nested objects too, protecting the raw records.

Accidental mutation can be dangerous in preprocessing, experiment tracking, and model evaluation because raw data or results may be changed unexpectedly.

## Hashability
A tuple can be used as a dictionary key because an immutable tuple with hashable contents is hashable. A list is mutable, so it cannot be used as a dictionary key.

## Sets vs Lists for Validation
A set is clearer for validation because operations such as `-` and `&` directly express difference and intersection. Set membership checks are also efficient because sets use hash-based lookup.

## Clean-Code Refactoring
The original Task 9 code used names such as `x`, `y`, `z`, and `d`, which made the purpose of the data harder to understand. The refactor uses descriptive names and separates responsibilities into `preprocessing.py`, `analysis.py`, and `main.py`.

Part A was verified by comparing the selected IDs and label counts with the behavior of the original code.

Part B separates incomplete-record handling, label normalization, analysis, summary creation, and display. The raw records are not mutated.

## Handling Incomplete Records
A record is complete only when it contains every required field. Incomplete records are skipped from analysis but their IDs are reported. Labels are normalized by stripping spaces and converting them to lowercase in a new list.

## Edge Cases Tested
- Empty list passed to `filter_by_confidence()` returns `[]`.
- Empty list passed to `average_confidence()` returns `None`.
- Confidence exactly `0.80` is included because the rule is `>= 0.80`.
- Duplicate labels are handled by sets/counting.
- Missing `confidence` causes the record to be reported as skipped.
- Raw label `"Spam"` remains unchanged after normalization.

## What I Found Difficult
- Understanding the difference between an alias and a real copy.
- Understanding why shallow copy does not fully protect nested dictionaries.
- Choosing the correct data structure for each type of information.
- Keeping the Task 9 processing functions separate.

## What I Learned
I learned that data structures are chosen according to what the data means. I also learned that clean code is not only about getting the correct output; names, responsibilities, and avoiding accidental mutation make code easier to maintain.

## AI Engineering Relevance
Data structures and clean code are useful in:
- **Preprocessing:** storing and cleaning model inputs.
- **Configuration:** dictionaries can store model settings.
- **Model outputs:** lists of dictionaries can represent prediction records.
- **Validation:** sets can quickly identify unexpected labels.
- **Maintainability:** separate functions/files make data-processing pipelines easier to test and update.

## AI Usage Log

### Tool Used
ChatGPT

### What I Asked
I asked for help solving the required Week 4 lab tasks and organizing the work as a repository-ready submission.

### What I Used
I used the generated beginner-friendly Python solutions, file organization, test cases, and README structure as a starting point.

### What I Verified or Changed Myself
I verified that the scripts run, checked the required outputs and edge cases, and reviewed the code so I can explain the submitted work.

## Repository Structure
```text
labs/week04/
├── task01_lists.py
├── task02_copying.py
├── task03_tuples.py
├── task04_dictionaries.py
├── task05_sets.py
├── task06_comprehensions.py
├── task07_iteration_tools.py
├── task08_data_modeling.py
├── task09_clean_code/
│   ├── main.py
│   ├── preprocessing.py
│   └── analysis.py
└── README.md
```

## How to Run
From the repository root:

```bash
python labs/week04/task01_lists.py
python labs/week04/task02_copying.py
python labs/week04/task03_tuples.py
python labs/week04/task04_dictionaries.py
python labs/week04/task05_sets.py
python labs/week04/task06_comprehensions.py
python labs/week04/task07_iteration_tools.py
python labs/week04/task08_data_modeling.py
```

For Task 9:

```bash
cd labs/week04/task09_clean_code
python main.py
```

## Suggested Git Commits
```bash
git add labs/week04/task01_lists.py
git commit -m "Lab04: add list processing exercises"

git add labs/week04/task04_dictionaries.py
git commit -m "Lab04: add structured dictionary exercises"

git add labs/week04/task05_sets.py
git commit -m "Lab04: add set validation exercises"

git add labs/week04/task06_comprehensions.py
git commit -m "Lab04: add collection comprehensions"

git add labs/week04/task09_clean_code/
git commit -m "Lab04: refactor prediction analysis for clean code"

git add labs/week04/task09_clean_code/
git commit -m "Lab04: handle incomplete prediction records"
```

## Submission Checklist
- All required tasks are inside `labs/week04/`.
- Task 1 uses `append()`, `extend()`, `index()`, and non-destructive sorting.
- Task 2 covers aliasing, shallow copy, and deep copy.
- Task 3 covers tuples, unpacking, empty input, and tuple dictionary keys.
- Task 4 covers dictionaries and nested dictionaries.
- Task 5 covers union, intersection, and difference.
- Task 6 contains all three comprehension types.
- Task 7 uses `enumerate()` and `zip()`.
- Task 8 explains data-structure choices and implements examples.
- Task 9 is split across multiple files and handles incomplete/inconsistent records.
- README and AI Usage Log are included.
