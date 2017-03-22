# GOAL: cue task 4s, 2s blank screen, 2s fixation cross, 15s of trial, 15s of break
# CUES: acoustic stimuli (left/right) duration 1.5-8s

import os
from psychopy import data, visual, gui, core, event
from PIL import Image

# ------------------------------------
# EXPERIMENT SETTINGS
# ------------------------------------

datapath = 'data'                    # directory to save data
impath = 'images'                    # directory where images can be found
imlist = ['left', 'right']           # image names without suffixes
suffix = '.png'                      # suffix for images
scrnsize = (1200, 800)               # screen size in pixels
timelimit = 4                        # image freezing time in seconds
changetime = .5                      # image changing time in seconds

# ----------------------------------------------
# STORE INFORMATION ABOUT THE EXPERIMENT SESSION
# ----------------------------------------------

exp_name = 'Motor Imagery'
exp_info = {'participant': '',
            'gender': ('male', 'female', 'other'),
            'age': '',
            'left-handed': False}

# Get subject name, gender, age, handedness through a dialog box
# (see http://www.psychopy.org/api/gui.html)
dlg = gui.DlgFromDict(dictionary=exp_info, title=exp_name)

# If 'Cancel' is pressed, quit
if not dlg.OK:
    core.quit()

# Get date and time and store this information as general session info
exp_info['date'] = data.getDateStr()
exp_info['exp_name'] = exp_name

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
    im_fname = os.path.join(impath, im+suffix)
    if not os.path.exists(im_fname):
        raise Exception('Image files not fond in image folder: ' + str(im))

# TODO: find a way to define a set image order

orilist = [0, 0, 0]

# ----------------------------------------------
# CREATION OF WINDOW AND STIMULI
# ----------------------------------------------

# Open a window
window = visual.Window(size=scrnsize, color='black', units='pix',
                       fullscr=False)

# Define trial start text
text = "Press spacebar to start the trial"
start_message = visual.TextStim(window, text=text, color='red', height=20)

# Define the bitmap stimuli (contents can still change)
bitmap1 = visual.ImageStim(window, size=scrnsize)
bitmap2 = visual.ImageStim(window, size=scrnsize)

# ----------------------------------------------
# DEFINE A TRIAL SEQUENCE
# ----------------------------------------------

# Define a list of trials with their properties:
#   - Which image (without the suffix)
#   - Which orientation

# TODO: stim_order list, orientations?
stim_order = []
for im, ori in zip(imlist, orilist):
    stim_order.append({'im': im, 'ori': ori})

trials = data.TrialHandler(stim_order, nReps=2, extraInfo=exp_info,
                           method='sequential', originPath=datapath)

print(trials)

# ----------------------------------------------
# START THE EXPERIMENT
# ----------------------------------------------

# Initialize two clocks:
# - for image change time
# - for response time
change_clock = core.Clock()
rt_clock = core.Clock()
trial_clock = core.Clock()

event_list = []
trial_clock.reset()
for trial in trials:
    # Display trial start text
    start_message.draw()
    window.flip()

    # Wait for a spacebar press to start trial or escape to quit
    keys = event.waitKeys(keyList=['space', 'escape'])

    # Set clocks to 0
    change_clock.reset()
    rt_clock.reset()

    # display image for 4 seconds
    # Set the images and orientation (?)
    im_fname = os.path.join(impath, trial['im'])
    bitmap1.setImage(im_fname + suffix)
    bitmap1.setOri(trial['ori'])
    # display image
    bitmap1.draw()
    window.flip()
    # Record start-time
    event_list.append([trial['im'], trial_clock.getTime()])
    # Wait 4 seconds
    core.wait(4)

    # Blank screen for 2 sec
    window.flip(clearBuffer=True)
    # Record
    event_list.append(['blank screen', trial_clock.getTime()])
    # Wait 2 seconds
    core.wait(2)

    # Fixation cross for 2 seconds
    im_fname = os.path.join(impath, 'cross')
    bitmap1.setImage(im_fname + suffix)
    bitmap1.setOri(0)
    # display cross
    bitmap1.draw()
    window.flip()
    # Record
    event_list.append(['cross', trial_clock.getTime()])
    # Wait 2 seconds
    core.wait(2)

    print(event_list)
    # Advance to the next trial

# ----------------------------------------------
# END THE EXPERIMENT
# ----------------------------------------------

# Save all data to a file
trials.saveAsWideText(data_fname + '.csv', delim=',')

# Quit the experiment
