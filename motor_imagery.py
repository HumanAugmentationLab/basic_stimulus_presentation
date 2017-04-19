# GOAL: cue task 4s, 2s blank screen, 2s fixation cross, 15s of trial, 15s of break
# CUES: acoustic stimuli (left/right) duration 1.5-8s

import os
from psychopy import data, visual, gui, core, event
# ------------------------------------
# EXPERIMENT SETTINGS
# ------------------------------------


class Experiment:
    def __init__(self):
        self.datapath = 'data'            # directory to save data
        self.impath = 'images'            # directory where images can be found
        self.suffix = '.png'              # suffix for images
        self.scrnsize = (1200, 800)       # screen size in pixels
        self.timelimit = 4                # image freezing time in seconds
        self.changetime = .5              # image changing time in seconds
        self.num_trials = 6               # number of trials before break
        self.break_time = 15              # number of seconds for break
        self.event_list = []
        self.trial_clock = core.Clock()

# ----------------------------------------------
# STORE INFORMATION ABOUT THE EXPERIMENT SESSION
# ----------------------------------------------
    def set_imlist(self, trial_duration, num_trials=1):
        '''makes the trial the correct duration'''
        self.imlist = []
        trial_number = trial_duration // 8
        for n in range(num_trials):
            trial_list = []
            for i in range(trial_number):
                trial_list.append('left')
                trial_list.append('right')
            self.imlist.append(trial_list)

    def store_info(self, exp_name):
        self.exp_info = {'participant': '',
                         'gender': ('male', 'female', 'other'),
                         'age': '',
                         'left-handed': False}

        # Get subject name, gender, age, handedness through a dialog box
        # (see http://www.psychopy.org/api/gui.html)
        dlg = gui.DlgFromDict(dictionary=self.exp_info, title=exp_name)

        # If 'Cancel' is pressed, quit
        if not dlg.OK:
            core.quit()

        # Get date and time and store this information as general session info
        self.exp_info['date'] = data.getDateStr()
        self.exp_info['exp_name'] = exp_name

        # Check for datapath directory
        if not os.path.isdir(self.datapath):
            os.makedirs(self.datapath)

        # Create a unique filename for the experiment data
        data_fname = self.exp_info['participant'] + '_' + self.exp_info['date']
        data_fname = os.path.join(self.datapath, data_fname)

# ----------------------------------------------
# PREPARE CONDTIONS LIST
# ----------------------------------------------

    def prep_cond_list(self):
        # Check if all images exist
        for im in self.imlist:
            for i in im:
                print(i)
                im_fname = os.path.join(self.impath, i + self.suffix)
                if not os.path.exists(im_fname):
                    raise Exception('Image files not fond in image folder: '
                                    + str(im))

        # TODO: find a way to define a set image order

        self.orilist = [0, 0, 0]

# ----------------------------------------------
# CREATION OF WINDOW AND STIMULI
# ----------------------------------------------
    def make_window(self):
        # Open a window
        self.window = visual.Window(size=self.scrnsize, color='black', units='pix',
                                    fullscr=False)

        # Define trial start text
        text = "Press spacebar to start the trial"
        self.start_message = visual.TextStim(self.window, text=text,
                                             color='red', height=20)

        # Define the bitmap stimuli (contents can still change)
        self.bitmap1 = visual.ImageStim(self.window, size=self.scrnsize)
        self.bitmap2 = visual.ImageStim(self.window, size=self.scrnsize)

# ----------------------------------------------
# DEFINE A TRIAL SEQUENCE
# ----------------------------------------------

# Define a list of trials with their properties:
#   - Which image (without the suffix)
#   - Which orientation

# TODO: stim_order list, orientations?
    def make_trial_seq(self):
        stim_order = []
        for im, ori in zip(self.imlist, self.orilist):
            stim_order.append({'im': im, 'ori': ori})
        print(stim_order)

        self.trials = data.TrialHandler(stim_order, nReps=2,
                                        extraInfo=self.exp_info,
                                        method='sequential',
                                        originPath=self.datapath)

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
        self.bitmap1.setImage(im_fname + self.suffix)
        self.bitmap1.setOri(ori)
        # display image
        self.bitmap1.draw()
        self.window.flip()
        # Record start-time
        self.event_list.append([im_name, self.trial_clock.getTime()])
        # Wait 4 seconds
        core.wait(duration)

    def blank_screen(self, duration=0):
        self.window.flip(clearBuffer=True)
        # Record
        self.event_list.append(['blank screen', self.trial_clock.getTime()])
        # Wait 2 seconds
        core.wait(duration)

    def run_trial(self):
        self.trial_clock.reset()
        for trial in self.trials:
            # Display trial start text
            self.start_message.draw()
            self.window.flip()
            # Wait for a spacebar press to start trial or escape to quit
            self.keys = event.waitKeys(keyList=['space', 'escape'])
            
            for im in trial['im']:


                # display image for 4 seconds
                self.disp_im(im, ori=trial['ori'], duration=4)

                # Blank screen for 2 sec
                self.blank_screen(duration=2)

                # Fixation cross for 2 seconds
                self.disp_im('cross', duration=2)

                self.trials.addData('event times', self.event_list)
                print(self.event_list)
                # Advance to the next trial

# ----------------------------------------------
# END THE EXPERIMENT
# ----------------------------------------------

# Save all data to a file
    def save_data(self):
        self.trials.saveAsWideText(self.data_fname + '.csv', delim=',')

# Quit the experiment

    def prep_exp(self):
        self.set_imlist(trial_duration=200)
        self.store_info('Motor Imagery')
        self.prep_cond_list()
        self.make_window()
        self.make_trial_seq()

    def run_experiment(self):
        self.prep_exp()
        self.run_trial()


if __name__ == "__main__":
    exp = Experiment()
    exp.run_experiment()
