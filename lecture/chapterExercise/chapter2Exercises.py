import math

# Exercise 2.2.1
radius = 5
volume_sphere = 4 * math.pi * radius ** 3 / 3
print('volume:', volume_sphere)

# Exercise 2.2.2
price_book = 24.95 * (1 - 0.4) * 60
price_shipping = 3 + 59 * 0.75
price_sum = price_book + price_shipping
print('total price is:', price_sum)

# Exercise 2.2.3
start_h = 6
start_m = 58
run_s = (15 * 2 + 12 * 3) - int((15 * 2 + 12 * 3) / 60) * 60
run_m = 8 * 2 + 7 * 3 + int((15 * 2 + 12 * 3) / 60)
end_s = run_s
end_m = (start_m + run_m) - int((start_m + run_m) / 60) * 60
end_h = start_h + int((start_m + run_m) / 60)
print('I get home for breakfast at {0}:{1}:{2}'.format(end_h, end_m, end_s))
