#!/usr/bin/env python3
import random
import time
import argparse
import os
from datetime import datetime

LOG_FILE = 'ironmaiden_events.log'

LOCATIONS = [
    'Central Park', 'Times Square', 'Golden Gate Bridge', 'Eiffel Tower',
    'London Eye', 'Tokyo Tower', 'Sydney Opera House', 'Red Square',
    'Colosseum', 'Great Wall', 'Burj Khalifa', 'Niagara Falls'
]

def generate_fake_imsi():

  return ''.join(str(random.randint(0, 9)) for _ in range(15))

def generate_event():
    imsi = generate_fake_imsi()
    location = random.choice(LOCATIONS)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    event = {
        'imsi': imsi,
        'location': location,
        'timestamp': timestamp
    }
    return event

def log_event(event):
    with open(LOG_FILE, 'a') as f:
        f.write(f"{event['timestamp']} | IMSI: {event['imsi']} | Location: {event['location']}\n")

def print_event(event):
    print(f"[IMSI-Catcher Event] {event['timestamp']} | IMSI: {event['imsi']} | Location: {event['location']}")

def view_log():
    if not os.path.exists(LOG_FILE):
        print("No events logged yet.")
        return
    with open(LOG_FILE, 'r') as f:
        print(f.read())

def summary():
    if not os.path.exists(LOG_FILE):
        print("No events logged yet.")
        return
    locations = {}
    total = 0
    with open(LOG_FILE, 'r') as f:
        for line in f:
            total += 1
            parts = line.strip().split('|')
            if len(parts) == 3:
                loc = parts[2].replace('Location: ', '').strip()
                locations[loc] = locations.get(loc, 0) + 1
    print(f"Total IMSI-catcher events: {total}")
    print("Events by location:")
    for loc, count in sorted(locations.items(), key=lambda x: -x[1]):
        print(f"  {loc}: {count}")

def ascii_map():

  print("\nIMSI-Catcher ASCII Map (randomized):")
    map_grid = [['.' for _ in range(40)] for _ in range(12)]
    for idx, loc in enumerate(LOCATIONS):
        x = random.randint(0, 39)
        y = idx
        map_grid[y][x] = str(idx % 10)
    for row in map_grid:
        print(''.join(row))
    print("Legend:")
    for idx, loc in enumerate(LOCATIONS):
        print(f"  {idx % 10}: {loc}")

def main():
    parser = argparse.ArgumentParser(description='IronMaiden IMSI-Catcher Simulator')
    parser.add_argument('--generate', type=int, metavar='N', help='Generate N fake IMSI-catcher events')
    parser.add_argument('--view-log', action='store_true', help='View the event log')
    parser.add_argument('--summary', action='store_true', help='Print a summary of events')
    parser.add_argument('--ascii-map', action='store_true', help='Show a random ASCII map of event locations')
    args = parser.parse_args()

    if args.generate:
        for _ in range(args.generate):
            event = generate_event()
            log_event(event)
            print_event(event)
            time.sleep(0.2)
    elif args.view_log:
        view_log()
    elif args.summary:
        summary()
    elif args.ascii_map:
        ascii_map()
    else:
        parser.print_help()

if __name__ == '__main__':
    main() 
