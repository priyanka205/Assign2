import subprocess

with open('./newtasklist01.txt','w+') as fout:
    subprocess.run("tasklist",stdout=fout)