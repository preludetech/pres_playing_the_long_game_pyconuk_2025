timing = """
intro 01:20
me 3:42
what 00:46
futures: 1:11
looking back: 04:17
2023: 1:39
2024: 1:30
TODO post training 00:00
2025: 2:45
DS economic: 00:52
TODO TOol use 03:00
TODO GPT5 02:00 
TODO Vibe 03:00 

Future: 3:16
Bubble bursts: 04:17
stabalise: 01:40
todo job market 05:00
predictions: 01:15

Advice 4:45
Fundamentals: 05:00
"""

def parse_time(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

total_seconds = 0
for line in timing.strip().split('\n'):
    if line.strip():
        time_part = line.split()[-1]
        total_seconds += parse_time(time_part)

total_minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

print(f"total time = {total_minutes}:{remaining_seconds:02d}")