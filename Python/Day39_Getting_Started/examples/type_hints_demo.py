# Type hints (PEP 484) do not enforce types at runtime, but tooling uses them.
def greeting(name: str) -> str:
    return "Hello " + name

age: int = 25
is_active: bool = True