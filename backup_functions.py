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

	os.system(f'{BVHOME}/bin/bv axon-runprocess {file_parsed_template_path}')


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

	os.system(f'{BVHOME}/bin/bv axon-runprocess {file_parsed_template_path}')


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

	os.system(f'{BVHOME}/bin/bv axon-runprocess {file_parsed_template_path}')


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

	os.system(f'{BVHOME}/bin/bv axon-runprocess {file_parsed_template_path}')


def run_import_t1_from_freesurfer(SUBJECT):
	#IMPORT T1MRI
	file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/import_t1_bv503.bvproc')
	file_parsed_template_path = os.path.join(scriptDIR, f'{SUBJECT}_import_t1_bv503.bvproc')
	f_in = open(file_template_path, 'r')
	f_out = open(file_parsed_template_path, 'w')

	for line in f_in:
		#read replace the string and write to output file
		line = line.replace('BVDIR', BVDIR)
		line = line.replace('SUBJECT', SUBJECT)
		line = line.replace('FSDIR', FSDIR)
		line = line.replace('BVHOME', BVHOME)	
		f_out.write(line)
	#close input and output files
	f_in.close()
	f_out.close()

	os.system(f'{BVHOME}/bin/bv axon-runprocess {file_parsed_template_path}')


def run_import_t1_from_freesurfer(SUBJECT):
	#IMPORT T1MRI
	file_template_path = os.path.join(MAINDIR, 'brainvisa_templates/import_t1_bv503.bvproc')
	file_parsed_template_path = os.path.join(scriptDIR, f'{SUBJECT}_import_t1_bv503.bvproc')
	f_in = open(file_template_path, 'r')
	f_out = open(file_parsed_template_path, 'w')

	for line in f_in:
		#read replace the string and write to output file
		line = line.replace('BVDIR', BVDIR)
		line = line.replace('SUBJECT', SUBJECT)
		line = line.replace('FSDIR', FSDIR)
		line = line.replace('BVHOME', BVHOME)	
		f_out.write(line)
	#close input and output files
	f_in.close()
	f_out.close()

	os.system(f'{BVHOME}/bin/bv axon-runprocess --enabledb {file_parsed_template_path}')