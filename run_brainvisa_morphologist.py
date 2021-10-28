import os
import argparse

DEBUG = True

if DEBUG:
	# Main folders testing
	MAINDIR = './' #Scripts Folder
	BVDIR = '/home/zaffaro/Desktop/kki_bv_database' # Folder containing subjects processed with brainvisa
	#FSDIR = '/home/zaffaro/Desktop/fs_subjects' # INPUTS, folder containing subjects processed with freesurfer
	FSDIR = '/home/zaffaro/Desktop/sbj2'
	#BVHOME = 'brainvisa-4.5.0-mandriva'
	BVHOME = 'brainvisa-5.0.3'
	BV_VER = 5
	scriptDIR = os.path.join(BVDIR, 'BV_scripts')
else:
	# Main folders
	MAINDIR = '/usr/local/ENIGMA50/' #Scripts Folder
	BVDIR = '/usr/local/bv_dir' # Folder containing subjects processed with brainvisa
	FSDIR = '/usr/local/fs_sbj' # INPUTS, folder containing subjects processed with freesurfer
	#BVHOME = '/usr/local/brainvisa-5.0.2'
	BVHOME = '/usr/local/brainvisa-4.5' #os.path.join(os.environ['HOME'], 'brainvisa-5.0.2
	BV_VER = 4
	scriptDIR = os.path.join(BVDIR, 'BV_scripts')


def folder_creation(SUBJECT):
	# Main folders creation
	if not os.path.exists(BVDIR):
		os.makedirs(BVDIR)
	if not os.path.exists(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/registration')):
		os.makedirs(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/registration'))
	if not os.path.exists(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/default_analysis')):
		os.makedirs(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/default_analysis'))
	if not os.path.exists(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/default_analysis/segmentation')):
		os.makedirs(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/default_analysis/segmentation'))
	if not os.path.exists(scriptDIR):
		os.makedirs(scriptDIR)
	DATABASE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'database')
	if not os.path.exists(DATABASE_PATH):
		create_database(DATABASE_PATH)


def create_database(DATABASE_PATH):
	#CREATE DATABASE
	file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/template_create_database.bvproc')
	file_parsed_template_path = os.path.join(scriptDIR, 'create_database.bvproc')
	f_in = open(file_template_path, 'r')
	f_out = open(file_parsed_template_path, 'w')

	for line in f_in:
		#read replace the string and write to output file
		line = line.replace('DATABASE_PATH', DATABASE_PATH)
		f_out.write(line)
	#close input and output files
	f_in.close()
	f_out.close()

	os.system(f'{BVHOME}/bin/bv axon-runprocess {file_parsed_template_path}')


def convert_freesurfer_to_brainvisa(SUBJECT):
	#IMPORT FREESURFER
	if BV_VER == 4:
		file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/template_fs_import_4.5_ok.bvproc')
	else:
		file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/import_freesurfer_bv503.bvproc')
	file_parsed_template_path = os.path.join(scriptDIR, f'{SUBJECT}_fs_import_ok.bvproc')
	f_in = open(file_template_path, 'r')
	f_out = open(file_parsed_template_path, 'w')

	for line in f_in:
		#read replace the string and write to output file
		line = line.replace('BVDIR', BVDIR)
		line = line.replace('SUBJECT', SUBJECT)
		line = line.replace('subjid', SUBJECT)
		line = line.replace('FSDIR', FSDIR)
		line = line.replace('BVHOME', BVHOME)	
		f_out.write(line)
	#close input and output files
	f_in.close()
	f_out.close()

	#os.system(f'{BVHOME}/bin/brainvisa -r {file_parsed_template_path}  --enable-db')
	os.system(f'{BVHOME}/bin/bv axon-runprocess --enabledb {file_parsed_template_path}')


def run_morphologist(SUBJECT):
	#MORPHOLOGIST PIPELINE
	if BV_VER == 4:
		file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/template_T1_4.5_ok.bvproc')
	else:
		file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/template_morphologist_503.bvproc')
	file_parsed_template_path = os.path.join(scriptDIR, f'{SUBJECT}_morphologist_503.bvproc')
	f_in = open(file_template_path, 'r')
	f_out = open(file_parsed_template_path, 'w')

	for line in f_in:
		#read replace the string and write to output file
		line = line.replace('BVDIR', BVDIR)
		line = line.replace('SUBJECT', SUBJECT)
		line = line.replace('BVHOME', BVHOME)	
		f_out.write(line)
	#close input and output files
	f_in.close()
	f_out.close()

	os.system(f'{BVHOME}/bin/bv axon-runprocess {file_parsed_template_path}')


def main():
	#Settings
	parser = argparse.ArgumentParser(description='BrainVisa Cortical Surface pipeline')
	parser.add_argument('--subject', '-s', type=str, help="subject ID")
	parser.add_argument('--list', '-l', action='store_true', help="folder with subjects")
	args = parser.parse_args()

	if not (args.list or args.subject):
		parser.error('No action requested, add -list or -subject')

	
	if args.list:
		subjects_path = os.path.join(BVDIR, 'subjects')
		subjects = [f for f in os.listdir(subjects_path) if (os.path.isdir(os.path.join(subjects_path, f)))]

		for sbj in subjects:
			#Brainvisa pipeline
			print(f'*** {sbj} Morphologist pipeline started ***\n')
			folder_creation(sbj)
			folder_creation(sbj)
			convert_freesurfer_to_brainvisa(sbj)
			#run_morphologist(sbj)
	else:
		sbj =  args.subject
		
		#Brainvisa pipeline
		print(f'*** {sbj} Morphologist pipeline started ***\n')
		folder_creation(sbj)
		convert_freesurfer_to_brainvisa(sbj)
		run_morphologist(sbj)

if __name__ == '__main__':
	main()