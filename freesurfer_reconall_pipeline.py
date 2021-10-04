import os
import os.path as path
import subprocess
import datetime
from multiprocessing import Pool

# Folder with t1 images containing only the *.nii
T1_DIR = './t1_images'

# Getting the subjects list in the folder
subjects = [f for f in os.listdir(T1_DIR)]

output = open("out.txt", "w")

def reconall(subject):
	begin_time = datetime.datetime.now()

	subject_name = subject.split('.')[0]
	subject_t1_path = os.path.join(T1_DIR, subject)

	# Write on subject log files
	output.write(f'SUBJECT: {subject_name} inizio: {begin_time}\n')
	output.flush()

	# Run freesurfer recon-all pipeline
	print(f'RUNNING: recon-all -s {subject_name} -i {subject_t1_path} -all')
	subprocess.run(['recon-all', '-s', subject_name, '-i', subject_t1_path, '-all'])

	end_time = datetime.datetime.now() - begin_time

	# Write on subject log files
	output.write(f'SUBJECT: {subject_name} fine: {end_time}\n')
	output.flush()

def pool_handler(subjects_list):
	# Setting multi processing
	n_processes = 45
	p = Pool(n_processes)
	# Inputs: (target function, list_of_inputs)
	p.map(reconall, subjects_list)

if __name__ == '__main__': 
	pool_handler(subjects)
	output.close()