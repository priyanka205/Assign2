import subprocess

# with open('./newtasklist01.txt','w+') as fout:
with open('./priyanka02.txt','w+') as fout:
    subprocess.run("tasklist",stdout=fout) #to create new file


    # to run the windows subprocess command
    #in terminal: python sub_process.py or tasklist > priyanka02.txt

with open('./priyanka02.txt','r') as infile:
    for line in infile:
        print(line) #to read file