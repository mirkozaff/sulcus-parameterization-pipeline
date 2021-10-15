import os
import argparse

DEBUG = True

if DEBUG:
	# Main folders testing
	MAINDIR = './' #Scripts Folder
	BVDIR = './bv_dir_5.0.2' # Folder containing subjects processed with brainvisa
	FSDIR = '/home/zaffaro/Desktop/Docker test/docker_bv/fs_subjects' # INPUTS, folder containing subjects processed with freesurfer
	#BVHOME = 'brainvisa-4.5.0-mandriva'
	BVHOME = './brainvisa'
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
		os.mkdir(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/registration'))
	if not os.path.exists(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/default_analysis')):
		os.mkdir(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/default_analysis'))
	if not os.path.exists(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/default_analysis/segmentation')):
		os.mkdir(os.path.join(BVDIR, 'subjects', SUBJECT, 't1mri/default_acquisition/default_analysis/segmentation'))
	if not os.path.exists(scriptDIR):
		os.mkdir(scriptDIR)


def left_sulci_parameterize(SUBJECT):
	#LEFT TEMPORAL SULCUS EXTRACTION
	file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/template_LEFTsulcus_parametrization.bvproc')
	file_parsed_template_path = os.path.join(scriptDIR, f'{SUBJECT}_LEFTsulcparam.bvproc')
	f_in = open(file_template_path, 'r')
	f_out = open(file_parsed_template_path, 'w')

	for line in f_in:
		#read replace the string and write to output file
		line = line.replace('BVDIR', BVDIR).replace('SUBJECT', SUBJECT).replace('BVHOME', BVHOME)
		f_out.write(line)
	#close input and output files
	f_in.close()
	f_out.close()

	os.system(f'{BVHOME}/bin/brainvisa -r {file_parsed_template_path}')


def right_sulci_parameterize(SUBJECT):
	#RIGHT TEMPORAL SULCUS EXTRACTION
	file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/template_RIGHTsulcus_parametrization.bvproc')
	file_parsed_template_path = os.path.join(scriptDIR, f'{SUBJECT}_RIGHTsulcparam.bvproc')
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
	parser.add_argument('--subject', '-s', type=str, help="subject ID")
	parser.add_argument('--list', '-l', action='store_true', help="folder with subjects")
	args = parser.parse_args()

	if not (args.list or args.subject):
		parser.error('No action requested, add -list or -subject')

	subjects_path = os.path.join(BVDIR, 'subjects')
	subjects = [f for f in os.listdir(subjects_path) if (os.path.isdir(os.path.join(subjects_path, f))) and ('KK' in f)]

	if args.list:
		for sbj in subjects:
			#Extraction pipeline
			print(f'*** {sbj} extraction pipeline started ***\n')
			folder_creation(sbj)
			left_sulci_parameterize(sbj)
			right_sulci_parameterize(sbj)
	else: 
		sbj = args.subject

		#Extraction pipeline
		print(f'*** {sbj} extraction pipeline started ***\n')
		folder_creation(sbj)
		left_sulci_parameterize(sbj)
		right_sulci_parameterize(sbj)
	

if __name__ == '__main__':
	main()