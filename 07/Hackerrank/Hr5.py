#Time Conversion
def timeConversion(s):
    # Split the input string into hours, minutes, seconds, and AM/PM
    time_parts = s.split(":")
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2][:2])  # Extract the first two characters for seconds
    am_pm = time_parts[2][-2:]  # Extract AM or PM

    # Convert to 24-hour format
    if am_pm == "AM":
        if hours == 12:
            hours = 0
    elif am_pm == "PM":
        if hours != 12:
            hours += 12

    # Format the result
    result = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    
    return result

# Input
s = input()

# Convert and output the time in 24-hour format
result = timeConversion(s)
print(result)