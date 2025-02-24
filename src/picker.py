from random import randint
import sys

legends = [
		"Bangalore",
		"Fuse",
		"Ash",
		"Maggie",
		"Ballistic",
		"Pathfinder",
		"Wraith",
		"Octane",
		"Revenant",
		"Horizon",
		"Alter",
		"Bloodhound",
		"Crypto",
		"Valkyrie",
		"Seer",
		"Vantage",
		"Gibraltar",
		"Lifeline",
		"Mirage",
		"Loba",
		"Newcastle",
		"Conduit",
		"Caustic",
		"Wattson",
		"Rampart",
		"Catalyst"
	]

def pick(list):
	print(list[randint(0, len(list) - 1)])

def randomness_test(list, amount):
	tracker_list = []
	length = len(list)
	for i in range(length):
		tracker_list.append(0)
	for i in range(amount):
		rng = randint(0, length - 1)
		tracker_list[rng] += 1
	print(f"distribution of values: {tracker_list}")


if len(sys.argv) < 2:
	print("\nError: Must provide additional argument!\nExample of usage: src/picker.py any | assault | skirmisher | recon | support | controller\n", end = "")
else:
	if "any" in sys.argv: pick(legends)
	elif "assault" in sys.argv: pick(legends[0:5])
	elif "skirmisher" in sys.argv: pick(legends[5:11])
	elif "recon" in sys.argv: pick(legends[11:16])
	elif "support" in sys.argv: pick(legends[16:22])
	elif "controller" in sys.argv: pick(legends[22:])
	elif "test" in sys.argv: randomness_test(legends[0:5], 100_000)
	else:
		sys.quit()

