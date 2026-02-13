import validator


def record_spell(spell_name: str, ingredients: str) -> str:
    if validator.validate_ingredients(ingredients) == f"{ingredients} - VALID":
        return (f"Spell recorded: {[spell_name]} "
                f"({validator.validate_ingredients()})")
    else:
        return (f"Spell rejected: {spell_name} "
                f"({validator.validate_ingredients()})")
