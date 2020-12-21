import sys

infile = sys.argv[1]
process_to_check = sys.argv[2]

with open (infile,"r") as infile:
    process_is = False

    for line in infile:
        line_split = line.split(" ")
        if process_to_check in line_split:
            print(f"process {process_to_check} exists.")
            process_is = True

            break
    if process_is == False:
        print(f"process {process_to_check} doesnot exists.")


    
    


# def check_if_process_exists():
#     pass