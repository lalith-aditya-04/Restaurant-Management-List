restaurants = []


def insert_restaurant(id, res_name, spl_food, rating, location, price):

    restaurant = [id, res_name, spl_food, rating, location, price]

    restaurants.append(restaurant)

    print("Restaurant added successfully!")


def get_all_restaurants():

    return restaurants


def search_restaurant(res_name):

    for restaurant in restaurants:

        if restaurant[1].lower() == res_name.lower():
            return restaurant

    return None


def delete_restaurant(res_name):

    for restaurant in restaurants:

        if restaurant[1].lower() == res_name.lower():

            restaurants.remove(restaurant)

            print("Restaurant deleted successfully!")

            return True

    print("Restaurant not found!")

    return False


def update_price(res_name, new_price):

    restaurant = search_restaurant(res_name)

    if restaurant:

        restaurant[5] = new_price

        print("Price updated successfully!")

        return True

    print("Restaurant not found!")

    return False