#!/usr/bin/env python3
"""Print current traffic to stdout."""
import WazeRouteCalculator
import logging
from datetime import datetime

if __name__ == "__main__":
    NOW_STRING = datetime.now().isoformat()

    # Configure logging for WazeRouteCalculator to see more details if needed
    log = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
    log.setLevel(logging.ERROR) # Set to INFO for less verbose output, or DEBUG for more details
    handler = logging.StreamHandler()
    log.addHandler(handler)

    # Define start and end addresses
    start_address = "120 Carnotstraat, Antwerpen, Belgium"
    end_address = "51.215447,4.4447065" # "51°12'55.6N 4°26'46.2E" # "412 N12, Antwerpen, Belgium"
    region = "EU" # Using 'EU' region for broader compatibility

    # print(f"Calculating routes from: {start_address} to {end_address}\n")

    route = WazeRouteCalculator.WazeRouteCalculator(start_address, end_address, region)
    # route.calc_route_info()

    # print("Calculate multiple routes")
    # calc_all_routes_info takes an optional single parameter, the number of routes to fetch. Note that the Waze API may not return as many possibilities as requested. The function returns a dict: {'routeType-shortRouteName': (route_time1, route_distance1), 'routeType-shortRouteName': (route_time2, route_distance2), ...}.
    # route.calc_all_routes_info(3)

    try:
        index = 0
        for r in route.get_route(3):
            index += 1
            if index <= 3:
                # \t{r['routeType']}  : stuff like ['Best', 'Natural'] or ['Natural']
                # \t{r['routeName']}  : stuff like 'Carnotstraat Antwerpen', 'Kerkstraat Antwerpen' but not unique per route
                print(f"{NOW_STRING}\t{start_address}\t{end_address}\t{r['totalRouteTime']}\t{r['streetNames']}")
    except Exception as e:
        print(f"{NOW_STRING} Fout bij ophalen route {r}: {e}")
