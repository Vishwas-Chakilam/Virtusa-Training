def safe_cast(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        return None

print(safe_cast("123"))  # 123
print(safe_cast("abc"))  # None