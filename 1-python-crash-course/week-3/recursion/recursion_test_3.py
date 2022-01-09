def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        # below function returns True if number is equal to 1, otherwise returns false
        # if we assume base is the smallest possible multiple of that number, then if a number is smaller it must be 1
        return number == 1

    # Recursive case: keep dividing number by base.
    return is_power_of(number / base, base)

print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False
