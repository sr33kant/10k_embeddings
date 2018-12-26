import os
import shutil
import datetime
import glob
import multiprocessing as mp
import re
import time
def clean_sent(line):



    line = line.lower()
    line = re.sub(r'([^\s\w])+', '', line)
    #line = re.sub(r'^http?:\/\/.*[\r\n]*', '', line)
    line = re.sub(r'((1-\d{3}-\d{3}-\d{4})|(\(\d{3}\) \d{3}-\d{4})|(\d{3}-\d{3}-\d{4}))', '', line)
    line = re.sub(r'\b\d+(?:\.\d+)?\s+', '', line)
    line=line.lower()
    return line

def read_chunk(fopen, number_of_blocks, block):

    fopen.seek(0, 2)

    file_size = fopen.tell()

    ini = file_size * block / number_of_blocks

    end = file_size * (1 + block) / number_of_blocks

    if ini <= 0:

        fopen.seek(0)

    else:

        fopen.seek(ini - 1)

        fopen.readline()

    while fopen.tell() < end:

        yield fopen.readline()

def pprocess(params):

    filename, chunk_number, number_of_chunks = params
    with open(filename,'rt',encoding="utf-8") as fp:

        for line in read_chunk(fp, number_of_chunks, chunk_number):
            cleaned_files(clean_sent(line),chunk_number)

def cleaned_files(sent,chunk_number):

    #with open('C:\\Users\\sreek\\PycharmProjects\\SEC-Edgar-Data\\'+str(chunk_number)+'.txt', 'a') as fop:
    with open('C:\\Users\\sreek\\PycharmProjects\\SEC-Edgar-Data\\output_file.txt', 'a') as fop:
        fop.write(sent)

if __name__=="__main__":
    t1 = time.time()
    pool = mp.Pool()
    number_of_chunks=mp.cpu_count()
    filename='C:\\Users\\sreek\\PycharmProjects\\SEC-Edgar-Data\\merged_file.txt'
    tasks= [(filename, i, number_of_chunks) for i in range(number_of_chunks)]
    pool.map(pprocess,tasks)
    t2=time.time()
    print(t2-t1)