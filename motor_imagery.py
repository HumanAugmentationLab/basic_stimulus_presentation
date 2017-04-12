# GOAL: cue task 4s, 2s blank screen, 2s fixation cross, 15s of trial, 15s of break
# CUES: acoustic stimuli (left/right) duration 1.5-8s

import os
from psychopy import data, visual, gui, core, event
from PIL import Image
# ------------------------------------
# EXPERIMENT SETTINGS
# ------------------------------------


class Experiment:
    def __init__(self):
        self.datapath = 'data'                    # directory to save data
        self.impath = 'images'                    # directory where images can be found
        self.imlist = ['left', 'right']           # image names without suffixes
        self.suffix = '.png'                      # suffix for images
        self.scrnsize = (1200, 800)               # screen size in pixels
        self.timelimit = 4                        # image freezing time in seconds
        self.changetime = .5                      # image changing time in seconds
        self.num_trials = 6                       # number of trials before break
        self.break_time = 15                      # number of seconds for break
        self.event_list = []
        self.trial_clock = core.Clock()

# ----------------------------------------------
# STORE INFORMATION ABOUT THE EXPERIMENT SESSION
# ----------------------------------------------
    def store_info(self, exp_name):
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
        if not os.path.isdir(self.datapath):
            os.makedirs(self.datapath)

        # Create a unique filename for the experiment data
        data_fname = exp_info['participant'] + '_' + exp_info['date']
        data_fname = os.path.join(datapath, data_fname)

# ----------------------------------------------
# PREPARE CONDTIONS LIST
# ----------------------------------------------

    def prep_cond_list(self):
        # Check if all images exist
        for im in self.imlist:
            im_fname = os.path.join(impath, im+suffix)
            if not os.path.exists(im_fname):
                raise Exception('Image files not fond in image folder: ' + str(im))

        # TODO: find a way to define a set image order

        orilist = [0, 0, 0]

# ----------------------------------------------
# CREATION OF WINDOW AND STIMULI
# ----------------------------------------------
    def make_window(self):
        # Open a window
        window = visual.Window(size=scrnsize, color='black', units='pix',
                               fullscr=False)

        # Define trial start text
        text = "Press spacebar to start the trial"
        start_message = visual.TextStim(window, text=text, color='red', height=20)

        # Define the bitmap stimuli (contents can still change)
        bitmap1 = visual.ImageStim(window, size=scrnsize)
        bitmap2 = visual.ImageStim(window, size=scrnsize)`

# ----------------------------------------------
# DEFINE A TRIAL SEQUENCE
# ----------------------------------------------

# Define a list of trials with their properties:
#   - Which image (without the suffix)
#   - Which orientation

# TODO: stim_order list, orientations?
    def make_trial_seq(self):
        stim_order = []
        for im, ori in zip(imlist, orilist):
            stim_order.append({'im': im, 'ori': ori})
        print(stim_order)

        self.trials = data.TrialHandler(stim_order, nReps=2, extraInfo=exp_info,
                                        method='sequential', originPath=datapath)

        print(self.trials)

# ----------------------------------------------
# START THE EXPERIMENT
# ----------------------------------------------

# Initialize two clocks:
# - for image change time
# - for response time
    def disp_im(self, im_name, ori=0, duration=0):
        '''displays image (im_name) on screen with orientation (ori) in degrees,
        and leaves it on the screen for (duration) in seconds'''
        im_fname = os.path.join(self.impath, im_name)
        bitmap1.setImage(im_fname + suffix)
        bitmap1.setOri(ori)
        # display image
        bitmap1.draw()
        window.flip()
        # Record start-time
        self.event_list.append([im_name, trial_clock.getTime()])
        # Wait 4 seconds
        core.wait(duration)

    def blank_screen(duration=0):
        window.flip(clearBuffer=True)
        # Record
        self.event_list.append(['blank screen', trial_clock.getTime()])
        # Wait 2 seconds
        core.wait(duration)

    def run_trial(self):
        trial_clock.reset()
        for trial in self.trials:
            # Display trial start text
            start_message.draw()
            window.flip()

            # Wait for a spacebar press to start trial or escape to quit
            keys = event.waitKeys(keyList=['space', 'escape'])

            # display image for 4 seconds
            self.disp_im(trial['im'], ori=trial['ori'], duration=4)

            # Blank screen for 2 sec
            self.blank_screen(duration=2)

            # Fixation cross for 2 seconds
            self.disp_im('cross', duration=2)
            im_fname = os.path.join(impath, 'cross')

            self.trials.addData('event times', event_list)
            print(event_list)
            # Advance to the next trial

# ----------------------------------------------
# END THE EXPERIMENT
# ----------------------------------------------

# Save all data to a file
    def save_data(self):
        self.trials.saveAsWideText(data_fname + '.csv', delim=',')

# Quit the experiment

    def prep_exp(self):
        self.store_info('Motor Imagery')
        self.prep_cond_list()
        self.make_window()
        self.make_trial_seq()

    def run_experiment(self):
        self.prep_exp()
        self.run_trial()
