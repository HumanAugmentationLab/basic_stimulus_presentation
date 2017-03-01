# GOAL: cue task 4s, 2s blank screen, 2s fixation cross, 15s of trial, 15s of break
# CUES: acoustic stimuli (left/right) duration 1.5-8s

import os
from psychopy import data

# ------------------------------------
# EXPERIMENT SETTINGS
# ------------------------------------

datapath = 'data'                    # directory to save data
impath = 'images'                    # directory where images can be found
imlist = ['left', 'right', 'cross']  # image names without suffixes
suffix = '.png'                      # suffix for images
scrnsize = (1200, 800)               # screen size in pixels
timelimit = 4                        # image freezing time in seconds
changetime = .5                      # image changing time in seconds

# ----------------------------------------------
# STORE INFORMATION ABOUT THE EXPERIMENT SESSION
# ----------------------------------------------

exp_name = 'Motor Imagery'
exp_info = {}

# Get subject name, gender, age, handedness through a dialog box
# If 'Cancel' is pressed, quit
# Get date and time
# Store this information as general session info

# Check for datapath directory
if not os.path.isdir(datapath):
    os.makedirs(datapath)

# Create a unique filename for the experiment data
data_fname = exp_info['participant'] + '_' + exp_info['date']
data_fname = os.path.join(datapath, data_fname)

# ----------------------------------------------
# PREPARE CONDTIONS LIST
# ----------------------------------------------

# Check if all images exist
for im in imlist:
    im_fname = os.path.join(impath, im+sfx)
    if not os.path.exists(im_fname):
        raise Exception('Image files not fond in image folder: ' + str(im))

# TODO: find a way to define a set image order

# ----------------------------------------------
# CREATION OF WINDOW AND STIMULI
# ----------------------------------------------

# Open a window

# Define trial start text
text = "Press spacebar to start the trial"

# Define the bitmap stimuli (contents can still change)
# Define a bubble (position and size can still change)

# ----------------------------------------------
# DEFINE A TRIAL SEQUENCE
# ----------------------------------------------

# Define a list of trials with their properties:
#   - Which image (without the suffix)
#   - Which orientation

# TODO: stim_order list, orientations?
stim_order = []
for im in imlist:
    stim_order.append({'im': im, 'ori': })

trials = data.TrialHandler(stim_order, nReps=1, extraInfo=exp_info,
                           method='sequential', originPath=datapath)

# ----------------------------------------------
# START THE EXPERIMENT
# ----------------------------------------------

for trial in trials:
    # Display trial start text

    # Wait for a spacebar press to start trial or escape to quit

    # Set the images and orientation (?)
    im_fname = os.path.join(impath, trial['im'])
    trial['ori']

    # Empty keypresses list
    key_presses = []

    # Start the trial

    # Stop trial if spacebar or escape has been pressed or 30s has passed
    while not response and time < timelimit:
        # Switch image

        # TODO: Display images

        # For the duration of 'changetime,' wait for spacebar or escape press
        while time < changetime:
            if response:
                break

    # Aanlyze the keypress
    if response:
        if escape_pressed:
            # Escape press = quit the experiment
            break
        elif spacebar_pressed:
            # Spacebar press = correct change detection; register response time
            # ???????
            acc = 1
            rt = timelimit

    # Add the current trial's data to TrialHandler
    trials.addData('rt', rt)
    trials.addData('acc', acc)

    # Advance to the next trial

# ----------------------------------------------
# END THE EXPERIMENT
# ----------------------------------------------

# Save all data to a file
trials.saveAsWideText(data_fname + '.csv', delim=',')

# Quit the experiment
