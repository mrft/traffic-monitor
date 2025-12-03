#!/usr/bin/env python3
"""Print current traffic to stdout.

Usage: print_routes.py <start_address> <end_address> [--region REGION]
"""
import argparse
import logging
from datetime import datetime
import WazeRouteCalculator


def main():
    parser = argparse.ArgumentParser(description="Print current traffic to stdout")
    parser.add_argument("start_address", help="Start address (string or coords)")
    parser.add_argument("end_address", help="End address (string or coords)")
    parser.add_argument("--region", default="EU", help="Waze region (default: EU)")
    args = parser.parse_args()

    NOW_STRING = datetime.now().isoformat()

    # Configure logging for WazeRouteCalculator to see more details if needed
    log = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
    log.setLevel(logging.ERROR)  # Set to INFO for less verbose output, or DEBUG for more details
    handler = logging.StreamHandler()
    log.addHandler(handler)

    start_address = args.start_address
    end_address = args.end_address
    region = args.region

    route = WazeRouteCalculator.WazeRouteCalculator(start_address, end_address, region)

    try:
        index = 0
        for r in route.get_route(3):
            index += 1
            if index <= 3:
                # \t{r['routeType']}  : stuff like ['Best', 'Natural'] or ['Natural']
                # \t{r['routeName']}  : stuff like 'Carnotstraat Antwerpen', 'Kerkstraat Antwerpen' but not unique per route
                print(f"{NOW_STRING}\t{start_address}\t{end_address}\t{r['totalRouteTime']}\t{r['streetNames']}")
    except Exception as e:
        print(f"{NOW_STRING} Error fetching route: {e}")


if __name__ == "__main__":
    main()
