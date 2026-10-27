MANUFACTURING COST AND PROFITABILITY ANALYSIS:
STATEMENT:
Create a Python program that calculates the manufacturing cost and profitability of a product. The program takes the quantity produced and sold, material, labor, and overhead costs, and the selling price per unit. It calculates total manufacturing cost, cost per unit, revenue, profit, and profit margin.
OBJECTIVE:
- Calculate total material, labor, and overhead costs.
- Find the total and per-unit manufacturing cost.
- Calculate sales revenue and profit.
- Calculate profit margin and report whether the business made a profit or loss.
ASSUMPTIONS:
- All costs and prices are entered in the same currency.
- Quantity produced must be greater than zero.
- Quantity sold cannot be negative or greater than quantity produced.
- Material, labor, and overhead costs are total costs for the production batch.
- All produced units have the same manufacturing cost.
- Unsold units are not counted as sales revenue.
- Profit is calculated as sales revenue minus the full production cost for the batch. This simple model does not calculate inventory value or other expenses such as tax, marketing, or shipping.
- If revenue is zero, profit margin is reported as not applicable.
ALGORITHM:
1. Ask for the quantity produced and quantity sold.
2. Ask for total material, labor, and overhead costs.
3. Ask for the selling price per unit.
4. Check that the inputs are valid.
5. Add material, labor, and overhead costs to find total manufacturing cost.
6. Divide total manufacturing cost by quantity produced to find cost per unit.
7. Multiply quantity sold by selling price per unit to find revenue.
8. Subtract total manufacturing cost from revenue to find profit or loss.
9. If revenue is greater than zero, divide profit by revenue and multiply by 100 to find profit margin.
10. Display the results.
FLOWCHART:
```mermaid
flowchart TD
    A([Start]) --> B[Enter production and sales quantities]
    B --> C[Enter material, labor, overhead, and selling price]
    C --> D{Are inputs valid?}
    D -- No --> E[Display input error]
    E --> B
    D -- Yes --> F[Calculate total manufacturing cost]
    F --> G[Calculate cost per unit]
    G --> H[Calculate sales revenue]
    H --> I[Calculate profit or loss]
    I --> J{Is revenue greater than zero?}
    J -- Yes --> K[Calculate profit margin]
    J -- No --> L[Mark margin not applicable]
    K --> M[Display analysis]
    L --> M
    M --> N([End])
```
PSEUDOCODE:
INPUT quantity produced
INPUT quantity sold
INPUT material cost
INPUT labor cost
INPUT overhead cost
INPUT selling price per unit

IF quantity produced <= 0:
    DISPLAY error
ELSE IF quantity sold < 0 OR quantity sold > quantity produced:
    DISPLAY error
ELSE IF any cost or selling price is negative:
    DISPLAY error
ELSE:
    total manufacturing cost =
        material cost + labor cost + overhead cost

    cost per unit =
        total manufacturing cost / quantity produced

    sales revenue =
        quantity sold * selling price per unit

    profit or loss =
        sales revenue - total manufacturing cost

    IF sales revenue > 0:
        profit margin =
            (profit or loss / sales revenue) * 100
    ELSE:
        profit margin = not applicable

    DISPLAY total manufacturing cost
    DISPLAY cost per unit
    DISPLAY sales revenue
    DISPLAY profit or loss
    DISPLAY profit margin
PYTHON SOURCE CODE:
# Manufacturing Cost and Profitability Analysis
# All monetary values should use the same currency.

def get_non_negative_number(prompt):
    """Ask for a number that is zero or greater."""
    while True:
        try:
            number = float(input(prompt))
            if number < 0:
                print("Please enter a number that is not negative.")
            else:
                return number
        except ValueError:
            print("Please enter a valid number.")


def get_whole_number(prompt):
    """Ask for a whole number."""
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Please enter a whole number.")


print("Manufacturing Cost and Profitability Analysis")

# Get a valid production quantity.
while True:
    quantity_produced = get_whole_number("Quantity produced: ")
    if quantity_produced <= 0:
        print("Quantity produced must be greater than zero.")
    else:
        break

# Get a valid sales quantity.
while True:
    quantity_sold = get_whole_number("Quantity sold: ")
    if quantity_sold < 0:
        print("Quantity sold cannot be negative.")
    elif quantity_sold > quantity_produced:
        print("Quantity sold cannot be greater than quantity produced.")
    else:
        break

material_cost = get_non_negative_number("Total material cost: ")
labor_cost = get_non_negative_number("Total labor cost: ")
overhead_cost = get_non_negative_number("Total overhead cost: ")
selling_price = get_non_negative_number("Selling price per unit: ")

# Calculate costs and profitability.
total_manufacturing_cost = material_cost + labor_cost + overhead_cost
cost_per_unit = total_manufacturing_cost / quantity_produced
sales_revenue = quantity_sold * selling_price
profit_or_loss = sales_revenue - total_manufacturing_cost

if sales_revenue > 0:
    profit_margin = (profit_or_loss / sales_revenue) * 100
else:
    profit_margin = None

# Display the results.
print("\n--- Results ---")
print(f"Total manufacturing cost: {total_manufacturing_cost:.2f}")
print(f"Manufacturing cost per unit: {cost_per_unit:.2f}")
print(f"Sales revenue: {sales_revenue:.2f}")

if profit_or_loss > 0:
    print(f"Profit: {profit_or_loss:.2f}")
elif profit_or_loss < 0:
    print(f"Loss: {abs(profit_or_loss):.2f}")
else:
    print("Result: Break-even (no profit or loss)")

if profit_margin is not None:
    print(f"Profit margin: {profit_margin:.2f}%")
else:
    print("Profit margin: Not applicable because revenue is zero.")
TEST CASES:
All amounts below use generic currency units.
Test	Produced	Sold	Material	Labor	Overhead	Price per unit	Expected result
Profit	100	80	2,000	1,000	500	50	Cost = 3,500; revenue = 4,000; profit = 500; margin = 12.50%
Loss	100	100	4,000	1,500	500	50	Cost = 6,000; revenue = 5,000; loss = 1,000; margin = -20.00%
Break-even	10	10	300	100	100	50	Cost = 500; revenue = 500; profit/loss = 0; margin = 0.00%
No sales	10	0	300	100	100	50	Cost = 500; revenue = 0; loss = 500; margin = not applicable
Invalid quantity	10	12	300	100	100	50	Program rejects quantity sold because it exceeds production


CONCLUSION:
This beginner-friendly program combines material, labor, and overhead costs to estimate the cost of manufacturing a batch. It compares that cost with sales revenue to report profit or loss and profit margin. For real business reporting, the model can be extended to account for unsold inventory, taxes, shipping, and other operating expenses.
