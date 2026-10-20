# Test Cases

Use each row as a separate program run.

| Test | Units | Material/unit | Labour/unit | Wastage | Machine | Selling/unit | Target profit | Expected result |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 100 | 50 | 20 | 200 | 300 | 100 | 2000 | Total cost 7500; revenue 10000; profit 2500; target achieved |
| 2 | 50 | 60 | 20 | 100 | 200 | 70 | 500 | Total cost 4300; revenue 3500; profit -800; target not achieved |
| 3 | 10 | 10 | 5 | 0 | 0 | 15 | 0 | Total cost 150; revenue 150; profit 0; target achieved |
| 4 | 0 | 50 | 20 | 200 | 300 | 100 | 2000 | Invalid input |
| 5 | 20 | 10 | 5 | -10 | 100 | 30 | 100 | Invalid input |

## Calculation for Test Case 1
- Material cost = 100 × 50 = 5000
- Labour cost = 100 × 20 = 2000
- Total production cost = 5000 + 2000 + 200 + 300 = 7500
- Sales revenue = 100 × 100 = 10000
- Profit = 10000 − 7500 = 2500
- Since 2500 ≥ 2000, the target is achieved.
