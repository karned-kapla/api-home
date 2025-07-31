import pytest
from pydantic import ValidationError

from models.home_model import HomeWrite


def test_home_creation():
    home_data = {
        "name": "Home Name",
        "description": "This is a home description.",
        "price": 10.99,
        "quantity": 2,
        "number_of_persons": 4,
        "origin_country": "France",
        "attributes": ["vegan", "gluten-free"],
        "utensils": ["pan", "knife"],
        "ingredients": [
            {"name": "Sugar", "quantity": 100, "unit": "grams"},
            {"name": "Salt"}
        ],
        "steps": [
            {"step_number": 1, "description": "First step", "duration": "10 min"},
            {"step_number": 2, "description": "Second step"}
        ],
        "thumbnail_url": "http://example.com/thumbnail.jpg",
        "large_image_url": "http://example.com/large_image.jpg",
        "source_reference": "Source Reference"
    }
    home = HomeWrite(**home_data)
    assert home.name == "Home Name"
    assert home.description == "This is a home description."
    assert home.price == 10.99
    assert home.quantity == 2
    assert home.number_of_persons == 4
    assert home.origin_country == "France"
    assert home.attributes == ["vegan", "gluten-free"]
    assert home.utensils == ["pan", "knife"]
    assert len(home.ingredients) == 2
    assert len(home.steps) == 2
    assert str(home.thumbnail_url) == "http://example.com/thumbnail.jpg"
    assert str(home.large_image_url) == "http://example.com/large_image.jpg"
    assert home.source_reference == "Source Reference"


def test_home_creation_with_defaults():
    home_data = {
        "name": "Minimal Home"
    }
    home = HomeWrite(**home_data)
    assert home.name == "Minimal Home"
    assert home.description is None
    assert home.price is None
    assert home.quantity is None
    assert home.number_of_persons is None
    assert home.origin_country is None
    assert home.attributes == []
    assert home.utensils == []
    assert home.ingredients == []
    assert home.steps == []
    assert home.thumbnail_url is None
    assert home.large_image_url is None
    assert home.source_reference is None


def test_home_validation_error():
    invalid_home_data = {
        "name": "Invalid Home",
        "number_of_persons": 0
    }
    with pytest.raises(ValidationError):
        HomeWrite(**invalid_home_data)


def test_home_missing_fields():
    incomplete_home_data = {
        "description": "Incomplete Home"
    }
    with pytest.raises(ValidationError):
        HomeWrite(**incomplete_home_data)

def test_home_invalid_description_type():
    invalid_home_data = {
        "name": "Invalid Home",
        "description": 123
    }
    with pytest.raises(ValidationError):
        HomeWrite(**invalid_home_data)

def test_home_invalid_price_type():
    invalid_home_data = {
        "name": "Invalid Home",
        "price": "ten"
    }
    with pytest.raises(ValidationError):
        HomeWrite(**invalid_home_data)

def test_home_invalid_quantity_type():
    invalid_home_data = {
        "name": "Invalid Home",
        "quantity": "two"
    }
    with pytest.raises(ValidationError):
        HomeWrite(**invalid_home_data)

def test_home_invalid_number_of_persons_type():
    invalid_home_data = {
        "name": "Invalid Home",
        "number_of_persons": "four"
    }
    with pytest.raises(ValidationError):
        HomeWrite(**invalid_home_data)

def test_home_invalid_origin_country_type():
    invalid_home_data = {
        "name": "Invalid Home",
        "origin_country": 42
    }
    with pytest.raises(ValidationError):
        HomeWrite(**invalid_home_data)

def test_home_invalid_attributes_type():
    invalid_home_data = {
        "name": "Invalid Home",
        "attributes": "vegan"
    }
    with pytest.raises(ValidationError):
        HomeWrite(**invalid_home_data)

def test_home_invalid_utensils_type():
    invalid_home_data = {
        "name": "Invalid Home",
        "utensils": "pan"
    }
    with pytest.raises(ValidationError):
        HomeWrite(**invalid_home_data)

def test_home_invalid_ingredients_type():
    invalid_home_data = {
        "name": "Invalid Home",
        "ingredients": "Sugar"
    }
    with pytest.raises(ValidationError):
        HomeWrite(**invalid_home_data)

def test_home_invalid_steps_type():
    invalid_home_data = {
        "name": "Invalid Home",
        "steps": "First step"
    }
    with pytest.raises(ValidationError):
        HomeWrite(**invalid_home_data)

def test_home_invalid_thumbnail_url_type():
    invalid_home_data = {
        "name": "Invalid Home",
        "thumbnail_url": 123
    }
    with pytest.raises(ValidationError):
        HomeWrite(**invalid_home_data)

def test_home_invalid_large_image_url_type():
    invalid_home_data = {
        "name": "Invalid Home",
        "large_image_url": 123
    }
    with pytest.raises(ValidationError):
        HomeWrite(**invalid_home_data)

def test_home_invalid_source_reference_type():
    invalid_home_data = {
        "name": "Invalid Home",
        "source_reference": 123
    }
    with pytest.raises(ValidationError):
        HomeWrite(**invalid_home_data)

def test_home_invalid_url():
    invalid_home_data = {
        "name": "Invalid Home",
        "thumbnail_url": "invalid_url",
        "large_image_url": "invalid_url"
    }
    with pytest.raises(ValidationError):
        HomeWrite(**invalid_home_data)

def test_home_invalid_list_types():
    invalid_home_data = {
        "name": "Invalid Home",
        "attributes": ["vegan", 123],
        "utensils": ["pan", 42]
    }
    with pytest.raises(ValidationError):
        HomeWrite(**invalid_home_data)