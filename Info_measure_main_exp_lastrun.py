#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Thu Feb 16 13:27:44 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from Ini_code




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'Info_measure_main_exp'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/ouyukun/Desktop/-qianchen_info_measure_main_exp2a/Info_measure_main_exp_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Startup" ---
# Run 'Begin Experiment' code from Python_initialisation
# VARIOUS INITIALISATIONS #

# updated later in screen_scale to get mm values
win_pix_x = (win.size[0]);
win_pix_y = (win.size[1]);

# --- Initialize components for Routine "StimSetUp" ---
# Run 'Begin Experiment' code from Ini_code
# initialisations
# timing
fixation_cross_duration = 0.5
image_duration = 0.15
exit_message_duration = fixation_cross_duration + image_duration

# feedback square height
feedback_square_width = 0.03 # set in fractions of screen height

# response feedback time
response_feedback_time = 4

# Set response size
win_pix_x = (win.size[0]);
win_pix_y = (win.size[1]);
a = win_pix_y*0.75/6
b = win_pix_y*0.75/3
#print('Response width: ',a)
#print('Response height: ',b)

# trial number setup
trialnumber = 0
alltrials = 240

# --- Initialize components for Routine "Consent" ---
consent_text = visual.TextStim(win=win, name='consent_text',
    text='This is an Informed Consent Form. Please read and understand the statements below.\n\n1, I understand that my taking part in the study is voluntary and that I am free to leave the study at any time, without giving any reason. I understand that my medical care or legal rights will not be affected in any way.\n\n2, I agree to the use and release of study-related information about me for the purposes described in this Informed Consent Form.\n\n3, I agree to the re-use of data collected in this study for future studies in a de-identified manner as described in this Informed Consent form.\n\n4, I understand that my consent continues until and unless I withdraw my consent that can be done at any time by giving notice to the investigator. I understand that if I withdraw my consent I will not be able to continue to take part in the study.\n\n5, I understand that if I withdraw consent, the study researchers will no longer use or release information that identifies me in connection with the study unless it is needed to keep the scientific quality of the study. I understand that if I withdraw consent the study researchers may still use any study-related information about me that was collected before I withdrew consent.\n\n6, I have read and I understand the information provided in this Informed Consent Form. I have had the opportunity to ask questions and have had these questions answered satisfactorily.\n\n7, I have had time to consider the information provided in this Informed Consent Form to consider answers to my questions, and to consider whether I wish to take part in the study.\n\nIf you understand the statements above, and freely consent to participate in the study, press [Space] to begin the experiment.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
monash_logo = visual.ImageStim(
    win=win,
    name='monash_logo', units='pix', 
    image='Monash_University_logo.svg.png', mask=None, anchor='center',
    ori=0.0, pos=(0,win_pix_y*0.20), size=(win_pix_x*0.09,win_pix_y*0.09),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "instruction_1" ---
instruction_1_text = visual.TextStim(win=win, name='instruction_1_text',
    text='Welcome to our experiment!\n\nIn this experiment, you will see the following images, and will be asked to report how similar these images are to each other.  ',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
all_patches = visual.ImageStim(
    win=win,
    name='all_patches', units='norm', 
    image='instructions/all_patches.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.1), size=(0.7, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
space_press_continue = keyboard.Keyboard()
press_space_continue = visual.TextStim(win=win, name='press_space_continue',
    text='Press <space> to continue',
    font='Arial',
    units='norm', pos=(0, -0.6), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Esc_exit = visual.TextStim(win=win, name='Esc_exit',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "instruction_2" ---
instruction_text_2 = visual.TextStim(win=win, name='instruction_text_2',
    text='In each trial of this experiment, you are first asked to fixate on the cross appearing in the middle of the screen.\n\nThen, a small image will appear, which will be quickly masked.\n\nNOTE: The image will be presented for a slightly shorter time in the actual experiment.',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
space_press_continue_2 = keyboard.Keyboard()
press_space_continue_2 = visual.TextStim(win=win, name='press_space_continue_2',
    text='Press <space> to continue',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Esc_exit_2 = visual.TextStim(win=win, name='Esc_exit_2',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "instruction_3" ---
instruction_text_3 = visual.TextStim(win=win, name='instruction_text_3',
    text='Then, the cross will appear again, which is followed by a second image and the masks. \n\nNOTE: The image will be presented for a slightly shorter time in the actual experiment.',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
space_press_continue_3 = keyboard.Keyboard()
press_space_continue_3 = visual.TextStim(win=win, name='press_space_continue_3',
    text='Press <space> to continue',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Esc_exit_3 = visual.TextStim(win=win, name='Esc_exit_3',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "instruction_4" ---
instruction_text_4 = visual.TextStim(win=win, name='instruction_text_4',
    text='Finally, a response screen will appear. You are asked to rate how similar the two images you just saw are to each other, by choosing one of the numbers on the response screen.\n\n0 =>  most similar\n7 => most different',
    font='Arial',
    units='norm', pos=(0, 0.65), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
use_all_numbers = visual.TextStim(win=win, name='use_all_numbers',
    text='NOTE: Some image pairs might be more similar to each other than the other pairs. Therefore, please try to use numbers of the entire scale to express their varying similarity levels. ',
    font='Arial',
    units='norm', pos=(0, 0.3), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
response_screen_intr = visual.ImageStim(
    win=win,
    name='response_screen_intr', units='height', 
    image='instructions/response screen.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.15), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
space_press_continue_4 = keyboard.Keyboard()
space_continue_low = visual.TextStim(win=win, name='space_continue_low',
    text='Press <space> to continue',
    font='Arial',
    units='norm', pos=(0, -0.8), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
Esc_exit_4 = visual.TextStim(win=win, name='Esc_exit_4',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "instruction_5" ---
instruction_text_5 = visual.TextStim(win=win, name='instruction_text_5',
    text='After choosing, move your cursor back to the centre and click and hold the yellow square to continue.',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
response_screen_after = visual.ImageStim(
    win=win,
    name='response_screen_after', units='height', 
    image='instructions/response screen 2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.1), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
space_press_continue_5 = keyboard.Keyboard()
space_continue_low_2 = visual.TextStim(win=win, name='space_continue_low_2',
    text='Press <space> to continue',
    font='Arial',
    units='norm', pos=(0, -0.7), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Esc_exit_5 = visual.TextStim(win=win, name='Esc_exit_5',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "begin_practice" ---
prac_begin_text = visual.TextStim(win=win, name='prac_begin_text',
    text="The entire experiment will take approximately 30 minutes to complete.\n\nNow, let's become familiar with the experiment task with some practice",
    font='Arial',
    units='norm', pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
prac_begin_space = visual.TextStim(win=win, name='prac_begin_space',
    text='Press <space> to begin practice trials',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.07, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
space_press_continue_6 = keyboard.Keyboard()
Esc_exit_6 = visual.TextStim(win=win, name='Esc_exit_6',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "prac_patch_1" ---
fixation_cross = visual.ShapeStim(
    win=win, name='fixation_cross', vertices='cross',units='pix', 
    size=(30, 30),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
practice_patch_1 = visual.ImageStim(
    win=win,
    name='practice_patch_1', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(win_pix_y*0.75/3,win_pix_y*0.75/3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Esc_exit_13 = visual.TextStim(win=win, name='Esc_exit_13',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "mask" ---
mask_image = visual.ImageStim(
    win=win,
    name='mask_image', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(win_pix_y*0.75/3,win_pix_y*0.75/3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Esc_exit_14 = visual.TextStim(win=win, name='Esc_exit_14',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "prac_patch_2" ---
fixation_cross_3 = visual.ShapeStim(
    win=win, name='fixation_cross_3', vertices='cross',units='pix', 
    size=(30, 30),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
practice_patch_2 = visual.ImageStim(
    win=win,
    name='practice_patch_2', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(win_pix_y*0.75/3,win_pix_y*0.75/3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Esc_exit_12 = visual.TextStim(win=win, name='Esc_exit_12',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "mask" ---
mask_image = visual.ImageStim(
    win=win,
    name='mask_image', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(win_pix_y*0.75/3,win_pix_y*0.75/3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Esc_exit_14 = visual.TextStim(win=win, name='Esc_exit_14',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "prac_response" ---
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
response1disk_3 = visual.ImageStim(
    win=win,
    name='response1disk_3', units='pix', 
    image='response67.png', mask=None, anchor='center',
    ori=0, pos=[a,a], size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response5disk_3 = visual.ImageStim(
    win=win,
    name='response5disk_3', units='pix', 
    image='response23.png', mask=None, anchor='center',
    ori=0, pos=(-a,-a), size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response3disk_3 = visual.ImageStim(
    win=win,
    name='response3disk_3', units='pix', 
    image='response45.png', mask=None, anchor='center',
    ori=0, pos=[a,-a], size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response7disk_3 = visual.ImageStim(
    win=win,
    name='response7disk_3', units='pix', 
    image='response01.png', mask=None, anchor='center',
    ori=0, pos=(-a,a), size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
text = visual.TextStim(win=win, name='text',
    text='Please rate how similar the two images you just saw are. \n\nPlease click and hold to indicate your choice.',
    font='Arial',
    units='norm', pos=(0, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
most_similar_3 = visual.TextStim(win=win, name='most_similar_3',
    text='Very similar',
    font='Arial',
    units='norm', pos=(-0.4, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
most_different_3 = visual.TextStim(win=win, name='most_different_3',
    text='Very different',
    font='Arial',
    units='norm', pos=(0.4, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
Esc_exit_7 = visual.TextStim(win=win, name='Esc_exit_7',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# --- Initialize components for Routine "resposne_feedback" ---
text_55 = visual.TextStim(win=win, name='text_55',
    text='',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_56 = visual.TextStim(win=win, name='text_56',
    text='',
    font='Arial',
    units='norm', pos=(0, -0.2), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Esc_exit_8 = visual.TextStim(win=win, name='Esc_exit_8',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "prac_correct_mouse" ---
mouse_12 = event.Mouse(win=win)
x, y = [None, None]
mouse_12.mouseClock = core.Clock()
response1disk_4 = visual.ImageStim(
    win=win,
    name='response1disk_4', units='pix', 
    image='response67.png', mask=None, anchor='center',
    ori=0, pos=[a,a], size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk_4 = visual.ImageStim(
    win=win,
    name='response3disk_4', units='pix', 
    image='response45.png', mask=None, anchor='center',
    ori=0, pos=[a,-a], size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response5disk_4 = visual.ImageStim(
    win=win,
    name='response5disk_4', units='pix', 
    image='response23.png', mask=None, anchor='center',
    ori=0, pos=(-a,-a), size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response7disk_4 = visual.ImageStim(
    win=win,
    name='response7disk_4', units='pix', 
    image='response01.png', mask=None, anchor='center',
    ori=0, pos=(-a,a), size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
text_52 = visual.TextStim(win=win, name='text_52',
    text='Please click and hold the yellow square in the middle of the response numbers to continue',
    font='Arial',
    units='norm', pos=(0, -0.7), height=0.07, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
center_square_2 = visual.Rect(
    win=win, name='center_square_2',units='pix', 
    width=(win_pix_y*0.75/20,win_pix_y*0.75/20)[0], height=(win_pix_y*0.75/20,win_pix_y*0.75/20)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='yellow', fillColor='yellow',
    opacity=None, depth=-6.0, interpolate=True)
most_similar_4 = visual.TextStim(win=win, name='most_similar_4',
    text='Very similar',
    font='Arial',
    units='norm', pos=(-0.4, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
most_different_4 = visual.TextStim(win=win, name='most_different_4',
    text='Very different',
    font='Arial',
    units='norm', pos=(0.4, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
Esc_exit_9 = visual.TextStim(win=win, name='Esc_exit_9',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# --- Initialize components for Routine "begin_task" ---
mouse_1 = event.Mouse(win=win)
x, y = [None, None]
mouse_1.mouseClock = core.Clock()
begin_mouse_center = visual.TextStim(win=win, name='begin_mouse_center',
    text='This is the end of the practice trials. Press <space> to begin the main experiment.',
    font='Arial',
    units='norm', pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Esc_exit_15 = visual.TextStim(win=win, name='Esc_exit_15',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
space_press_continue_7 = keyboard.Keyboard()

# --- Initialize components for Routine "patch_1" ---
fixation_cross_1 = visual.ShapeStim(
    win=win, name='fixation_cross_1', vertices='cross',units='pix', 
    size=(30, 30),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
first_patch = visual.ImageStim(
    win=win,
    name='first_patch', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(win_pix_y*0.75/3,win_pix_y*0.75/3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Esc_exit_16 = visual.TextStim(win=win, name='Esc_exit_16',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "mask" ---
mask_image = visual.ImageStim(
    win=win,
    name='mask_image', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(win_pix_y*0.75/3,win_pix_y*0.75/3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Esc_exit_14 = visual.TextStim(win=win, name='Esc_exit_14',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "patch_2" ---
fixation_cross_2 = visual.ShapeStim(
    win=win, name='fixation_cross_2', vertices='cross',units='pix', 
    size=(30, 30),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
second_patch = visual.ImageStim(
    win=win,
    name='second_patch', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(win_pix_y*0.75/3,win_pix_y*0.75/3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Esc_exit_17 = visual.TextStim(win=win, name='Esc_exit_17',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "mask" ---
mask_image = visual.ImageStim(
    win=win,
    name='mask_image', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(win_pix_y*0.75/3,win_pix_y*0.75/3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Esc_exit_14 = visual.TextStim(win=win, name='Esc_exit_14',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "response" ---
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
response1disk = visual.ImageStim(
    win=win,
    name='response1disk', units='pix', 
    image='response67.png', mask=None, anchor='center',
    ori=0, pos=[a,a], size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response3disk = visual.ImageStim(
    win=win,
    name='response3disk', units='pix', 
    image='response45.png', mask=None, anchor='center',
    ori=0, pos=[a,-a], size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response5disk = visual.ImageStim(
    win=win,
    name='response5disk', units='pix', 
    image='response23.png', mask=None, anchor='center',
    ori=0, pos=(-a,-a), size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response7disk = visual.ImageStim(
    win=win,
    name='response7disk', units='pix', 
    image='response01.png', mask=None, anchor='center',
    ori=0, pos=(-a,a), size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
text_23 = visual.TextStim(win=win, name='text_23',
    text='Please rate how similar the two images you just saw are. \n\nPlease click and hold to indicate your choice.',
    font='Arial',
    units='norm', pos=(0, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
most_similar = visual.TextStim(win=win, name='most_similar',
    text='Very similar',
    font='Arial',
    units='norm', pos=(-0.4, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
most_different = visual.TextStim(win=win, name='most_different',
    text='Very different',
    font='Arial',
    units='norm', pos=(0.4, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
Esc_exit_10 = visual.TextStim(win=win, name='Esc_exit_10',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# --- Initialize components for Routine "correct_mouse" ---
mouse_11 = event.Mouse(win=win)
x, y = [None, None]
mouse_11.mouseClock = core.Clock()
response1disk_2 = visual.ImageStim(
    win=win,
    name='response1disk_2', units='pix', 
    image='response67.png', mask=None, anchor='center',
    ori=0, pos=[a,a], size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk_2 = visual.ImageStim(
    win=win,
    name='response3disk_2', units='pix', 
    image='response45.png', mask=None, anchor='center',
    ori=0, pos=[a,-a], size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response5disk_2 = visual.ImageStim(
    win=win,
    name='response5disk_2', units='pix', 
    image='response23.png', mask=None, anchor='center',
    ori=0, pos=(-a,-a), size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response7disk_2 = visual.ImageStim(
    win=win,
    name='response7disk_2', units='pix', 
    image='response01.png', mask=None, anchor='center',
    ori=0, pos=(-a,a), size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
text_51 = visual.TextStim(win=win, name='text_51',
    text='Please click and hold the yellow square in the middle of the response numbers to continue',
    font='Arial',
    units='norm', pos=(0, -0.6), height=0.07, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
center_square = visual.Rect(
    win=win, name='center_square',units='pix', 
    width=(win_pix_y*0.75/20,win_pix_y*0.75/20)[0], height=(win_pix_y*0.75/20,win_pix_y*0.75/20)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='yellow', fillColor='yellow',
    opacity=None, depth=-6.0, interpolate=True)
most_similar_2 = visual.TextStim(win=win, name='most_similar_2',
    text='Very similar',
    font='Arial',
    units='norm', pos=(-0.4, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
most_different_2 = visual.TextStim(win=win, name='most_different_2',
    text='Very different',
    font='Arial',
    units='norm', pos=(0.4, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
trial_text_2 = visual.TextStim(win=win, name='trial_text_2',
    text='',
    font='Arial',
    units='norm', pos=(0, -0.8), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
Esc_exit_11 = visual.TextStim(win=win, name='Esc_exit_11',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "patch_2" ---
fixation_cross_2 = visual.ShapeStim(
    win=win, name='fixation_cross_2', vertices='cross',units='pix', 
    size=(30, 30),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
second_patch = visual.ImageStim(
    win=win,
    name='second_patch', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(win_pix_y*0.75/3,win_pix_y*0.75/3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Esc_exit_17 = visual.TextStim(win=win, name='Esc_exit_17',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "mask" ---
mask_image = visual.ImageStim(
    win=win,
    name='mask_image', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(win_pix_y*0.75/3,win_pix_y*0.75/3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Esc_exit_14 = visual.TextStim(win=win, name='Esc_exit_14',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "patch_1" ---
fixation_cross_1 = visual.ShapeStim(
    win=win, name='fixation_cross_1', vertices='cross',units='pix', 
    size=(30, 30),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
first_patch = visual.ImageStim(
    win=win,
    name='first_patch', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(win_pix_y*0.75/3,win_pix_y*0.75/3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Esc_exit_16 = visual.TextStim(win=win, name='Esc_exit_16',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "mask" ---
mask_image = visual.ImageStim(
    win=win,
    name='mask_image', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(win_pix_y*0.75/3,win_pix_y*0.75/3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Esc_exit_14 = visual.TextStim(win=win, name='Esc_exit_14',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "response_2" ---
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
response1disk_5 = visual.ImageStim(
    win=win,
    name='response1disk_5', units='pix', 
    image='response67.png', mask=None, anchor='center',
    ori=0, pos=[a,a], size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response3disk_5 = visual.ImageStim(
    win=win,
    name='response3disk_5', units='pix', 
    image='response45.png', mask=None, anchor='center',
    ori=0, pos=[a,-a], size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response5disk_5 = visual.ImageStim(
    win=win,
    name='response5disk_5', units='pix', 
    image='response23.png', mask=None, anchor='center',
    ori=0, pos=(-a,-a), size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response7disk_5 = visual.ImageStim(
    win=win,
    name='response7disk_5', units='pix', 
    image='response01.png', mask=None, anchor='center',
    ori=0, pos=(-a,a), size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
text_24 = visual.TextStim(win=win, name='text_24',
    text='Please rate how similar the two images you just saw are. \n\nPlease click and hold to indicate your choice.',
    font='Arial',
    units='norm', pos=(0, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
most_similar_5 = visual.TextStim(win=win, name='most_similar_5',
    text='Very similar',
    font='Arial',
    units='norm', pos=(-0.4, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
most_different_5 = visual.TextStim(win=win, name='most_different_5',
    text='Very different',
    font='Arial',
    units='norm', pos=(0.4, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
Esc_exit_18 = visual.TextStim(win=win, name='Esc_exit_18',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# --- Initialize components for Routine "correct_mouse" ---
mouse_11 = event.Mouse(win=win)
x, y = [None, None]
mouse_11.mouseClock = core.Clock()
response1disk_2 = visual.ImageStim(
    win=win,
    name='response1disk_2', units='pix', 
    image='response67.png', mask=None, anchor='center',
    ori=0, pos=[a,a], size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk_2 = visual.ImageStim(
    win=win,
    name='response3disk_2', units='pix', 
    image='response45.png', mask=None, anchor='center',
    ori=0, pos=[a,-a], size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response5disk_2 = visual.ImageStim(
    win=win,
    name='response5disk_2', units='pix', 
    image='response23.png', mask=None, anchor='center',
    ori=0, pos=(-a,-a), size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response7disk_2 = visual.ImageStim(
    win=win,
    name='response7disk_2', units='pix', 
    image='response01.png', mask=None, anchor='center',
    ori=0, pos=(-a,a), size=[b,b],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
text_51 = visual.TextStim(win=win, name='text_51',
    text='Please click and hold the yellow square in the middle of the response numbers to continue',
    font='Arial',
    units='norm', pos=(0, -0.6), height=0.07, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
center_square = visual.Rect(
    win=win, name='center_square',units='pix', 
    width=(win_pix_y*0.75/20,win_pix_y*0.75/20)[0], height=(win_pix_y*0.75/20,win_pix_y*0.75/20)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='yellow', fillColor='yellow',
    opacity=None, depth=-6.0, interpolate=True)
most_similar_2 = visual.TextStim(win=win, name='most_similar_2',
    text='Very similar',
    font='Arial',
    units='norm', pos=(-0.4, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
most_different_2 = visual.TextStim(win=win, name='most_different_2',
    text='Very different',
    font='Arial',
    units='norm', pos=(0.4, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
trial_text_2 = visual.TextStim(win=win, name='trial_text_2',
    text='',
    font='Arial',
    units='norm', pos=(0, -0.8), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
Esc_exit_11 = visual.TextStim(win=win, name='Esc_exit_11',
    text='Press <Esc> to exit experiment',
    font='Arial',
    units='norm', pos=(0.75, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='aqua', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "end_of_experiment" ---
thank_you = visual.TextStim(win=win, name='thank_you',
    text='Thank you for your participation! Your responses have been recorded.\n\nPress <space> to exit experiment',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
space_exit = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Startup" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
StartupComponents = []
for thisComponent in StartupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Startup" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Startup" ---
for thisComponent in StartupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Startup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "StimSetUp" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
StimSetUpComponents = []
for thisComponent in StimSetUpComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "StimSetUp" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StimSetUpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "StimSetUp" ---
for thisComponent in StimSetUpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "StimSetUp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Consent" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
ConsentComponents = [consent_text, monash_logo, key_resp]
for thisComponent in ConsentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Consent" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *consent_text* updates
    if consent_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consent_text.frameNStart = frameN  # exact frame index
        consent_text.tStart = t  # local t and not account for scr refresh
        consent_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consent_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'consent_text.started')
        consent_text.setAutoDraw(True)
    
    # *monash_logo* updates
    if monash_logo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        monash_logo.frameNStart = frameN  # exact frame index
        monash_logo.tStart = t  # local t and not account for scr refresh
        monash_logo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(monash_logo, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'monash_logo.started')
        monash_logo.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ConsentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Consent" ---
for thisComponent in ConsentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "Consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_press_continue.keys = []
space_press_continue.rt = []
_space_press_continue_allKeys = []
# keep track of which components have finished
instruction_1Components = [instruction_1_text, all_patches, space_press_continue, press_space_continue, Esc_exit]
for thisComponent in instruction_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_1_text* updates
    if instruction_1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_1_text.frameNStart = frameN  # exact frame index
        instruction_1_text.tStart = t  # local t and not account for scr refresh
        instruction_1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_1_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruction_1_text.started')
        instruction_1_text.setAutoDraw(True)
    
    # *all_patches* updates
    if all_patches.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        all_patches.frameNStart = frameN  # exact frame index
        all_patches.tStart = t  # local t and not account for scr refresh
        all_patches.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(all_patches, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'all_patches.started')
        all_patches.setAutoDraw(True)
    
    # *space_press_continue* updates
    waitOnFlip = False
    if space_press_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_press_continue.frameNStart = frameN  # exact frame index
        space_press_continue.tStart = t  # local t and not account for scr refresh
        space_press_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_press_continue, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_press_continue.started')
        space_press_continue.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_press_continue.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_press_continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_press_continue.status == STARTED and not waitOnFlip:
        theseKeys = space_press_continue.getKeys(keyList=['space'], waitRelease=False)
        _space_press_continue_allKeys.extend(theseKeys)
        if len(_space_press_continue_allKeys):
            space_press_continue.keys = _space_press_continue_allKeys[-1].name  # just the last key pressed
            space_press_continue.rt = _space_press_continue_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *press_space_continue* updates
    if press_space_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        press_space_continue.frameNStart = frameN  # exact frame index
        press_space_continue.tStart = t  # local t and not account for scr refresh
        press_space_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(press_space_continue, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'press_space_continue.started')
        press_space_continue.setAutoDraw(True)
    
    # *Esc_exit* updates
    if Esc_exit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Esc_exit.frameNStart = frameN  # exact frame index
        Esc_exit.tStart = t  # local t and not account for scr refresh
        Esc_exit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Esc_exit, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Esc_exit.started')
        Esc_exit.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_1" ---
for thisComponent in instruction_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space_press_continue.keys in ['', [], None]:  # No response was made
    space_press_continue.keys = None
thisExp.addData('space_press_continue.keys',space_press_continue.keys)
if space_press_continue.keys != None:  # we had a response
    thisExp.addData('space_press_continue.rt', space_press_continue.rt)
thisExp.nextEntry()
# the Routine "instruction_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
patch_1_movie = visual.MovieStim3(
    win=win, name='patch_1_movie', units='norm',
    noAudio = False,
    filename='instructions/instruction_patch_1.mp4',
    ori=0.0, pos=(0, -0.1), opacity=1.0,
    loop=True, anchor='center',
    size=(0.5,0.68),
    depth=-1.0,
    )
space_press_continue_2.keys = []
space_press_continue_2.rt = []
_space_press_continue_2_allKeys = []
# keep track of which components have finished
instruction_2Components = [instruction_text_2, patch_1_movie, space_press_continue_2, press_space_continue_2, Esc_exit_2]
for thisComponent in instruction_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_text_2* updates
    if instruction_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_text_2.frameNStart = frameN  # exact frame index
        instruction_text_2.tStart = t  # local t and not account for scr refresh
        instruction_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_text_2, 'tStartRefresh')  # time at next scr refresh
        instruction_text_2.setAutoDraw(True)
    
    # *patch_1_movie* updates
    if patch_1_movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        patch_1_movie.frameNStart = frameN  # exact frame index
        patch_1_movie.tStart = t  # local t and not account for scr refresh
        patch_1_movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(patch_1_movie, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'patch_1_movie.started')
        patch_1_movie.setAutoDraw(True)
    
    # *space_press_continue_2* updates
    waitOnFlip = False
    if space_press_continue_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_press_continue_2.frameNStart = frameN  # exact frame index
        space_press_continue_2.tStart = t  # local t and not account for scr refresh
        space_press_continue_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_press_continue_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_press_continue_2.started')
        space_press_continue_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_press_continue_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_press_continue_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_press_continue_2.status == STARTED and not waitOnFlip:
        theseKeys = space_press_continue_2.getKeys(keyList=['space'], waitRelease=False)
        _space_press_continue_2_allKeys.extend(theseKeys)
        if len(_space_press_continue_2_allKeys):
            space_press_continue_2.keys = _space_press_continue_2_allKeys[-1].name  # just the last key pressed
            space_press_continue_2.rt = _space_press_continue_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *press_space_continue_2* updates
    if press_space_continue_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        press_space_continue_2.frameNStart = frameN  # exact frame index
        press_space_continue_2.tStart = t  # local t and not account for scr refresh
        press_space_continue_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(press_space_continue_2, 'tStartRefresh')  # time at next scr refresh
        press_space_continue_2.setAutoDraw(True)
    
    # *Esc_exit_2* updates
    if Esc_exit_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Esc_exit_2.frameNStart = frameN  # exact frame index
        Esc_exit_2.tStart = t  # local t and not account for scr refresh
        Esc_exit_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Esc_exit_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Esc_exit_2.started')
        Esc_exit_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_2" ---
for thisComponent in instruction_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
patch_1_movie.stop()
# check responses
if space_press_continue_2.keys in ['', [], None]:  # No response was made
    space_press_continue_2.keys = None
thisExp.addData('space_press_continue_2.keys',space_press_continue_2.keys)
if space_press_continue_2.keys != None:  # we had a response
    thisExp.addData('space_press_continue_2.rt', space_press_continue_2.rt)
thisExp.nextEntry()
# the Routine "instruction_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
patch_2_movie = visual.MovieStim3(
    win=win, name='patch_2_movie', units='norm',
    noAudio = False,
    filename='instructions/instruction_patch_2.mp4',
    ori=0.0, pos=(0, -0.1), opacity=1.0,
    loop=True, anchor='center',
    size=(0.5,0.68),
    depth=-1.0,
    )
space_press_continue_3.keys = []
space_press_continue_3.rt = []
_space_press_continue_3_allKeys = []
# keep track of which components have finished
instruction_3Components = [instruction_text_3, patch_2_movie, space_press_continue_3, press_space_continue_3, Esc_exit_3]
for thisComponent in instruction_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_text_3* updates
    if instruction_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_text_3.frameNStart = frameN  # exact frame index
        instruction_text_3.tStart = t  # local t and not account for scr refresh
        instruction_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_text_3, 'tStartRefresh')  # time at next scr refresh
        instruction_text_3.setAutoDraw(True)
    
    # *patch_2_movie* updates
    if patch_2_movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        patch_2_movie.frameNStart = frameN  # exact frame index
        patch_2_movie.tStart = t  # local t and not account for scr refresh
        patch_2_movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(patch_2_movie, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'patch_2_movie.started')
        patch_2_movie.setAutoDraw(True)
    
    # *space_press_continue_3* updates
    waitOnFlip = False
    if space_press_continue_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_press_continue_3.frameNStart = frameN  # exact frame index
        space_press_continue_3.tStart = t  # local t and not account for scr refresh
        space_press_continue_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_press_continue_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_press_continue_3.started')
        space_press_continue_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_press_continue_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_press_continue_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_press_continue_3.status == STARTED and not waitOnFlip:
        theseKeys = space_press_continue_3.getKeys(keyList=['space'], waitRelease=False)
        _space_press_continue_3_allKeys.extend(theseKeys)
        if len(_space_press_continue_3_allKeys):
            space_press_continue_3.keys = _space_press_continue_3_allKeys[-1].name  # just the last key pressed
            space_press_continue_3.rt = _space_press_continue_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *press_space_continue_3* updates
    if press_space_continue_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        press_space_continue_3.frameNStart = frameN  # exact frame index
        press_space_continue_3.tStart = t  # local t and not account for scr refresh
        press_space_continue_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(press_space_continue_3, 'tStartRefresh')  # time at next scr refresh
        press_space_continue_3.setAutoDraw(True)
    
    # *Esc_exit_3* updates
    if Esc_exit_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Esc_exit_3.frameNStart = frameN  # exact frame index
        Esc_exit_3.tStart = t  # local t and not account for scr refresh
        Esc_exit_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Esc_exit_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Esc_exit_3.started')
        Esc_exit_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_3" ---
for thisComponent in instruction_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
patch_2_movie.stop()
# check responses
if space_press_continue_3.keys in ['', [], None]:  # No response was made
    space_press_continue_3.keys = None
thisExp.addData('space_press_continue_3.keys',space_press_continue_3.keys)
if space_press_continue_3.keys != None:  # we had a response
    thisExp.addData('space_press_continue_3.rt', space_press_continue_3.rt)
thisExp.nextEntry()
# the Routine "instruction_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction_4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_press_continue_4.keys = []
space_press_continue_4.rt = []
_space_press_continue_4_allKeys = []
# keep track of which components have finished
instruction_4Components = [instruction_text_4, use_all_numbers, response_screen_intr, space_press_continue_4, space_continue_low, Esc_exit_4]
for thisComponent in instruction_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction_4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_text_4* updates
    if instruction_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_text_4.frameNStart = frameN  # exact frame index
        instruction_text_4.tStart = t  # local t and not account for scr refresh
        instruction_text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruction_text_4.started')
        instruction_text_4.setAutoDraw(True)
    
    # *use_all_numbers* updates
    if use_all_numbers.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        use_all_numbers.frameNStart = frameN  # exact frame index
        use_all_numbers.tStart = t  # local t and not account for scr refresh
        use_all_numbers.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(use_all_numbers, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'use_all_numbers.started')
        use_all_numbers.setAutoDraw(True)
    
    # *response_screen_intr* updates
    if response_screen_intr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        response_screen_intr.frameNStart = frameN  # exact frame index
        response_screen_intr.tStart = t  # local t and not account for scr refresh
        response_screen_intr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(response_screen_intr, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'response_screen_intr.started')
        response_screen_intr.setAutoDraw(True)
    
    # *space_press_continue_4* updates
    waitOnFlip = False
    if space_press_continue_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_press_continue_4.frameNStart = frameN  # exact frame index
        space_press_continue_4.tStart = t  # local t and not account for scr refresh
        space_press_continue_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_press_continue_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_press_continue_4.started')
        space_press_continue_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_press_continue_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_press_continue_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_press_continue_4.status == STARTED and not waitOnFlip:
        theseKeys = space_press_continue_4.getKeys(keyList=['space'], waitRelease=False)
        _space_press_continue_4_allKeys.extend(theseKeys)
        if len(_space_press_continue_4_allKeys):
            space_press_continue_4.keys = _space_press_continue_4_allKeys[-1].name  # just the last key pressed
            space_press_continue_4.rt = _space_press_continue_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_continue_low* updates
    if space_continue_low.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_continue_low.frameNStart = frameN  # exact frame index
        space_continue_low.tStart = t  # local t and not account for scr refresh
        space_continue_low.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_continue_low, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_continue_low.started')
        space_continue_low.setAutoDraw(True)
    
    # *Esc_exit_4* updates
    if Esc_exit_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Esc_exit_4.frameNStart = frameN  # exact frame index
        Esc_exit_4.tStart = t  # local t and not account for scr refresh
        Esc_exit_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Esc_exit_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Esc_exit_4.started')
        Esc_exit_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_4" ---
for thisComponent in instruction_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space_press_continue_4.keys in ['', [], None]:  # No response was made
    space_press_continue_4.keys = None
thisExp.addData('space_press_continue_4.keys',space_press_continue_4.keys)
if space_press_continue_4.keys != None:  # we had a response
    thisExp.addData('space_press_continue_4.rt', space_press_continue_4.rt)
thisExp.nextEntry()
# the Routine "instruction_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction_5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_press_continue_5.keys = []
space_press_continue_5.rt = []
_space_press_continue_5_allKeys = []
# keep track of which components have finished
instruction_5Components = [instruction_text_5, response_screen_after, space_press_continue_5, space_continue_low_2, Esc_exit_5]
for thisComponent in instruction_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction_5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_text_5* updates
    if instruction_text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_text_5.frameNStart = frameN  # exact frame index
        instruction_text_5.tStart = t  # local t and not account for scr refresh
        instruction_text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_text_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruction_text_5.started')
        instruction_text_5.setAutoDraw(True)
    
    # *response_screen_after* updates
    if response_screen_after.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        response_screen_after.frameNStart = frameN  # exact frame index
        response_screen_after.tStart = t  # local t and not account for scr refresh
        response_screen_after.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(response_screen_after, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'response_screen_after.started')
        response_screen_after.setAutoDraw(True)
    
    # *space_press_continue_5* updates
    waitOnFlip = False
    if space_press_continue_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_press_continue_5.frameNStart = frameN  # exact frame index
        space_press_continue_5.tStart = t  # local t and not account for scr refresh
        space_press_continue_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_press_continue_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_press_continue_5.started')
        space_press_continue_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_press_continue_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_press_continue_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_press_continue_5.status == STARTED and not waitOnFlip:
        theseKeys = space_press_continue_5.getKeys(keyList=['space'], waitRelease=False)
        _space_press_continue_5_allKeys.extend(theseKeys)
        if len(_space_press_continue_5_allKeys):
            space_press_continue_5.keys = _space_press_continue_5_allKeys[-1].name  # just the last key pressed
            space_press_continue_5.rt = _space_press_continue_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_continue_low_2* updates
    if space_continue_low_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_continue_low_2.frameNStart = frameN  # exact frame index
        space_continue_low_2.tStart = t  # local t and not account for scr refresh
        space_continue_low_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_continue_low_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_continue_low_2.started')
        space_continue_low_2.setAutoDraw(True)
    
    # *Esc_exit_5* updates
    if Esc_exit_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Esc_exit_5.frameNStart = frameN  # exact frame index
        Esc_exit_5.tStart = t  # local t and not account for scr refresh
        Esc_exit_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Esc_exit_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Esc_exit_5.started')
        Esc_exit_5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_5" ---
for thisComponent in instruction_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space_press_continue_5.keys in ['', [], None]:  # No response was made
    space_press_continue_5.keys = None
thisExp.addData('space_press_continue_5.keys',space_press_continue_5.keys)
if space_press_continue_5.keys != None:  # we had a response
    thisExp.addData('space_press_continue_5.rt', space_press_continue_5.rt)
thisExp.nextEntry()
# the Routine "instruction_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "begin_practice" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_press_continue_6.keys = []
space_press_continue_6.rt = []
_space_press_continue_6_allKeys = []
# keep track of which components have finished
begin_practiceComponents = [prac_begin_text, prac_begin_space, space_press_continue_6, Esc_exit_6]
for thisComponent in begin_practiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "begin_practice" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prac_begin_text* updates
    if prac_begin_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_begin_text.frameNStart = frameN  # exact frame index
        prac_begin_text.tStart = t  # local t and not account for scr refresh
        prac_begin_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_begin_text, 'tStartRefresh')  # time at next scr refresh
        prac_begin_text.setAutoDraw(True)
    
    # *prac_begin_space* updates
    if prac_begin_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_begin_space.frameNStart = frameN  # exact frame index
        prac_begin_space.tStart = t  # local t and not account for scr refresh
        prac_begin_space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_begin_space, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'prac_begin_space.started')
        prac_begin_space.setAutoDraw(True)
    
    # *space_press_continue_6* updates
    waitOnFlip = False
    if space_press_continue_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_press_continue_6.frameNStart = frameN  # exact frame index
        space_press_continue_6.tStart = t  # local t and not account for scr refresh
        space_press_continue_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_press_continue_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_press_continue_6.started')
        space_press_continue_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_press_continue_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_press_continue_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_press_continue_6.status == STARTED and not waitOnFlip:
        theseKeys = space_press_continue_6.getKeys(keyList=['space'], waitRelease=False)
        _space_press_continue_6_allKeys.extend(theseKeys)
        if len(_space_press_continue_6_allKeys):
            space_press_continue_6.keys = _space_press_continue_6_allKeys[-1].name  # just the last key pressed
            space_press_continue_6.rt = _space_press_continue_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Esc_exit_6* updates
    if Esc_exit_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Esc_exit_6.frameNStart = frameN  # exact frame index
        Esc_exit_6.tStart = t  # local t and not account for scr refresh
        Esc_exit_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Esc_exit_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Esc_exit_6.started')
        Esc_exit_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in begin_practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "begin_practice" ---
for thisComponent in begin_practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space_press_continue_6.keys in ['', [], None]:  # No response was made
    space_press_continue_6.keys = None
thisExp.addData('space_press_continue_6.keys',space_press_continue_6.keys)
if space_press_continue_6.keys != None:  # we had a response
    thisExp.addData('space_press_continue_6.rt', space_press_continue_6.rt)
thisExp.nextEntry()
# the Routine "begin_practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('info_exp_prac_cond.xlsx', selection='0:3'),
    seed=None, name='prac_loop')
thisExp.addLoop(prac_loop)  # add the loop to the experiment
thisPrac_loop = prac_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_loop.rgb)
if thisPrac_loop != None:
    for paramName in thisPrac_loop:
        exec('{} = thisPrac_loop[paramName]'.format(paramName))

for thisPrac_loop in prac_loop:
    currentLoop = prac_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_loop.rgb)
    if thisPrac_loop != None:
        for paramName in thisPrac_loop:
            exec('{} = thisPrac_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "prac_patch_1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    practice_patch_1.setImage(Patch_1_name)
    # Run 'Begin Routine' code from disable_mouse_3
    event.Mouse(visible=False)
    # keep track of which components have finished
    prac_patch_1Components = [fixation_cross, practice_patch_1, Esc_exit_13]
    for thisComponent in prac_patch_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_patch_1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.tStart = t  # local t and not account for scr refresh
            fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(True)
        if fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross.tStartRefresh + fixation_cross_duration-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross.tStop = t  # not accounting for scr refresh
                fixation_cross.frameNStop = frameN  # exact frame index
                fixation_cross.setAutoDraw(False)
        
        # *practice_patch_1* updates
        if practice_patch_1.status == NOT_STARTED and tThisFlip >= fixation_cross_duration-frameTolerance:
            # keep track of start time/frame for later
            practice_patch_1.frameNStart = frameN  # exact frame index
            practice_patch_1.tStart = t  # local t and not account for scr refresh
            practice_patch_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_patch_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_patch_1.started')
            practice_patch_1.setAutoDraw(True)
        if practice_patch_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_patch_1.tStartRefresh + image_duration-frameTolerance:
                # keep track of stop time/frame for later
                practice_patch_1.tStop = t  # not accounting for scr refresh
                practice_patch_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_patch_1.stopped')
                practice_patch_1.setAutoDraw(False)
        
        # *Esc_exit_13* updates
        if Esc_exit_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Esc_exit_13.frameNStart = frameN  # exact frame index
            Esc_exit_13.tStart = t  # local t and not account for scr refresh
            Esc_exit_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Esc_exit_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Esc_exit_13.started')
            Esc_exit_13.setAutoDraw(True)
        if Esc_exit_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Esc_exit_13.tStartRefresh + exit_message_duration-frameTolerance:
                # keep track of stop time/frame for later
                Esc_exit_13.tStop = t  # not accounting for scr refresh
                Esc_exit_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Esc_exit_13.stopped')
                Esc_exit_13.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_patch_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_patch_1" ---
    for thisComponent in prac_patch_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "prac_patch_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    prac_mask_loop_1 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('masks_cond.xlsx', selection='0:5'),
        seed=None, name='prac_mask_loop_1')
    thisExp.addLoop(prac_mask_loop_1)  # add the loop to the experiment
    thisPrac_mask_loop_1 = prac_mask_loop_1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_mask_loop_1.rgb)
    if thisPrac_mask_loop_1 != None:
        for paramName in thisPrac_mask_loop_1:
            exec('{} = thisPrac_mask_loop_1[paramName]'.format(paramName))
    
    for thisPrac_mask_loop_1 in prac_mask_loop_1:
        currentLoop = prac_mask_loop_1
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_mask_loop_1.rgb)
        if thisPrac_mask_loop_1 != None:
            for paramName in thisPrac_mask_loop_1:
                exec('{} = thisPrac_mask_loop_1[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mask" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        mask_image.setImage(mask_name)
        # keep track of which components have finished
        maskComponents = [mask_image, Esc_exit_14]
        for thisComponent in maskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mask" ---
        while continueRoutine and routineTimer.getTime() < 0.06:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *mask_image* updates
            if mask_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mask_image.frameNStart = frameN  # exact frame index
                mask_image.tStart = t  # local t and not account for scr refresh
                mask_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask_image, 'tStartRefresh')  # time at next scr refresh
                mask_image.setAutoDraw(True)
            if mask_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask_image.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    mask_image.tStop = t  # not accounting for scr refresh
                    mask_image.frameNStop = frameN  # exact frame index
                    mask_image.setAutoDraw(False)
            
            # *Esc_exit_14* updates
            if Esc_exit_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Esc_exit_14.frameNStart = frameN  # exact frame index
                Esc_exit_14.tStart = t  # local t and not account for scr refresh
                Esc_exit_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Esc_exit_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Esc_exit_14.started')
                Esc_exit_14.setAutoDraw(True)
            if Esc_exit_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Esc_exit_14.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    Esc_exit_14.tStop = t  # not accounting for scr refresh
                    Esc_exit_14.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Esc_exit_14.stopped')
                    Esc_exit_14.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in maskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mask" ---
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.060000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'prac_mask_loop_1'
    
    
    # --- Prepare to start Routine "prac_patch_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    practice_patch_2.setImage(Patch_2_name)
    # keep track of which components have finished
    prac_patch_2Components = [fixation_cross_3, practice_patch_2, Esc_exit_12]
    for thisComponent in prac_patch_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_patch_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross_3* updates
        if fixation_cross_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross_3.frameNStart = frameN  # exact frame index
            fixation_cross_3.tStart = t  # local t and not account for scr refresh
            fixation_cross_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross_3, 'tStartRefresh')  # time at next scr refresh
            fixation_cross_3.setAutoDraw(True)
        if fixation_cross_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross_3.tStartRefresh + fixation_cross_duration-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross_3.tStop = t  # not accounting for scr refresh
                fixation_cross_3.frameNStop = frameN  # exact frame index
                fixation_cross_3.setAutoDraw(False)
        
        # *practice_patch_2* updates
        if practice_patch_2.status == NOT_STARTED and tThisFlip >= fixation_cross_duration-frameTolerance:
            # keep track of start time/frame for later
            practice_patch_2.frameNStart = frameN  # exact frame index
            practice_patch_2.tStart = t  # local t and not account for scr refresh
            practice_patch_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_patch_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_patch_2.started')
            practice_patch_2.setAutoDraw(True)
        if practice_patch_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_patch_2.tStartRefresh + image_duration-frameTolerance:
                # keep track of stop time/frame for later
                practice_patch_2.tStop = t  # not accounting for scr refresh
                practice_patch_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_patch_2.stopped')
                practice_patch_2.setAutoDraw(False)
        
        # *Esc_exit_12* updates
        if Esc_exit_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Esc_exit_12.frameNStart = frameN  # exact frame index
            Esc_exit_12.tStart = t  # local t and not account for scr refresh
            Esc_exit_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Esc_exit_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Esc_exit_12.started')
            Esc_exit_12.setAutoDraw(True)
        if Esc_exit_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Esc_exit_12.tStartRefresh + exit_message_duration-frameTolerance:
                # keep track of stop time/frame for later
                Esc_exit_12.tStop = t  # not accounting for scr refresh
                Esc_exit_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Esc_exit_12.stopped')
                Esc_exit_12.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_patch_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_patch_2" ---
    for thisComponent in prac_patch_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "prac_patch_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    prac_mask_loop_2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('masks_cond.xlsx', selection='0:5'),
        seed=None, name='prac_mask_loop_2')
    thisExp.addLoop(prac_mask_loop_2)  # add the loop to the experiment
    thisPrac_mask_loop_2 = prac_mask_loop_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_mask_loop_2.rgb)
    if thisPrac_mask_loop_2 != None:
        for paramName in thisPrac_mask_loop_2:
            exec('{} = thisPrac_mask_loop_2[paramName]'.format(paramName))
    
    for thisPrac_mask_loop_2 in prac_mask_loop_2:
        currentLoop = prac_mask_loop_2
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_mask_loop_2.rgb)
        if thisPrac_mask_loop_2 != None:
            for paramName in thisPrac_mask_loop_2:
                exec('{} = thisPrac_mask_loop_2[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mask" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        mask_image.setImage(mask_name)
        # keep track of which components have finished
        maskComponents = [mask_image, Esc_exit_14]
        for thisComponent in maskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mask" ---
        while continueRoutine and routineTimer.getTime() < 0.06:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *mask_image* updates
            if mask_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mask_image.frameNStart = frameN  # exact frame index
                mask_image.tStart = t  # local t and not account for scr refresh
                mask_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask_image, 'tStartRefresh')  # time at next scr refresh
                mask_image.setAutoDraw(True)
            if mask_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask_image.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    mask_image.tStop = t  # not accounting for scr refresh
                    mask_image.frameNStop = frameN  # exact frame index
                    mask_image.setAutoDraw(False)
            
            # *Esc_exit_14* updates
            if Esc_exit_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Esc_exit_14.frameNStart = frameN  # exact frame index
                Esc_exit_14.tStart = t  # local t and not account for scr refresh
                Esc_exit_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Esc_exit_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Esc_exit_14.started')
                Esc_exit_14.setAutoDraw(True)
            if Esc_exit_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Esc_exit_14.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    Esc_exit_14.tStop = t  # not accounting for scr refresh
                    Esc_exit_14.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Esc_exit_14.stopped')
                    Esc_exit_14.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in maskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mask" ---
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.060000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'prac_mask_loop_2'
    
    
    # --- Prepare to start Routine "prac_response" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from code
    
    
    
    # Run 'Begin Routine' code from enable_mouse_2
    event.Mouse(visible=True)
    # keep track of which components have finished
    prac_responseComponents = [mouse_2, response1disk_3, response5disk_3, response3disk_3, response7disk_3, text, most_similar_3, most_different_3, Esc_exit_7]
    for thisComponent in prac_responseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_response" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse_2* updates
        if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_2.started', t)
            mouse_2.status = STARTED
            mouse_2.mouseClock.reset()
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([response1disk,response3disk,response5disk,response7disk])
                        clickableList = [response1disk,response3disk,response5disk,response7disk]
                    except:
                        clickableList = [[response1disk,response3disk,response5disk,response7disk]]
                    for obj in clickableList:
                        if obj.contains(mouse_2):
                            gotValidClick = True
                            mouse_2.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *response1disk_3* updates
        if response1disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk_3.frameNStart = frameN  # exact frame index
            response1disk_3.tStart = t  # local t and not account for scr refresh
            response1disk_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk_3, 'tStartRefresh')  # time at next scr refresh
            response1disk_3.setAutoDraw(True)
        
        # *response5disk_3* updates
        if response5disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk_3.frameNStart = frameN  # exact frame index
            response5disk_3.tStart = t  # local t and not account for scr refresh
            response5disk_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk_3, 'tStartRefresh')  # time at next scr refresh
            response5disk_3.setAutoDraw(True)
        
        # *response3disk_3* updates
        if response3disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk_3.frameNStart = frameN  # exact frame index
            response3disk_3.tStart = t  # local t and not account for scr refresh
            response3disk_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk_3, 'tStartRefresh')  # time at next scr refresh
            response3disk_3.setAutoDraw(True)
        
        # *response7disk_3* updates
        if response7disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk_3.frameNStart = frameN  # exact frame index
            response7disk_3.tStart = t  # local t and not account for scr refresh
            response7disk_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk_3, 'tStartRefresh')  # time at next scr refresh
            response7disk_3.setAutoDraw(True)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        
        # *most_similar_3* updates
        if most_similar_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            most_similar_3.frameNStart = frameN  # exact frame index
            most_similar_3.tStart = t  # local t and not account for scr refresh
            most_similar_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(most_similar_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'most_similar_3.started')
            most_similar_3.setAutoDraw(True)
        
        # *most_different_3* updates
        if most_different_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            most_different_3.frameNStart = frameN  # exact frame index
            most_different_3.tStart = t  # local t and not account for scr refresh
            most_different_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(most_different_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'most_different_3.started')
            most_different_3.setAutoDraw(True)
        
        # *Esc_exit_7* updates
        if Esc_exit_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Esc_exit_7.frameNStart = frameN  # exact frame index
            Esc_exit_7.tStart = t  # local t and not account for scr refresh
            Esc_exit_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Esc_exit_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Esc_exit_7.started')
            Esc_exit_7.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_responseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_response" ---
    for thisComponent in prac_responseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for prac_loop (TrialHandler)
    x, y = mouse_2.getPos()
    buttons = mouse_2.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([response1disk,response3disk,response5disk,response7disk])
            clickableList = [response1disk,response3disk,response5disk,response7disk]
        except:
            clickableList = [[response1disk,response3disk,response5disk,response7disk]]
        for obj in clickableList:
            if obj.contains(mouse_2):
                gotValidClick = True
                mouse_2.clicked_name.append(obj.name)
    prac_loop.addData('mouse_2.x', x)
    prac_loop.addData('mouse_2.y', y)
    prac_loop.addData('mouse_2.leftButton', buttons[0])
    prac_loop.addData('mouse_2.midButton', buttons[1])
    prac_loop.addData('mouse_2.rightButton', buttons[2])
    if len(mouse_2.clicked_name):
        prac_loop.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
    # Run 'End Routine' code from code
    # Save similarity rating 
    mousexpos=mouse.getPos()[0]  # get x position of mouse
    mouseypos=mouse.getPos()[1]  # get y position of mouse
    
    # Triangle 7
    x11d = a - b/2;
    y11d = a + b/2;
    x12d = a + b/2;
    y12d = a + b/2;
    x13d = a - b/2;
    y13d = a - b/2;
    a1d = ((y12d - y13d)*(mousexpos - x13d) + (x13d - x12d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
    b1d = ((y13d - y11d)*(mousexpos - x13d) + (x11d - x13d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
    c1d = 1 - a1d - b1d;
    
    # Triangle 6 
    x21d = a - b/2;
    y21d = a - b/2
    x22d = a + b/2
    y22d = a + b/2
    x23d = a + b/2
    y23d = a - b/2
    a2d = ((y22d - y23d)*(mousexpos - x23d) + (x23d - x22d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
    b2d = ((y23d - y21d)*(mousexpos - x23d) + (x21d - x23d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
    c2d = 1 - a2d - b2d
    
    # Triangle 5
    x31d = a - b/2
    y31d = -(a - b/2)
    x32d = a + b/2
    y32d = -(a - b/2) 
    x33d = a + b/2
    y33d = -(a + b/2)
    a3d = ((y32d - y33d)*(mousexpos - x33d) + (x33d - x32d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
    b3d = ((y33d - y31d)*(mousexpos - x33d) + (x31d - x33d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
    c3d = 1 - a3d - b3d
    
    
    # Triangle 4 
    x41d = a - b/2
    y41d = -(a - b/2)
    x42d = a + b/2
    y42d = -(a + b/2)
    x43d = a - b/2
    y43d = -(a + b/2)
    a4d = ((y42d - y43d)*(mousexpos - x43d) + (x43d - x42d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
    b4d = ((y43d - y41d)*(mousexpos - x43d) + (x41d - x43d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
    c4d = 1 - a4d - b4d
    
    #  Triangle 3
    x51d = -(a + b/2)
    y51d = -(a + b/2)
    x52d = -(a - b/2)
    y52d = -(a - b/2)
    x53d = -(a - b/2)
    y53d = -(a + b/2)
    a5d = ((y52d - y53d)*(mousexpos - x53d) + (x53d - x52d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
    b5d = ((y53d - y51d)*(mousexpos - x53d) + (x51d - x53d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
    c5d = 1 - a5d - b5d
    
    # Triangle 2
    x61d = -(a+b/2)
    y61d = -(a-b/2)
    x62d = -(a-b/2)
    y62d = -(a-b/2)
    x63d = -(a+b/2)
    y63d = - (a+b/2)
    a6d = ((y62d - y63d)*(mousexpos - x63d) + (x63d - x62d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
    b6d = ((y63d - y61d)*(mousexpos - x63d) + (x61d - x63d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
    c6d = 1 - a6d - b6d
    
    # Triangle 1 
    
    x71d = -(a + b/2)
    y71d = a + b/2
    x72d = -(a - b/2)
    y72d = a - b/2
    x73d = -(a + b/2)
    y73d = a - b/2
    a7d = ((y72d - y73d)*(mousexpos - x73d) + (x73d - x72d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
    b7d = ((y73d - y71d)*(mousexpos - x73d) + (x71d - x73d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
    c7d = 1 - a7d - b7d
    
    
    # Triangle 0 
    x81d = -(a + b/2)
    y81d = a + b/2
    x82d = -(a - b/2)
    y82d = a + b/2
    x83d = -(a - b/2)
    y83d = a - b/2
    a8d = ((y82d - y83d)*(mousexpos - x83d) + (x83d - x82d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
    b8d = ((y83d - y81d)*(mousexpos - x83d) + (x81d - x83d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
    c8d = 1 - a8d - b8d
    
    if (0 <= a1d <= 1) and (0 <= b1d <= 1) and (0 <= c1d <= 1):
        similarity = 7
    elif (0 <= a2d <= 1) and (0 <= b2d <= 1) and (0 <= c2d <= 1):
        similarity = 6
    elif (0 <= a3d <= 1) and (0 <= b3d <= 1) and (0 <= c3d <= 1):
        similarity = 5
    elif (0 <= a4d <= 1) and (0 <= b4d <= 1) and (0 <= c4d <= 1):
        similarity = 4
    elif (0 <= a5d <= 1) and (0 <= b5d <= 1) and (0 <= c5d <= 1):
        similarity = 3
    elif (0 <= a6d <= 1) and (0 <= b6d <= 1) and (0 <= c6d <= 1):
        similarity = 2
    elif (0 <= a7d <= 1) and (0 <= b7d <= 1) and (0 <= c7d <= 1):
        similarity = 1
    elif (0 <= a8d <= 1) and (0 <= b8d <= 1) and (0 <= c8d <= 1):
        similarity = 0
    
    thisExp.addData("similarity", similarity);
    thisExp.addData("response_time", mouse.mouseClock.getTime())  # Save time relative to start of mouse
    thisExp.addData("Pass", 1)  # Save time relative to start of mouse
    
    # the Routine "prac_response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "resposne_feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    if 0 <= similarity <= 1:
        responsefeedback = f'You selected {similarity}'
        responsefeedback1 = f'{similarity} indicates you found the images very similar';
    
    if 2 <= similarity <= 3:
        responsefeedback = f'You selected {similarity}'
        responsefeedback1 = f'{similarity} indicates you found the images similar';
    
    
    if 4 <= similarity  <= 5:
        responsefeedback = f'You selected {similarity}' ;
        responsefeedback1 = f'{similarity} indicates you found the images different';
    
    if 6 <= similarity  <= 7:
        responsefeedback = f'You selected {similarity}' ;
        responsefeedback1 = f'{similarity} indicates you found the images very different';
    text_55.setText(responsefeedback)
    text_56.setText(responsefeedback1)
    # keep track of which components have finished
    resposne_feedbackComponents = [text_55, text_56, Esc_exit_8]
    for thisComponent in resposne_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "resposne_feedback" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_55* updates
        if text_55.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_55.frameNStart = frameN  # exact frame index
            text_55.tStart = t  # local t and not account for scr refresh
            text_55.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_55, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_55.started')
            text_55.setAutoDraw(True)
        if text_55.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_55.tStartRefresh + response_feedback_time-frameTolerance:
                # keep track of stop time/frame for later
                text_55.tStop = t  # not accounting for scr refresh
                text_55.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_55.stopped')
                text_55.setAutoDraw(False)
        
        # *text_56* updates
        if text_56.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_56.frameNStart = frameN  # exact frame index
            text_56.tStart = t  # local t and not account for scr refresh
            text_56.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_56, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_56.started')
            text_56.setAutoDraw(True)
        if text_56.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_56.tStartRefresh + response_feedback_time-frameTolerance:
                # keep track of stop time/frame for later
                text_56.tStop = t  # not accounting for scr refresh
                text_56.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_56.stopped')
                text_56.setAutoDraw(False)
        
        # *Esc_exit_8* updates
        if Esc_exit_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Esc_exit_8.frameNStart = frameN  # exact frame index
            Esc_exit_8.tStart = t  # local t and not account for scr refresh
            Esc_exit_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Esc_exit_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Esc_exit_8.started')
            Esc_exit_8.setAutoDraw(True)
        if Esc_exit_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Esc_exit_8.tStartRefresh + response_feedback_time-frameTolerance:
                # keep track of stop time/frame for later
                Esc_exit_8.tStop = t  # not accounting for scr refresh
                Esc_exit_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Esc_exit_8.stopped')
                Esc_exit_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in resposne_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "resposne_feedback" ---
    for thisComponent in resposne_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "resposne_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prac_correct_mouse" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_12
    mouse_12.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    prac_correct_mouseComponents = [mouse_12, response1disk_4, response3disk_4, response5disk_4, response7disk_4, text_52, center_square_2, most_similar_4, most_different_4, Esc_exit_9]
    for thisComponent in prac_correct_mouseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_correct_mouse" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse_12* updates
        if mouse_12.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_12.frameNStart = frameN  # exact frame index
            mouse_12.tStart = t  # local t and not account for scr refresh
            mouse_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_12.started', t)
            mouse_12.status = STARTED
            mouse_12.mouseClock.reset()
            prevButtonState = mouse_12.getPressed()  # if button is down already this ISN'T a new click
        if mouse_12.status == STARTED:  # only update if started and not finished!
            buttons = mouse_12.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(center_square)
                        clickableList = center_square
                    except:
                        clickableList = [center_square]
                    for obj in clickableList:
                        if obj.contains(mouse_12):
                            gotValidClick = True
                            mouse_12.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *response1disk_4* updates
        if response1disk_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk_4.frameNStart = frameN  # exact frame index
            response1disk_4.tStart = t  # local t and not account for scr refresh
            response1disk_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk_4, 'tStartRefresh')  # time at next scr refresh
            response1disk_4.setAutoDraw(True)
        
        # *response3disk_4* updates
        if response3disk_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk_4.frameNStart = frameN  # exact frame index
            response3disk_4.tStart = t  # local t and not account for scr refresh
            response3disk_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk_4, 'tStartRefresh')  # time at next scr refresh
            response3disk_4.setAutoDraw(True)
        
        # *response5disk_4* updates
        if response5disk_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk_4.frameNStart = frameN  # exact frame index
            response5disk_4.tStart = t  # local t and not account for scr refresh
            response5disk_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk_4, 'tStartRefresh')  # time at next scr refresh
            response5disk_4.setAutoDraw(True)
        
        # *response7disk_4* updates
        if response7disk_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk_4.frameNStart = frameN  # exact frame index
            response7disk_4.tStart = t  # local t and not account for scr refresh
            response7disk_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk_4, 'tStartRefresh')  # time at next scr refresh
            response7disk_4.setAutoDraw(True)
        
        # *text_52* updates
        if text_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_52.frameNStart = frameN  # exact frame index
            text_52.tStart = t  # local t and not account for scr refresh
            text_52.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
            text_52.setAutoDraw(True)
        
        # *center_square_2* updates
        if center_square_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            center_square_2.frameNStart = frameN  # exact frame index
            center_square_2.tStart = t  # local t and not account for scr refresh
            center_square_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(center_square_2, 'tStartRefresh')  # time at next scr refresh
            center_square_2.setAutoDraw(True)
        
        # *most_similar_4* updates
        if most_similar_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            most_similar_4.frameNStart = frameN  # exact frame index
            most_similar_4.tStart = t  # local t and not account for scr refresh
            most_similar_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(most_similar_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'most_similar_4.started')
            most_similar_4.setAutoDraw(True)
        
        # *most_different_4* updates
        if most_different_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            most_different_4.frameNStart = frameN  # exact frame index
            most_different_4.tStart = t  # local t and not account for scr refresh
            most_different_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(most_different_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'most_different_4.started')
            most_different_4.setAutoDraw(True)
        
        # *Esc_exit_9* updates
        if Esc_exit_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Esc_exit_9.frameNStart = frameN  # exact frame index
            Esc_exit_9.tStart = t  # local t and not account for scr refresh
            Esc_exit_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Esc_exit_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Esc_exit_9.started')
            Esc_exit_9.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_correct_mouseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_correct_mouse" ---
    for thisComponent in prac_correct_mouseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for prac_loop (TrialHandler)
    x, y = mouse_12.getPos()
    buttons = mouse_12.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(center_square)
            clickableList = center_square
        except:
            clickableList = [center_square]
        for obj in clickableList:
            if obj.contains(mouse_12):
                gotValidClick = True
                mouse_12.clicked_name.append(obj.name)
    prac_loop.addData('mouse_12.x', x)
    prac_loop.addData('mouse_12.y', y)
    prac_loop.addData('mouse_12.leftButton', buttons[0])
    prac_loop.addData('mouse_12.midButton', buttons[1])
    prac_loop.addData('mouse_12.rightButton', buttons[2])
    if len(mouse_12.clicked_name):
        prac_loop.addData('mouse_12.clicked_name', mouse_12.clicked_name[0])
    # the Routine "prac_correct_mouse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'prac_loop'


# --- Prepare to start Routine "begin_task" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_1
mouse_1.x = []
mouse_1.y = []
mouse_1.leftButton = []
mouse_1.midButton = []
mouse_1.rightButton = []
mouse_1.time = []
mouse_1.clicked_name = []
gotValidClick = False  # until a click is received
space_press_continue_7.keys = []
space_press_continue_7.rt = []
_space_press_continue_7_allKeys = []
# keep track of which components have finished
begin_taskComponents = [mouse_1, begin_mouse_center, Esc_exit_15, space_press_continue_7]
for thisComponent in begin_taskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "begin_task" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *mouse_1* updates
    if mouse_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_1.frameNStart = frameN  # exact frame index
        mouse_1.tStart = t  # local t and not account for scr refresh
        mouse_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_1, 'tStartRefresh')  # time at next scr refresh
        mouse_1.status = STARTED
        mouse_1.mouseClock.reset()
        prevButtonState = mouse_1.getPressed()  # if button is down already this ISN'T a new click
    if mouse_1.status == STARTED:  # only update if started and not finished!
        buttons = mouse_1.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(center_square)
                    clickableList = center_square
                except:
                    clickableList = [center_square]
                for obj in clickableList:
                    if obj.contains(mouse_1):
                        gotValidClick = True
                        mouse_1.clicked_name.append(obj.name)
                x, y = mouse_1.getPos()
                mouse_1.x.append(x)
                mouse_1.y.append(y)
                buttons = mouse_1.getPressed()
                mouse_1.leftButton.append(buttons[0])
                mouse_1.midButton.append(buttons[1])
                mouse_1.rightButton.append(buttons[2])
                mouse_1.time.append(mouse_1.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # *begin_mouse_center* updates
    if begin_mouse_center.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_mouse_center.frameNStart = frameN  # exact frame index
        begin_mouse_center.tStart = t  # local t and not account for scr refresh
        begin_mouse_center.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_mouse_center, 'tStartRefresh')  # time at next scr refresh
        begin_mouse_center.setAutoDraw(True)
    
    # *Esc_exit_15* updates
    if Esc_exit_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Esc_exit_15.frameNStart = frameN  # exact frame index
        Esc_exit_15.tStart = t  # local t and not account for scr refresh
        Esc_exit_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Esc_exit_15, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Esc_exit_15.started')
        Esc_exit_15.setAutoDraw(True)
    
    # *space_press_continue_7* updates
    waitOnFlip = False
    if space_press_continue_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_press_continue_7.frameNStart = frameN  # exact frame index
        space_press_continue_7.tStart = t  # local t and not account for scr refresh
        space_press_continue_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_press_continue_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_press_continue_7.started')
        space_press_continue_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_press_continue_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_press_continue_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_press_continue_7.status == STARTED and not waitOnFlip:
        theseKeys = space_press_continue_7.getKeys(keyList=['space'], waitRelease=False)
        _space_press_continue_7_allKeys.extend(theseKeys)
        if len(_space_press_continue_7_allKeys):
            space_press_continue_7.keys = _space_press_continue_7_allKeys[-1].name  # just the last key pressed
            space_press_continue_7.rt = _space_press_continue_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in begin_taskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "begin_task" ---
for thisComponent in begin_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_1.x', mouse_1.x)
thisExp.addData('mouse_1.y', mouse_1.y)
thisExp.addData('mouse_1.leftButton', mouse_1.leftButton)
thisExp.addData('mouse_1.midButton', mouse_1.midButton)
thisExp.addData('mouse_1.rightButton', mouse_1.rightButton)
thisExp.addData('mouse_1.time', mouse_1.time)
thisExp.addData('mouse_1.clicked_name', mouse_1.clicked_name)
thisExp.nextEntry()
# check responses
if space_press_continue_7.keys in ['', [], None]:  # No response was made
    space_press_continue_7.keys = None
thisExp.addData('space_press_continue_7.keys',space_press_continue_7.keys)
if space_press_continue_7.keys != None:  # we had a response
    thisExp.addData('space_press_continue_7.rt', space_press_continue_7.rt)
thisExp.nextEntry()
# the Routine "begin_task" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
first_pass_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('info_exp_patch_3_cond.xlsx', selection='0:120'),
    seed=None, name='first_pass_loop')
thisExp.addLoop(first_pass_loop)  # add the loop to the experiment
thisFirst_pass_loop = first_pass_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFirst_pass_loop.rgb)
if thisFirst_pass_loop != None:
    for paramName in thisFirst_pass_loop:
        exec('{} = thisFirst_pass_loop[paramName]'.format(paramName))

for thisFirst_pass_loop in first_pass_loop:
    currentLoop = first_pass_loop
    # abbreviate parameter names if possible (e.g. rgb = thisFirst_pass_loop.rgb)
    if thisFirst_pass_loop != None:
        for paramName in thisFirst_pass_loop:
            exec('{} = thisFirst_pass_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "patch_1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    first_patch.setImage(Patch_1_name)
    # Run 'Begin Routine' code from disable_mouse
    event.Mouse(visible=False)
    # keep track of which components have finished
    patch_1Components = [fixation_cross_1, first_patch, Esc_exit_16]
    for thisComponent in patch_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "patch_1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross_1* updates
        if fixation_cross_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross_1.frameNStart = frameN  # exact frame index
            fixation_cross_1.tStart = t  # local t and not account for scr refresh
            fixation_cross_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross_1, 'tStartRefresh')  # time at next scr refresh
            fixation_cross_1.setAutoDraw(True)
        if fixation_cross_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross_1.tStartRefresh + fixation_cross_duration-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross_1.tStop = t  # not accounting for scr refresh
                fixation_cross_1.frameNStop = frameN  # exact frame index
                fixation_cross_1.setAutoDraw(False)
        
        # *first_patch* updates
        if first_patch.status == NOT_STARTED and tThisFlip >= fixation_cross_duration-frameTolerance:
            # keep track of start time/frame for later
            first_patch.frameNStart = frameN  # exact frame index
            first_patch.tStart = t  # local t and not account for scr refresh
            first_patch.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_patch, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'first_patch.started')
            first_patch.setAutoDraw(True)
        if first_patch.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > first_patch.tStartRefresh + image_duration-frameTolerance:
                # keep track of stop time/frame for later
                first_patch.tStop = t  # not accounting for scr refresh
                first_patch.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'first_patch.stopped')
                first_patch.setAutoDraw(False)
        
        # *Esc_exit_16* updates
        if Esc_exit_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Esc_exit_16.frameNStart = frameN  # exact frame index
            Esc_exit_16.tStart = t  # local t and not account for scr refresh
            Esc_exit_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Esc_exit_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Esc_exit_16.started')
            Esc_exit_16.setAutoDraw(True)
        if Esc_exit_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Esc_exit_16.tStartRefresh + exit_message_duration-frameTolerance:
                # keep track of stop time/frame for later
                Esc_exit_16.tStop = t  # not accounting for scr refresh
                Esc_exit_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Esc_exit_16.stopped')
                Esc_exit_16.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in patch_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "patch_1" ---
    for thisComponent in patch_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "patch_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    mask_loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('masks_cond.xlsx', selection='0:5'),
        seed=None, name='mask_loop')
    thisExp.addLoop(mask_loop)  # add the loop to the experiment
    thisMask_loop = mask_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMask_loop.rgb)
    if thisMask_loop != None:
        for paramName in thisMask_loop:
            exec('{} = thisMask_loop[paramName]'.format(paramName))
    
    for thisMask_loop in mask_loop:
        currentLoop = mask_loop
        # abbreviate parameter names if possible (e.g. rgb = thisMask_loop.rgb)
        if thisMask_loop != None:
            for paramName in thisMask_loop:
                exec('{} = thisMask_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mask" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        mask_image.setImage(mask_name)
        # keep track of which components have finished
        maskComponents = [mask_image, Esc_exit_14]
        for thisComponent in maskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mask" ---
        while continueRoutine and routineTimer.getTime() < 0.06:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *mask_image* updates
            if mask_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mask_image.frameNStart = frameN  # exact frame index
                mask_image.tStart = t  # local t and not account for scr refresh
                mask_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask_image, 'tStartRefresh')  # time at next scr refresh
                mask_image.setAutoDraw(True)
            if mask_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask_image.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    mask_image.tStop = t  # not accounting for scr refresh
                    mask_image.frameNStop = frameN  # exact frame index
                    mask_image.setAutoDraw(False)
            
            # *Esc_exit_14* updates
            if Esc_exit_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Esc_exit_14.frameNStart = frameN  # exact frame index
                Esc_exit_14.tStart = t  # local t and not account for scr refresh
                Esc_exit_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Esc_exit_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Esc_exit_14.started')
                Esc_exit_14.setAutoDraw(True)
            if Esc_exit_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Esc_exit_14.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    Esc_exit_14.tStop = t  # not accounting for scr refresh
                    Esc_exit_14.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Esc_exit_14.stopped')
                    Esc_exit_14.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in maskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mask" ---
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.060000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'mask_loop'
    
    
    # --- Prepare to start Routine "patch_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    second_patch.setImage(Patch_2_name)
    # Run 'Begin Routine' code from disable_mouse_2
    event.Mouse(visible=False)
    # keep track of which components have finished
    patch_2Components = [fixation_cross_2, second_patch, Esc_exit_17]
    for thisComponent in patch_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "patch_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross_2* updates
        if fixation_cross_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross_2.frameNStart = frameN  # exact frame index
            fixation_cross_2.tStart = t  # local t and not account for scr refresh
            fixation_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross_2, 'tStartRefresh')  # time at next scr refresh
            fixation_cross_2.setAutoDraw(True)
        if fixation_cross_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross_2.tStartRefresh + fixation_cross_duration-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross_2.tStop = t  # not accounting for scr refresh
                fixation_cross_2.frameNStop = frameN  # exact frame index
                fixation_cross_2.setAutoDraw(False)
        
        # *second_patch* updates
        if second_patch.status == NOT_STARTED and tThisFlip >= fixation_cross_duration-frameTolerance:
            # keep track of start time/frame for later
            second_patch.frameNStart = frameN  # exact frame index
            second_patch.tStart = t  # local t and not account for scr refresh
            second_patch.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(second_patch, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'second_patch.started')
            second_patch.setAutoDraw(True)
        if second_patch.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > second_patch.tStartRefresh + image_duration-frameTolerance:
                # keep track of stop time/frame for later
                second_patch.tStop = t  # not accounting for scr refresh
                second_patch.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'second_patch.stopped')
                second_patch.setAutoDraw(False)
        
        # *Esc_exit_17* updates
        if Esc_exit_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Esc_exit_17.frameNStart = frameN  # exact frame index
            Esc_exit_17.tStart = t  # local t and not account for scr refresh
            Esc_exit_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Esc_exit_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Esc_exit_17.started')
            Esc_exit_17.setAutoDraw(True)
        if Esc_exit_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Esc_exit_17.tStartRefresh + exit_message_duration-frameTolerance:
                # keep track of stop time/frame for later
                Esc_exit_17.tStop = t  # not accounting for scr refresh
                Esc_exit_17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Esc_exit_17.stopped')
                Esc_exit_17.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in patch_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "patch_2" ---
    for thisComponent in patch_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "patch_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    mask_loop_2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('masks_cond.xlsx', selection='0:5'),
        seed=None, name='mask_loop_2')
    thisExp.addLoop(mask_loop_2)  # add the loop to the experiment
    thisMask_loop_2 = mask_loop_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMask_loop_2.rgb)
    if thisMask_loop_2 != None:
        for paramName in thisMask_loop_2:
            exec('{} = thisMask_loop_2[paramName]'.format(paramName))
    
    for thisMask_loop_2 in mask_loop_2:
        currentLoop = mask_loop_2
        # abbreviate parameter names if possible (e.g. rgb = thisMask_loop_2.rgb)
        if thisMask_loop_2 != None:
            for paramName in thisMask_loop_2:
                exec('{} = thisMask_loop_2[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mask" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        mask_image.setImage(mask_name)
        # keep track of which components have finished
        maskComponents = [mask_image, Esc_exit_14]
        for thisComponent in maskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mask" ---
        while continueRoutine and routineTimer.getTime() < 0.06:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *mask_image* updates
            if mask_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mask_image.frameNStart = frameN  # exact frame index
                mask_image.tStart = t  # local t and not account for scr refresh
                mask_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask_image, 'tStartRefresh')  # time at next scr refresh
                mask_image.setAutoDraw(True)
            if mask_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask_image.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    mask_image.tStop = t  # not accounting for scr refresh
                    mask_image.frameNStop = frameN  # exact frame index
                    mask_image.setAutoDraw(False)
            
            # *Esc_exit_14* updates
            if Esc_exit_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Esc_exit_14.frameNStart = frameN  # exact frame index
                Esc_exit_14.tStart = t  # local t and not account for scr refresh
                Esc_exit_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Esc_exit_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Esc_exit_14.started')
                Esc_exit_14.setAutoDraw(True)
            if Esc_exit_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Esc_exit_14.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    Esc_exit_14.tStop = t  # not accounting for scr refresh
                    Esc_exit_14.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Esc_exit_14.stopped')
                    Esc_exit_14.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in maskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mask" ---
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.060000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'mask_loop_2'
    
    
    # --- Prepare to start Routine "response" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from code_4
    # Count trial numbers 
    trialnumber =  trialnumber + 1;
    
    # text for indicating trial number
    trial_num_feedback = f'You have completed {trialnumber} of {alltrials} trials'
    # Run 'Begin Routine' code from enable_mouse
    event.Mouse(visible=True)
    # keep track of which components have finished
    responseComponents = [mouse, response1disk, response3disk, response5disk, response7disk, text_23, most_similar, most_different, Esc_exit_10]
    for thisComponent in responseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "response" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([response1disk,response3disk,response5disk,response7disk])
                        clickableList = [response1disk,response3disk,response5disk,response7disk]
                    except:
                        clickableList = [[response1disk,response3disk,response5disk,response7disk]]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *response1disk* updates
        if response1disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk.frameNStart = frameN  # exact frame index
            response1disk.tStart = t  # local t and not account for scr refresh
            response1disk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk, 'tStartRefresh')  # time at next scr refresh
            response1disk.setAutoDraw(True)
        
        # *response3disk* updates
        if response3disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk.frameNStart = frameN  # exact frame index
            response3disk.tStart = t  # local t and not account for scr refresh
            response3disk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk, 'tStartRefresh')  # time at next scr refresh
            response3disk.setAutoDraw(True)
        
        # *response5disk* updates
        if response5disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk.frameNStart = frameN  # exact frame index
            response5disk.tStart = t  # local t and not account for scr refresh
            response5disk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk, 'tStartRefresh')  # time at next scr refresh
            response5disk.setAutoDraw(True)
        
        # *response7disk* updates
        if response7disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk.frameNStart = frameN  # exact frame index
            response7disk.tStart = t  # local t and not account for scr refresh
            response7disk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk, 'tStartRefresh')  # time at next scr refresh
            response7disk.setAutoDraw(True)
        
        # *text_23* updates
        if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_23.frameNStart = frameN  # exact frame index
            text_23.tStart = t  # local t and not account for scr refresh
            text_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_23.started')
            text_23.setAutoDraw(True)
        
        # *most_similar* updates
        if most_similar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            most_similar.frameNStart = frameN  # exact frame index
            most_similar.tStart = t  # local t and not account for scr refresh
            most_similar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(most_similar, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'most_similar.started')
            most_similar.setAutoDraw(True)
        
        # *most_different* updates
        if most_different.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            most_different.frameNStart = frameN  # exact frame index
            most_different.tStart = t  # local t and not account for scr refresh
            most_different.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(most_different, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'most_different.started')
            most_different.setAutoDraw(True)
        
        # *Esc_exit_10* updates
        if Esc_exit_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Esc_exit_10.frameNStart = frameN  # exact frame index
            Esc_exit_10.tStart = t  # local t and not account for scr refresh
            Esc_exit_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Esc_exit_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Esc_exit_10.started')
            Esc_exit_10.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "response" ---
    for thisComponent in responseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for first_pass_loop (TrialHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([response1disk,response3disk,response5disk,response7disk])
            clickableList = [response1disk,response3disk,response5disk,response7disk]
        except:
            clickableList = [[response1disk,response3disk,response5disk,response7disk]]
        for obj in clickableList:
            if obj.contains(mouse):
                gotValidClick = True
                mouse.clicked_name.append(obj.name)
    first_pass_loop.addData('mouse.x', x)
    first_pass_loop.addData('mouse.y', y)
    first_pass_loop.addData('mouse.leftButton', buttons[0])
    first_pass_loop.addData('mouse.midButton', buttons[1])
    first_pass_loop.addData('mouse.rightButton', buttons[2])
    if len(mouse.clicked_name):
        first_pass_loop.addData('mouse.clicked_name', mouse.clicked_name[0])
    # Run 'End Routine' code from code_4
    # Save similarity rating 
    mousexpos=mouse.getPos()[0]  # get x position of mouse
    mouseypos=mouse.getPos()[1]  # get y position of mouse
    
    # Triangle 7
    x11d = a - b/2;
    y11d = a + b/2;
    x12d = a + b/2;
    y12d = a + b/2;
    x13d = a - b/2;
    y13d = a - b/2;
    a1d = ((y12d - y13d)*(mousexpos - x13d) + (x13d - x12d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
    b1d = ((y13d - y11d)*(mousexpos - x13d) + (x11d - x13d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
    c1d = 1 - a1d - b1d;
    
    # Triangle 6 
    x21d = a - b/2;
    y21d = a - b/2
    x22d = a + b/2
    y22d = a + b/2
    x23d = a + b/2
    y23d = a - b/2
    a2d = ((y22d - y23d)*(mousexpos - x23d) + (x23d - x22d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
    b2d = ((y23d - y21d)*(mousexpos - x23d) + (x21d - x23d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
    c2d = 1 - a2d - b2d
    
    # Triangle 5
    x31d = a - b/2
    y31d = -(a - b/2)
    x32d = a + b/2
    y32d = -(a - b/2) 
    x33d = a + b/2
    y33d = -(a + b/2)
    a3d = ((y32d - y33d)*(mousexpos - x33d) + (x33d - x32d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
    b3d = ((y33d - y31d)*(mousexpos - x33d) + (x31d - x33d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
    c3d = 1 - a3d - b3d
    
    
    # Triangle 4 
    x41d = a - b/2
    y41d = -(a - b/2)
    x42d = a + b/2
    y42d = -(a + b/2)
    x43d = a - b/2
    y43d = -(a + b/2)
    a4d = ((y42d - y43d)*(mousexpos - x43d) + (x43d - x42d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
    b4d = ((y43d - y41d)*(mousexpos - x43d) + (x41d - x43d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
    c4d = 1 - a4d - b4d
    
    #  Triangle 3
    x51d = -(a + b/2)
    y51d = -(a + b/2)
    x52d = -(a - b/2)
    y52d = -(a - b/2)
    x53d = -(a - b/2)
    y53d = -(a + b/2)
    a5d = ((y52d - y53d)*(mousexpos - x53d) + (x53d - x52d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
    b5d = ((y53d - y51d)*(mousexpos - x53d) + (x51d - x53d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
    c5d = 1 - a5d - b5d
    
    # Triangle 2
    x61d = -(a+b/2)
    y61d = -(a-b/2)
    x62d = -(a-b/2)
    y62d = -(a-b/2)
    x63d = -(a+b/2)
    y63d = - (a+b/2)
    a6d = ((y62d - y63d)*(mousexpos - x63d) + (x63d - x62d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
    b6d = ((y63d - y61d)*(mousexpos - x63d) + (x61d - x63d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
    c6d = 1 - a6d - b6d
    
    # Triangle 1 
    
    x71d = -(a + b/2)
    y71d = a + b/2
    x72d = -(a - b/2)
    y72d = a - b/2
    x73d = -(a + b/2)
    y73d = a - b/2
    a7d = ((y72d - y73d)*(mousexpos - x73d) + (x73d - x72d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
    b7d = ((y73d - y71d)*(mousexpos - x73d) + (x71d - x73d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
    c7d = 1 - a7d - b7d
    
    
    # Triangle 0 
    x81d = -(a + b/2)
    y81d = a + b/2
    x82d = -(a - b/2)
    y82d = a + b/2
    x83d = -(a - b/2)
    y83d = a - b/2
    a8d = ((y82d - y83d)*(mousexpos - x83d) + (x83d - x82d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
    b8d = ((y83d - y81d)*(mousexpos - x83d) + (x81d - x83d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
    c8d = 1 - a8d - b8d
    
    if (0 <= a1d <= 1) and (0 <= b1d <= 1) and (0 <= c1d <= 1):
        similarity = 7
    elif (0 <= a2d <= 1) and (0 <= b2d <= 1) and (0 <= c2d <= 1):
        similarity = 6
    elif (0 <= a3d <= 1) and (0 <= b3d <= 1) and (0 <= c3d <= 1):
        similarity = 5
    elif (0 <= a4d <= 1) and (0 <= b4d <= 1) and (0 <= c4d <= 1):
        similarity = 4
    elif (0 <= a5d <= 1) and (0 <= b5d <= 1) and (0 <= c5d <= 1):
        similarity = 3
    elif (0 <= a6d <= 1) and (0 <= b6d <= 1) and (0 <= c6d <= 1):
        similarity = 2
    elif (0 <= a7d <= 1) and (0 <= b7d <= 1) and (0 <= c7d <= 1):
        similarity = 1
    elif (0 <= a8d <= 1) and (0 <= b8d <= 1) and (0 <= c8d <= 1):
        similarity = 0
    
    thisExp.addData("similarity", similarity);
    thisExp.addData("response_time", mouse.mouseClock.getTime())  # Save time relative to start of mouse
    thisExp.addData("Pass", 1)  # Save time relative to start of mouse
    thisExp.addData("trialNumber", trialnumber)  # Save trial number
    # the Routine "response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "correct_mouse" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_11
    mouse_11.clicked_name = []
    gotValidClick = False  # until a click is received
    trial_text_2.setText(trial_num_feedback)
    # keep track of which components have finished
    correct_mouseComponents = [mouse_11, response1disk_2, response3disk_2, response5disk_2, response7disk_2, text_51, center_square, most_similar_2, most_different_2, trial_text_2, Esc_exit_11]
    for thisComponent in correct_mouseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "correct_mouse" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse_11* updates
        if mouse_11.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_11.frameNStart = frameN  # exact frame index
            mouse_11.tStart = t  # local t and not account for scr refresh
            mouse_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_11.started', t)
            mouse_11.status = STARTED
            mouse_11.mouseClock.reset()
            prevButtonState = mouse_11.getPressed()  # if button is down already this ISN'T a new click
        if mouse_11.status == STARTED:  # only update if started and not finished!
            buttons = mouse_11.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(center_square)
                        clickableList = center_square
                    except:
                        clickableList = [center_square]
                    for obj in clickableList:
                        if obj.contains(mouse_11):
                            gotValidClick = True
                            mouse_11.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *response1disk_2* updates
        if response1disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk_2.frameNStart = frameN  # exact frame index
            response1disk_2.tStart = t  # local t and not account for scr refresh
            response1disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk_2, 'tStartRefresh')  # time at next scr refresh
            response1disk_2.setAutoDraw(True)
        
        # *response3disk_2* updates
        if response3disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk_2.frameNStart = frameN  # exact frame index
            response3disk_2.tStart = t  # local t and not account for scr refresh
            response3disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk_2, 'tStartRefresh')  # time at next scr refresh
            response3disk_2.setAutoDraw(True)
        
        # *response5disk_2* updates
        if response5disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk_2.frameNStart = frameN  # exact frame index
            response5disk_2.tStart = t  # local t and not account for scr refresh
            response5disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk_2, 'tStartRefresh')  # time at next scr refresh
            response5disk_2.setAutoDraw(True)
        
        # *response7disk_2* updates
        if response7disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk_2.frameNStart = frameN  # exact frame index
            response7disk_2.tStart = t  # local t and not account for scr refresh
            response7disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk_2, 'tStartRefresh')  # time at next scr refresh
            response7disk_2.setAutoDraw(True)
        
        # *text_51* updates
        if text_51.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_51.frameNStart = frameN  # exact frame index
            text_51.tStart = t  # local t and not account for scr refresh
            text_51.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_51, 'tStartRefresh')  # time at next scr refresh
            text_51.setAutoDraw(True)
        
        # *center_square* updates
        if center_square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            center_square.frameNStart = frameN  # exact frame index
            center_square.tStart = t  # local t and not account for scr refresh
            center_square.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(center_square, 'tStartRefresh')  # time at next scr refresh
            center_square.setAutoDraw(True)
        
        # *most_similar_2* updates
        if most_similar_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            most_similar_2.frameNStart = frameN  # exact frame index
            most_similar_2.tStart = t  # local t and not account for scr refresh
            most_similar_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(most_similar_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'most_similar_2.started')
            most_similar_2.setAutoDraw(True)
        
        # *most_different_2* updates
        if most_different_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            most_different_2.frameNStart = frameN  # exact frame index
            most_different_2.tStart = t  # local t and not account for scr refresh
            most_different_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(most_different_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'most_different_2.started')
            most_different_2.setAutoDraw(True)
        
        # *trial_text_2* updates
        if trial_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_text_2.frameNStart = frameN  # exact frame index
            trial_text_2.tStart = t  # local t and not account for scr refresh
            trial_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_text_2.started')
            trial_text_2.setAutoDraw(True)
        
        # *Esc_exit_11* updates
        if Esc_exit_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Esc_exit_11.frameNStart = frameN  # exact frame index
            Esc_exit_11.tStart = t  # local t and not account for scr refresh
            Esc_exit_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Esc_exit_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Esc_exit_11.started')
            Esc_exit_11.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in correct_mouseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "correct_mouse" ---
    for thisComponent in correct_mouseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for first_pass_loop (TrialHandler)
    x, y = mouse_11.getPos()
    buttons = mouse_11.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(center_square)
            clickableList = center_square
        except:
            clickableList = [center_square]
        for obj in clickableList:
            if obj.contains(mouse_11):
                gotValidClick = True
                mouse_11.clicked_name.append(obj.name)
    first_pass_loop.addData('mouse_11.x', x)
    first_pass_loop.addData('mouse_11.y', y)
    first_pass_loop.addData('mouse_11.leftButton', buttons[0])
    first_pass_loop.addData('mouse_11.midButton', buttons[1])
    first_pass_loop.addData('mouse_11.rightButton', buttons[2])
    if len(mouse_11.clicked_name):
        first_pass_loop.addData('mouse_11.clicked_name', mouse_11.clicked_name[0])
    # the Routine "correct_mouse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'first_pass_loop'


# set up handler to look after randomisation of conditions etc
double_pass_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('info_exp_patch_3_cond.xlsx', selection='0:120'),
    seed=None, name='double_pass_loop')
thisExp.addLoop(double_pass_loop)  # add the loop to the experiment
thisDouble_pass_loop = double_pass_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDouble_pass_loop.rgb)
if thisDouble_pass_loop != None:
    for paramName in thisDouble_pass_loop:
        exec('{} = thisDouble_pass_loop[paramName]'.format(paramName))

for thisDouble_pass_loop in double_pass_loop:
    currentLoop = double_pass_loop
    # abbreviate parameter names if possible (e.g. rgb = thisDouble_pass_loop.rgb)
    if thisDouble_pass_loop != None:
        for paramName in thisDouble_pass_loop:
            exec('{} = thisDouble_pass_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "patch_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    second_patch.setImage(Patch_2_name)
    # Run 'Begin Routine' code from disable_mouse_2
    event.Mouse(visible=False)
    # keep track of which components have finished
    patch_2Components = [fixation_cross_2, second_patch, Esc_exit_17]
    for thisComponent in patch_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "patch_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross_2* updates
        if fixation_cross_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross_2.frameNStart = frameN  # exact frame index
            fixation_cross_2.tStart = t  # local t and not account for scr refresh
            fixation_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross_2, 'tStartRefresh')  # time at next scr refresh
            fixation_cross_2.setAutoDraw(True)
        if fixation_cross_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross_2.tStartRefresh + fixation_cross_duration-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross_2.tStop = t  # not accounting for scr refresh
                fixation_cross_2.frameNStop = frameN  # exact frame index
                fixation_cross_2.setAutoDraw(False)
        
        # *second_patch* updates
        if second_patch.status == NOT_STARTED and tThisFlip >= fixation_cross_duration-frameTolerance:
            # keep track of start time/frame for later
            second_patch.frameNStart = frameN  # exact frame index
            second_patch.tStart = t  # local t and not account for scr refresh
            second_patch.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(second_patch, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'second_patch.started')
            second_patch.setAutoDraw(True)
        if second_patch.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > second_patch.tStartRefresh + image_duration-frameTolerance:
                # keep track of stop time/frame for later
                second_patch.tStop = t  # not accounting for scr refresh
                second_patch.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'second_patch.stopped')
                second_patch.setAutoDraw(False)
        
        # *Esc_exit_17* updates
        if Esc_exit_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Esc_exit_17.frameNStart = frameN  # exact frame index
            Esc_exit_17.tStart = t  # local t and not account for scr refresh
            Esc_exit_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Esc_exit_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Esc_exit_17.started')
            Esc_exit_17.setAutoDraw(True)
        if Esc_exit_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Esc_exit_17.tStartRefresh + exit_message_duration-frameTolerance:
                # keep track of stop time/frame for later
                Esc_exit_17.tStop = t  # not accounting for scr refresh
                Esc_exit_17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Esc_exit_17.stopped')
                Esc_exit_17.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in patch_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "patch_2" ---
    for thisComponent in patch_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "patch_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    mask_loop_3 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('masks_cond.xlsx', selection='0:5'),
        seed=None, name='mask_loop_3')
    thisExp.addLoop(mask_loop_3)  # add the loop to the experiment
    thisMask_loop_3 = mask_loop_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMask_loop_3.rgb)
    if thisMask_loop_3 != None:
        for paramName in thisMask_loop_3:
            exec('{} = thisMask_loop_3[paramName]'.format(paramName))
    
    for thisMask_loop_3 in mask_loop_3:
        currentLoop = mask_loop_3
        # abbreviate parameter names if possible (e.g. rgb = thisMask_loop_3.rgb)
        if thisMask_loop_3 != None:
            for paramName in thisMask_loop_3:
                exec('{} = thisMask_loop_3[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mask" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        mask_image.setImage(mask_name)
        # keep track of which components have finished
        maskComponents = [mask_image, Esc_exit_14]
        for thisComponent in maskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mask" ---
        while continueRoutine and routineTimer.getTime() < 0.06:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *mask_image* updates
            if mask_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mask_image.frameNStart = frameN  # exact frame index
                mask_image.tStart = t  # local t and not account for scr refresh
                mask_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask_image, 'tStartRefresh')  # time at next scr refresh
                mask_image.setAutoDraw(True)
            if mask_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask_image.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    mask_image.tStop = t  # not accounting for scr refresh
                    mask_image.frameNStop = frameN  # exact frame index
                    mask_image.setAutoDraw(False)
            
            # *Esc_exit_14* updates
            if Esc_exit_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Esc_exit_14.frameNStart = frameN  # exact frame index
                Esc_exit_14.tStart = t  # local t and not account for scr refresh
                Esc_exit_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Esc_exit_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Esc_exit_14.started')
                Esc_exit_14.setAutoDraw(True)
            if Esc_exit_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Esc_exit_14.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    Esc_exit_14.tStop = t  # not accounting for scr refresh
                    Esc_exit_14.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Esc_exit_14.stopped')
                    Esc_exit_14.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in maskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mask" ---
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.060000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'mask_loop_3'
    
    
    # --- Prepare to start Routine "patch_1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    first_patch.setImage(Patch_1_name)
    # Run 'Begin Routine' code from disable_mouse
    event.Mouse(visible=False)
    # keep track of which components have finished
    patch_1Components = [fixation_cross_1, first_patch, Esc_exit_16]
    for thisComponent in patch_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "patch_1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross_1* updates
        if fixation_cross_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross_1.frameNStart = frameN  # exact frame index
            fixation_cross_1.tStart = t  # local t and not account for scr refresh
            fixation_cross_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross_1, 'tStartRefresh')  # time at next scr refresh
            fixation_cross_1.setAutoDraw(True)
        if fixation_cross_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross_1.tStartRefresh + fixation_cross_duration-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross_1.tStop = t  # not accounting for scr refresh
                fixation_cross_1.frameNStop = frameN  # exact frame index
                fixation_cross_1.setAutoDraw(False)
        
        # *first_patch* updates
        if first_patch.status == NOT_STARTED and tThisFlip >= fixation_cross_duration-frameTolerance:
            # keep track of start time/frame for later
            first_patch.frameNStart = frameN  # exact frame index
            first_patch.tStart = t  # local t and not account for scr refresh
            first_patch.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_patch, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'first_patch.started')
            first_patch.setAutoDraw(True)
        if first_patch.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > first_patch.tStartRefresh + image_duration-frameTolerance:
                # keep track of stop time/frame for later
                first_patch.tStop = t  # not accounting for scr refresh
                first_patch.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'first_patch.stopped')
                first_patch.setAutoDraw(False)
        
        # *Esc_exit_16* updates
        if Esc_exit_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Esc_exit_16.frameNStart = frameN  # exact frame index
            Esc_exit_16.tStart = t  # local t and not account for scr refresh
            Esc_exit_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Esc_exit_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Esc_exit_16.started')
            Esc_exit_16.setAutoDraw(True)
        if Esc_exit_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Esc_exit_16.tStartRefresh + exit_message_duration-frameTolerance:
                # keep track of stop time/frame for later
                Esc_exit_16.tStop = t  # not accounting for scr refresh
                Esc_exit_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Esc_exit_16.stopped')
                Esc_exit_16.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in patch_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "patch_1" ---
    for thisComponent in patch_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "patch_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    mask_loop_4 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('masks_cond.xlsx', selection='0:5'),
        seed=None, name='mask_loop_4')
    thisExp.addLoop(mask_loop_4)  # add the loop to the experiment
    thisMask_loop_4 = mask_loop_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMask_loop_4.rgb)
    if thisMask_loop_4 != None:
        for paramName in thisMask_loop_4:
            exec('{} = thisMask_loop_4[paramName]'.format(paramName))
    
    for thisMask_loop_4 in mask_loop_4:
        currentLoop = mask_loop_4
        # abbreviate parameter names if possible (e.g. rgb = thisMask_loop_4.rgb)
        if thisMask_loop_4 != None:
            for paramName in thisMask_loop_4:
                exec('{} = thisMask_loop_4[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mask" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        mask_image.setImage(mask_name)
        # keep track of which components have finished
        maskComponents = [mask_image, Esc_exit_14]
        for thisComponent in maskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mask" ---
        while continueRoutine and routineTimer.getTime() < 0.06:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *mask_image* updates
            if mask_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mask_image.frameNStart = frameN  # exact frame index
                mask_image.tStart = t  # local t and not account for scr refresh
                mask_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask_image, 'tStartRefresh')  # time at next scr refresh
                mask_image.setAutoDraw(True)
            if mask_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask_image.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    mask_image.tStop = t  # not accounting for scr refresh
                    mask_image.frameNStop = frameN  # exact frame index
                    mask_image.setAutoDraw(False)
            
            # *Esc_exit_14* updates
            if Esc_exit_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Esc_exit_14.frameNStart = frameN  # exact frame index
                Esc_exit_14.tStart = t  # local t and not account for scr refresh
                Esc_exit_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Esc_exit_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Esc_exit_14.started')
                Esc_exit_14.setAutoDraw(True)
            if Esc_exit_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Esc_exit_14.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    Esc_exit_14.tStop = t  # not accounting for scr refresh
                    Esc_exit_14.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Esc_exit_14.stopped')
                    Esc_exit_14.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in maskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mask" ---
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.060000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'mask_loop_4'
    
    
    # --- Prepare to start Routine "response_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from code_5
    # Count trial numbers 
    trialnumber =  trialnumber + 1;
    
    # text for indicating trial number
    trial_num_feedback = f'You have completed {trialnumber} of {alltrials} trials'
    # Run 'Begin Routine' code from enable_mouse_3
    event.Mouse(visible=True)
    # keep track of which components have finished
    response_2Components = [mouse_3, response1disk_5, response3disk_5, response5disk_5, response7disk_5, text_24, most_similar_5, most_different_5, Esc_exit_18]
    for thisComponent in response_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "response_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse_3* updates
        if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_3.started', t)
            mouse_3.status = STARTED
            mouse_3.mouseClock.reset()
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([response1disk,response3disk,response5disk,response7disk])
                        clickableList = [response1disk,response3disk,response5disk,response7disk]
                    except:
                        clickableList = [[response1disk,response3disk,response5disk,response7disk]]
                    for obj in clickableList:
                        if obj.contains(mouse_3):
                            gotValidClick = True
                            mouse_3.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *response1disk_5* updates
        if response1disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk_5.frameNStart = frameN  # exact frame index
            response1disk_5.tStart = t  # local t and not account for scr refresh
            response1disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk_5, 'tStartRefresh')  # time at next scr refresh
            response1disk_5.setAutoDraw(True)
        
        # *response3disk_5* updates
        if response3disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk_5.frameNStart = frameN  # exact frame index
            response3disk_5.tStart = t  # local t and not account for scr refresh
            response3disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk_5, 'tStartRefresh')  # time at next scr refresh
            response3disk_5.setAutoDraw(True)
        
        # *response5disk_5* updates
        if response5disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk_5.frameNStart = frameN  # exact frame index
            response5disk_5.tStart = t  # local t and not account for scr refresh
            response5disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk_5, 'tStartRefresh')  # time at next scr refresh
            response5disk_5.setAutoDraw(True)
        
        # *response7disk_5* updates
        if response7disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk_5.frameNStart = frameN  # exact frame index
            response7disk_5.tStart = t  # local t and not account for scr refresh
            response7disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk_5, 'tStartRefresh')  # time at next scr refresh
            response7disk_5.setAutoDraw(True)
        
        # *text_24* updates
        if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_24.frameNStart = frameN  # exact frame index
            text_24.tStart = t  # local t and not account for scr refresh
            text_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_24.started')
            text_24.setAutoDraw(True)
        
        # *most_similar_5* updates
        if most_similar_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            most_similar_5.frameNStart = frameN  # exact frame index
            most_similar_5.tStart = t  # local t and not account for scr refresh
            most_similar_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(most_similar_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'most_similar_5.started')
            most_similar_5.setAutoDraw(True)
        
        # *most_different_5* updates
        if most_different_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            most_different_5.frameNStart = frameN  # exact frame index
            most_different_5.tStart = t  # local t and not account for scr refresh
            most_different_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(most_different_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'most_different_5.started')
            most_different_5.setAutoDraw(True)
        
        # *Esc_exit_18* updates
        if Esc_exit_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Esc_exit_18.frameNStart = frameN  # exact frame index
            Esc_exit_18.tStart = t  # local t and not account for scr refresh
            Esc_exit_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Esc_exit_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Esc_exit_18.started')
            Esc_exit_18.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in response_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "response_2" ---
    for thisComponent in response_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for double_pass_loop (TrialHandler)
    x, y = mouse_3.getPos()
    buttons = mouse_3.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([response1disk,response3disk,response5disk,response7disk])
            clickableList = [response1disk,response3disk,response5disk,response7disk]
        except:
            clickableList = [[response1disk,response3disk,response5disk,response7disk]]
        for obj in clickableList:
            if obj.contains(mouse_3):
                gotValidClick = True
                mouse_3.clicked_name.append(obj.name)
    double_pass_loop.addData('mouse_3.x', x)
    double_pass_loop.addData('mouse_3.y', y)
    double_pass_loop.addData('mouse_3.leftButton', buttons[0])
    double_pass_loop.addData('mouse_3.midButton', buttons[1])
    double_pass_loop.addData('mouse_3.rightButton', buttons[2])
    if len(mouse_3.clicked_name):
        double_pass_loop.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
    # Run 'End Routine' code from code_5
    # Save similarity rating 
    mousexpos=mouse.getPos()[0]  # get x position of mouse
    mouseypos=mouse.getPos()[1]  # get y position of mouse
    
    # Triangle 7
    x11d = a - b/2;
    y11d = a + b/2;
    x12d = a + b/2;
    y12d = a + b/2;
    x13d = a - b/2;
    y13d = a - b/2;
    a1d = ((y12d - y13d)*(mousexpos - x13d) + (x13d - x12d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
    b1d = ((y13d - y11d)*(mousexpos - x13d) + (x11d - x13d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
    c1d = 1 - a1d - b1d;
    
    # Triangle 6 
    x21d = a - b/2;
    y21d = a - b/2
    x22d = a + b/2
    y22d = a + b/2
    x23d = a + b/2
    y23d = a - b/2
    a2d = ((y22d - y23d)*(mousexpos - x23d) + (x23d - x22d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
    b2d = ((y23d - y21d)*(mousexpos - x23d) + (x21d - x23d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
    c2d = 1 - a2d - b2d
    
    # Triangle 5
    x31d = a - b/2
    y31d = -(a - b/2)
    x32d = a + b/2
    y32d = -(a - b/2) 
    x33d = a + b/2
    y33d = -(a + b/2)
    a3d = ((y32d - y33d)*(mousexpos - x33d) + (x33d - x32d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
    b3d = ((y33d - y31d)*(mousexpos - x33d) + (x31d - x33d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
    c3d = 1 - a3d - b3d
    
    
    # Triangle 4 
    x41d = a - b/2
    y41d = -(a - b/2)
    x42d = a + b/2
    y42d = -(a + b/2)
    x43d = a - b/2
    y43d = -(a + b/2)
    a4d = ((y42d - y43d)*(mousexpos - x43d) + (x43d - x42d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
    b4d = ((y43d - y41d)*(mousexpos - x43d) + (x41d - x43d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
    c4d = 1 - a4d - b4d
    
    #  Triangle 3
    x51d = -(a + b/2)
    y51d = -(a + b/2)
    x52d = -(a - b/2)
    y52d = -(a - b/2)
    x53d = -(a - b/2)
    y53d = -(a + b/2)
    a5d = ((y52d - y53d)*(mousexpos - x53d) + (x53d - x52d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
    b5d = ((y53d - y51d)*(mousexpos - x53d) + (x51d - x53d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
    c5d = 1 - a5d - b5d
    
    # Triangle 2
    x61d = -(a+b/2)
    y61d = -(a-b/2)
    x62d = -(a-b/2)
    y62d = -(a-b/2)
    x63d = -(a+b/2)
    y63d = - (a+b/2)
    a6d = ((y62d - y63d)*(mousexpos - x63d) + (x63d - x62d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
    b6d = ((y63d - y61d)*(mousexpos - x63d) + (x61d - x63d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
    c6d = 1 - a6d - b6d
    
    # Triangle 1 
    
    x71d = -(a + b/2)
    y71d = a + b/2
    x72d = -(a - b/2)
    y72d = a - b/2
    x73d = -(a + b/2)
    y73d = a - b/2
    a7d = ((y72d - y73d)*(mousexpos - x73d) + (x73d - x72d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
    b7d = ((y73d - y71d)*(mousexpos - x73d) + (x71d - x73d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
    c7d = 1 - a7d - b7d
    
    
    # Triangle 0 
    x81d = -(a + b/2)
    y81d = a + b/2
    x82d = -(a - b/2)
    y82d = a + b/2
    x83d = -(a - b/2)
    y83d = a - b/2
    a8d = ((y82d - y83d)*(mousexpos - x83d) + (x83d - x82d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
    b8d = ((y83d - y81d)*(mousexpos - x83d) + (x81d - x83d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
    c8d = 1 - a8d - b8d
    
    if (0 <= a1d <= 1) and (0 <= b1d <= 1) and (0 <= c1d <= 1):
        similarity = 7
    elif (0 <= a2d <= 1) and (0 <= b2d <= 1) and (0 <= c2d <= 1):
        similarity = 6
    elif (0 <= a3d <= 1) and (0 <= b3d <= 1) and (0 <= c3d <= 1):
        similarity = 5
    elif (0 <= a4d <= 1) and (0 <= b4d <= 1) and (0 <= c4d <= 1):
        similarity = 4
    elif (0 <= a5d <= 1) and (0 <= b5d <= 1) and (0 <= c5d <= 1):
        similarity = 3
    elif (0 <= a6d <= 1) and (0 <= b6d <= 1) and (0 <= c6d <= 1):
        similarity = 2
    elif (0 <= a7d <= 1) and (0 <= b7d <= 1) and (0 <= c7d <= 1):
        similarity = 1
    elif (0 <= a8d <= 1) and (0 <= b8d <= 1) and (0 <= c8d <= 1):
        similarity = 0
    
    thisExp.addData("similarity", similarity);
    thisExp.addData("response_time", mouse.mouseClock.getTime())  # Save time relative to start of mouse
    thisExp.addData("Pass", 2)  # Save time relative to start of mouse
    thisExp.addData("trialNumber", trialnumber)  # Save trial number
    # the Routine "response_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "correct_mouse" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_11
    mouse_11.clicked_name = []
    gotValidClick = False  # until a click is received
    trial_text_2.setText(trial_num_feedback)
    # keep track of which components have finished
    correct_mouseComponents = [mouse_11, response1disk_2, response3disk_2, response5disk_2, response7disk_2, text_51, center_square, most_similar_2, most_different_2, trial_text_2, Esc_exit_11]
    for thisComponent in correct_mouseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "correct_mouse" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse_11* updates
        if mouse_11.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_11.frameNStart = frameN  # exact frame index
            mouse_11.tStart = t  # local t and not account for scr refresh
            mouse_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_11.started', t)
            mouse_11.status = STARTED
            mouse_11.mouseClock.reset()
            prevButtonState = mouse_11.getPressed()  # if button is down already this ISN'T a new click
        if mouse_11.status == STARTED:  # only update if started and not finished!
            buttons = mouse_11.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(center_square)
                        clickableList = center_square
                    except:
                        clickableList = [center_square]
                    for obj in clickableList:
                        if obj.contains(mouse_11):
                            gotValidClick = True
                            mouse_11.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *response1disk_2* updates
        if response1disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk_2.frameNStart = frameN  # exact frame index
            response1disk_2.tStart = t  # local t and not account for scr refresh
            response1disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk_2, 'tStartRefresh')  # time at next scr refresh
            response1disk_2.setAutoDraw(True)
        
        # *response3disk_2* updates
        if response3disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk_2.frameNStart = frameN  # exact frame index
            response3disk_2.tStart = t  # local t and not account for scr refresh
            response3disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk_2, 'tStartRefresh')  # time at next scr refresh
            response3disk_2.setAutoDraw(True)
        
        # *response5disk_2* updates
        if response5disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk_2.frameNStart = frameN  # exact frame index
            response5disk_2.tStart = t  # local t and not account for scr refresh
            response5disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk_2, 'tStartRefresh')  # time at next scr refresh
            response5disk_2.setAutoDraw(True)
        
        # *response7disk_2* updates
        if response7disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk_2.frameNStart = frameN  # exact frame index
            response7disk_2.tStart = t  # local t and not account for scr refresh
            response7disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk_2, 'tStartRefresh')  # time at next scr refresh
            response7disk_2.setAutoDraw(True)
        
        # *text_51* updates
        if text_51.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_51.frameNStart = frameN  # exact frame index
            text_51.tStart = t  # local t and not account for scr refresh
            text_51.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_51, 'tStartRefresh')  # time at next scr refresh
            text_51.setAutoDraw(True)
        
        # *center_square* updates
        if center_square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            center_square.frameNStart = frameN  # exact frame index
            center_square.tStart = t  # local t and not account for scr refresh
            center_square.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(center_square, 'tStartRefresh')  # time at next scr refresh
            center_square.setAutoDraw(True)
        
        # *most_similar_2* updates
        if most_similar_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            most_similar_2.frameNStart = frameN  # exact frame index
            most_similar_2.tStart = t  # local t and not account for scr refresh
            most_similar_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(most_similar_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'most_similar_2.started')
            most_similar_2.setAutoDraw(True)
        
        # *most_different_2* updates
        if most_different_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            most_different_2.frameNStart = frameN  # exact frame index
            most_different_2.tStart = t  # local t and not account for scr refresh
            most_different_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(most_different_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'most_different_2.started')
            most_different_2.setAutoDraw(True)
        
        # *trial_text_2* updates
        if trial_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_text_2.frameNStart = frameN  # exact frame index
            trial_text_2.tStart = t  # local t and not account for scr refresh
            trial_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_text_2.started')
            trial_text_2.setAutoDraw(True)
        
        # *Esc_exit_11* updates
        if Esc_exit_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Esc_exit_11.frameNStart = frameN  # exact frame index
            Esc_exit_11.tStart = t  # local t and not account for scr refresh
            Esc_exit_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Esc_exit_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Esc_exit_11.started')
            Esc_exit_11.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in correct_mouseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "correct_mouse" ---
    for thisComponent in correct_mouseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for double_pass_loop (TrialHandler)
    x, y = mouse_11.getPos()
    buttons = mouse_11.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(center_square)
            clickableList = center_square
        except:
            clickableList = [center_square]
        for obj in clickableList:
            if obj.contains(mouse_11):
                gotValidClick = True
                mouse_11.clicked_name.append(obj.name)
    double_pass_loop.addData('mouse_11.x', x)
    double_pass_loop.addData('mouse_11.y', y)
    double_pass_loop.addData('mouse_11.leftButton', buttons[0])
    double_pass_loop.addData('mouse_11.midButton', buttons[1])
    double_pass_loop.addData('mouse_11.rightButton', buttons[2])
    if len(mouse_11.clicked_name):
        double_pass_loop.addData('mouse_11.clicked_name', mouse_11.clicked_name[0])
    # the Routine "correct_mouse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'double_pass_loop'


# --- Prepare to start Routine "end_of_experiment" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_exit.keys = []
space_exit.rt = []
_space_exit_allKeys = []
# keep track of which components have finished
end_of_experimentComponents = [thank_you, space_exit]
for thisComponent in end_of_experimentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end_of_experiment" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank_you* updates
    if thank_you.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank_you.frameNStart = frameN  # exact frame index
        thank_you.tStart = t  # local t and not account for scr refresh
        thank_you.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank_you, 'tStartRefresh')  # time at next scr refresh
        thank_you.setAutoDraw(True)
    
    # *space_exit* updates
    waitOnFlip = False
    if space_exit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_exit.frameNStart = frameN  # exact frame index
        space_exit.tStart = t  # local t and not account for scr refresh
        space_exit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_exit, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_exit.started')
        space_exit.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_exit.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_exit.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_exit.status == STARTED and not waitOnFlip:
        theseKeys = space_exit.getKeys(keyList=['space'], waitRelease=False)
        _space_exit_allKeys.extend(theseKeys)
        if len(_space_exit_allKeys):
            space_exit.keys = _space_exit_allKeys[-1].name  # just the last key pressed
            space_exit.rt = _space_exit_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_of_experimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end_of_experiment" ---
for thisComponent in end_of_experimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space_exit.keys in ['', [], None]:  # No response was made
    space_exit.keys = None
thisExp.addData('space_exit.keys',space_exit.keys)
if space_exit.keys != None:  # we had a response
    thisExp.addData('space_exit.rt', space_exit.rt)
thisExp.nextEntry()
# the Routine "end_of_experiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
