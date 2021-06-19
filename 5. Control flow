# Write a function to calculate required capacity of transport hub by provided schedule and observation period.

# Each transport vehicle that visits the hub described by two parameters:
# 1) period (n means that transport visits hub every n days)
# 2) amount of goods transport can take.
# Each vehicle belongs to one of following types: if 2) is positive vehicle is producer (delivers goods to hub), otherwise - consumer (takes goods from hub).

# Delivery model:
# a) each day number (zero or more) of producers and number (zero or more) of consumers
# visit the hub
# b) producers always deliver amount of goods equal to its capacity
# c) consumers always take all available goods up to its capacity (e.g. if vehicle capacity=3 and available on hub=7 vehicle will take 3; if capacity=3, on hub=2 , vehicle will take 2), if required consumers wait producers till the end of the day to take as much goods as possible
# d) each day vehicles can visit hub in any order (not dependent on vehicle order in schedule), so more goods can be observed on hub during the day than at the end of day

# The task is to find minimum hub capacity such that producers always will have place to ship off their cargo during observation period.

# Schedule format: list of strings, each string is period and capacity (negative for consumers) separated by space.
# Example: schedule ["2 -2", "3 3"], number of observed days 7
# transport hub capacity: 4
# (day: 1, goods on hub at the end of day: 0), (2, 0), (3, 3), (4, 1), (5, 1), (6, 2), (7, 2) -- max amount on day 6, because producer can arrive earlier

# Function signature: def transport_hub (schedule, days)


def transport_hub(schedule, days):
    min_hub_capacity = 0
    filtered_schedule = list(map(lambda s: tuple(map(int, s.split())), schedule))

    current_goods = 0

    producers_goods = [0] * (days + 1)
    consumers_capacity = [0] * (days + 1)

    for sch in filtered_schedule:
        for day in range(sch[0], days + 1, sch[0]):
            if sch[1] > 0:
                producers_goods[day] += sch[1]
            else:
                consumers_capacity[day] += sch[1]

    for day in range(1, days + 1):
        current_goods += producers_goods[day]
        min_hub_capacity = max(min_hub_capacity, current_goods)
        current_goods += consumers_capacity[day]
        current_goods = max(current_goods, 0)

    return min_hub_capacity
