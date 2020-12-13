with open("input", "r") as file:
    input = file.read().splitlines()

timestamp = int(input[0])
bus_ids = [int(bus_id) for bus_id in input[1].split(",") if bus_id.isdigit()]


def check_bus_times(bus_id):
    i, time = 0, bus_id
    while time < timestamp:
        time = bus_id * i
        i += 1
    return (time, bus_id)


earliest_buses = list(map(check_bus_times, bus_ids))
earliest_bus_time, earliest_bus = min(earliest_buses)

print(earliest_bus * (earliest_bus_time - timestamp))
