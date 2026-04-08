# For-Else loop: Else executes ONLY if the loop completed naturally (no break)
target = 5
for i in range(3):
    if i == target:
        print("Found")
        break
else:
    print("Not Found") # Executes!