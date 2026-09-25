# Smart Travel Planner

Smart Travel Planner is a beginner-friendly Python console program that estimates
the cost of a trip. It collects basic traveler and budget information, performs
the calculations, and prints a clean travel summary.

## How to run

Make sure Python 3 is installed, then run this command from the project folder:

```text
python smart_travel_planner.py
```

The program asks for:

- Traveler name and destination
- Number of travelers and travel days
- Transportation cost per traveler
- Hotel cost per day
- Food cost per traveler per day
- Activity cost per traveler

Food cost per traveler per day is collected because it is needed to calculate the
total food cost accurately.

## Project flow

1. The program starts in the `main()` function and displays a welcome message.
2. It collects the traveler's name and destination.
3. It asks for the number of travelers and travel days.
4. It validates both values to make sure they are whole numbers greater than zero.
5. It collects transportation, hotel, food, and activity costs.
6. It validates every cost so negative values are not accepted.
7. It stores the trip details in a dictionary.
8. It calls a separate function for each major cost calculation.
9. It adds the individual costs to find the overall trip cost.
10. It calculates the cost per traveler and average daily cost.
11. It stores the calculated costs in a dictionary.
12. It displays a formatted travel summary.

## Code explanation

### 1. Input and validation functions

The program uses helper functions so input is collected consistently. The
`get_positive_integer()` function repeats the question until the user enters a
whole number greater than zero:

```python
def get_positive_integer(prompt):
	while True:
		try:
			value = int(input(prompt))
			if value > 0:
				return value
			print("Please enter a number greater than 0.")
		except ValueError:
			print("Please enter a whole number.")
```

The `get_non_negative_float()` function converts costs to `float` values and
rejects negative costs. `try` and `except` prevent the program from stopping
when the user types invalid text.

### 2. Calculation functions

Each major calculation has its own function. Parameters receive the required
values, and `return` sends the answer back to `main()`:

```python
def calculate_food_cost(
		cost_per_traveler_per_day, number_of_travelers, number_of_days):
	return (cost_per_traveler_per_day * number_of_travelers
			* number_of_days)


def calculate_overall_trip_cost(transportation, hotel, food, activities):
	return transportation + hotel + food + activities
```

The other functions use the same pattern for transportation, hotel, activities,
cost per traveler, and average daily cost.

### 3. Organizing information with dictionaries

The program stores related values in dictionaries. Dictionary keys describe the
values, which makes the data easier to read:

```python
travel_information = {
	"traveler_name": traveler_name,
	"destination": destination,
	"number_of_travelers": number_of_travelers,
	"number_of_days": number_of_days,
}
```

The calculated values are stored in a second `costs` dictionary. The summary
function reads values with expressions such as `costs["overall"]`.

### 4. The `main()` function

`main()` controls the program flow. It collects input, calls the calculation
functions, creates the dictionaries, and sends the final data to
`display_travel_summary()`:

```python
transportation = calculate_transportation_cost(
	transportation_per_traveler, number_of_travelers)
hotel = calculate_hotel_cost(hotel_cost_per_day, number_of_days)
overall = calculate_overall_trip_cost(transportation, hotel, food, activities)
```

This keeps input, calculations, and output organized into separate parts.

### 5. Starting the program

The final two lines make sure `main()` runs when the file is executed directly:

```python
if __name__ == "__main__":
	main()
```

## Calculations

The program calculates and displays:

- Total transportation cost
- Total hotel cost
- Total food cost
- Total activity cost
- Overall trip cost
- Cost per traveler
- Average daily cost

Each major calculation has its own function. The functions receive values through
parameters and return the calculated results. The program uses a dictionary to
keep related travel information and calculated costs organized.

## Input validation

- The number of travelers must be greater than zero.
- The number of travel days must be greater than zero.
- Costs must be zero or greater.
- Invalid whole numbers and decimal values are requested again.

## Python concepts demonstrated

This project demonstrates variables, strings, integers, floats, user input, type
conversion, dictionaries, functions, parameters, return values, arithmetic
operations, loops, validation, and formatted output. It uses only Python's
built-in features and does not use a database, files, APIs, external libraries,
or classes.