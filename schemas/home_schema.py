

def home_serial(home) -> dict:
    return {
        "uuid": str(home["_id"]),
        "name": home["name"],
        "description": home.get("description"),
        "created_by": home.get("created_by")
    }


def list_home_serial(homes) -> list:
    return [home_serial(home) for home in homes]
