class ValidationError(Exception):
    pass

def validate_age(age):
    if age < 0:
        raise ValidationError("Age cannot be negative.")
    return True

try:
    validate_age(-5)
except ValidationError as e:
    print(f"Validation failed: {e}")