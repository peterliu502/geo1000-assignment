# GEO1000 - Assignment 0
# Authors: Liu Zhenyu
# Studentnumbers: 5386586


def temp_windchill(temp_in_c , windspeed_in_kmh):
    return 13.12 + 0.6215 * temp_in_c - 11.37 * windspeed_in_kmh ** 0.16 + 0.3965 * temp_in_c * windspeed_in_kmh ** 0.16


print(temp_windchill (5.0, 10.0))
print(temp_windchill (-1.0, 35.0))