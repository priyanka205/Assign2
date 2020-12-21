# memory {}

def process_memory(tasklist_file):

    with open(f"{tasklist_file}.txt","r") as file:

        for line in file:
            if line.startswith("Image Name") or line.startswith("=") or line.startswith("\n"):
                continue
            else:
                line_list = line.split(" ")
                memory_value=""
                for v in line_list[-1].strip():
                    if v == "," or v=="k":
                        continue
                    else:
                        memory_value += v
                if line_list[0] in memory.keys():
                    memory[line_list[0]] += int(memory_value)
                else:
                    memory[line_list[0]] = int(memory_value)

    sorted_memory = {k: v for k, v in sorted(memory.items(), key=lambda item: item[1])} 
    return sorted_memory              







