# Exception chaining
def fetch_data():
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("Data fetch failed due to division by zero") from e

try:
    fetch_data()
except Exception as e:
    print(f"Exception: {repr(e)}")
    print(f"Original Cause: {repr(e.__cause__)}")