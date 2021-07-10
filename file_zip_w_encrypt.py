# -*- coding: utf-8 -*-
import pyminizip
import os

# compress level
com_lvl = 5

def main(log_directory, password):
    for file in os.listdir(log_directory):
        if file.split(".")[1] in ['py', 'exe']:
            continue
        print ('[Info.]\t\t'+file)
        # compressing file
        pyminizip.compress(file.encode('cp950'), None, (file.split(".")[0]+'.zip').encode('cp950'), password, com_lvl)
        print ('[Output]\t'+(file.split(".")[0]+'.zip'))

if __name__ == '__main__':
    print ("[Input] directory:")
    input_dir = input()
    print ("[Input] password:")
    input_pw = input()
    main(input_dir, input_pw)
    os.system("pause")