import argparse
import json
import random
import math

# Parse args
ap = argparse.ArgumentParser()
ap.add_argument("config", help="System config JSON")
args = ap.parse_args()

# Load the cfg
cfg = json.load(open(args.config))


def calculate(runner: dict, error: float):
    runner["i"] += (error * cfg["output"]["period"])
    derivative = (error - runner["error"]) / cfg["output"]["period"]

    runner["error"] = error

    return (runner["gains"][0] * error) + (runner["gains"][1] * runner["i"]) + (runner["gains"][2] * derivative)


runners = []

for i in range(500):
    runners.append({
        "setpoint": random.choice(range(cfg["setpoint_range"][0], cfg["setpoint_range"][1])),
        "gains": [
            random.randint(0, 100000000)/100000,
            random.randint(0, 100000000)/100000,
            random.randint(0, 100000000)/100000
        ],
        "error": 1000000000,
        "i": 0.0,
        "output": 0.0,
        "val": 0.0,
    })

try:
    for _I in range(600):

        for _ in range(300):
            for runner in runners:

                error = runner["setpoint"] - \
                    (runner["val"] * cfg["output"]["minmax"][1])

                out = calculate(runner, error)
                runner["output"] = max(
                    min(out, cfg["output"]["accel"]), cfg["output"]["accel"] * -1) / cfg["output"]["minmax"][1]

                runner["val"] += runner["output"]

                if bool(str(runner["error"]) == "nan"):
                    runner["error"] = 1000000000000000000000

        # Sort, and kill runners
        runners.sort(key=lambda x: abs(x["error"]))
        # runners.reverse()

        # Kill bottom half of runners
        runners = runners[:int((len(runners))/2)]

        # Fill in more runners
        for i in range(len(runners)):
            runners.append({
                "setpoint": random.choice(range(cfg["setpoint_range"][0], cfg["setpoint_range"][1])),
                "gains": [
                    random.randint(0, 100000000) /
                    random.choice(range(100000000, 10000000000000)),
                    random.randint(
                        0, 100000000)/random.choice(range(1000000000000, 1000000000000000000)),
                    random.randint(
                        0, 100000000)/random.choice(range(1000000000, 10000000000000000)),
                ],
                "error": 1000000000,
                "i": 0.0,
                "output": 0.0,
                "val": 0.0,
            })

        print(runners[0]["error"])
except KeyboardInterrupt as e:
    pass

# Sort, and kill runners
runners.sort(key=lambda x: abs(x["error"]))
# runners.reverse()

# Kill bottom half of runners
runners = runners[:int((len(runners))/2)]

print(runners)
