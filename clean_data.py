import os
import os.path as path
#from run_brainvisa_cortical_surface import BVDIR

#'KKI2009-22-MPRAGE', 'KKI2009-26-MPRAGE', 'KKI2009-14-MPRAGE', 'KKI2009-08-MPRAGE', 'KKI2009-01-MPRAGE' corrupted

BVDIR = '/home/zaffaro/Desktop/sulcus-parameterization-pipeline/bv_dir_corrected'

subjects_path = f'{BVDIR}/subjects/'#KKI2009-01-MPRAGE/t1mri/default_acquisition/default_analysis/folds/3.1/default_session_auto/'
subjects = [f for f in os.listdir(subjects_path) if (path.isdir(path.join(subjects_path, f))) and ('KK' in f)]

for s in subjects:
    files_path = f'{BVDIR}/subjects/{s}/t1mri/default_acquisition/default_analysis/folds/3.1/default_session_auto/'
    files = [f.split('corrected') for f in os.listdir(files_path) if path.isfile(path.join(files_path, f)) and 'corrected' in f]
    #files = [f for f in os.listdir(files_path) if path.isfile(path.join(files_path, f))]
    for f in files:
        if ('half' in f[0]) and (os.path.exists(path.join(files_path, f'{f[0]}corrected{f[1]}'))):
            os.remove(path.join(files_path, f'{f[0]}corrected{f[1]}'))
            print(f'remove {f[0]}corrected{f[1]}')
        if '...' in f[1]:
            os.remove(path.join(files_path, f'{f[0]}corrected{f[1]}'))
            print(f'remove {f[0]}corrected{f[1]}')
            if os.path.exists(path.join(files_path, f'{f[0]}corrected...data')):
                print(f'remove: {f[0]}corrected...data')
                os.system(f"rm -rf {path.join(files_path, f'{f[0]}corrected...data')}")
        
    files_set = set()
    for f in files:
        if 'half' not in f[0]:
            files_set.add(f[0])
        else:
            print(f)
    for f in files_set:
        max = 1
        end_path = ''
        for f2 in files:
            if f == f2[0]:
                if f2[1][0] == '.':
                    continue
                elif int(f2[1][0]) > max:
                    if os.path.exists(path.join(files_path, f'{f}corrected{end_path}.arg.minf')):
                        print(f'remove: {f}corrected{end_path}.arg.minf')
                        os.remove(path.join(files_path, f'{f}corrected{end_path}.arg.minf'))
                    if os.path.exists(path.join(files_path, f'{f}corrected{end_path}.arg')):
                        print(f'remove: {f}corrected{end_path}.arg')
                        os.remove(path.join(files_path, f'{f}corrected{end_path}.arg'))
                    if os.path.exists(path.join(files_path, f'{f}corrected{end_path}.data')):
                        print(f'remove: {f}corrected{end_path}.data')
                        os.system(f"rm -rf {path.join(files_path, f'{f}corrected{end_path}.data')}")
                    print('')

                    max = int(f2[1][0])                    
                    end_path = f2[1][0]
                elif int(f2[1][0]) < max:
                    if os.path.exists(path.join(files_path, f'{f}corrected{f2[1][0]}.arg.minf')):
                        print(f'remove: {f}corrected{f2[1][0]}.arg.minf')
                        os.remove(path.join(files_path, f'{f}corrected{f2[1][0]}.arg.minf'))
                    if os.path.exists(path.join(files_path, f'{f}corrected{f2[1][0]}.arg')):
                        print(f'remove: {f}corrected{f2[1][0]}.arg')
                        os.remove(path.join(files_path, f'{f}corrected{f2[1][0]}.arg'))
                    if os.path.exists(path.join(files_path, f'{f}corrected{f2[1][0]}.data')):
                        print(f'remove: {f}corrected{f2[1][0]}.data')
                        os.system(f"rm -rf {path.join(files_path, f'{f}corrected{f2[1][0]}.data')}")
                    print('')
                  
        print(f'best: {f}corrected{end_path}.arg.minf')
        print(f'best: {f}corrected{end_path}.arg')
        if os.path.exists(path.join(files_path, f'{f[:-1]}.arg.minf')):
            os.remove(path.join(files_path, f'{f[:-1]}.arg.minf'))
        if os.path.exists(path.join(files_path, f'{f[:-1]}.arg')):
            os.remove(path.join(files_path, f'{f[:-1]}.arg'))
        if os.path.exists(path.join(files_path, f'{f[:-1]}.data')):
            os.system(f"rm -rf {path.join(files_path, f'{f[:-1]}.data')}")

        os.rename(path.join(files_path, f'{f}corrected{end_path}.arg.minf'), path.join(files_path, f'{f[:-1]}.arg.minf'))
        os.rename(path.join(files_path, f'{f}corrected{end_path}.arg'), path.join(files_path, f'{f[:-1]}.arg'))
        if os.path.exists(path.join(files_path, f'{f}corrected{int(end_path)+1}.data')):
            os.rename(path.join(files_path, f'{f}corrected{int(end_path)+1}.data'), path.join(files_path, f'{f[:-1]}.data'))
            if os.path.exists(path.join(files_path, f'{f}corrected{end_path}.data')):
                os.system(f"rm -rf {path.join(files_path, f'{f}corrected{end_path}.data')}")
        else:
            os.rename(path.join(files_path, f'{f}corrected{end_path}.data'), path.join(files_path, f'{f[:-1]}.data'))
        
