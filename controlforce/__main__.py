from .cfgloader import CFGLoader
import argparse

# Parse args
ap = argparse.ArgumentParser()
ap.add_argument("config", help="System config JSON")
args = ap.parse_args()

# Load the cfg
cfg = CFGLoader(open(args.config))

# Get the system
sys = cfg.getSys()

## Handle Training ##