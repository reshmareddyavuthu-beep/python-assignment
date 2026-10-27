
NESTED LIST SPORTS PERFORMANCE ANALYSIS:
STATEMENT:
Create a beginner-friendly Python program that stores several athletes’ scores across multiple sports events using a nested list. The program calculates each athlete’s average score, identifies their best event, and ranks athletes by average score.
OBJECTIVE:
- Store athlete names and event scores in a nested list.
- Calculate each athlete’s average score.
- Find each athlete’s highest-scoring event.
- Rank athletes from highest to lowest average.
ASSUMPTIONS:
- Each score is from 0 to 100.
- Every athlete has a score for every event.
- All events have equal weight.
- Athlete names and event names are entered in the same order for everyone.
- Athletes with equal averages share the same rank.
- The example does not account for different scoring systems across sports.
ALGORITHM:
1. Ask for the number of athletes and events.
2. Collect the event names.
3. For each athlete:
   - Collect their name.
   - Enter one score for every event.
   - Store the name and scores in a nested list.
4. Calculate each athlete’s average score.
5. Find their highest score and corresponding event.
6. Sort athletes by average score in descending order.
7. Display each athlete’s average, best event, and rank.
FLOWCHART:
```mermaid
flowchart TD
    A([Start]) --> B[Enter number of athletes and events]
    B --> C[Enter event names]
    C --> D[Enter athlete name and event scores]
    D --> E{Are scores between 0 and 100?}
    E -- No --> D
    E -- Yes --> F{More athletes?}
    F -- Yes --> D
    F -- No --> G[Calculate averages and best events]
    G --> H[Sort athletes by average]
    H --> I[Display ranked results]
    I --> J([End])
```
PSEUDOCSDE:
INPUT number of athletes
INPUT number of events
INPUT event names

SET athlete_records to an empty list

FOR each athlete:
    INPUT athlete name
    SET scores to an empty list

    FOR each event:
        INPUT score
        WHILE score is below 0 or above 100:
            DISPLAY error
            INPUT score again
        ADD score to scores

    ADD [athlete name, scores] to athlete_records

FOR each athlete record:
    CALCULATE average score
    FIND highest score
    FIND event with highest score
    SAVE average and best event

SORT athletes by average from highest to lowest
DISPLAY each athlete's rank, average, and best event
PYTHON SOURCE CODE:
# Nested List Sports Performance Analysis
# Scores for each athlete are stored in a nested list.

def get_positive_integer(prompt):
    """Ask for a whole number greater than zero."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Enter a number greater than zero.")
        except ValueError:
            print("Please enter a whole number.")


def get_score(athlete_name, event_name):
    """Ask for a score between 0 and 100."""
    while True:
        try:
            score = float(
                input(f"Score for {athlete_name} in {event_name}: ")
            )

            if 0 <= score <= 100:
                return score

            print("The score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


print("Sports Performance Analysis\n")

athlete_count = get_positive_integer("Number of athletes: ")
event_count = get_positive_integer("Number of events: ")

events = []

for number in range(1, event_count + 1):
    event_name = input(f"Enter event {number}'s name: ").strip()

    while not event_name:
        print("Event name cannot be blank.")
        event_name = input(f"Enter event {number}'s name: ").strip()

    events.append(event_name)

# Each item in athlete_records is:
# [athlete_name, [score_for_event_1, score_for_event_2, ...]]
athlete_records = []

for number in range(1, athlete_count + 1):
    athlete_name = input(f"\nEnter athlete {number}'s name: ").strip()

    while not athlete_name:
        print("Athlete name cannot be blank.")
        athlete_name = input(f"Enter athlete {number}'s name: ").strip()

    scores = []

    for event_name in events:
        score = get_score(athlete_name, event_name)
        scores.append(score)

    athlete_records.append([athlete_name, scores])

# Create a list containing each athlete's results.
results = []

for athlete_name, scores in athlete_records:
    average_score = sum(scores) / len(scores)
    best_score = max(scores)
    best_event_index = scores.index(best_score)
    best_event = events[best_event_index]

    results.append({
        "name": athlete_name,
        "scores": scores,
        "average": average_score,
        "best_score": best_score,
        "best_event": best_event,
    })

# Sort from highest average score to lowest.
results.sort(key=lambda athlete: athlete["average"], reverse=True)

print("\n--- Sports Performance Rankings ---")

previous_average = None
current_rank = 0

for position, athlete in enumerate(results, start=1):
    if athlete["average"] != previous_average:
        current_rank = position

    print(
        f"Rank {current_rank}: {athlete['name']} | "
        f"Average: {athlete['average']:.2f} | "
        f"Best event: {athlete['best_event']} "
        f"({athlete['best_score']:.1f})"
    )

    previous_average = athlete["average"]
TEST CASES:
Athlete scores	Expected average	Expected best event
Asha: Cricket 80, Football 90, Tennis 70	80.00	Football (90)
Bala: Cricket 95, Football 85, Tennis 90	90.00	Cricket (95)
Chitra: Cricket 60, Football 60, Tennis 60	60.00	Cricket (60), the first event with the highest score
Scores include 105	—	105 is rejected; program asks for a score from 0 to 100
Two athletes average 80	80.00 each	They share the same rank


CONCLUSION:
This program uses a nested list to keep each athlete’s scores together. It calculates averages, identifies the best event, and ranks athletes by average score. It is a simple starting point; real sports comparisons may need event-specific scoring rules or weights.

  
