import subprocess

with open('./tasklist03.txt','w+') as fout:
    subprocess.run("tasklist",stdout=fout)