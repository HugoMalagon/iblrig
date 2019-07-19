import os
import subprocess
import time
from pathlib import Path
import logging

# import user_settings  # PyBpod creates this file on run.
import iblrig.fake_user_settings as user_settings
import task_settings
from session_params import SessionParamHandler

log = logging.getLogger('iblrig')

sph = SessionParamHandler(task_settings, user_settings)

CWD = os.getcwd()
BONSAI_FOLDER = Path(sph.IBLRIG_FOLDER) / 'Bonsai'

bns = str(BONSAI_FOLDER / 'Bonsai64.exe')
# wrkfl = Path(sph.IBLRIG_FOLDER) / 'visual_stim' / \
#     sph.VISUAL_STIMULUS_TYPE / 'certification.bonsai'
misc_folder = Path(sph.IBLRIG_FOLDER) / 'visual_stim' / 'misc'
stim_00_folder = misc_folder / '00_SpacerStim'
stim_01_folder = misc_folder / '01_ReceptiveFieldMappingStim'
stim_02_folder = misc_folder / '02_OrientationDirectionSelectivityStim'
stim_03_folder = misc_folder / '03_ContrastReversingCheckerboardStim'
stim_04_folder = misc_folder / '04_ContrastSelectivityTaskStim'
wrkfl_00 = str(stim_00_folder / 'spacer.bonsai')
wrkfl_01 = str(stim_01_folder / 'ReceptiveFieldMappingStim.bonsai')
wrkfl_02 = str(stim_02_folder / 'OrientationDirectionSelectivityStim.bonsai')
wrkfl_03 = str(stim_03_folder / 'ContrastReversingCheckerboardStim.bonsai')
wrkfl_04 = str(stim_04_folder / 'ContrastSelectivityTaskStim.bonsai')

# Flags
noedit = '--no-editor'  # implies start and no-debug?
noboot = '--no-boot'
# Properties
cmd_01_save_to = '-p:FileNameRFMapStim=' + str(
    Path(sph.SESSION_RAW_DATA_FOLDER) / '_iblrig_RFMapStim.raw.bin')
cmd_01_runtime = '-p:MappingTime=00:10:00'  # '-p:MappingTime=00:00:03'
cmd_03_runtime = '-p:CheckerboardTime=00:10:00'  # '-p:CheckerboardTime=00:00:03'
cmd_04_stims_test = '-p:StimFileName=' + str(stim_04_folder / 'stims.csv')  # 'stims_test.csv')
# Commands
cmd_00 = [bns, wrkfl_00, noedit, noboot]
cmd_01 = [bns, wrkfl_01, noedit, noboot, cmd_01_save_to, cmd_01_runtime]
cmd_02 = [bns, wrkfl_02, noedit, noboot]
cmd_03 = [bns, wrkfl_03, noedit, noboot, cmd_03_runtime]
cmd_04 = [bns, wrkfl_04, noedit, noboot, cmd_04_stims_test]

log.info('Starting Receptive Field Mapping Simulus:')
log.info(' '.join(cmd_01))
os.chdir(stim_00_folder)
s = subprocess.run(cmd_00, stdout=subprocess.PIPE)  # call locks!
os.chdir(stim_01_folder)
s = subprocess.run(cmd_01, stdout=subprocess.PIPE)  # call locks!
log.info('Starting Orientation Direction Selectivity Simulus:')
log.info(' '.join(cmd_02))
os.chdir(stim_00_folder)
s = subprocess.run(cmd_00, stdout=subprocess.PIPE)  # call locks!
os.chdir(stim_02_folder)
s = subprocess.run(cmd_02, stdout=subprocess.PIPE)  # call locks!
log.info('Starting Orientation Direction Selectivity Simulus:')
log.info(' '.join(cmd_03))
os.chdir(stim_00_folder)
s = subprocess.run(cmd_00, stdout=subprocess.PIPE)  # call locks!
os.chdir(stim_03_folder)
s = subprocess.run(cmd_03, stdout=subprocess.PIPE)  # call locks!
log.info('Starting Contrast Reversing Checkerboard Simulus:')
log.info(' '.join(cmd_04))
os.chdir(stim_00_folder)
s = subprocess.run(cmd_00, stdout=subprocess.PIPE)  # call locks!
os.chdir(stim_04_folder)
s = subprocess.run(cmd_04, stdout=subprocess.PIPE)  # call locks!
os.chdir(CWD)
log.info('Starting 900 seconds of nothingness... [yes, it''s 15 minutes] :)')
time.sleep(900)
log.info("You're done, please remove the mouse.\n" * 42)