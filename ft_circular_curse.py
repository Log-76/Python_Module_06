from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell
import alchemy.grimoire

print("=== Circular Curse Breaking ===")
print(f'validate_ingredients("fire air"): {validate_ingredients("fire air")}')
print('validate_ingredients("dragon scales"): '
      f'{validate_ingredients("dragon scales")}\n')
print("Testing spell recording with validation:")
print('record_spell("Fireball", "fire air"):'
      f'{record_spell("Fireball", "fire air")}')
print('record_spell("Dark Magic", "shadow"):'
      f'{record_spell("Dark Magic", "shadow")}')
print("\nTesting late import technique:")
print('record_spell("Lightning", "air"):'
      f'{alchemy.grimoire.record_spell("Lightning", "air")}')
