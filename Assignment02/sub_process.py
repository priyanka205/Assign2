import subprocess# subprocess is a library

# with open('./newtasklist01.txt','w+') as fout:
with open('./priyanka02.txt','w+') as fout:
    subprocess.run("tasklist",stdout=fout) #to create new file


# # #     # to run the windows subprocess command
# # #     #in terminal: python sub_process.py or tasklist > priyanka02.txt

with open('./priyanka02.txt','r') as infile:
    for line in infile:
        print(line) #to read file.

# # # from this we can create any file from terminal form python command

import subprocess
import sys 

filename = sys.argv[1]

with open(f'./{filename}.txt','w+') as fout:
    subprocess.run("tasklist",stdout=fout)

# #in terminal we nedd to write python sub_process and name for the txt file eg: mylist01.txt

import subprocess
import sys
subprocess.run("tasklist")# to run in the terminal of tasklist 