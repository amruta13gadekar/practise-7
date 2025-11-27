import sys

if len(sys.argv) == 3:
    held = int(sys.argv[1])
    attended = int(sys.argv[2])
    print("User provided values:")
else:
    held = 40
    attended = 30
    print("No input given - using default values:")

attendance = (attended / held) * 100

print("Attendance Percentage:", attendance)


