import database


USER_CHOICE = """
Enter:

- 'a' to add a new restaurant
- 'l' to list all restaurants
- 's' to search for a restaurant
- 'd' to delete a restaurant
- 'p' to update restaurant price
- 'q' to quit

Your choice: """


# Add Restaurant
def prompt_add_restaurant():

    id = int(input("Enter restaurant id: "))
    res_name = input("Enter restaurant name: ")
    spl_food = input("Enter special food: ")
    rating = float(input("Enter restaurant rating: "))
    location = input("Enter restaurant location: ")
    price = float(input("Enter average price: "))

    database.insert_restaurant(
        id,
        res_name,
        spl_food,
        rating,
        location,
        price
    )


# List Restaurants
def list_restaurants():

    restaurants = database.get_all_restaurants()

    for restaurant in restaurants:

        print(
            f"ID: {restaurant[0]} "
            f"| Name: {restaurant[1]} "
            f"| Special Food: {restaurant[2]} "
            f"| Rating: {restaurant[3]} "
            f"| Location: {restaurant[4]} "
            f"| Price: ₹{restaurant[5]}"
        )


# Search Restaurant
def prompt_search_restaurant():

    res_name = input("Enter restaurant name: ")

    restaurant = database.search_restaurant(res_name)

    if restaurant:

        print("\nRestaurant Found!")

        print(f"ID           : {restaurant[0]}")
        print(f"Name         : {restaurant[1]}")
        print(f"Special Food : {restaurant[2]}")
        print(f"Rating       : {restaurant[3]}")
        print(f"Location     : {restaurant[4]}")
        print(f"Price        : ₹{restaurant[5]}")

    else:

        print("Restaurant not found!")


# Delete Restaurant
def prompt_delete_restaurant():

    res_name = input("Enter restaurant name to delete: ")

    database.delete_restaurant(res_name)


# Update Price
def prompt_update_price():

    res_name = input("Enter restaurant name: ")

    new_price = float(input("Enter new price: "))

    database.update_price(
        res_name,
        new_price
    )


def menu():

    user_input = input(USER_CHOICE)

    while user_input != "q":

        if user_input == "a":
            prompt_add_restaurant()

        elif user_input == "l":
            list_restaurants()

        elif user_input == "s":
            prompt_search_restaurant()

        elif user_input == "d":
            prompt_delete_restaurant()

        elif user_input == "p":
            prompt_update_price()

        else:
            print("Invalid choice!")

        user_input = input(USER_CHOICE)


menu()