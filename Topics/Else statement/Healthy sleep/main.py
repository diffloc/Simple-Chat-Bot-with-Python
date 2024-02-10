minimum_hours = int(input())
maximum_hours = int(input())
actual_hours = int(input())

if actual_hours < minimum_hours:
    print("Deficiency")
elif actual_hours > maximum_hours:
    print("Excess")
else:
    print("Normal")
