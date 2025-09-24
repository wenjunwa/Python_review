
import time

my_timer = int(input("Enter a time in second: "))
for x in range(my_timer, 0, -1):
    second = x % 60
    minute = int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minute:02}:{second:02}")
    time.sleep(1)
print("Time is up")
