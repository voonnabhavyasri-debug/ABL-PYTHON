# Problem Statement

An examination result system must process marks in multiple subjects, check subject-wise pass marks, apply a limited grace-mark policy when allowed, and classify the final result without allowing marks to exceed the maximum.

## Objectives
1. Accept marks for three subjects.
2. Validate marks against the maximum marks.
3. Apply grace marks according to the stated policy.
4. Display final marks and pass/fail classification.

## Assumptions
- Each subject is out of 100 and requires at least 35 marks to pass.
- At most 5 grace marks can be awarded in total.
- Grace marks are used only to help a student pass a subject that is short by 1 to 5 marks.
- Grace marks cannot raise a subject above 100.
- Grace marks are awarded in subject order until the limit is used.