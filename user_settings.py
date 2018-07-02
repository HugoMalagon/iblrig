# import logging

# SETTINGS_PRIORITY = 0
# # THESE SETTINGS ARE NEEDED FOR PYSETTINGS
# APP_LOG_FILENAME = 'app.log'
# APP_LOG_HANDLER_CONSOLE_LEVEL = logging.WARNING
# APP_LOG_HANDLER_FILE_LEVEL    = logging.WARNING

# CONTROL_EVENTS_GRAPH_DEFAULT_SCALE  = 100
# BOARD_LOG_WINDOW_REFRESH_RATE       = 1000

# USE_MULTIPROCESSING = True

# PYFORMS_MAINWINDOW_MARGIN       = 0
# PYFORMS_STYLESHEET              = ''
# PYFORMS_STYLESHEET_DARWIN       = ''
# PYFORMS_SILENT_PLUGINS_FINDER   = False

# PYFORMS_MATPLOTLIB_ENABLED  = True
# PYFORMS_WEB_ENABLED         = True
# PYFORMS_GL_ENABLED          = False
# PYFORMS_VISVIS_ENABLED      = False

# GENERIC_EDITOR_PLUGINS_PATH = None
# GENERIC_EDITOR_PLUGINS_LIST = [
# 'pybpodgui_plugin',
# 'pybpodgui_plugin_timeline',
# 'pybpodgui_plugin_session_history',
# 'pybpod_rotaryencoder_module',
# 'water_calibration_plugin']  # 'pybpod_old_format']



# TARGET_BPOD_FIRMWARE_VERSION = '21'

# DEFAULT_PROJECT_PATH = 'C:\\IBL_root\\pybpod_projects\\IBL'
# GENERIC_EDITOR_TITLE = 'IBL'
# ############ BPODGUI PLUGIN SETTINGS ############

# BOARD_LOG_WINDOW_REFRESH_RATE  = 1000
# SESSIONLOG_PLUGIN_REFRESH_RATE = 500
# TIMELINE_PLUGIN_REFRESH_RATE   = 500

# PYBOARD_COMMUNICATION_THREAD_REFRESH_TIME  = 1 # timer for thread look for events (seconds)
# PYBOARD_COMMUNICATION_PROCESS_REFRESH_TIME = 1 # timer for process look for events (seconds)
# PYBOARD_COMMUNICATION_PROCESS_TIME_2_LIVE  = 0 # wait before killing process (seconds)


# GENERIC_EDITOR_PLUGINS_PATH = "C:/IBL_root/water-calibration-plugin"
import logging

SETTINGS_PRIORITY = 0

GENERIC_EDITOR_PLUGINS_LIST = [
    #'water_calibration_plugin',
    'pybranch',
    'pyforms',
    'pyforms_generic_editor',
    'sca',
    'pybpodgui_plugin',
    'pybpodgui_plugin_timeline',
    'pybpodgui_plugin_trial_timeline',
    'pybpodgui_plugin_session_history',
    'pybpod_rotaryencoder_module',
    'pybpod_analogoutput_module',
    'pybpod_alyx_module',
    'pge_plugin_terminal',
    #'pybpodgui_plugin_oldformat',
]

#DEFAULT_PROJECT_PATH = '../test-project'
#DEFAULT_PROJECT_PATH = 'new-format'
#DEFAULT_PROJECT_PATH = '../pybpod_projects/IBL'

PYFORMS_SILENT_PLUGINS_FINDER   = False

PYBPOD_EXTRA_INFO = {'Users','Subjects'}

DEFAULT_PROJECT_PATH = 'C:\\IBL_root\\pybpod_projects\\IBL'
ALYX_ADDR = 'http://alyx.champalimaud.pt:8000'

APP_LOG_HANDLER_CONSOLE_LEVEL = logging.ERROR
APP_LOG_HANDLER_FILE_LEVEL    = logging.ERROR

PYBPOD_API_LOG_LEVEL = logging.ERROR


#PYBOARD_COMMUNICATION_THREAD_REFRESH_TIME  = 0.5 # timer for thread look for events (seconds)
#PYBOARD_COMMUNICATION_PROCESS_REFRESH_TIME = 0.5 # timer for process look for events (seconds)
