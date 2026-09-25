
import time

minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total_seconds = minutes * 60 + seconds

while total_seconds > 0:
    minutes_left = total_seconds // 60
    seconds_left = total_seconds % 60

    print(f"\rTime left: {minutes_left:02d}:{seconds_left:02d}", end="")

    time.sleep(1)
    total_seconds -= 1

print("\nTime's up!")

