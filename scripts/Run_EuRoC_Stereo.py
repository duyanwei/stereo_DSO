#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@file Run_EuRoC_Stereo.py
@author Yanwei Du (duyanwei0702@gmail.com)
@date 08-03-2022
@version 1.0
@license Copyright (c) 2022
@desc None
'''

# This script is to run all the experiments in one program

import os
import subprocess
import time

# DATA_ROOT = '/mnt/DATA/Datasets/EuRoC/'
DATA_ROOT = '/media/duyanwei/Du/data/EuRoC/MAV/'
SeqNameList = [
    'MH_01_easy', 'MH_02_easy', 'MH_03_medium',
    'MH_04_difficult', 'MH_05_difficult',
    'V1_01_easy', 'V1_02_medium', 'V1_03_difficult',
    'V2_01_easy', 'V2_02_medium', 'V2_03_difficult']
RESULT_ROOT = os.path.join(
    os.environ['SLAM_RESULT'], 'stereo_DSO/EuRoC/')
NumRepeating = 1
SleepTime = 5  # 10 # 25 # second
# FeaturePool = [500]
SpeedPool = [1.0] # , 2.0, 3.0] # , 4.0, 5.0] # x
EnableViewer = 0
EnableLogging =1
VI_SDSO_PATH = os.path.join(os.environ['SLAM_OPENSOURCE'], 'direct/stereo_DSO')

# ----------------------------------------------------------------------------------------------------------------------


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ALERT = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# loop over play speed
for speed in SpeedPool:

    speed_str = str(speed)
    result_dir = os.path.join(RESULT_ROOT, 'Fast' + speed_str)

    # create result dir first level
    cmd_mkdir = 'mkdir -p ' + result_dir
    subprocess.call(cmd_mkdir, shell=True)

    # loop over num of repeating
    for iteration in range(NumRepeating):

        # create result dir second level
        experiment_dir = os.path.join(result_dir, 'Round' + str(iteration + 1))
        cmd_mkdir = 'mkdir -p ' + experiment_dir
        subprocess.call(cmd_mkdir, shell=True)

        # loop over sequence
        for sn, sname in enumerate(SeqNameList):

            print(bcolors.ALERT + "====================================================================" + bcolors.ENDC)

            SeqName = SeqNameList[sn]
            print(bcolors.OKGREEN + f'Seq: {SeqName}; Speed: {speed_str}; Round: {str(iteration + 1)};')

            file_data = os.path.join(DATA_ROOT, SeqName)
            file_traj = os.path.join(experiment_dir, SeqName)
            file_log = '> ' + file_traj + '_logging.txt' if EnableLogging else ''

            # compose cmd
            cmd_slam = \
                VI_SDSO_PATH + '/build/bin/dso_dataset' + \
                    ' files0=' + os.path.join(file_data, 'mav0/cam0/data') + \
                    ' files1=' + os.path.join(file_data, 'mav0/cam1/data') + \
                    ' calib0=' + os.path.join(VI_SDSO_PATH, 'calib/euroc/cam0.txt') + \
                    ' calib1=' + os.path.join(VI_SDSO_PATH, 'calib/euroc/cam1.txt') + \
                    ' T_stereo=' + os.path.join(VI_SDSO_PATH, 'calib/euroc/T_C0C1.txt') + \
                    ' groundtruth=' + os.path.join(file_data, 'mav0/state_groundtruth_estimate0/data.csv') + \
                    ' pic_timestamp=' + os.path.join(file_data, 'mav0/cam0/data.csv') + \
                    ' pic_timestamp1=' + os.path.join(file_data, 'mav0/cam1/data.csv') + \
                    ' preset=0 mode=1 nomt=1 glog_loglevl=1' + \
                    ' speed=' + speed_str + \
                    ' nogui=' + str(0 if EnableViewer else 1) + \
                    ' quite=1' + \
                    ' savefile_tail=' + file_traj + \
                    ' ' + file_log

            print(bcolors.WARNING + "cmd_slam: \n" + cmd_slam + bcolors.ENDC)

            print(bcolors.OKGREEN + "Launching SLAM" + bcolors.ENDC)
            # proc_slam = subprocess.Popen(cmd_slam, shell=True) # starts a new shell and runs the result
            subprocess.call(cmd_slam, shell=True)

            print(bcolors.OKGREEN + "Finished" + bcolors.ENDC)
            subprocess.call('pkill dso_dataset', shell=True)
            time.sleep(SleepTime)