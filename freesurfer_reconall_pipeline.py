import os
import os.path as path
import subprocess
import datetime

T1_DIR = './t1_images'

subjects = [f for f in os.listdir(T1_DIR)]

output = open("out.txt", "w")

for s in subjects:
    begin_time = datetime.datetime.now()

    subject_name = s.split('.')[0]
    subject_t1_path = os.path.join(T1_DIR, s)

    output.write(f'SUBJECT: {subject_name} inizio: {begin_time}')

    print(f'RUNNING: recon-all -s {subject_name} -i {subject_t1_path} -all')
    subprocess.run(['recon-all', '-s', subject_name, '-i', subject_t1_path, '-all'])

    end_time = datetime.datetime.now() - begin_time
    output.write(f'SUBJECT: {subject_name} inizio: {end_time}')

output.close()