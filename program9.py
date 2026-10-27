CAMPUS EVENT SEATING AND ENTRY VALIDATION
STATEMENT:
Create a beginner-friendly Python program to assign registered attendees to campus event seats and validate their entry. The program should check whether each attendee has a valid ticket, confirm their assigned seat, prevent duplicate entries, and report when seating capacity is full.
OBJECTIVES:
- Store available seat numbers and attendee ticket details.
- Assign each registered attendee an available seat.
- Validate ticket IDs at the entrance.
- Prevent a ticket from being used more than once.
- Display entry approval or rejection with a reason.
ASSUMPTIONS:
- Each ticket ID is unique.
- Each attendee can occupy one seat.
- Only registered attendees can receive seats.
- A valid ticket can be used once.
- Seats are assigned in order, starting from seat 1.
- This example uses a simple list of ticket IDs rather than secure barcode scanning.
- No special seating, accessibility, or group-seating rules are included.
ALGORITHM:
1. Ask for the number of available seats.
2. Ask how many people are registered.
3. Collect each attendee’s name and unique ticket ID.
4. Assign a seat to each attendee while seats remain.
5. Record attendees without seats if registration exceeds capacity.
6. At entry, ask for a ticket ID.
7. Check whether the ticket ID exists in the attendee list.
8. If it is unknown, reject entry.
9. If it has already been used, reject duplicate entry.
10. If it is valid and unused, mark it as used and approve entry.
11. Display each attendee’s seat assignment and entry status.
FLOWCHART:
```mermaid
flowchart TD
    A([Start]) --> B[Enter capacity and attendee details]
    B --> C[Assign seats while available]
    C --> D[Enter ticket ID at entrance]
    D --> E{Is ticket registered?}
    E -- No --> F[Reject: unknown ticket]
    E -- Yes --> G{Was ticket used already?}
    G -- Yes --> H[Reject: duplicate entry]
    G -- No --> I[Approve entry and mark ticket used]
    F --> J{More tickets to check?}
    H --> J
    I --> J
    J -- Yes --> D
    J -- No --> K[Display seating and entry summary]
    K --> L([End])
```
PSEUDOCODE:
INPUT seating capacity
INPUT number of registered attendees

CREATE empty attendee list

FOR each attendee:
    INPUT name
    INPUT unique ticket ID

    IF a seat is available:
        ASSIGN next seat number
        STORE attendee, ticket ID, and seat
    ELSE:
        STORE attendee as waitlisted

CREATE empty list of used ticket IDs

INPUT number of entry checks

FOR each entry check:
    INPUT ticket ID

    IF ticket ID is not registered:
        REJECT entry
    ELSE IF ticket ID is already used:
        REJECT duplicate entry
    ELSE:
        APPROVE entry
        ADD ticket ID to used ticket IDs

DISPLAY attendee seat assignments
DISPLAY waitlisted attendees
DISPLAY entry results
PYTHON SOURCE CODE :
# Campus Event Seating and Entry Validation
# This program assigns seats and checks tickets at the entrance.

def get_non_negative_integer(prompt):
    """Ask for a whole number that is zero or greater."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Enter zero or a positive whole number.")
        except ValueError:
            print("Please enter a whole number.")


print("Campus Event Seating and Entry System\n")

capacity = get_non_negative_integer("Number of available seats: ")
attendee_count = get_non_negative_integer("Number of registered attendees: ")

attendees = []
ticket_ids = set()

# Collect attendee details and assign seats.
for number in range(1, attendee_count + 1):
    print(f"\nAttendee {number}")

    name = input("Name: ").strip()
    while not name:
        print("Name cannot be blank.")
        name = input("Name: ").strip()

    ticket_id = input("Unique ticket ID: ").strip()
    while not ticket_id or ticket_id in ticket_ids:
        if not ticket_id:
            print("Ticket ID cannot be blank.")
        else:
            print("That ticket ID is already registered.")
        ticket_id = input("Enter a different ticket ID: ").strip()

    ticket_ids.add(ticket_id)

    if len(attendees) < capacity:
        seat_number = len(attendees) + 1
        attendees.append({
            "name": name,
            "ticket_id": ticket_id,
            "seat": seat_number,
            "status": "Seated",
        })
    else:
        attendees.append({
            "name": name,
            "ticket_id": ticket_id,
            "seat": None,
            "status": "Waitlisted - no seat available",
        })

# Ask how many tickets will be checked at the entrance.
entry_check_count = get_non_negative_integer(
    "\nHow many tickets will be checked at the entrance? "
)

used_ticket_ids = set()
entry_results = []

for check_number in range(1, entry_check_count + 1):
    ticket_id = input(f"\nEnter ticket ID for check {check_number}: ").strip()

    matching_attendee = None

    for attendee in attendees:
        if attendee["ticket_id"] == ticket_id:
            matching_attendee = attendee
            break

    if matching_attendee is None:
        result = "REJECTED - ticket not registered"
    elif matching_attendee["seat"] is None:
        result = "REJECTED - no seat was assigned"
    elif ticket_id in used_ticket_ids:
        result = "REJECTED - ticket already used"
    else:
        used_ticket_ids.add(ticket_id)
        result = (
            f"APPROVED - {matching_attendee['name']}, "
            f"Seat {matching_attendee['seat']}"
        )

    entry_results.append((ticket_id, result))
    print(result)

# Display seating assignments.
print("\n--- Seating List ---")

if not attendees:
    print("No attendees were registered.")
else:
    for attendee in attendees:
        if attendee["seat"] is not None:
            print(
                f"Seat {attendee['seat']}: {attendee['name']} "
                f"(Ticket {attendee['ticket_id']})"
            )
        else:
            print(
                f"{attendee['name']} (Ticket {attendee['ticket_id']}): "
                f"{attendee['status']}"
            )

# Display entry check summary.
print("\n--- Entry Check Summary ---")
if not entry_results:
    print("No tickets were checked.")
else:
    for ticket_id, result in entry_results:
        print(f"{ticket_id}: {result}")
TESTCASES:
Capacity	Registered attendees	Entry checks	Expected result
2	Asha/T101, Bala/T102	T101	T101 approved with Seat 1
1	Chitra/T201, Dev/T202	T202	T202 rejected because no seat was assigned
2	Esha/T301	T999	T999 rejected because it is not registered
2	Farah/T401	T401, then T401 again	First check approved; second rejected as already used
2	Gita/T501, Hari/T501	—	Duplicate ticket ID is rejected during registration
0	Isha/T601	T601	Attendee is waitlisted; entry is rejected because no seat was assigned


CONCLUSION:
This program assigns numbered seats up to the event’s capacity and validates registered tickets at the entrance. It blocks unknown tickets, duplicate use, and entry for attendees without an assigned seat. Real event systems may also need waitlist promotion, reserved seating, QR scanning, and secure ticket storage.