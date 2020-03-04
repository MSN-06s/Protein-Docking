#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import sys
import os
import shutil

#Parse args
pdb_dir=sys.argv[1]
out_dir=sys.argv[2]

path = os.getcwd()
f_list = os.listdir(pdb_dir)
f = open('error_file.txt',w)
#Extract and rename pdb files
for i in f_list:
    try:
        os.chdir(f'{pdb_dir}\\{i}\\model\\01')
        os.rename('model.pdb',f'{i}.pdb')
        shutil.copy(f'{i}.pdb',f'{out_dir}')
    except FileNotFoundError:
        try:
            os.chdir((f'{pdb_dir}\\{i}\\{i}\\model\\01'))
            os.rename('model.pdb',f'{i}.pdb')
            shutil.copy(f'{i}.pdb',f'{out_dir}')
        except:
            f.write(i)
            continue
    except:
        f.write(i)
        continue
f.close()

        



