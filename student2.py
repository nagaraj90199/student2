import sys
if len(sys.argv) == 3:
    scipt_name=sys.argv[0]
    name=sys.argv[1]
    rollno=sys.argv[2]
    print("user provided input values:")

else:
    script name=sys.argv[0]
    name="Nagaraj"
    rollno="101"
    print("no input given - using default values:")
print("Scipt Name:",scipt_name)
print("Student Name:",name)
print("Roll no:",rollno)

