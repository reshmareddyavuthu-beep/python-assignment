
HACKATHON TEAM FORMATION AND RANKING:
STATEMENT:
Create a beginner-friendly Python program that forms hackathon teams from a list of participants and ranks the teams using their project scores.

The program should put participants into teams of a chosen size, collect a score for each team, and display the teams from highest score to lowest.
 OBJECTIVES:
- Collect participant names.
- Divide participants into teams of a specified size.
- Handle a group that does not divide evenly into teams.
- Enter and validate a project score for each team.
- Rank teams from highest score to lowest.
ASSUMPTIONS:
- Each participant can belong to only one team.
- Participants are placed in the order entered.
- The final team may have fewer members than the requested team size.
- Each team receives one score from 0 to 100.
- Teams with equal scores share the same position in the ranking.
- This beginner example does not match participants by skills or preferences.
ALGORITHIM:
1. Ask for the number of participants.
2. Ask for each participant’s name.
3. Ask for the maximum team size.
4. Divide participants into teams in the order entered.
5. For each team, ask for a project score from 0 to 100.
6. Validate each score.
7. Sort teams by score in descending order.
8. Display each team’s rank, score, and members.
FLOWCHART:
```mermaid
flowchart TD
    A([Start]) --> B[Enter participant names]
    B --> C[Enter maximum team size]
    C --> D[Divide participants into teams]
    D --> E[Enter score for each team]
    E --> F{Is score between 0 and 100?}
    F -- No --> E
    F -- Yes --> G{More teams to score?}
    G -- Yes --> E
    G -- No --> H[Sort teams by score, highest first]
    H --> I[Display ranking and members]
    I --> J([End])
```
PSEUDOCODE:
INPUT number of participants
INPUT each participant's name
INPUT team size

CREATE an empty list of teams

FOR each participant:
    ADD participant to the current team
    IF current team reaches team size:
        ADD current team to teams
        START a new team

IF current team is not empty:
    ADD current team to teams

FOR each team:
    INPUT team score
    WHILE score is below 0 or above 100:
        DISPLAY error
        INPUT score again

SORT teams by score from highest to lowest

SET rank to 1
FOR each team in sorted order:
    DISPLAY rank, score, and team members
    UPDATE rank, keeping equal scores at the same position
PYTHON SOURCE CODE:
# Hackathon Team Formation and Ranking
# Participants are assigned in the order they are entered.

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


def get_score(team_number):
    """Ask for a score from 0 to 100."""
    while True:
        try:
            score = float(input(f"Enter the score for Team {team_number} (0-100): "))
            if 0 <= score <= 100:
                return score
            print("The score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


print("Hackathon Team Formation and Ranking\n")

participant_count = get_positive_integer("Number of participants: ")

participants = []

for number in range(1, participant_count + 1):
    name = input(f"Enter participant {number}'s name: ").strip()

    while not name:
        print("Name cannot be blank.")
        name = input(f"Enter participant {number}'s name: ").strip()

    participants.append(name)

team_size = get_positive_integer("Maximum members per team: ")

# Divide participants into teams.
teams = []

for start in range(0, len(participants), team_size):
    members = participants[start:start + team_size]
    teams.append({
        "members": members,
        "score": 0
    })

print(f"\nThe program formed {len(teams)} team(s).")

# Enter a score for each team.
for number, team in enumerate(teams, start=1):
    print(f"\nTeam {number}: {', '.join(team['members'])}")
    team["score"] = get_score(number)

# Sort teams from highest score to lowest.
ranked_teams = sorted(
    teams,
    key=lambda team: team["score"],
    reverse=True
)

print("\n--- Hackathon Team Rankings ---")

previous_score = None
current_rank = 0

for position, team in enumerate(ranked_teams, start=1):
    if team["score"] != previous_score:
        current_rank = position

    print(
        f"Rank {current_rank}: "
        f"Score {team['score']:.1f} — "
        f"{', '.join(team['members'])}"
    )

    previous_score = team["score"]
TEST CASES:
Participants	Team size	Team scores	Expected result
Asha, Bala, Chitra, Dev	2	85, 92	Two teams; second team ranks first
Asha, Bala, Chitra, Dev, Esha	2	80, 95, 70	Three teams; last team has one member; second team ranks first
Ana, Ben, Chen, Diya	2	90, 90	Teams share rank 1
One participant	3	75	One team with one member
Score entered as 105	Any valid team	105, then 80	105 is rejected; program asks for a score from 0 to 100
Team size entered as 0	—	—	Program rejects it and asks for a positive number


CONCLUSION:
This program groups participants in the order entered, collects a score for each team, and ranks teams from highest to lowest. It supports teams of different sizes when the participant count does not divide evenly and handles tied scores. For a real hackathon, team formation could be improved by considering skills, interests, or participant preferences.
