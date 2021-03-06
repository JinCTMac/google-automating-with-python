filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
# any file that ends with .hpp extension needs to be updated to .h instead
newfilenames = []
for file in filenames:
    if "hpp" in file:
        new_file = file.replace("hpp", "h")
        newfilenames.append(new_file)
    else:
        newfilenames.append(file)

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
