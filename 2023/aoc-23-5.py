def solution(file):
    # Initialize the mappings
    seed_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temp = {}
    temp_to_humidity = {}
    humidity_to_location = {}

    # Read input from the file
    with open(file, 'r') as input_file:
        lines = input_file.readlines()

    # Parse the input and populate the dictionaries
    current_map = None
    maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temp, temp_to_humidity, humidity_to_location]

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('seeds:'):
            seeds = list(map(int, line.split(':')[1].strip().split()))
        elif line.endswith('map:'):
            current_map = maps.pop(0)
        else:
            rows = list(map(int, line.split()))
            start, end, length = rows
            for i in range(length):
                current_map[start + i] = end + i

    # Perform translations to find the lowest location number
    def translate(seed):
        current = seed
        while current in seed_to_soil:
            current = seed_to_soil[current]
        return current

    locations = [translate(seed) for seed in seeds]
    min_location = min(locations)

    print("Lowest location number:", min_location)


    print("Seed to Soil:", seed_to_soil)
    print("Soil to Fertilizer:", soil_to_fertilizer)
    print("Fertilizer to Water:", fertilizer_to_water)
    print("Water to Light:", water_to_light)
    print("Light to Temperature:", light_to_temp)
    print("Temperature to Humidity:", temp_to_humidity)
    print("Humidity to Location:", humidity_to_location)



# def solution2(file):
#     pass

print(solution('./data/sample5.txt'))
# print(solution('./data/test5.txt'))

# # print(solution2('./data/sample5.txt'))
# # print(solution2('./data/test5.txt'))

