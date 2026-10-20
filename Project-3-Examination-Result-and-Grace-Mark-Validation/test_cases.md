# Test Cases

| Test | Input marks | Expected result |
|---|---|---|
| 1 | 34, 60, 70 | Final marks [35, 60, 70], 1 grace mark, PASS |
| 2 | 30, 60, 70 | Final marks [30, 60, 70], 0 grace marks, FAIL |
| 3 | 34, 33, 70 | First subject gets 2 grace marks in total? Policy applies in order: final [35, 33, 70], 1 grace mark, FAIL |
| 4 | 100, 101, 50 | Invalid marks |