 STUDENT PERFORMANCE TREND ANALYSIS:
STATEMENT:
Create a beginner-friendly Python program that records a student’s marks across several assessments, calculates the average and percentage, and identifies whether performance is improving, declining, or staying steady.
OBJECTIVES:
- Accept marks for multiple assessments.
- Calculate the average mark and overall percentage.
- Compare the first and last marks to describe the performance trend.
- Display a simple performance summary.
ASSUMPTIONS:
- Each assessment is scored out of 100.
- Marks must be between 0 and 100.
- At least two assessments are needed to identify a trend.
- The trend is based on the difference between the first and last marks:
  - Increase of more than 2 points: Improving
  - Decrease of more than 2 points: Declining
  - Difference from −2 to +2 points: Steady
- All assessments have equal weight.
- The program does not account for differences in assessment difficulty.
ALGORITHM:
1. Ask how many assessments the student completed.
2. Require at least two assessments.
3. For each assessment, ask for a mark between 0 and 100.
4. Calculate the average mark.
5. Calculate the percentage from the average.
6. Compare the last mark with the first mark.
7. Classify the trend using the 2-point threshold.
8. Display the marks, average, percentage, and trend.

FLOW CHART:
    A([Start]) --> B[Enter number of assessments]
    B --> C{At least two?}
    C -- No --> D[Display error and ask again]
    D --> B
    C -- Yes --> E[Enter each mark from 0 to 100]
    E --> F{Is each mark valid?}
    F -- No --> E
    F -- Yes --> G[Calculate average and percentage]
    G --> H[Compare last mark with first mark]
    H --> I{Difference greater than 2?}
    I -- Yes --> J[Trend is Improving]
    I -- No --> K{Difference less than -2?}
    K -- Yes --> L[Trend is Declining]
    K -- No --> M[Trend is Steady]
    J --> N[Display summary]
    L --> N
    M --> N
    N --> O([End])
```
PSEUDOCODE:
INPUT number of assessments
WHILE number of assessments is less than 2:
    DISPLAY error
    INPUT number of assessments again

SET marks to an empty list

FOR each assessment:
    INPUT mark
    WHILE mark is less than 0 or greater than 100:
        DISPLAY error
        INPUT mark again
    ADD mark to marks

CALCULATE average mark
SET percentage equal to average mark

SET change to last mark minus first mark

IF change > 2:
    SET trend to "Improving"
ELSE IF change < -2:
    SET trend to "Declining"
ELSE:
    SET trend to "Steady"

DISPLAY marks, average, percentage, and trend
PYTHON SOURCE CODE:
# Student Performance Trend Analysis
# Each assessment is scored out of 100.

TREND_THRESHOLD = 2


def get_assessment_count():
    """Get a whole number of assessments, with at least two."""
    while True:
        try:
            count = int(input("How many assessments? "))

            if count >= 2:
                return count

            print("Enter at least two assessments to analyze a trend.")

        except ValueError:
            print("Please enter a whole number.")


def get_mark(assessment_number):
    """Get a mark between 0 and 100."""
    while True:
        try:
            mark = float(input(f"Enter mark for assessment {assessment_number}: "))

            if 0 <= mark <= 100:
                return mark

            print("The mark must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


print("Student Performance Trend Analysis\n")

assessment_count = get_assessment_count()
marks = []

for number in range(1, assessment_count + 1):
    mark = get_mark(number)
    marks.append(mark)

average_mark = sum(marks) / len(marks)
percentage = average_mark  # Each assessment is out of 100.
change = marks[-1] - marks[0]

if change > TREND_THRESHOLD:
    trend = "Improving"
elif change < -TREND_THRESHOLD:
    trend = "Declining"
else:
    trend = "Steady"

print("\n--- Performance Summary ---")
print("Marks:", ", ".join(f"{mark:.1f}" for mark in marks))
print(f"Average mark: {average_mark:.2f} out of 100")
print(f"Overall percentage: {percentage:.2f}%")
print(f"Change from first to last assessment: {change:+.2f} points")
print(f"Performance trend: {trend}")
TEST CASES:
Marks entered	Expected average	Expected trend
60, 70, 80	70.00	Improving
85, 80, 75	80.00	Declining
70, 71, 69	70.00	Steady
50, 50	50.00	Steady
0, 10	5.00	Improving
80, 105	Invalid input; 105 must be rejected and entered again	
Only 1 assessment	Invalid count; at least 2 are required	


CONCLUSION:
This program summarizes a student’s assessment marks and labels the trend as improving, declining, or steady based on the first and last marks. It validates the inputs and gives a simple starting point for tracking performance. For a fuller analysis, the program could also compare each assessment with the previous one or calculate trends separately by subject.

  
