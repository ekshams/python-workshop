from error import ValueTooMaximum
num = 3

try:
    if num > 10:
        raise ValueTooMaximum
except ValueTooMaximum:
    print("value too maximum")
finally:
    print("done")
    
