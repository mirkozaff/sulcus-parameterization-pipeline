import os
import argparse

# Main folders
MAINDIR = './'
BVDIR = './bv_dir_5.0.2' #<- OUTPUTS, folder will be  created
FSDIR = './freesurfer/subjects' # INPUTS, folder containing subjects processed with freesurfer
#BVHOME = './brainvisa-4.5.0-mandriva'
BVHOME = './brainvisa'
BV_VER = 5
scriptDIR = os.path.join(BVDIR, 'BV_scripts')


def folder_creation(SUBJECT):
	# Main folders creation
	if not os.path.exists(BVDIR):
		os.makedirs(BVDIR)
	if not os.path.exists(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/registration')):
		os.mkdir(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/registration'))
	if not os.path.exists(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/default_analysis')):
		os.mkdir(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/default_analysis'))
	if not os.path.exists(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/default_analysis/segmentation')):
		os.mkdir(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/default_analysis/segmentation'))
	if not os.path.exists(scriptDIR):
		os.mkdir(scriptDIR)


def import_freesurfer(SUBJECT):
	#IMPORT FREESURFER
	file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/template_fs_import_4.5_ok.bvproc')
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

	os.system(f'{BVHOME}/bin/brainvisa -r {file_parsed_template_path}')

def run_import_t1mri(SUBJECT):
	#IMPORT T1MRI
	file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/import_t1mri_bv5_02.bvproc')
	file_parsed_template_path = os.path.join(scriptDIR, f'{SUBJECT}_import_t1mri_bv5_02.bvproc')
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

	os.system(f'{BVHOME}/bin/brainvisa -r {file_parsed_template_path}')

def run_morphologist(SUBJECT):
	#MORPHOLOGIST PIPELINE
	if BV_VER == 4:
		file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/template_T1_4.5_ok.bvproc')
	else:
		file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/template_T1_5.02_ok.bvproc')
	file_parsed_template_path = os.path.join(scriptDIR, f'{SUBJECT}_T1.bvproc')
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

	os.system(f'{BVHOME}/bin/brainvisa -r {file_parsed_template_path}')


def run_left_sulci_recognition(SUBJECT):
	#LEFT SULCI RECOGNITION
	file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/template_left_spam.bvproc')
	file_parsed_template_path = os.path.join(scriptDIR, f'{SUBJECT}_Lspam.bvproc')
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

	os.system(f'{BVHOME}/bin/brainvisa -r {file_parsed_template_path}')


def run_right_sulci_recognition(SUBJECT):
	#RIGHT SULCI RECOGNITION
	file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/template_right_spam.bvproc')
	file_parsed_template_path = os.path.join(scriptDIR, f'{SUBJECT}_Rspam.bvproc')
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

	os.system(f'{BVHOME}/bin/brainvisa -r {file_parsed_template_path}')


def run_sulcal_measures(SUBJECT):
	#SULCAL MEASURES
	if BV_VER == 4:
		file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/by_subject_sulcal_measures_temp.bvproc')
	else:
		file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/by_subject_sulcal_measures_temp_5_02.bvproc')
	file_parsed_template_path = os.path.join(scriptDIR, f'{SUBJECT}_by_subject_sulcal_measures.bvproc')
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

	os.system(f'{BVHOME}/bin/brainvisa -r {file_parsed_template_path}')


def main():
	#Settings
	parser = argparse.ArgumentParser(description='BrainVisa Cortical Surface pipeline')
	parser.add_argument('--subject', '-s', type=str, required = True, help="subject ID")
	args = parser.parse_args()

	'''
	subjects_path = os.path.join(BVDIR, 'subjects')
	subjects = [f for f in os.listdir(subjects_path) if (os.path.isdir(os.path.join(subjects_path, f))) and ('KK' in f)]

	for sbj in subjects:
		#Brainvisa pipeline
		print(f'*** {sbj} Morphologist pipeline started ***\n')
		folder_creation(sbj)
		#import_freesurfer(sbj)
		if BV_VER == 5:
			run_import_t1mri(sbj)
		run_morphologist(sbj)
		if BV_VER == 4:
			run_left_sulci_recognition(sbj)
			run_right_sulci_recognition(sbj)
		run_sulcal_measures(sbj)
	'''

	sbj =  args.subject

	#Brainvisa pipeline
	print(f'*** {sbj} Morphologist pipeline started ***\n')
	folder_creation(sbj)
	#import_freesurfer(sbj)
	if BV_VER == 5:
		run_import_t1mri(sbj)
	run_morphologist(sbj)
	if BV_VER == 4:
		run_left_sulci_recognition(sbj)
		run_right_sulci_recognition(sbj)
	run_sulcal_measures(sbj)

if __name__ == '__main__':
	main()
