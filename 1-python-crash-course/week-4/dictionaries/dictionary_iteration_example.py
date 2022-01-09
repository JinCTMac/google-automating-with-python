def car_listing(car_prices):
    result = ""
    for car in car_prices:
        result += "{car} costs {price} dollars".format(
            car=car, price=car_prices[car]) + "\n"
    return result

# Or

# for car, price in car_prices.items():
    # result += "{} costs {} dollars".format(car, price)

print(
    car_listing({
        "Kia Soul": 19000,
        "Lamborghini Diablo": 55000,
        "Ford Fiesta": 13000,
        "Toyota Prius": 24000
    }))
