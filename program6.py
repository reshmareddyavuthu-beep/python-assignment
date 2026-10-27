PROGRESSIVE WATER TRAFFIC ANALYSIS:
STATEMENT:
Create a beginner-friendly Python program that calculates a household’s water bill based on monthly water consumption. The program applies progressive tariff rates, adds a fixed service charge and tax, and displays a breakdown of the bill.
OBJECTIVES:
- Calculate charges for water used in multiple consumption slabs.
- Add a fixed service charge and tax.
- Display the slab usage and total bill.
- Validate inputs, including negative consumption.
ASSUMPTIONS:
The following rates are examples only. Replace them with the rates used by your water provider.
Consumption portion	Rate per unit
First 10 units	5.00
Next 10 units (11–20)	8.00
Next 10 units (21–30)	12.00
Above 30 units	16.00


- Consumption is entered in whole units.
- Fixed service charge: 25.00 generic currency units.
- Tax: 5% of the water charge plus fixed service charge.
- There are no rebates or late fees.
- Consumption cannot be negative.
- Charges are rounded to two decimal places for display.
ALGORITHM:
1. Set the slab limits, rates, fixed charge, and tax rate.
2. Ask the user for monthly water consumption.
3. Check that the entered consumption is a non-negative number.
4. Calculate the number of units charged in each slab.
5. Multiply each slab’s units by its rate and add the charges.
6. Add the fixed service charge.
7. Calculate tax on the water charge plus fixed charge.
8. Add tax to find the final bill.
9. Display the slab breakdown, water charge, fixed charge, tax, and total.
FLOWCHART:
```mermaid
flowchart TD
    A([Start]) --> B[Enter monthly water consumption]
    B --> C{Is consumption valid and non-negative?}
    C -- No --> D[Display error and ask again]
    D --> B
    C -- Yes --> E[Split usage across tariff slabs]
    E --> F[Calculate each slab charge]
    F --> G[Add slab charges]
    G --> H[Add fixed service charge]
    H --> I[Calculate tax]
    I --> J[Calculate final bill]
    J --> K[Display bill breakdown]
    K --> L([End])
```
PSEUDOCODE:
SET slab limits and rates
SET fixed charge
SET tax rate

INPUT water consumption

WHILE consumption is invalid or negative:
    DISPLAY error
    INPUT consumption again

CALCULATE units in each slab
CALCULATE charge for each slab
CALCULATE total water charge

CALCULATE subtotal = water charge + fixed charge
CALCULATE tax = subtotal * tax rate
CALCULATE final bill = subtotal + tax

DISPLAY slab usage and charges
DISPLAY water charge, fixed charge, tax, and final bill
PYTHON SOURCE CODE:
# Progressive Water Tariff Calculator
# Example tariff values only. Replace them with your provider's rates.

FIXED_CHARGE = 25.00
TAX_RATE = 0.05


def get_consumption():
    """Ask for non-negative water consumption."""
    while True:
        try:
            consumption = float(input("Enter monthly water consumption: "))

            if consumption < 0:
                print("Consumption cannot be negative.")
            else:
                return consumption

        except ValueError:
            print("Please enter a valid number.")


print("Progressive Water Tariff Calculator\n")

consumption = get_consumption()

# Split consumption among the four slabs.
slab_1_units = min(consumption, 10)
slab_2_units = min(max(consumption - 10, 0), 10)
slab_3_units = min(max(consumption - 20, 0), 10)
slab_4_units = max(consumption - 30, 0)

# Calculate the charge for each slab.
slab_1_charge = slab_1_units * 5.00
slab_2_charge = slab_2_units * 8.00
slab_3_charge = slab_3_units * 12.00
slab_4_charge = slab_4_units * 16.00

water_charge = (
    slab_1_charge
    + slab_2_charge
    + slab_3_charge
    + slab_4_charge
)

subtotal = water_charge + FIXED_CHARGE
tax = subtotal * TAX_RATE
total_bill = subtotal + tax

print("\n--- Water Bill Breakdown ---")
print(f"Slab 1: {slab_1_units:.2f} units × 5.00 = {slab_1_charge:.2f}")
print(f"Slab 2: {slab_2_units:.2f} units × 8.00 = {slab_2_charge:.2f}")
print(f"Slab 3: {slab_3_units:.2f} units × 12.00 = {slab_3_charge:.2f}")
print(f"Slab 4: {slab_4_units:.2f} units × 16.00 = {slab_4_charge:.2f}")
print(f"Water charge: {water_charge:.2f}")
print(f"Fixed service charge: {FIXED_CHARGE:.2f}")
print(f"Tax ({TAX_RATE * 100:.0f}%): {tax:.2f}")
print(f"Total bill: {total_bill:.2f}")
TEST CASES:
All amounts use generic currency units.
Consumption	Water charge	Fixed charge	Tax	Expected total bill
0 units	0.00	25.00	1.25	26.25
10 units	50.00	25.00	3.75	78.75
15 units	90.00	25.00	5.75	120.75
30 units	250.00	25.00	13.75	288.75
35 units	330.00	25.00	17.75	372.75
-3 units	—	—	—	Rejected; prompt for valid consumption


CONCLUSION:
This program calculates a water bill by charging each portion of consumption at its corresponding slab rate. It then adds a fixed service charge and tax, showing a clear bill breakdown. The example rates and tax should be updated to match the actual water provider’s tariff.