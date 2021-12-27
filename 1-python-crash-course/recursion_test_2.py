def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result

print(factorial(5))

# as we can see, the recursive factorial function calls the function inside itself with n - 1 until it reaches the base case, at which point it returns the results of each inner function call until it reaches the correct result
