

def home_serial(home) -> dict:
    return {
        "uuid": str(home["_id"]),
        "name": home["name"],
        "description": home.get("description"),
        "price": home.get("price"),
        "quantity": home.get("quantity"),
        "number_of_persons": home.get("number_of_persons"),
        "origin_country": home.get("origin_country"),
        "attributes": home.get("attributes", []),
        "utensils": home.get("utensils", []),
        "ingredients": [{"name": item.get("name"), "quantity": item.get("quantity"), "unit": item.get("unit"), "created_by": item.get("created_by")} for item in home.get("ingredients", [])],
        "steps": [{"step_number": item.get("step_number"), "description": item.get("description"), "duration": item.get("duration"), "created_by": item.get("created_by")} for item in home.get("steps", [])],
        "thumbnail_url": home.get("thumbnail_url"),
        "large_image_url": home.get("large_image_url"),
        "source_reference": home.get("source_reference"),
        "created_by": home.get("created_by")
    }


def list_home_serial(homes) -> list:
    return [home_serial(home) for home in homes]
