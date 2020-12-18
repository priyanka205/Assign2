import subprocess
import sys
from memory_calc import process_memory

# subprocess.run("tasklist")
filename = sys.argv[1]# from this we can create any file from arguments
get_max = sys.argv[2]
get_min = sys.argv[3]
get_process_memory = sys.argv[4]


with open(f'./{filename}.txt','w+') as fout:
    subprocess.run("tasklist",stdout=fout)

memory_sorted = process_memory(filename)
#max
def get_max_memory():
    max_key = list(memory_sorted.keys())[-1]
    return max_key

#min
def get_min_memory():
    min_key = list(memory_sorted.keys())[0]
    return min_key

#total memory
def get_memory_from_particular_process(process_name):
    memory_consumed = memory_sorted[f"{process_name}"]
    return memory_consumed

if get_max == "True":
    print(f"Maximum memory is consumed by {get_max_memory()}.")

if get_min == "True":
    print(f"Minimum memory is consumed by {get_min_memory()}.")

processes = get_process_memory.split(",")
for process in processes:
    value = get_memory_from_particular_process(process)
    print(f"Memory consumed by {process} is {value}.")

print("Program executed successfully:)")


