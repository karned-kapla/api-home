from schemas.home_schema import home_serial, list_home_serial


def test_home_serial():
    home = {
        "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
        "_id": "12345",
        "name": "Home Name",
        "description": "This is a home description.",
        "price": 10.99,
        "quantity": 2,
        "number_of_persons": 4,
        "origin_country": "France",
        "attributes": ["vegan", "gluten-free"],
        "utensils": ["pan", "knife"],
        "ingredients": [
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Sugar", "quantity": 100, "unit": "grams"},
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Salt"}
        ],
        "steps": [
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 1, "description": "First step", "duration": 10},
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 2, "description": "Second step"}
        ],
        "thumbnail_url": "http://example.com/thumbnail.jpg",
        "large_image_url": "http://example.com/large_image.jpg",
        "source_reference": "Source Reference"
    }
    expected_output = {
        "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
        "uuid": "12345",
        "name": "Home Name",
        "description": "This is a home description.",
        "price": 10.99,
        "quantity": 2,
        "number_of_persons": 4,
        "origin_country": "France",
        "attributes": ["vegan", "gluten-free"],
        "utensils": ["pan", "knife"],
        "ingredients": [
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Sugar", "quantity": 100, "unit": "grams"},
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Salt", "quantity": None, "unit": None}
        ],
        "steps": [
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 1, "description": "First step", "duration": 10},
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 2, "description": "Second step", "duration": None}
        ],
        "thumbnail_url": "http://example.com/thumbnail.jpg",
        "large_image_url": "http://example.com/large_image.jpg",
        "source_reference": "Source Reference"
    }
    assert home_serial(home) == expected_output

    home_minimal = {
        "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
        "_id": "67890",
        "name": "Minimal Home"
    }
    expected_output_minimal = {
        "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
        "uuid": "67890",
        "name": "Minimal Home",
        "description": None,
        "price": None,
        "quantity": None,
        "number_of_persons": None,
        "origin_country": None,
        "attributes": [],
        "utensils": [],
        "ingredients": [],
        "steps": [],
        "thumbnail_url": None,
        "large_image_url": None,
        "source_reference": None
    }
    assert home_serial(home_minimal) == expected_output_minimal


def test_list_home_serial():
    homes = [
        {
            "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
            "_id": "12345",
            "name": "Home Name",
            "description": "This is a home description.",
            "price": 10.99,
            "quantity": 2,
            "number_of_persons": 4,
            "origin_country": "France",
            "attributes": ["vegan", "gluten-free"],
            "utensils": ["pan", "knife"],
            "ingredients": [
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Sugar", "quantity": 100, "unit": "grams"},
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Salt"}
            ],
            "steps": [
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 1, "description": "First step", "duration": 10},
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 2, "description": "Second step"}
            ],
            "thumbnail_url": "http://example.com/thumbnail.jpg",
            "large_image_url": "http://example.com/large_image.jpg",
            "source_reference": "Source Reference"
        },
        {
            "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
            "_id": "67890",
            "name": "Minimal Home"
        }
    ]
    expected_output = [
        {
            "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
            "uuid": "12345",
            "name": "Home Name",
            "description": "This is a home description.",
            "price": 10.99,
            "quantity": 2,
            "number_of_persons": 4,
            "origin_country": "France",
            "attributes": ["vegan", "gluten-free"],
            "utensils": ["pan", "knife"],
            "ingredients": [
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Sugar", "quantity": 100, "unit": "grams"},
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Salt", "quantity": None, "unit": None}
            ],
            "steps": [
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 1, "description": "First step", "duration": 10},
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 2, "description": "Second step", "duration": None}
            ],
            "thumbnail_url": "http://example.com/thumbnail.jpg",
            "large_image_url": "http://example.com/large_image.jpg",
            "source_reference": "Source Reference"
        },
        {
            "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
            "uuid": "67890",
            "name": "Minimal Home",
            "description": None,
            "price": None,
            "quantity": None,
            "number_of_persons": None,
            "origin_country": None,
            "attributes": [],
            "utensils": [],
            "ingredients": [],
            "steps": [],
            "thumbnail_url": None,
            "large_image_url": None,
            "source_reference": None
        }
    ]
    assert list_home_serial(homes) == expected_output

    empty_homes = []
    expected_output_empty = []
    assert list_home_serial(empty_homes) == expected_output_empty