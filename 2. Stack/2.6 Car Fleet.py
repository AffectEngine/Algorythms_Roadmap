def carFleet(target, position, speed):
	cars = sorted(zip(position, speed), reverse=True)
	fleet_count = 0
	prev_time = -1

	for pos, spd in cars:
		time = (target - pos) / spd

		if time > prev_time:
			fleet_count += 1
			prev_time = time

	return fleet_count


print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
