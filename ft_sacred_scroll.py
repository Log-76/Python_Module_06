import alchemy.elements


def main() -> None:

    print("=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire():{alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water():{alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_air():{alchemy.elements.create_air()}")
    print(f"alchemy.elements.create_earth():{alchemy.elements.create_earth()}")
    print("\nTesting package-level access (controlled by __init__.py)")
    print(f"alchemy.elements.create_fire():{alchemy.create_fire()}")
    print(f"alchemy.elements.create_water():{alchemy.create_water()}")
    try:
        print(alchemy.create_earth())
    except Exception:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        print(alchemy.create_air())
    except Exception:
        print("alchemy.create_air(): AttributeError - not exposed")

    # Test 3: Package metadata
    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


main()
