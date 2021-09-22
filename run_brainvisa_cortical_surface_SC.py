import os
import argparse

# Main folders
MAINDIR = './'
BVDIR = './bv_dir_5.0.2' #<- OUTPUTS, folder will be  created
#FSDIR = '/home/zaffaro/freesurfer/subjects' # INPUTS, folder containing subjects processed with freesurfer
BVHOME = './brainvisa'
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


def left_central_sulci_parameterize(SUBJECT):
	#LEFT TEMPORAL SULCUS EXTRACTION
	file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/template_LEFTCENTRALsulcus_parametrization.bvproc')
	file_parsed_template_path = os.path.join(scriptDIR, f'{SUBJECT}_LEFTCENTRALsulcparam.bvproc')
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


def right_central_sulci_parameterize(SUBJECT):
	#RIGHT TEMPORAL SULCUS EXTRACTION
	file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/template_RIGHTCENTRALsulcus_parametrization.bvproc')
	file_parsed_template_path = os.path.join(scriptDIR, f'{SUBJECT}_RIGHTCENTRALsulcparam.bvproc')
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
	parser.add_argument('--subject', '-s', type=str, default='KKI2009-28-MPRAGE', #required = True,
						help="subject ID")
	args = parser.parse_args()

	subjects_path = os.path.join(BVDIR, 'subjects')
	subjects = [f for f in os.listdir(subjects_path) if (os.path.isdir(os.path.join(subjects_path, f))) and ('KK' in f)]

	for sbj in subjects:
		#Extraction pipeline
		print(f'*** {sbj} extraction pipeline started ***\n')
		folder_creation(sbj)
		left_central_sulci_parameterize(sbj)
		right_central_sulci_parameterize(sbj)
	

if __name__ == '__main__':
	main()