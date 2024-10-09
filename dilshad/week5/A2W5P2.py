def calculate_fare(distance_km):
    base_fare = 4.00
    fare_per_140m = 0.25
    distance_m = distance_km * 1000
    additional_fare = ((distance_m + 139) // 140) * fare_per_140m
    total_fare = base_fare + additional_fare
    return total_fare


if __name__ == '__main__':

    user_input = float(input("Distance travaled in km: "))
    fare = calculate_fare(user_input)
    print(f"Total fare: {fare:.2f}")
