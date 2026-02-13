from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    validation_result = validate_ingredients(ingredients)
    if "- VALID" in validation_result:
        return (f"Spell recorded: {[spell_name]} "
                f"({validate_ingredients(ingredients)})")
    else:
        return (f"Spell rejected: {spell_name} "
                f"({validate_ingredients(ingredients)})")
