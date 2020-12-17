

memory = list()

with open("new_tasklist01.txt", "r") as file:
    
    for line in file:
        temp_list = []
        if line.startswith("Image Name") or line.startswith("=") or line.startswith("\n"):
            continue
        else:
            line_list = line.split("  ")
            memory_value =""
            for v in line_list[-1].strip():
                if v == "," or v=="K":
                    continue
                else:
                    memory_value += v
            temp_list.append(line_list[0])
            temp_list.append(int(memory_value))
            memory.append(temp_list)


print(memory)
memory_list = memory[0:20]
print(memory_list)
print()
memory_dict = {}

for item in memory_list:
    # print(item)
    key = item[0]
    value = item[1]
    if key in memory_dict:
        memory_dict[key] += value 
    else:
        memory_dict[key] = value

    

print(memory_dict)
print()
print(memory_dict.keys())

print(memory_dict.values())
print(max(memory_dict.values()))

# refined_memory = list()
# for data in memory:
#     if data not in refined_memory:
#         refined_memory.append(data)
#     else:
#         refined_memory[data[0]] += data[1]





            