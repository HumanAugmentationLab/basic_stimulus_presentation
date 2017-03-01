# GOAL: cue task 4s, 2s blank screen, 2s fixation cross, 15s of trial, 15s of break
# CUES: acoustic stimuli (left/right) duration 1.5-8s

import os

# ------------------------------------
# EXPERIMENT SETTINGS
# ------------------------------------

datapath = 'data'                    # directory to save data
impath = 'images'                    # directory where images can be found
imlist = ['left', 'right', 'cross']  # image names without suffixes
suffix = '.png'                         # suffix for images
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
# Randomize the image order
