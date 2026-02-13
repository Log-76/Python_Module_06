def validate_ingredients(ingredients: str) -> str:
    valid_elements = ["fire", "water", "earth", "air"]
    # Convert to lowercase for case-insensitive comparison
    ingredients_lower = ingredients.lower()

    # Check if any valid element is present in the ingredients string
    is_valid = any(element in ingredients_lower for element in valid_elements)
    if is_valid:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
