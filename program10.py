
SMART CLASSROOM TIMETABLE ALLOCATION:
STATEMENT:
Create a beginner-friendly Python program that assigns classes to available classrooms and time slots. The program should prevent two classes from using the same room at the same time and report any classes that cannot be scheduled.
OBJECTIVES:
- Store classroom names and their capacities.
- Collect class details, including subject, time slot, and number of students.
- Assign each class to a suitable room that is available at that time.
- Avoid room and time conflicts.
- Report classes that could not be scheduled.
ASSUMPTIONS:
- Each class needs one classroom and one time slot.
- A room can host only one class per time slot.
- A class can be placed only in a room that has enough seats.
- The program assigns rooms in the order classes are entered.
- Time slots are entered using consistent labels, such as Monday 9:00 AM.
- The program does not check instructor availability, equipment, building locations, or student timetable conflicts.
ALGORITHM:
1. Ask for the number of classrooms.
2. For each classroom, enter its name and capacity.
3. Ask how many classes need scheduling.
4. For each class, enter the subject, time slot, and student count.
5. Check each classroom in order:
   - Confirm that its capacity is enough.
   - Confirm that it is not already booked in that time slot.
6. Assign the class to the first suitable room.
7. If no room is suitable, add the class to the unscheduled list.
8. Display the timetable and any unscheduled classes.
FLOWCHART:
```mermaid
flowchart TD
    A([Start]) --> B[Enter classrooms and capacities]
    B --> C[Enter class details]
    C --> D{Room capacity enough?}
    D -- No --> E[Try next room]
    D -- Yes --> F{Room free in time slot?}
    F -- No --> E
    F -- Yes --> G[Assign class to room]
    E --> H{More rooms to check?}
    H -- Yes --> D
    H -- No --> I[Mark class unscheduled]
    G --> J{More classes?}
    I --> J
    J -- Yes --> C
    J -- No --> K[Display timetable and unscheduled classes]
    K --> L([End])
```
PSEUDOCODE:
INPUT number of rooms

FOR each room:
    INPUT room name
    INPUT room capacity
    CREATE empty list of booked time slots

INPUT number of classes
CREATE empty timetable
CREATE empty unscheduled list

FOR each class:
    INPUT subject
    INPUT time slot
    INPUT number of students
    SET assigned = false

    FOR each room:
        IF room capacity >= number of students
           AND time slot is not booked in room:
               ASSIGN class to room
               ADD time slot to room's booked slots
               SET assigned = true
               STOP checking rooms

    IF assigned is false:
        ADD class to unscheduled list

DISPLAY timetable
DISPLAY unscheduled classes
PYTHON SOURCE CODE:
# Smart Classroom Timetable Allocation
# A room can host one class per time slot.

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


print("Smart Classroom Timetable Allocation\n")

# Collect classroom details.
rooms = []
room_count = get_positive_integer("How many classrooms are available? ")

for number in range(1, room_count + 1):
    print(f"\nClassroom {number}")

    name = input("Room name or number: ").strip()
    while not name:
        print("Room name cannot be blank.")
        name = input("Room name or number: ").strip()

    capacity = get_positive_integer(f"Capacity of {name}: ")

    rooms.append({
        "name": name,
        "capacity": capacity,
        "booked_slots": []
    })

# Collect and schedule classes.
class_count = get_positive_integer("\nHow many classes need scheduling? ")

timetable = []
unscheduled = []

for number in range(1, class_count + 1):
    print(f"\nClass {number}")

    subject = input("Subject or class name: ").strip()
    while not subject:
        print("Subject name cannot be blank.")
        subject = input("Subject or class name: ").strip()

    time_slot = input("Time slot (for example, Monday 9:00 AM): ").strip()
    while not time_slot:
        print("Time slot cannot be blank.")
        time_slot = input("Time slot: ").strip()

    student_count = get_positive_integer("Number of students: ")

    assigned_room = None

    # Find the first room with enough seats that is free at this time.
    for room in rooms:
        room_is_large_enough = room["capacity"] >= student_count
        room_is_free = time_slot not in room["booked_slots"]

        if room_is_large_enough and room_is_free:
            assigned_room = room
            break

    if assigned_room is not None:
        assigned_room["booked_slots"].append(time_slot)

        timetable.append({
            "subject": subject,
            "time_slot": time_slot,
            "room": assigned_room["name"],
            "students": student_count
        })

        print(f"Scheduled in room {assigned_room['name']}.")
    else:
        unscheduled.append({
            "subject": subject,
            "time_slot": time_slot,
            "students": student_count
        })

        print("Could not schedule this class.")

# Display the timetable.
print("\n--- Timetable ---")

if timetable:
    for entry in timetable:
        print(
            f"{entry['time_slot']} | {entry['subject']} | "
            f"Room {entry['room']} | {entry['students']} students"
        )
else:
    print("No classes were scheduled.")

# Display classes that could not be scheduled.
print("\n--- Unscheduled Classes ---")

if unscheduled:
    for entry in unscheduled:
        print(
            f"{entry['subject']} | {entry['time_slot']} | "
            f"{entry['students']} students"
        )
else:
    print("All classes were scheduled.")
TEST CASES:
Rooms	Classes	Expected result
Room A (30 seats), Room B (50 seats)	Math, Monday 9 AM, 25 students	Math assigned to Room A
Room A (30 seats)	Math and Science, both Monday 9 AM, 25 students each	First class gets Room A; second is unscheduled
Room A (20 seats), Room B (40 seats)	History, Tuesday 10 AM, 35 students	History assigned to Room B
Room A (20 seats)	Biology, Wednesday 1 PM, 25 students	Biology is unscheduled because the room is too small
Room A (30 seats)	Math Monday 9 AM, Science Monday 10 AM	Both classes use Room A in different time slots


CONCLUSION:
This program creates a basic classroom timetable by matching class size with room capacity and checking room availability for each time slot. It prevents room conflicts and lists classes that could not be scheduled. A larger system could also check instructor availability, student conflicts, required equipment, and room location.

  