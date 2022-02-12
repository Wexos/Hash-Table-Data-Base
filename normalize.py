import os

for file_name in os.listdir("."):
    if os.path.isfile(file_name) and file_name.endswith(".txt"):
        with open(file_name, "r") as input:
            lines = input.readlines()

        lines = sorted(lines, key=lambda x: x.lower())
        line_set = set()

        with open(file_name, "w") as output:
            for line in lines:
                line = line.strip().rstrip()

                if line in line_set:
                    print(f"Duplicate removed: {line}")
                    continue

                line_set.add(line)

                output.write(f"{line}\n")
            