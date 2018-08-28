import csv
from sys import argv
from time import time
from math import floor

USAGE_MSG ='''\tusage:\tpython3 train.py <[-h]/[train_file.csv]>
\tflag -h to get info about csv file construction and virtual environment for this app'''
HELP_FLAG_MSG = 'help flag msg'

ERR_MSG = '\tError:'
IS_A_DIR_ERR_MSG = 'is a directory!'
FILE_NOT_FOUND_ERR_MSG = 'file not found!'

LOG_OPEN_SUCCESS_MSG = 'Opened'
LOG_TRN_HEAD_MSG = '--- Training ---'
LOG_TRN_STEP_MSG1 = 'Training'
LOG_TRN_STEP_MSG2 = 'took'
LOG_TRN_STEP_MSG3 = 'ms'
LOG_TRN_FIN_MSG1 = 'Training took'
LOG_TRN_FIN_MSG2 = 's or'
LOG_TRN_FIN_MSG3 = 'min'

MODEL_FILE_NAME = 'model42'
MODEL_FILE_EXT = '.csv'

LOG_MDL_HEAD_MSG = '--- Saving ---'
LOG_MDL_WAIT_MSG = '.'
LOG_MDL_FIN_MSG = 'Successfully save to'

result_saver = []
if len(argv) != 2:
    print(USAGE_MSG)
    exit(-1)
if argv[1] == '-h':
    print(HELP_FLAG_MSG)
    exit(0)
try:
    with open(argv[1]) as csvfile:
        print(LOG_OPEN_SUCCESS_MSG, argv[1])
        readCSV = csv.reader(csvfile, delimiter=',')
        print(LOG_TRN_HEAD_MSG)
        global_time = 0
        step = 0
        for row in readCSV:
            start_time = time()
            form_res = []
            for i in range(800):
                form_res.append(i)
            result_saver.append(form_res)
            #train func
            end_time = time()
            global_time += (end_time - start_time)
            try:
                print(LOG_TRN_STEP_MSG1, '#' + str(row[0]), LOG_TRN_STEP_MSG2,
                      (end_time - start_time) * 1000, LOG_TRN_STEP_MSG3)
            except IndexError:
                break
        print(LOG_TRN_FIN_MSG1, global_time, LOG_TRN_FIN_MSG2, global_time/60, LOG_TRN_FIN_MSG3)
except IsADirectoryError:
    print(ERR_MSG, argv[1], IS_A_DIR_ERR_MSG, '\n')
    print(USAGE_MSG)
    exit(-1)
except FileNotFoundError:
    print(ERR_MSG, argv[1], FILE_NOT_FOUND_ERR_MSG, '\n')
    print(USAGE_MSG)
    exit(-1)
file_name_editor = '_new'
file_name_cnt = -1
while True:
    file_name_cnt += 1
    try:
        if file_name_cnt == 0:
            file_name = MODEL_FILE_NAME + MODEL_FILE_EXT
        else:
            file_name = MODEL_FILE_NAME + file_name_editor + str(file_name_cnt) + MODEL_FILE_EXT
        with open(file_name, 'x') as csvfile:
            print(LOG_MDL_HEAD_MSG)
            writeCSV = csv.writer(csvfile)
            current_sec = 0
            start_time = time()
            old_str = ''
            for i in range(0, len(result_saver)):
                writeCSV.writerow(result_saver[i])
                new_str = str(floor(i*100/len(result_saver))) + "%"
                print('\033[%iD' % len(old_str) + new_str, end='', flush=True)
                old_str = new_str
            print('\033[%iD' % len(old_str) + LOG_MDL_FIN_MSG, file_name)
        break
    except FileExistsError:
        pass