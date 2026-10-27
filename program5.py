UNIVERSITY HOSTEL ROOM ALLOCATION:
STATEMENT:
Create a beginner-friendly Python program that assigns students to hostel rooms based on room capacity and student preferences. The program should avoid assigning more students than a room can hold and report when a student cannot be allocated a room.
OBJECTIVES:
- Store available rooms and their capacities.
- Collect student names and room preferences.
- Assign each student to a preferred room when space is available.
- Assign another available room if the preference is full or unavailable.
- Report students who could not be assigned a room.
ASSUMPTIONS:
- Each student needs one bed.
- Room capacities are positive whole numbers.
- Each student may list one or more preferred room numbers.
- Preferences are considered in the order entered.
- If no preferred room has space, the program assigns any available room.
- A student is left unassigned only when all rooms are full.
- This is a simple example and does not include gender, accessibility, year of study, or other institutional policies.
ALGORITHM:
1. Ask how many rooms are available.
2. For each room, enter its room number and capacity.
3. Ask how many students need accommodation.
4. For each student:
   - Enter their name.
   - Enter their preferred room numbers in order.
   - Check the preferred rooms one by one.
   - Assign the student to the first preferred room with space.
   - If no preferred room has space, assign any room with space.
   - If every room is full, mark the student as unassigned.
5. Display each room’s assigned students and any unassigned students.
FLOWCHART:
```mermaid
flowchart TD
    A([Start]) --> B[Enter rooms and capacities]
    B --> C[Enter number of students]
    C --> D[Enter student name and preferences]
    D --> E{Preferred room has space?}
    E -- Yes --> F[Assign student to preferred room]
    E -- No --> G{Any room has space?}
    G -- Yes --> H[Assign student to an available room]
    G -- No --> I[Mark student unassigned]
    F --> J{More students?}
    H --> J
    I --> J
    J -- Yes --> D
    J -- No --> K[Display room assignments and unassigned students]
    K --> L([End])
```
PSEUDOCODE:
INPUT number of rooms

FOR each room:
    INPUT room number
    INPUT capacity
    SET assigned students to an empty list

INPUT number of students

FOR each student:
    INPUT student name
    INPUT preferred room numbers

    SET assigned = false

    FOR each preferred room:
        IF room exists AND room has space:
            ASSIGN student to that room
            SET assigned = true
            STOP checking preferences

    IF assigned is false:
        FOR each available room:
            IF room has space:
                ASSIGN student to that room
                SET assigned = true
                STOP checking rooms

    IF assigned is false:
        ADD student to unassigned list

DISPLAY each room and its assigned students
DISPLAY unassigned students, if any
PYTHON SOURCE CODE:
# University Hostel Room Allocation
# This example allocates one bed to each student.

def get_positive_integer(prompt):
    """Ask for a whole number greater than zero."""
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a whole number.")


def get_room_preferences(prompt):
    """Read room numbers separated by commas."""
    while True:
        text = input(prompt).strip()

        if not text:
            print("Enter at least one room number.")
            continue

        preferences = [item.strip() for item in text.split(",")]

        if all(item.isdigit() for item in preferences):
            return preferences

        print("Enter room numbers separated by commas, such as 101, 102.")


print("University Hostel Room Allocation\n")

rooms = {}

room_count = get_positive_integer("How many rooms are available? ")

for number in range(1, room_count + 1):
    room_number = input(f"Enter room number {number}: ").strip()

    while not room_number or room_number in rooms:
        if not room_number:
            print("Room number cannot be blank.")
        else:
            print("That room number has already been entered.")
        room_number = input(f"Enter a different room number for room {number}: ").strip()

    capacity = get_positive_integer(
        f"Enter the capacity of room {room_number}: "
    )

    rooms[room_number] = {
        "capacity": capacity,
        "students": []
    }

student_count = get_positive_integer("\nHow many students need rooms? ")

unassigned_students = []

for number in range(1, student_count + 1):
    print(f"\nStudent {number}")
    name = input("Student name: ").strip()

    while not name:
        print("Name cannot be blank.")
        name = input("Student name: ").strip()

    preferences = get_room_preferences(
        "Preferred room numbers in order, separated by commas: "
    )

    assigned = False

    # First, try the student's preferred rooms.
    for room_number in preferences:
        if room_number in rooms:
            room = rooms[room_number]
            if len(room["students"]) < room["capacity"]:
                room["students"].append(name)
                print(f"{name} assigned to preferred room {room_number}.")
                assigned = True
                break

    # If no preferred room is available, try any room with space.
    if not assigned:
        for room_number, room in rooms.items():
            if len(room["students"]) < room["capacity"]:
                room["students"].append(name)
                print(f"{name} assigned to available room {room_number}.")
                assigned = True
                break

    # Record the student if every room is full.
    if not assigned:
        unassigned_students.append(name)
        print(f"No room is available for {name}.")

print("\n--- Room Allocation Summary ---")

for room_number, room in rooms.items():
    print(f"\nRoom {room_number}: {len(room['students'])}/{room['capacity']} beds used")

    if room["students"]:
        for student in room["students"]:
            print(f"  - {student}")
    else:
        print("  No students assigned.")

if unassigned_students:
    print("\nStudents without a room:")
    for student in unassigned_students:
        print(f"  - {student}")
else:
    print("\nAll students were assigned a room.")
TEST CASES:
Rooms (capacity)	Students and preferences	Expected result
Room 101 (2), Room 102 (1)	Asha prefers 101; Bala prefers 101; Chitra prefers 101	Asha and Bala go to 101; Chitra is assigned to 102
Room 201 (1), Room 202 (1)	Devi prefers unavailable room 999	Devi is assigned to the available room 201
Room 301 (1)	Farah prefers 301; Gita prefers 301	Farah is assigned to 301; Gita is unassigned
Room 401 (2)	Hari prefers 401; Isha prefers 401	Both are assigned to 401
Capacity entered as 0	—	Program asks for a capacity greater than zero


CONCLUSION:
This program assigns students to rooms while checking room capacity and trying their preferences first. It reports any students who could not be accommodated. A real university allocation system may need additional rules, such as accessibility requirements, roommate requests, or room eligibility.

