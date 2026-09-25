"""A beginner-friendly console program for planning a travel budget."""


def get_positive_integer(prompt):
    """Get a whole number greater than zero."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a whole number.")


def get_non_negative_float(prompt):
    """Get a decimal number that is zero or greater."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Cost cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


def calculate_transportation_cost(cost_per_traveler, number_of_travelers):
    """Return the total transportation cost for all travelers."""
    return cost_per_traveler * number_of_travelers


def calculate_hotel_cost(cost_per_day, number_of_days):
    """Return the total hotel cost for the trip."""
    return cost_per_day * number_of_days


def calculate_food_cost(cost_per_traveler_per_day, number_of_travelers, number_of_days):
    """Return the total food cost for all travelers and days."""
    return cost_per_traveler_per_day * number_of_travelers * number_of_days


def calculate_activity_cost(cost_per_traveler, number_of_travelers):
    """Return the total activity cost for all travelers."""
    return cost_per_traveler * number_of_travelers


def calculate_overall_trip_cost(transportation, hotel, food, activities):
    """Return all trip costs added together."""
    return transportation + hotel + food + activities


def calculate_cost_per_traveler(overall_cost, number_of_travelers):
    """Return the average total cost for one traveler."""
    return overall_cost / number_of_travelers


def calculate_average_daily_cost(overall_cost, number_of_days):
    """Return the average trip cost per day."""
    return overall_cost / number_of_days


def display_travel_summary(travel_information, costs):
    """Display the collected information and calculated costs."""
    print("\n" + "=" * 46)
    print("              SMART TRAVEL SUMMARY")
    print("=" * 46)
    print(f"Traveler name       : {travel_information['traveler_name']}")
    print(f"Destination         : {travel_information['destination']}")
    print(f"Number of travelers : {travel_information['number_of_travelers']}")
    print(f"Number of days      : {travel_information['number_of_days']}")
    print("-" * 46)
    print(f"Transportation cost : ${costs['transportation']:,.2f}")
    print(f"Hotel cost          : ${costs['hotel']:,.2f}")
    print(f"Food cost           : ${costs['food']:,.2f}")
    print(f"Activity cost       : ${costs['activities']:,.2f}")
    print("-" * 46)
    print(f"Overall trip cost   : ${costs['overall']:,.2f}")
    print(f"Cost per traveler   : ${costs['per_traveler']:,.2f}")
    print(f"Average daily cost  : ${costs['daily_average']:,.2f}")
    print("=" * 46)


def main():
    """Collect trip details, calculate costs, and show a summary."""
    print("Welcome to the Smart Travel Planner!")
    print("Enter your trip details below.\n")

    traveler_name = input("Traveler name: ").strip()
    destination = input("Destination: ").strip()
    number_of_travelers = get_positive_integer("Number of travelers: ")
    number_of_days = get_positive_integer("Number of travel days: ")

    transportation_per_traveler = get_non_negative_float(
        "Transportation cost per traveler: $")
    hotel_cost_per_day = get_non_negative_float("Hotel cost per day: $")
    food_cost_per_traveler_per_day = get_non_negative_float(
        "Food cost per traveler per day: $")
    activity_cost_per_traveler = get_non_negative_float(
        "Activity cost per traveler: $")

    # A dictionary keeps related trip details together.
    travel_information = {
        "traveler_name": traveler_name,
        "destination": destination,
        "number_of_travelers": number_of_travelers,
        "number_of_days": number_of_days,
    }

    transportation = calculate_transportation_cost(
        transportation_per_traveler, number_of_travelers)
    hotel = calculate_hotel_cost(hotel_cost_per_day, number_of_days)
    food = calculate_food_cost(
        food_cost_per_traveler_per_day, number_of_travelers, number_of_days)
    activities = calculate_activity_cost(
        activity_cost_per_traveler, number_of_travelers)
    overall = calculate_overall_trip_cost(transportation, hotel, food, activities)

    costs = {
        "transportation": transportation,
        "hotel": hotel,
        "food": food,
        "activities": activities,
        "overall": overall,
        "per_traveler": calculate_cost_per_traveler(
            overall, number_of_travelers),
        "daily_average": calculate_average_daily_cost(overall, number_of_days),
    }

    display_travel_summary(travel_information, costs)


if __name__ == "__main__":
    main()
