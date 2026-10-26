
""" PROGRESSIVE ELECTRICITY BILLING

PROBLEM STATEMENT:

Create a program to calculate a household’s electricity bill from its monthly consumption. The bill uses progressive consumption slabs: each portion of electricity is charged at the rate for its slab. Add fixed charges and a surcharge, subtract any rebate, then compare bills across months to flag unusual increases.

OBJECTIVES:

- Calculate energy charges across multiple slabs.
- Add fixed charges and surcharges, then deduct rebates.
- Compare monthly bills and flag significant increases.
- Demonstrate the calculation with clear beginner-level Python code and test cases.

ASSUMPTIONS:

For this example, the tariff is illustrative and uses generic currency units. Replace it with the rates that apply to your electricity provider.

Consumption portion               Rate per kWh 

 First 100 kWh                     5.50 
 Next 200 kWh (101–300)            7.20 
 Next 200 kWh (301–500)           9.50 
 Above 500 kWh                    11.00 



ALGORITHM:

1. Set the slab limits, rates, fixed charge, surcharge rate, rebate rate, and unusual-increase threshold.
2. Ask how many months of bills to calculate.
3. For each month:
   - Read the month name and electricity consumption.
   - Reject negative consumption.
   - Calculate each slab’s kWh:
     - First slab: up to 100 kWh.
     - Second slab: up to 300 kWh, less the first 100 kWh.
     - Third slab: up to 500 kWh, less the first 300 kWh.
     - Fourth slab: any consumption above 500 kWh.
   - Multiply each slab’s kWh by its rate and add the results.
   - Calculate the surcharge and rebate.
   - Calculate the total bill.
   - If a previous bill exists, calculate the percentage change and flag an increase above 20%.
4. Display each month’s slab charges, bill total, and comparison result.

FLOWCHART:

flowchart TD
    A([Start]) --> B[Set tariff and bill rules]
    B --> C[Enter number of months]
    C --> D{More months to process?}
    D -- Yes --> E[Enter month and kWh]
    E --> F{Is kWh negative?}
    F -- Yes --> E
    F -- No --> G[Split kWh across slabs]
    G --> H[Calculate energy charge]
    H --> I[Add fixed charge and surcharge]
    I --> J[Subtract rebate to get bill]
    J --> K{Previous bill exists?}
    K -- No --> M[Save bill and display result]
    K -- Yes --> L[Calculate percentage change]
    L --> N{Increase greater than 20%?}
    N -- Yes --> O[Flag unusual increase]
    N -- No --> M
    O --> M
    M --> D
    D -- No --> P([End])
```

PSEUDOCODE:


SET slab limits and rates
SET fixed charge, surcharge rate, rebate rate
SET unusual increase threshold to 20%

INPUT number of months
SET previous bill to none

FOR each month:
    INPUT month name
    INPUT electricity consumption

    IF consumption is negative:
        DISPLAY error
        ask for consumption again

    CALCULATE kWh in each slab
    CALCULATE energy charge from slab kWh and rates
    CALCULATE surcharge
    CALCULATE rebate
    CALCULATE total bill

    IF previous bill exists:
        CALCULATE percentage change

        IF percentage change > 20%:
            DISPLAY unusual increase
        ELSE:
            DISPLAY within normal range
    ELSE:
        DISPLAY no previous bill to compare

    SET previous bill to total bill
END FOR

DISPLAY all monthly bill results

PYTHON SOURCE CODE:"""
# Progressive Electricity Billing
# Example tariff values; replace them with your utility's actual rates.

FIXED_CHARGE = 150.00
SURCHARGE_RATE = 0.05
REBATE_RATE = 0.02
UNUSUAL_INCREASE_RATE = 0.20


def calculate_bill(consumption):
    """Calculate the bill for a given monthly consumption in kWh."""

    if consumption < 0:
        raise ValueError("Consumption cannot be negative.")

    # Calculate how many kWh fall into each slab.
    slab_1_kwh = min(consumption, 100)
    slab_2_kwh = min(max(consumption - 100, 0), 200)
    slab_3_kwh = min(max(consumption - 300, 0), 200)
    slab_4_kwh = max(consumption - 500, 0)

    # Calculate the charge for each slab.
    slab_1_charge = slab_1_kwh * 5.50
    slab_2_charge = slab_2_kwh * 7.20
    slab_3_charge = slab_3_kwh * 9.50
    slab_4_charge = slab_4_kwh * 11.00

    energy_charge = (
        slab_1_charge
        + slab_2_charge
        + slab_3_charge
        + slab_4_charge
    )

    surcharge = (energy_charge + FIXED_CHARGE) * SURCHARGE_RATE
    rebate = energy_charge * REBATE_RATE

    total_bill = (
        energy_charge
        + FIXED_CHARGE
        + surcharge
        - rebate
    )

    return {
        "slab_1_kwh": slab_1_kwh,
        "slab_2_kwh": slab_2_kwh,
        "slab_3_kwh": slab_3_kwh,
        "slab_4_kwh": slab_4_kwh,
        "energy_charge": energy_charge,
        "fixed_charge": FIXED_CHARGE,
        "surcharge": surcharge,
        "rebate": rebate,
        "total_bill": total_bill,
    }


def main():
    bills = []

    print("Progressive Electricity Bill Calculator")
    print("Enter consumption in kWh for each month.\n")

    while True:
        try:
            number_of_months = int(input("How many months? "))
            if number_of_months <= 0:
                print("Enter a number greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")

    for month_number in range(number_of_months):
        print(f"\nMonth {month_number + 1}")

        month = input("Month name (for example, Jan-2026): ").strip()

        while True:
            try:
                consumption = float(input("Consumption in kWh: "))
                if consumption < 0:
                    print("Consumption cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        bill = calculate_bill(consumption)
        bill["month"] = month

        # Compare this bill with the prior month's bill.
        if bills:
            previous_bill = bills[-1]["total_bill"]
            change = (bill["total_bill"] - previous_bill) / previous_bill
            bill["change"] = change

            if change > UNUSUAL_INCREASE_RATE:
                bill["status"] = "UNUSUAL INCREASE"
            else:
                bill["status"] = "Within range"
        else:
            bill["change"] = None
            bill["status"] = "No previous month"

        bills.append(bill)

    print("\nMonthly bill summary")
    print("-" * 76)

    for bill in bills:
        print(f"\n{bill['month']}")
        print(
            f"  Slab usage (kWh): "
            f"{bill['slab_1_kwh']:.1f}, "
            f"{bill['slab_2_kwh']:.1f}, "
            f"{bill['slab_3_kwh']:.1f}, "
            f"{bill['slab_4_kwh']:.1f}"
        )
        print(f"  Energy charge: {bill['energy_charge']:.2f}")
        print(f"  Fixed charge:  {bill['fixed_charge']:.2f}")
        print(f"  Surcharge:     {bill['surcharge']:.2f}")
        print(f"  Rebate:        {bill['rebate']:.2f}")
        print(f"  Total bill:    {bill['total_bill']:.2f}")

        if bill["change"] is None:
            print(f"  Comparison:    {bill['status']}")
        else:
            print(f"  Change:        {bill['change']:.1%}")
            print(f"  Comparison:    {bill['status']}")


if __name__ == "__main__":
    main()


"""TEST CASES:

Expected results below use the example tariff and generic currency units.

 Case     Consumption      Expected energy charge      Expected total bill         Purpose 

 1        0 kWh            0.00                           157.50                   Zero use; fixed charge and surcharge still apply 
 2        100 kWh         550.00                           721.00                   Exactly at the first slab limit 
 3        300 kWh         1,990.00                          2,269.20                Exactly at the second slab limit 
 4        500 kWh         3,890.00                          4,274.20                Exactly at the third slab limit 
 5        600 kWh         4,990.00                          5,434.20                Consumption in the fourth slab 
 6        -10 kWh                                                                     Must be rejected as invalid input 

The increase comparison can be checked with this example sequence:

Month            Usage                      Expected total                         Comparison 

 January        180 kWh                     1,317.28                                 No previous month 
 February       195 kWh                     1,428.52                                 Within range 
 March           365 kWh                     2,843.23                                 Unusual increase from February 

CONCLUSION:

This program calculates progressive electricity charges by applying the rate for each consumption slab only to the kWh within that slab. It then adds the fixed charge and surcharge, deducts the rebate, and compares each bill with the previous month. The example tariff and 20% alert threshold should be changed to match the user’s utility and preferred comparison rule."""