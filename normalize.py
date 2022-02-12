import os

for file_name in os.listdir("."):
    if os.path.isfile(file_name) and file_name.endswith(".txt"):
        with open(file_name, "r") as input:
            lines = input.readlines()

        lines = sorted(lines, key=lambda x: x.lower())

        with open(file_name, "w") as output:
            for line in lines:
                line = line.strip().rstrip()

                output.write(f"{line}\n")
            