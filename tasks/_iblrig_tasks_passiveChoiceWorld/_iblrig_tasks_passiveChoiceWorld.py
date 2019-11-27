#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Niccolò Bonacchi
# @Date: Friday, November 15th 2019, 12:05:29 pm
import logging
import math
import time

import matplotlib.pyplot as plt
import numpy as np
from pybpod_rotaryencoder_module.module import RotaryEncoder
from pybpodapi.protocol import Bpod, StateMachine

import iblrig.iotasks as iotasks
import iblrig.bonsai as bonsai
import iblrig.path_helper as ph
import iblrig.params as params
import iblrig.sound as sound
import task_settings
import user_settings
from session_params import SessionParamHandler

log = logging.getLogger('iblrig')
log.setLevel(logging.INFO)

# start sph
sph = SessionParamHandler(task_settings, user_settings)
# start Bonsai stim workflow

# get bpod
PARAMS = params.load_params_file()
bpod = Bpod(serial_port=PARAMS['COM_BPOD'])
# get soundcard bpod style
bpod_sound_card = [x for x in bpod.modules if x.name == 'SoundCard1'][0]
# Play tone
sc_play_tone = 2
bpod.load_serial_message(bpod_sound_card, sc_play_tone, [ord('P'), sph.GO_TONE_IDX])
# Play noise
sc_play_noise = 3
bpod.load_serial_message(bpod_sound_card, sc_play_noise, [ord('P'), sph.WHITE_NOISE_IDX])

# get soundcard
import usb
card = usb.core.find(idVendor=0x04d8, idProduct=0xee6a)
card_play_tone = [2, 6, 32, 255, 2, 2, 0, 43]
card_play_noise = [2, 6, 32, 255, 2, 3, 0, 44]


def do_gabor(pcs_idx, pos, cont, phase):
    # send pcs to Bonsai
    bonsai.send_stim_info(sph.OSC_CLIENT, pcs_idx, pos, cont, phase,
                          freq=0.10, angle=0., gain=4., sigma=7.)

    # TODO: make bpod osc override!!
    sph.OSC_CLIENT.send_message("/stim", 2)  # show_stim 2
    time.sleep(0.3)
    sph.OSC_CLIENT.send_message("/stim", 1)  # stop_stim 1


def do_valve_click(bpod, reward_valve_time):
    sma = StateMachine(bpod)
    sma.add_state(
        state_name='valve_open',
        state_timer=reward_valve_time,
        output_actions=[('Valve1', 255),
                        ('BNC1', 255)],  # To FPGA
        state_change_conditions={'Tup': 'exit'},
    )
    bpod.send_state_machine(sma)
    bpod.run_state_machine(sma)  # Locks until state machine 'exit' is reached
    return


def do_bpod_sound(bpod, sound_msg):
    sma = StateMachine(bpod)
    sma.add_state(
        state_name='play_tone',
        state_timer=0,
        output_actions=[('Serial3', sound_msg)],
        state_change_conditions={'BNC2Low': 'exit'},
    )
    bpod.send_state_machine(sma)
    bpod.run_state_machine(sma)  # Locks until state machine 'exit' is reached
    return


def do_card_sound(card, sound_msg):
    card.write(1, sound_msg, 100)
    time.sleep(0.1)
    return


pcs_idx = 0
for sdel, sid in zip(sph.STIM_DELAYS, sph.STIM_IDS):
    time.sleep(sdel)
    if sid == 'V':
        # Make bpod task with 1 state = valve_open -> exit
        do_valve_click(sph.REWARD_VALVE_TIME)
        # time.sleep(sph.REWARD_VALVE_TIME)
    elif sid == 'T':
        do_card_sound(card, card_play_tone)
        # time.sleep(0.1)
    elif sid == 'N':
        do_card_sound(card, card_play_noise)
        # time.sleep(0.5)
    elif sid == 'G':
        do_gabor(pcs_idx,
                 sph.POSITIONS[pcs_idx],
                 sph.CONTRASTS[pcs_idx],
                 sph.STIM_PHASE[pcs_idx])
        pcs_idx += 1
        # time.sleep(0.3)


if __name__ == "__main__":
    preloaded_session_num = 'mock'
    # Load session PCS
    position, contrast, phase = iotasks.load_passive_session_pcs(preloaded_session_num)
    # Load session stimDelays, stimIDs
    stimDelays, stimIDs = iotasks.load_passive_session_delays_ids(preloaded_session_num)
    print('.')
