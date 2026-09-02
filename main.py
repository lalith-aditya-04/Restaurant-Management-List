from fastapi import FastAPI
import database


app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Restaurant Management "
    }


@app.get("/restaurants")
def get_restaurants():

    return database.get_all_restaurants()


@app.get("/restaurants/{res_name}")
def search_restaurant(res_name: str):

    restaurant = database.search_restaurant(res_name)

    if restaurant:

        return restaurant

    return {
        "message": "Restaurant not found!"
    }


@app.post("/restaurants")
def add_restaurant(
    id: int,
    res_name: str,
    spl_food: str,
    rating: float,
    location: str,
    price: float
):

    database.insert_restaurant(
        id,
        res_name,
        spl_food,
        rating,
        location,
        price
    )

    return {
        "message": "Restaurant added successfully!"
    }


@app.delete("/restaurants/{res_name}")
def delete_restaurant(res_name: str):

    result = database.delete_restaurant(res_name)

    if result:

        return {
            "message": "Restaurant deleted successfully!"
        }

    return {
        "message": "Restaurant not found!"
    }


@app.put("/restaurants/{res_name}/price")
def update_price(
    res_name: str,
    new_price: float
):

    result = database.update_price(
        res_name,
        new_price
    )

    if result:

        return {
            "message": "Price updated successfully!"
        }

    return {
        "message": "Restaurant not found!"
    }