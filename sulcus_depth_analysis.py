import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline, interp1d, splrep, splev
import csv

# Main folders
BVDIR = '/home/zaffaro/Desktop/sulcus-parameterization-pipeline/bv_dir2' #<- OUTPUTS, folder will be  created

def folder_creation(SUBJECT):
	# Main folders creation
	graph_folder_path = os.path.join(BVDIR, 'subjects', SUBJECT, 'graph')
	if not os.path.exists(graph_folder_path):
		os.mkdir(graph_folder_path)
	return graph_folder_path

def graph(SUBJECT, emisphere, file, graph_folder_path, writer, smooth=False):
	file_graph_path = os.path.join(BVDIR, 'subjects', SUBJECT, 'sulci', file)
	df = pd.read_csv(file_graph_path, sep='\t', names=['id', 'depth', 'profile'], index_col='id', dtype={'id': int, 'depth': float, 'profile': float})

	smth = 300

	if smooth:
		bspl = splrep(df.index, df['depth'], s=smth)
		bspl_y = splev(df.index, bspl)
		plt.plot(df.index, bspl_y, label='depth')
	else:
		plt.plot(df.index, df['depth'], label='depth')
	
	plt.legend()
	plt.savefig(os.path.join(graph_folder_path, f'{SUBJECT}_{emisphere}_depth_plot.png'))
	plt.clf()	

	if smooth:
		bspl = splrep(df.index, df['profile'], s=smth)
		bspl_y = splev(df.index, bspl)
		plt.plot(df.index, bspl_y, label='profile')
	else:
		plt.plot(df.index, df['profile'], label='profile')
	
	plt.legend()
	plt.savefig(os.path.join(graph_folder_path, f'{SUBJECT}_{emisphere}_profile_plot.png'))
	plt.clf()

	if smooth:
		bspl = splrep(df.index, df['depth'], s=smth)
		bspl_y = splev(df.index, bspl)
		plt.plot(df.index, bspl_y, label='depth')
		bspl = splrep(df.index, df['profile'], s=smth)
		bspl_y = splev(df.index, bspl)
		plt.plot(df.index, bspl_y, label='profile')	
	else:
		df.plot()
	plt.savefig(os.path.join(graph_folder_path, f'{SUBJECT}_{emisphere}_depth-profile_plot.png'))
	plt.clf()

	for dp in df['profile']:
		writer.writerow([f'{SUBJECT}', f'{emisphere}', f'{dp}'])


def main():
	subjects_path = os.path.join(BVDIR, 'subjects')
	subjects = [f for f in os.listdir(subjects_path) if (os.path.isdir(os.path.join(subjects_path, f))) and ('KK' in f)]

	csvfile = open('subjects_profile2.csv', 'w')
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerow(['SUBJECT', 'EMISPHERE', 'DEPTH'])

	for sbj in subjects:#[6:10]:
		#Pipeline
		graph_folder_path = folder_creation(sbj)
		# Left sulcus plot
		graph(sbj, 'L', f'{sbj}_L_stsleft-depth.txt', graph_folder_path, writer, smooth=False)
		# Right sulcus plot
		graph(sbj, 'R', f'{sbj}_R_stsright-depth.txt', graph_folder_path, writer, smooth=False)

	csvfile.close()	

if __name__ == '__main__':
	main()