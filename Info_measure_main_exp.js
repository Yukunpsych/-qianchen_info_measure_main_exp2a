/****************************** 
 * Info_Measure_Main_Exp Test *
 ******************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.5.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'Info_measure_main_exp';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from Ini_code
/* Syntax Error: Fix Python code */
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(StartupRoutineBegin());
flowScheduler.add(StartupRoutineEachFrame());
flowScheduler.add(StartupRoutineEnd());
flowScheduler.add(StimSetUpRoutineBegin());
flowScheduler.add(StimSetUpRoutineEachFrame());
flowScheduler.add(StimSetUpRoutineEnd());
flowScheduler.add(ConsentRoutineBegin());
flowScheduler.add(ConsentRoutineEachFrame());
flowScheduler.add(ConsentRoutineEnd());
flowScheduler.add(instruction_1RoutineBegin());
flowScheduler.add(instruction_1RoutineEachFrame());
flowScheduler.add(instruction_1RoutineEnd());
flowScheduler.add(instruction_2RoutineBegin());
flowScheduler.add(instruction_2RoutineEachFrame());
flowScheduler.add(instruction_2RoutineEnd());
flowScheduler.add(instruction_3RoutineBegin());
flowScheduler.add(instruction_3RoutineEachFrame());
flowScheduler.add(instruction_3RoutineEnd());
flowScheduler.add(instruction_4RoutineBegin());
flowScheduler.add(instruction_4RoutineEachFrame());
flowScheduler.add(instruction_4RoutineEnd());
flowScheduler.add(instruction_5RoutineBegin());
flowScheduler.add(instruction_5RoutineEachFrame());
flowScheduler.add(instruction_5RoutineEnd());
flowScheduler.add(begin_practiceRoutineBegin());
flowScheduler.add(begin_practiceRoutineEachFrame());
flowScheduler.add(begin_practiceRoutineEnd());
const prac_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(prac_loopLoopBegin(prac_loopLoopScheduler));
flowScheduler.add(prac_loopLoopScheduler);
flowScheduler.add(prac_loopLoopEnd);
flowScheduler.add(begin_taskRoutineBegin());
flowScheduler.add(begin_taskRoutineEachFrame());
flowScheduler.add(begin_taskRoutineEnd());
const first_pass_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(first_pass_loopLoopBegin(first_pass_loopLoopScheduler));
flowScheduler.add(first_pass_loopLoopScheduler);
flowScheduler.add(first_pass_loopLoopEnd);
const double_pass_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(double_pass_loopLoopBegin(double_pass_loopLoopScheduler));
flowScheduler.add(double_pass_loopLoopScheduler);
flowScheduler.add(double_pass_loopLoopEnd);
flowScheduler.add(end_of_experimentRoutineBegin());
flowScheduler.add(end_of_experimentRoutineEachFrame());
flowScheduler.add(end_of_experimentRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'info_exp_prac_cond.xlsx', 'path': 'info_exp_prac_cond.xlsx'},
    {'name': 'absent_patch/patch0002271.jpg', 'path': 'absent_patch/patch0002271.jpg'},
    {'name': 'absent_patch/patch0002031.jpg', 'path': 'absent_patch/patch0002031.jpg'},
    {'name': 'instructions/instruction_patch_2.mp4', 'path': 'instructions/instruction_patch_2.mp4'},
    {'name': 'masks/mask_003.jpg', 'path': 'masks/mask_003.jpg'},
    {'name': 'Monash_University_logo.svg.png', 'path': 'Monash_University_logo.svg.png'},
    {'name': 'prac_patch/patch0002406.jpg', 'path': 'prac_patch/patch0002406.jpg'},
    {'name': 'masks/mask_004.jpg', 'path': 'masks/mask_004.jpg'},
    {'name': 'instructions/instruction_patch_1.mp4', 'path': 'instructions/instruction_patch_1.mp4'},
    {'name': 'info_exp_patch_3_cond.xlsx', 'path': 'info_exp_patch_3_cond.xlsx'},
    {'name': 'prac_patch/patch0002490.jpg', 'path': 'prac_patch/patch0002490.jpg'},
    {'name': 'masks_cond.xlsx', 'path': 'masks_cond.xlsx'},
    {'name': 'present_patch/cong_131_3_a.jpg', 'path': 'present_patch/cong_131_3_a.jpg'},
    {'name': 'absent_patch/patch0002367.jpg', 'path': 'absent_patch/patch0002367.jpg'},
    {'name': 'masks/mask_001.jpg', 'path': 'masks/mask_001.jpg'},
    {'name': 'instructions/all_patches.png', 'path': 'instructions/all_patches.png'},
    {'name': 'absent_patch/patch0002151.jpg', 'path': 'absent_patch/patch0002151.jpg'},
    {'name': 'prac_patch/patch0002526.jpg', 'path': 'prac_patch/patch0002526.jpg'},
    {'name': 'masks/mask_002.jpg', 'path': 'masks/mask_002.jpg'},
    {'name': 'absent_patch/patch0002043.jpg', 'path': 'absent_patch/patch0002043.jpg'},
    {'name': 'absent_patch/patch0002247.jpg', 'path': 'absent_patch/patch0002247.jpg'},
    {'name': 'instructions/response screen.png', 'path': 'instructions/response screen.png'},
    {'name': 'absent_patch/patch0001947.jpg', 'path': 'absent_patch/patch0001947.jpg'},
    {'name': 'response23.png', 'path': 'response23.png'},
    {'name': 'prac_patch/patch0002370.jpg', 'path': 'prac_patch/patch0002370.jpg'},
    {'name': 'response45.png', 'path': 'response45.png'},
    {'name': 'absent_patch/patch0002163.jpg', 'path': 'absent_patch/patch0002163.jpg'},
    {'name': 'absent_patch/patch0002223.jpg', 'path': 'absent_patch/patch0002223.jpg'},
    {'name': 'instructions/response screen 2.png', 'path': 'instructions/response screen 2.png'},
    {'name': 'absent_patch/patch0002211.jpg', 'path': 'absent_patch/patch0002211.jpg'},
    {'name': 'absent_patch/patch0002175.jpg', 'path': 'absent_patch/patch0002175.jpg'},
    {'name': 'masks/mask_005.jpg', 'path': 'masks/mask_005.jpg'},
    {'name': 'absent_patch/patch0002283.jpg', 'path': 'absent_patch/patch0002283.jpg'},
    {'name': 'prac_patch/patch0002514.jpg', 'path': 'prac_patch/patch0002514.jpg'},
    {'name': 'absent_patch/patch0001995.jpg', 'path': 'absent_patch/patch0001995.jpg'},
    {'name': 'absent_patch/patch0002079.jpg', 'path': 'absent_patch/patch0002079.jpg'},
    {'name': 'response67.png', 'path': 'response67.png'},
    {'name': 'response01.png', 'path': 'response01.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.5';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}


var StartupClock;
var win_pix_x;
var win_pix_y;
var StimSetUpClock;
var fixation_cross_duration;
var image_duration;
var exit_message_duration;
var feedback_square_width;
var response_feedback_time;
var a;
var b;
var trialnumber;
var alltrials;
var ConsentClock;
var consent_text;
var monash_logo;
var key_resp;
var instruction_1Clock;
var instruction_1_text;
var all_patches;
var space_press_continue;
var press_space_continue;
var Esc_exit;
var instruction_2Clock;
var instruction_text_2;
var space_press_continue_2;
var press_space_continue_2;
var Esc_exit_2;
var instruction_3Clock;
var instruction_text_3;
var space_press_continue_3;
var press_space_continue_3;
var Esc_exit_3;
var instruction_4Clock;
var instruction_text_4;
var use_all_numbers;
var response_screen_intr;
var space_press_continue_4;
var space_continue_low;
var Esc_exit_4;
var instruction_5Clock;
var instruction_text_5;
var response_screen_after;
var space_press_continue_5;
var space_continue_low_2;
var Esc_exit_5;
var begin_practiceClock;
var prac_begin_text;
var prac_begin_space;
var space_press_continue_6;
var Esc_exit_6;
var prac_patch_1Clock;
var fixation_cross;
var practice_patch_1;
var Esc_exit_13;
var maskClock;
var mask_image;
var Esc_exit_14;
var prac_patch_2Clock;
var fixation_cross_3;
var practice_patch_2;
var Esc_exit_12;
var prac_responseClock;
var mouse_2;
var response1disk_3;
var response5disk_3;
var response3disk_3;
var response7disk_3;
var text;
var most_similar_3;
var most_different_3;
var Esc_exit_7;
var resposne_feedbackClock;
var text_55;
var text_56;
var Esc_exit_8;
var prac_correct_mouseClock;
var mouse_12;
var response1disk_4;
var response3disk_4;
var response5disk_4;
var response7disk_4;
var text_52;
var center_square_2;
var most_similar_4;
var most_different_4;
var Esc_exit_9;
var begin_taskClock;
var mouse_1;
var begin_mouse_center;
var Esc_exit_15;
var space_press_continue_7;
var patch_1Clock;
var fixation_cross_1;
var first_patch;
var Esc_exit_16;
var patch_2Clock;
var fixation_cross_2;
var second_patch;
var Esc_exit_17;
var responseClock;
var mouse;
var response1disk;
var response3disk;
var response5disk;
var response7disk;
var text_23;
var most_similar;
var most_different;
var Esc_exit_10;
var correct_mouseClock;
var mouse_11;
var response1disk_2;
var response3disk_2;
var response5disk_2;
var response7disk_2;
var text_51;
var center_square;
var most_similar_2;
var most_different_2;
var trial_text_2;
var Esc_exit_11;
var response_2Clock;
var mouse_3;
var response1disk_5;
var response3disk_5;
var response5disk_5;
var response7disk_5;
var text_24;
var most_similar_5;
var most_different_5;
var Esc_exit_18;
var end_of_experimentClock;
var thank_you;
var space_exit;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Startup"
  StartupClock = new util.Clock();
  // Run 'Begin Experiment' code from Python_initialisation
  win_pix_x = psychoJS.window.size[0];
  win_pix_y = psychoJS.window.size[1];
  
  // Initialize components for Routine "StimSetUp"
  StimSetUpClock = new util.Clock();
  // Run 'Begin Experiment' code from Ini_code
  fixation_cross_duration = 0.5;
  image_duration = 0.15;
  exit_message_duration = (fixation_cross_duration + image_duration);
  feedback_square_width = 0.03;
  response_feedback_time = 4;
  win_pix_x = psychoJS.window.size[0];
  win_pix_y = psychoJS.window.size[1];
  a = ((win_pix_y * 0.75) / 6);
  b = ((win_pix_y * 0.75) / 3);
  trialnumber = 0;
  alltrials = 240;
  
  // Initialize components for Routine "Consent"
  ConsentClock = new util.Clock();
  consent_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'consent_text',
    text: 'This is an Informed Consent Form. Please read and understand the statements below.\n\n1, I understand that my taking part in the study is voluntary and that I am free to leave the study at any time, without giving any reason. I understand that my medical care or legal rights will not be affected in any way.\n\n2, I agree to the use and release of study-related information about me for the purposes described in this Informed Consent Form.\n\n3, I agree to the re-use of data collected in this study for future studies in a de-identified manner as described in this Informed Consent form.\n\n4, I understand that my consent continues until and unless I withdraw my consent that can be done at any time by giving notice to the investigator. I understand that if I withdraw my consent I will not be able to continue to take part in the study.\n\n5, I understand that if I withdraw consent, the study researchers will no longer use or release information that identifies me in connection with the study unless it is needed to keep the scientific quality of the study. I understand that if I withdraw consent the study researchers may still use any study-related information about me that was collected before I withdrew consent.\n\n6, I have read and I understand the information provided in this Informed Consent Form. I have had the opportunity to ask questions and have had these questions answered satisfactorily.\n\n7, I have had time to consider the information provided in this Informed Consent Form to consider answers to my questions, and to consider whether I wish to take part in the study.\n\nIf you understand the statements above, and freely consent to participate in the study, press [Space] to begin the experiment.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  monash_logo = new visual.ImageStim({
    win : psychoJS.window,
    name : 'monash_logo', units : 'pix', 
    image : 'Monash_University_logo.svg.png', mask : undefined,
    ori : 0.0, pos : [0, ((win_pix_y * 1.2) / 3)], size : [250, 125],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction_1"
  instruction_1Clock = new util.Clock();
  instruction_1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_1_text',
    text: 'Welcome to our experiment!\n\nIn this experiment, you will see the following images, and will be asked to report how similar these images are to each other.  ',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  all_patches = new visual.ImageStim({
    win : psychoJS.window,
    name : 'all_patches', units : 'norm', 
    image : 'instructions/all_patches.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.1)], size : [0.7, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  space_press_continue = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  press_space_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'press_space_continue',
    text: 'Press <space> to continue',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.6)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -3.0 
  });
  
  Esc_exit = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "instruction_2"
  instruction_2Clock = new util.Clock();
  instruction_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_text_2',
    text: 'In each trial of this experiment, you are first asked to fixate on the cross appearing in the middle of the screen.\n\nThen, a small image will appear, which will be quickly masked.\n\nNOTE: The image will be presented for a slightly shorter time in the actual experiment.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  space_press_continue_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  press_space_continue_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'press_space_continue_2',
    text: 'Press <space> to continue',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -3.0 
  });
  
  Esc_exit_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_2',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "instruction_3"
  instruction_3Clock = new util.Clock();
  instruction_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_text_3',
    text: 'Then, the cross will appear again, which is followed by a second image and the masks. \n\nNOTE: The image will be presented for a slightly shorter time in the actual experiment.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  space_press_continue_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  press_space_continue_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'press_space_continue_3',
    text: 'Press <space> to continue',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -3.0 
  });
  
  Esc_exit_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_3',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "instruction_4"
  instruction_4Clock = new util.Clock();
  instruction_text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_text_4',
    text: 'Finally, a response screen will appear. You are asked to rate how similar the two images you just saw are to each other, by choosing one of the numbers on the response screen.\n\n0 =>  most similar\n7 => most different',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.65], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  use_all_numbers = new visual.TextStim({
    win: psychoJS.window,
    name: 'use_all_numbers',
    text: 'NOTE: Some image pairs might be more similar to each other than the other pairs. Therefore, please try to use numbers of the entire scale to express their varying similarity levels. ',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.3], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -1.0 
  });
  
  response_screen_intr = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response_screen_intr', units : 'height', 
    image : 'instructions/response screen.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.15)], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  space_press_continue_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_continue_low = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_continue_low',
    text: 'Press <space> to continue',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -4.0 
  });
  
  Esc_exit_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_4',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -5.0 
  });
  
  // Initialize components for Routine "instruction_5"
  instruction_5Clock = new util.Clock();
  instruction_text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_text_5',
    text: 'After choosing, move your cursor back to the centre and click and hold the yellow square to continue.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  response_screen_after = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response_screen_after', units : 'height', 
    image : 'instructions/response screen 2.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.1)], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  space_press_continue_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_continue_low_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_continue_low_2',
    text: 'Press <space> to continue',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.7)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -3.0 
  });
  
  Esc_exit_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_5',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "begin_practice"
  begin_practiceClock = new util.Clock();
  prac_begin_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'prac_begin_text',
    text: "The entire experiment will take approximately 30 minutes to complete.\n\nNow, let's become familiar with the experiment task with some practice",
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  prac_begin_space = new visual.TextStim({
    win: psychoJS.window,
    name: 'prac_begin_space',
    text: 'Press <space> to begin practice trials',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -1.0 
  });
  
  space_press_continue_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Esc_exit_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_6',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "prac_patch_1"
  prac_patch_1Clock = new util.Clock();
  fixation_cross = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_cross', units : 'pix', 
    vertices: 'cross', size:[30, 30],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  practice_patch_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'practice_patch_1', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [((win_pix_y * 0.75) / 3), ((win_pix_y * 0.75) / 3)],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  Esc_exit_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_13',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "mask"
  maskClock = new util.Clock();
  mask_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mask_image', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [((win_pix_y * 0.75) / 3), ((win_pix_y * 0.75) / 3)],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  Esc_exit_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_14',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "prac_patch_2"
  prac_patch_2Clock = new util.Clock();
  fixation_cross_3 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_cross_3', units : 'pix', 
    vertices: 'cross', size:[30, 30],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  practice_patch_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'practice_patch_2', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [((win_pix_y * 0.75) / 3), ((win_pix_y * 0.75) / 3)],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  Esc_exit_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_12',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "prac_response"
  prac_responseClock = new util.Clock();
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  response1disk_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response1disk_3', units : 'pix', 
    image : 'response67.png', mask : undefined,
    ori : 0, pos : [a, a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  response5disk_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response5disk_3', units : 'pix', 
    image : 'response23.png', mask : undefined,
    ori : 0, pos : [(- a), (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  response3disk_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response3disk_3', units : 'pix', 
    image : 'response45.png', mask : undefined,
    ori : 0, pos : [a, (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  response7disk_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response7disk_3', units : 'pix', 
    image : 'response01.png', mask : undefined,
    ori : 0, pos : [(- a), a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Please rate how similar the two images you just saw are. \n\nPlease click and hold to indicate your choice.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  most_similar_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'most_similar_3',
    text: 'Very similar',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.4), 0.4], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -7.0 
  });
  
  most_different_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'most_different_3',
    text: 'Very different',
    font: 'Arial',
    units: 'norm', 
    pos: [0.4, 0.4], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -8.0 
  });
  
  Esc_exit_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_7',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -9.0 
  });
  
  // Initialize components for Routine "resposne_feedback"
  resposne_feedbackClock = new util.Clock();
  text_55 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_55',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.1,  wrapWidth: 1000, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  text_56 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_56',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.2)], height: 0.1,  wrapWidth: 1000, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  Esc_exit_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_8',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "prac_correct_mouse"
  prac_correct_mouseClock = new util.Clock();
  mouse_12 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_12.mouseClock = new util.Clock();
  response1disk_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response1disk_4', units : 'pix', 
    image : 'response67.png', mask : undefined,
    ori : 0, pos : [a, a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  response3disk_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response3disk_4', units : 'pix', 
    image : 'response45.png', mask : undefined,
    ori : 0, pos : [a, (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  response5disk_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response5disk_4', units : 'pix', 
    image : 'response23.png', mask : undefined,
    ori : 0, pos : [(- a), (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  response7disk_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response7disk_4', units : 'pix', 
    image : 'response01.png', mask : undefined,
    ori : 0, pos : [(- a), a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  text_52 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_52',
    text: 'Please click and hold the yellow square in the middle of the response numbers to continue',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.7)], height: 0.07,  wrapWidth: 1000, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: 1,
    depth: -5.0 
  });
  
  center_square_2 = new visual.Rect ({
    win: psychoJS.window, name: 'center_square_2', units : 'pix', 
    width: [((win_pix_y * 0.75) / 20), ((win_pix_y * 0.75) / 20)][0], height: [((win_pix_y * 0.75) / 20), ((win_pix_y * 0.75) / 20)][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('yellow'),
    fillColor: new util.Color('yellow'),
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  most_similar_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'most_similar_4',
    text: 'Very similar',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.4), 0.4], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -7.0 
  });
  
  most_different_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'most_different_4',
    text: 'Very different',
    font: 'Arial',
    units: 'norm', 
    pos: [0.4, 0.4], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -8.0 
  });
  
  Esc_exit_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_9',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -9.0 
  });
  
  // Initialize components for Routine "begin_task"
  begin_taskClock = new util.Clock();
  mouse_1 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_1.mouseClock = new util.Clock();
  begin_mouse_center = new visual.TextStim({
    win: psychoJS.window,
    name: 'begin_mouse_center',
    text: 'This is the end of the practice trials. Press <space> to begin the main experiment.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  Esc_exit_15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_15',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -2.0 
  });
  
  space_press_continue_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "patch_1"
  patch_1Clock = new util.Clock();
  fixation_cross_1 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_cross_1', units : 'pix', 
    vertices: 'cross', size:[30, 30],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  first_patch = new visual.ImageStim({
    win : psychoJS.window,
    name : 'first_patch', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [((win_pix_y * 0.75) / 3), ((win_pix_y * 0.75) / 3)],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  Esc_exit_16 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_16',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "patch_2"
  patch_2Clock = new util.Clock();
  fixation_cross_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_cross_2', units : 'pix', 
    vertices: 'cross', size:[30, 30],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  second_patch = new visual.ImageStim({
    win : psychoJS.window,
    name : 'second_patch', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [((win_pix_y * 0.75) / 3), ((win_pix_y * 0.75) / 3)],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  Esc_exit_17 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_17',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "response"
  responseClock = new util.Clock();
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  response1disk = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response1disk', units : 'pix', 
    image : 'response67.png', mask : undefined,
    ori : 0, pos : [a, a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  response3disk = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response3disk', units : 'pix', 
    image : 'response45.png', mask : undefined,
    ori : 0, pos : [a, (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  response5disk = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response5disk', units : 'pix', 
    image : 'response23.png', mask : undefined,
    ori : 0, pos : [(- a), (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  response7disk = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response7disk', units : 'pix', 
    image : 'response01.png', mask : undefined,
    ori : 0, pos : [(- a), a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  text_23 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_23',
    text: 'Please rate how similar the two images you just saw are. \n\nPlease click and hold to indicate your choice.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  most_similar = new visual.TextStim({
    win: psychoJS.window,
    name: 'most_similar',
    text: 'Very similar',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.4), 0.4], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -7.0 
  });
  
  most_different = new visual.TextStim({
    win: psychoJS.window,
    name: 'most_different',
    text: 'Very different',
    font: 'Arial',
    units: 'norm', 
    pos: [0.4, 0.4], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -8.0 
  });
  
  Esc_exit_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_10',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -9.0 
  });
  
  // Initialize components for Routine "correct_mouse"
  correct_mouseClock = new util.Clock();
  mouse_11 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_11.mouseClock = new util.Clock();
  response1disk_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response1disk_2', units : 'pix', 
    image : 'response67.png', mask : undefined,
    ori : 0, pos : [a, a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  response3disk_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response3disk_2', units : 'pix', 
    image : 'response45.png', mask : undefined,
    ori : 0, pos : [a, (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  response5disk_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response5disk_2', units : 'pix', 
    image : 'response23.png', mask : undefined,
    ori : 0, pos : [(- a), (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  response7disk_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response7disk_2', units : 'pix', 
    image : 'response01.png', mask : undefined,
    ori : 0, pos : [(- a), a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  text_51 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_51',
    text: 'Please click and hold the yellow square in the middle of the response numbers to continue',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.6)], height: 0.07,  wrapWidth: 1000, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: 1,
    depth: -5.0 
  });
  
  center_square = new visual.Rect ({
    win: psychoJS.window, name: 'center_square', units : 'pix', 
    width: [((win_pix_y * 0.75) / 20), ((win_pix_y * 0.75) / 20)][0], height: [((win_pix_y * 0.75) / 20), ((win_pix_y * 0.75) / 20)][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('yellow'),
    fillColor: new util.Color('yellow'),
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  most_similar_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'most_similar_2',
    text: 'Very similar',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.4), 0.4], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -7.0 
  });
  
  most_different_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'most_different_2',
    text: 'Very different',
    font: 'Arial',
    units: 'norm', 
    pos: [0.4, 0.4], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -8.0 
  });
  
  trial_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trial_text_2',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  Esc_exit_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_11',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -10.0 
  });
  
  // Initialize components for Routine "response_2"
  response_2Clock = new util.Clock();
  mouse_3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_3.mouseClock = new util.Clock();
  response1disk_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response1disk_5', units : 'pix', 
    image : 'response67.png', mask : undefined,
    ori : 0, pos : [a, a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  response3disk_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response3disk_5', units : 'pix', 
    image : 'response45.png', mask : undefined,
    ori : 0, pos : [a, (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  response5disk_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response5disk_5', units : 'pix', 
    image : 'response23.png', mask : undefined,
    ori : 0, pos : [(- a), (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  response7disk_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response7disk_5', units : 'pix', 
    image : 'response01.png', mask : undefined,
    ori : 0, pos : [(- a), a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  text_24 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_24',
    text: 'Please rate how similar the two images you just saw are. \n\nPlease click and hold to indicate your choice.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  most_similar_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'most_similar_5',
    text: 'Very similar',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.4), 0.4], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -7.0 
  });
  
  most_different_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'most_different_5',
    text: 'Very different',
    font: 'Arial',
    units: 'norm', 
    pos: [0.4, 0.4], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -8.0 
  });
  
  Esc_exit_18 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Esc_exit_18',
    text: 'Press <Esc> to exit experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('aqua'),  opacity: undefined,
    depth: -9.0 
  });
  
  // Initialize components for Routine "end_of_experiment"
  end_of_experimentClock = new util.Clock();
  thank_you = new visual.TextStim({
    win: psychoJS.window,
    name: 'thank_you',
    text: 'Thank you for your participation! Your responses have been recorded.\n\nPress <space> to exit experiment',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  space_exit = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var StartupComponents;
function StartupRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Startup' ---
    t = 0;
    StartupClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    StartupComponents = [];
    
    for (const thisComponent of StartupComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function StartupRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Startup' ---
    // get current time
    t = StartupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of StartupComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function StartupRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Startup' ---
    for (const thisComponent of StartupComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Startup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var StimSetUpComponents;
function StimSetUpRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'StimSetUp' ---
    t = 0;
    StimSetUpClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    StimSetUpComponents = [];
    
    for (const thisComponent of StimSetUpComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function StimSetUpRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'StimSetUp' ---
    // get current time
    t = StimSetUpClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of StimSetUpComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function StimSetUpRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'StimSetUp' ---
    for (const thisComponent of StimSetUpComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "StimSetUp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var ConsentComponents;
function ConsentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Consent' ---
    t = 0;
    ConsentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    ConsentComponents = [];
    ConsentComponents.push(consent_text);
    ConsentComponents.push(monash_logo);
    ConsentComponents.push(key_resp);
    
    for (const thisComponent of ConsentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ConsentRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Consent' ---
    // get current time
    t = ConsentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *consent_text* updates
    if (t >= 0.0 && consent_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consent_text.tStart = t;  // (not accounting for frame time here)
      consent_text.frameNStart = frameN;  // exact frame index
      
      consent_text.setAutoDraw(true);
    }

    
    // *monash_logo* updates
    if (t >= 0.0 && monash_logo.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      monash_logo.tStart = t;  // (not accounting for frame time here)
      monash_logo.frameNStart = frameN;  // exact frame index
      
      monash_logo.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ConsentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ConsentRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Consent' ---
    for (const thisComponent of ConsentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "Consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _space_press_continue_allKeys;
var instruction_1Components;
function instruction_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction_1' ---
    t = 0;
    instruction_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    space_press_continue.keys = undefined;
    space_press_continue.rt = undefined;
    _space_press_continue_allKeys = [];
    // keep track of which components have finished
    instruction_1Components = [];
    instruction_1Components.push(instruction_1_text);
    instruction_1Components.push(all_patches);
    instruction_1Components.push(space_press_continue);
    instruction_1Components.push(press_space_continue);
    instruction_1Components.push(Esc_exit);
    
    for (const thisComponent of instruction_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instruction_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction_1' ---
    // get current time
    t = instruction_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction_1_text* updates
    if (t >= 0.0 && instruction_1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_1_text.tStart = t;  // (not accounting for frame time here)
      instruction_1_text.frameNStart = frameN;  // exact frame index
      
      instruction_1_text.setAutoDraw(true);
    }

    
    // *all_patches* updates
    if (t >= 0.0 && all_patches.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      all_patches.tStart = t;  // (not accounting for frame time here)
      all_patches.frameNStart = frameN;  // exact frame index
      
      all_patches.setAutoDraw(true);
    }

    
    // *space_press_continue* updates
    if (t >= 0.0 && space_press_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_press_continue.tStart = t;  // (not accounting for frame time here)
      space_press_continue.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_press_continue.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_press_continue.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_press_continue.clearEvents(); });
    }

    if (space_press_continue.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_press_continue.getKeys({keyList: ['space'], waitRelease: false});
      _space_press_continue_allKeys = _space_press_continue_allKeys.concat(theseKeys);
      if (_space_press_continue_allKeys.length > 0) {
        space_press_continue.keys = _space_press_continue_allKeys[_space_press_continue_allKeys.length - 1].name;  // just the last key pressed
        space_press_continue.rt = _space_press_continue_allKeys[_space_press_continue_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *press_space_continue* updates
    if (t >= 0.0 && press_space_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      press_space_continue.tStart = t;  // (not accounting for frame time here)
      press_space_continue.frameNStart = frameN;  // exact frame index
      
      press_space_continue.setAutoDraw(true);
    }

    
    // *Esc_exit* updates
    if (t >= 0.0 && Esc_exit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit.tStart = t;  // (not accounting for frame time here)
      Esc_exit.frameNStart = frameN;  // exact frame index
      
      Esc_exit.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instruction_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instruction_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction_1' ---
    for (const thisComponent of instruction_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_press_continue.corr, level);
    }
    psychoJS.experiment.addData('space_press_continue.keys', space_press_continue.keys);
    if (typeof space_press_continue.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_press_continue.rt', space_press_continue.rt);
        routineTimer.reset();
        }
    
    space_press_continue.stop();
    // the Routine "instruction_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var patch_1_movieClock;
var patch_1_movie;
var _space_press_continue_2_allKeys;
var instruction_2Components;
function instruction_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction_2' ---
    t = 0;
    instruction_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    patch_1_movieClock = new util.Clock();
    patch_1_movie = new visual.MovieStim({
      win: psychoJS.window,
      name: 'patch_1_movie',
      units: 'norm',
      movie: 'instructions/instruction_patch_1.mp4',
      pos: [0, (- 0.1)],
      size: [0.5, 0.68],
      ori: 0.0,
      opacity: 1.0,
      loop: true,
      noAudio: false,
      });
    space_press_continue_2.keys = undefined;
    space_press_continue_2.rt = undefined;
    _space_press_continue_2_allKeys = [];
    // keep track of which components have finished
    instruction_2Components = [];
    instruction_2Components.push(instruction_text_2);
    instruction_2Components.push(patch_1_movie);
    instruction_2Components.push(space_press_continue_2);
    instruction_2Components.push(press_space_continue_2);
    instruction_2Components.push(Esc_exit_2);
    
    for (const thisComponent of instruction_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instruction_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction_2' ---
    // get current time
    t = instruction_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction_text_2* updates
    if (t >= 0.0 && instruction_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_text_2.tStart = t;  // (not accounting for frame time here)
      instruction_text_2.frameNStart = frameN;  // exact frame index
      
      instruction_text_2.setAutoDraw(true);
    }

    
    // *patch_1_movie* updates
    if (t >= 0.0 && patch_1_movie.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      patch_1_movie.tStart = t;  // (not accounting for frame time here)
      patch_1_movie.frameNStart = frameN;  // exact frame index
      
      patch_1_movie.setAutoDraw(true);
      patch_1_movie.play();
    }

    
    // *space_press_continue_2* updates
    if (t >= 0.0 && space_press_continue_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_press_continue_2.tStart = t;  // (not accounting for frame time here)
      space_press_continue_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_press_continue_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_press_continue_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_press_continue_2.clearEvents(); });
    }

    if (space_press_continue_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_press_continue_2.getKeys({keyList: ['space'], waitRelease: false});
      _space_press_continue_2_allKeys = _space_press_continue_2_allKeys.concat(theseKeys);
      if (_space_press_continue_2_allKeys.length > 0) {
        space_press_continue_2.keys = _space_press_continue_2_allKeys[_space_press_continue_2_allKeys.length - 1].name;  // just the last key pressed
        space_press_continue_2.rt = _space_press_continue_2_allKeys[_space_press_continue_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *press_space_continue_2* updates
    if (t >= 0.0 && press_space_continue_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      press_space_continue_2.tStart = t;  // (not accounting for frame time here)
      press_space_continue_2.frameNStart = frameN;  // exact frame index
      
      press_space_continue_2.setAutoDraw(true);
    }

    
    // *Esc_exit_2* updates
    if (t >= 0.0 && Esc_exit_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_2.tStart = t;  // (not accounting for frame time here)
      Esc_exit_2.frameNStart = frameN;  // exact frame index
      
      Esc_exit_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instruction_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instruction_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction_2' ---
    for (const thisComponent of instruction_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    patch_1_movie.stop();
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_press_continue_2.corr, level);
    }
    psychoJS.experiment.addData('space_press_continue_2.keys', space_press_continue_2.keys);
    if (typeof space_press_continue_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_press_continue_2.rt', space_press_continue_2.rt);
        routineTimer.reset();
        }
    
    space_press_continue_2.stop();
    // the Routine "instruction_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var patch_2_movieClock;
var patch_2_movie;
var _space_press_continue_3_allKeys;
var instruction_3Components;
function instruction_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction_3' ---
    t = 0;
    instruction_3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    patch_2_movieClock = new util.Clock();
    patch_2_movie = new visual.MovieStim({
      win: psychoJS.window,
      name: 'patch_2_movie',
      units: 'norm',
      movie: 'instructions/instruction_patch_2.mp4',
      pos: [0, (- 0.1)],
      size: [0.5, 0.68],
      ori: 0.0,
      opacity: 1.0,
      loop: true,
      noAudio: false,
      });
    space_press_continue_3.keys = undefined;
    space_press_continue_3.rt = undefined;
    _space_press_continue_3_allKeys = [];
    // keep track of which components have finished
    instruction_3Components = [];
    instruction_3Components.push(instruction_text_3);
    instruction_3Components.push(patch_2_movie);
    instruction_3Components.push(space_press_continue_3);
    instruction_3Components.push(press_space_continue_3);
    instruction_3Components.push(Esc_exit_3);
    
    for (const thisComponent of instruction_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instruction_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction_3' ---
    // get current time
    t = instruction_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction_text_3* updates
    if (t >= 0.0 && instruction_text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_text_3.tStart = t;  // (not accounting for frame time here)
      instruction_text_3.frameNStart = frameN;  // exact frame index
      
      instruction_text_3.setAutoDraw(true);
    }

    
    // *patch_2_movie* updates
    if (t >= 0.0 && patch_2_movie.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      patch_2_movie.tStart = t;  // (not accounting for frame time here)
      patch_2_movie.frameNStart = frameN;  // exact frame index
      
      patch_2_movie.setAutoDraw(true);
      patch_2_movie.play();
    }

    
    // *space_press_continue_3* updates
    if (t >= 0.0 && space_press_continue_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_press_continue_3.tStart = t;  // (not accounting for frame time here)
      space_press_continue_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_press_continue_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_press_continue_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_press_continue_3.clearEvents(); });
    }

    if (space_press_continue_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_press_continue_3.getKeys({keyList: ['space'], waitRelease: false});
      _space_press_continue_3_allKeys = _space_press_continue_3_allKeys.concat(theseKeys);
      if (_space_press_continue_3_allKeys.length > 0) {
        space_press_continue_3.keys = _space_press_continue_3_allKeys[_space_press_continue_3_allKeys.length - 1].name;  // just the last key pressed
        space_press_continue_3.rt = _space_press_continue_3_allKeys[_space_press_continue_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *press_space_continue_3* updates
    if (t >= 0.0 && press_space_continue_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      press_space_continue_3.tStart = t;  // (not accounting for frame time here)
      press_space_continue_3.frameNStart = frameN;  // exact frame index
      
      press_space_continue_3.setAutoDraw(true);
    }

    
    // *Esc_exit_3* updates
    if (t >= 0.0 && Esc_exit_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_3.tStart = t;  // (not accounting for frame time here)
      Esc_exit_3.frameNStart = frameN;  // exact frame index
      
      Esc_exit_3.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instruction_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instruction_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction_3' ---
    for (const thisComponent of instruction_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    patch_2_movie.stop();
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_press_continue_3.corr, level);
    }
    psychoJS.experiment.addData('space_press_continue_3.keys', space_press_continue_3.keys);
    if (typeof space_press_continue_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_press_continue_3.rt', space_press_continue_3.rt);
        routineTimer.reset();
        }
    
    space_press_continue_3.stop();
    // the Routine "instruction_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _space_press_continue_4_allKeys;
var instruction_4Components;
function instruction_4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction_4' ---
    t = 0;
    instruction_4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    space_press_continue_4.keys = undefined;
    space_press_continue_4.rt = undefined;
    _space_press_continue_4_allKeys = [];
    // keep track of which components have finished
    instruction_4Components = [];
    instruction_4Components.push(instruction_text_4);
    instruction_4Components.push(use_all_numbers);
    instruction_4Components.push(response_screen_intr);
    instruction_4Components.push(space_press_continue_4);
    instruction_4Components.push(space_continue_low);
    instruction_4Components.push(Esc_exit_4);
    
    for (const thisComponent of instruction_4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instruction_4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction_4' ---
    // get current time
    t = instruction_4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction_text_4* updates
    if (t >= 0.0 && instruction_text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_text_4.tStart = t;  // (not accounting for frame time here)
      instruction_text_4.frameNStart = frameN;  // exact frame index
      
      instruction_text_4.setAutoDraw(true);
    }

    
    // *use_all_numbers* updates
    if (t >= 0.0 && use_all_numbers.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      use_all_numbers.tStart = t;  // (not accounting for frame time here)
      use_all_numbers.frameNStart = frameN;  // exact frame index
      
      use_all_numbers.setAutoDraw(true);
    }

    
    // *response_screen_intr* updates
    if (t >= 0.0 && response_screen_intr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response_screen_intr.tStart = t;  // (not accounting for frame time here)
      response_screen_intr.frameNStart = frameN;  // exact frame index
      
      response_screen_intr.setAutoDraw(true);
    }

    
    // *space_press_continue_4* updates
    if (t >= 0.0 && space_press_continue_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_press_continue_4.tStart = t;  // (not accounting for frame time here)
      space_press_continue_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_press_continue_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_press_continue_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_press_continue_4.clearEvents(); });
    }

    if (space_press_continue_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_press_continue_4.getKeys({keyList: ['space'], waitRelease: false});
      _space_press_continue_4_allKeys = _space_press_continue_4_allKeys.concat(theseKeys);
      if (_space_press_continue_4_allKeys.length > 0) {
        space_press_continue_4.keys = _space_press_continue_4_allKeys[_space_press_continue_4_allKeys.length - 1].name;  // just the last key pressed
        space_press_continue_4.rt = _space_press_continue_4_allKeys[_space_press_continue_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_continue_low* updates
    if (t >= 0.0 && space_continue_low.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_continue_low.tStart = t;  // (not accounting for frame time here)
      space_continue_low.frameNStart = frameN;  // exact frame index
      
      space_continue_low.setAutoDraw(true);
    }

    
    // *Esc_exit_4* updates
    if (t >= 0.0 && Esc_exit_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_4.tStart = t;  // (not accounting for frame time here)
      Esc_exit_4.frameNStart = frameN;  // exact frame index
      
      Esc_exit_4.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instruction_4Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instruction_4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction_4' ---
    for (const thisComponent of instruction_4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_press_continue_4.corr, level);
    }
    psychoJS.experiment.addData('space_press_continue_4.keys', space_press_continue_4.keys);
    if (typeof space_press_continue_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_press_continue_4.rt', space_press_continue_4.rt);
        routineTimer.reset();
        }
    
    space_press_continue_4.stop();
    // the Routine "instruction_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _space_press_continue_5_allKeys;
var instruction_5Components;
function instruction_5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction_5' ---
    t = 0;
    instruction_5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    space_press_continue_5.keys = undefined;
    space_press_continue_5.rt = undefined;
    _space_press_continue_5_allKeys = [];
    // keep track of which components have finished
    instruction_5Components = [];
    instruction_5Components.push(instruction_text_5);
    instruction_5Components.push(response_screen_after);
    instruction_5Components.push(space_press_continue_5);
    instruction_5Components.push(space_continue_low_2);
    instruction_5Components.push(Esc_exit_5);
    
    for (const thisComponent of instruction_5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instruction_5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction_5' ---
    // get current time
    t = instruction_5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction_text_5* updates
    if (t >= 0.0 && instruction_text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_text_5.tStart = t;  // (not accounting for frame time here)
      instruction_text_5.frameNStart = frameN;  // exact frame index
      
      instruction_text_5.setAutoDraw(true);
    }

    
    // *response_screen_after* updates
    if (t >= 0.0 && response_screen_after.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response_screen_after.tStart = t;  // (not accounting for frame time here)
      response_screen_after.frameNStart = frameN;  // exact frame index
      
      response_screen_after.setAutoDraw(true);
    }

    
    // *space_press_continue_5* updates
    if (t >= 0.0 && space_press_continue_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_press_continue_5.tStart = t;  // (not accounting for frame time here)
      space_press_continue_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_press_continue_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_press_continue_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_press_continue_5.clearEvents(); });
    }

    if (space_press_continue_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_press_continue_5.getKeys({keyList: ['space'], waitRelease: false});
      _space_press_continue_5_allKeys = _space_press_continue_5_allKeys.concat(theseKeys);
      if (_space_press_continue_5_allKeys.length > 0) {
        space_press_continue_5.keys = _space_press_continue_5_allKeys[_space_press_continue_5_allKeys.length - 1].name;  // just the last key pressed
        space_press_continue_5.rt = _space_press_continue_5_allKeys[_space_press_continue_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_continue_low_2* updates
    if (t >= 0.0 && space_continue_low_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_continue_low_2.tStart = t;  // (not accounting for frame time here)
      space_continue_low_2.frameNStart = frameN;  // exact frame index
      
      space_continue_low_2.setAutoDraw(true);
    }

    
    // *Esc_exit_5* updates
    if (t >= 0.0 && Esc_exit_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_5.tStart = t;  // (not accounting for frame time here)
      Esc_exit_5.frameNStart = frameN;  // exact frame index
      
      Esc_exit_5.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instruction_5Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instruction_5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction_5' ---
    for (const thisComponent of instruction_5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_press_continue_5.corr, level);
    }
    psychoJS.experiment.addData('space_press_continue_5.keys', space_press_continue_5.keys);
    if (typeof space_press_continue_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_press_continue_5.rt', space_press_continue_5.rt);
        routineTimer.reset();
        }
    
    space_press_continue_5.stop();
    // the Routine "instruction_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _space_press_continue_6_allKeys;
var begin_practiceComponents;
function begin_practiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'begin_practice' ---
    t = 0;
    begin_practiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    space_press_continue_6.keys = undefined;
    space_press_continue_6.rt = undefined;
    _space_press_continue_6_allKeys = [];
    // keep track of which components have finished
    begin_practiceComponents = [];
    begin_practiceComponents.push(prac_begin_text);
    begin_practiceComponents.push(prac_begin_space);
    begin_practiceComponents.push(space_press_continue_6);
    begin_practiceComponents.push(Esc_exit_6);
    
    for (const thisComponent of begin_practiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function begin_practiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'begin_practice' ---
    // get current time
    t = begin_practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_begin_text* updates
    if (t >= 0.0 && prac_begin_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_begin_text.tStart = t;  // (not accounting for frame time here)
      prac_begin_text.frameNStart = frameN;  // exact frame index
      
      prac_begin_text.setAutoDraw(true);
    }

    
    // *prac_begin_space* updates
    if (t >= 0.0 && prac_begin_space.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_begin_space.tStart = t;  // (not accounting for frame time here)
      prac_begin_space.frameNStart = frameN;  // exact frame index
      
      prac_begin_space.setAutoDraw(true);
    }

    
    // *space_press_continue_6* updates
    if (t >= 0.0 && space_press_continue_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_press_continue_6.tStart = t;  // (not accounting for frame time here)
      space_press_continue_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_press_continue_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_press_continue_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_press_continue_6.clearEvents(); });
    }

    if (space_press_continue_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_press_continue_6.getKeys({keyList: ['space'], waitRelease: false});
      _space_press_continue_6_allKeys = _space_press_continue_6_allKeys.concat(theseKeys);
      if (_space_press_continue_6_allKeys.length > 0) {
        space_press_continue_6.keys = _space_press_continue_6_allKeys[_space_press_continue_6_allKeys.length - 1].name;  // just the last key pressed
        space_press_continue_6.rt = _space_press_continue_6_allKeys[_space_press_continue_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Esc_exit_6* updates
    if (t >= 0.0 && Esc_exit_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_6.tStart = t;  // (not accounting for frame time here)
      Esc_exit_6.frameNStart = frameN;  // exact frame index
      
      Esc_exit_6.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of begin_practiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function begin_practiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'begin_practice' ---
    for (const thisComponent of begin_practiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_press_continue_6.corr, level);
    }
    psychoJS.experiment.addData('space_press_continue_6.keys', space_press_continue_6.keys);
    if (typeof space_press_continue_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_press_continue_6.rt', space_press_continue_6.rt);
        routineTimer.reset();
        }
    
    space_press_continue_6.stop();
    // the Routine "begin_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var prac_loop;
function prac_loopLoopBegin(prac_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    prac_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'info_exp_prac_cond.xlsx', '0:3'),
      seed: undefined, name: 'prac_loop'
    });
    psychoJS.experiment.addLoop(prac_loop); // add the loop to the experiment
    currentLoop = prac_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPrac_loop of prac_loop) {
      snapshot = prac_loop.getSnapshot();
      prac_loopLoopScheduler.add(importConditions(snapshot));
      prac_loopLoopScheduler.add(prac_patch_1RoutineBegin(snapshot));
      prac_loopLoopScheduler.add(prac_patch_1RoutineEachFrame());
      prac_loopLoopScheduler.add(prac_patch_1RoutineEnd(snapshot));
      const prac_mask_loop_1LoopScheduler = new Scheduler(psychoJS);
      prac_loopLoopScheduler.add(prac_mask_loop_1LoopBegin(prac_mask_loop_1LoopScheduler, snapshot));
      prac_loopLoopScheduler.add(prac_mask_loop_1LoopScheduler);
      prac_loopLoopScheduler.add(prac_mask_loop_1LoopEnd);
      prac_loopLoopScheduler.add(prac_patch_2RoutineBegin(snapshot));
      prac_loopLoopScheduler.add(prac_patch_2RoutineEachFrame());
      prac_loopLoopScheduler.add(prac_patch_2RoutineEnd(snapshot));
      const prac_mask_loop_2LoopScheduler = new Scheduler(psychoJS);
      prac_loopLoopScheduler.add(prac_mask_loop_2LoopBegin(prac_mask_loop_2LoopScheduler, snapshot));
      prac_loopLoopScheduler.add(prac_mask_loop_2LoopScheduler);
      prac_loopLoopScheduler.add(prac_mask_loop_2LoopEnd);
      prac_loopLoopScheduler.add(prac_responseRoutineBegin(snapshot));
      prac_loopLoopScheduler.add(prac_responseRoutineEachFrame());
      prac_loopLoopScheduler.add(prac_responseRoutineEnd(snapshot));
      prac_loopLoopScheduler.add(resposne_feedbackRoutineBegin(snapshot));
      prac_loopLoopScheduler.add(resposne_feedbackRoutineEachFrame());
      prac_loopLoopScheduler.add(resposne_feedbackRoutineEnd(snapshot));
      prac_loopLoopScheduler.add(prac_correct_mouseRoutineBegin(snapshot));
      prac_loopLoopScheduler.add(prac_correct_mouseRoutineEachFrame());
      prac_loopLoopScheduler.add(prac_correct_mouseRoutineEnd(snapshot));
      prac_loopLoopScheduler.add(prac_loopLoopEndIteration(prac_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var prac_mask_loop_1;
function prac_mask_loop_1LoopBegin(prac_mask_loop_1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    prac_mask_loop_1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'masks_cond.xlsx', '0:5'),
      seed: undefined, name: 'prac_mask_loop_1'
    });
    psychoJS.experiment.addLoop(prac_mask_loop_1); // add the loop to the experiment
    currentLoop = prac_mask_loop_1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPrac_mask_loop_1 of prac_mask_loop_1) {
      snapshot = prac_mask_loop_1.getSnapshot();
      prac_mask_loop_1LoopScheduler.add(importConditions(snapshot));
      prac_mask_loop_1LoopScheduler.add(maskRoutineBegin(snapshot));
      prac_mask_loop_1LoopScheduler.add(maskRoutineEachFrame());
      prac_mask_loop_1LoopScheduler.add(maskRoutineEnd(snapshot));
      prac_mask_loop_1LoopScheduler.add(prac_mask_loop_1LoopEndIteration(prac_mask_loop_1LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function prac_mask_loop_1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(prac_mask_loop_1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function prac_mask_loop_1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var prac_mask_loop_2;
function prac_mask_loop_2LoopBegin(prac_mask_loop_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    prac_mask_loop_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'masks_cond.xlsx', '0:5'),
      seed: undefined, name: 'prac_mask_loop_2'
    });
    psychoJS.experiment.addLoop(prac_mask_loop_2); // add the loop to the experiment
    currentLoop = prac_mask_loop_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPrac_mask_loop_2 of prac_mask_loop_2) {
      snapshot = prac_mask_loop_2.getSnapshot();
      prac_mask_loop_2LoopScheduler.add(importConditions(snapshot));
      prac_mask_loop_2LoopScheduler.add(maskRoutineBegin(snapshot));
      prac_mask_loop_2LoopScheduler.add(maskRoutineEachFrame());
      prac_mask_loop_2LoopScheduler.add(maskRoutineEnd(snapshot));
      prac_mask_loop_2LoopScheduler.add(prac_mask_loop_2LoopEndIteration(prac_mask_loop_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function prac_mask_loop_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(prac_mask_loop_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function prac_mask_loop_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function prac_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(prac_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function prac_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var first_pass_loop;
function first_pass_loopLoopBegin(first_pass_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    first_pass_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'info_exp_patch_3_cond.xlsx', '0:120'),
      seed: undefined, name: 'first_pass_loop'
    });
    psychoJS.experiment.addLoop(first_pass_loop); // add the loop to the experiment
    currentLoop = first_pass_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisFirst_pass_loop of first_pass_loop) {
      snapshot = first_pass_loop.getSnapshot();
      first_pass_loopLoopScheduler.add(importConditions(snapshot));
      first_pass_loopLoopScheduler.add(patch_1RoutineBegin(snapshot));
      first_pass_loopLoopScheduler.add(patch_1RoutineEachFrame());
      first_pass_loopLoopScheduler.add(patch_1RoutineEnd(snapshot));
      const mask_loopLoopScheduler = new Scheduler(psychoJS);
      first_pass_loopLoopScheduler.add(mask_loopLoopBegin(mask_loopLoopScheduler, snapshot));
      first_pass_loopLoopScheduler.add(mask_loopLoopScheduler);
      first_pass_loopLoopScheduler.add(mask_loopLoopEnd);
      first_pass_loopLoopScheduler.add(patch_2RoutineBegin(snapshot));
      first_pass_loopLoopScheduler.add(patch_2RoutineEachFrame());
      first_pass_loopLoopScheduler.add(patch_2RoutineEnd(snapshot));
      const mask_loop_2LoopScheduler = new Scheduler(psychoJS);
      first_pass_loopLoopScheduler.add(mask_loop_2LoopBegin(mask_loop_2LoopScheduler, snapshot));
      first_pass_loopLoopScheduler.add(mask_loop_2LoopScheduler);
      first_pass_loopLoopScheduler.add(mask_loop_2LoopEnd);
      first_pass_loopLoopScheduler.add(responseRoutineBegin(snapshot));
      first_pass_loopLoopScheduler.add(responseRoutineEachFrame());
      first_pass_loopLoopScheduler.add(responseRoutineEnd(snapshot));
      first_pass_loopLoopScheduler.add(correct_mouseRoutineBegin(snapshot));
      first_pass_loopLoopScheduler.add(correct_mouseRoutineEachFrame());
      first_pass_loopLoopScheduler.add(correct_mouseRoutineEnd(snapshot));
      first_pass_loopLoopScheduler.add(first_pass_loopLoopEndIteration(first_pass_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var mask_loop;
function mask_loopLoopBegin(mask_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    mask_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'masks_cond.xlsx', '0:5'),
      seed: undefined, name: 'mask_loop'
    });
    psychoJS.experiment.addLoop(mask_loop); // add the loop to the experiment
    currentLoop = mask_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisMask_loop of mask_loop) {
      snapshot = mask_loop.getSnapshot();
      mask_loopLoopScheduler.add(importConditions(snapshot));
      mask_loopLoopScheduler.add(maskRoutineBegin(snapshot));
      mask_loopLoopScheduler.add(maskRoutineEachFrame());
      mask_loopLoopScheduler.add(maskRoutineEnd(snapshot));
      mask_loopLoopScheduler.add(mask_loopLoopEndIteration(mask_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function mask_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(mask_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function mask_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var mask_loop_2;
function mask_loop_2LoopBegin(mask_loop_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    mask_loop_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'masks_cond.xlsx', '0:5'),
      seed: undefined, name: 'mask_loop_2'
    });
    psychoJS.experiment.addLoop(mask_loop_2); // add the loop to the experiment
    currentLoop = mask_loop_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisMask_loop_2 of mask_loop_2) {
      snapshot = mask_loop_2.getSnapshot();
      mask_loop_2LoopScheduler.add(importConditions(snapshot));
      mask_loop_2LoopScheduler.add(maskRoutineBegin(snapshot));
      mask_loop_2LoopScheduler.add(maskRoutineEachFrame());
      mask_loop_2LoopScheduler.add(maskRoutineEnd(snapshot));
      mask_loop_2LoopScheduler.add(mask_loop_2LoopEndIteration(mask_loop_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function mask_loop_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(mask_loop_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function mask_loop_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function first_pass_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(first_pass_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function first_pass_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var double_pass_loop;
function double_pass_loopLoopBegin(double_pass_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    double_pass_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'info_exp_patch_3_cond.xlsx', '0:120'),
      seed: undefined, name: 'double_pass_loop'
    });
    psychoJS.experiment.addLoop(double_pass_loop); // add the loop to the experiment
    currentLoop = double_pass_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisDouble_pass_loop of double_pass_loop) {
      snapshot = double_pass_loop.getSnapshot();
      double_pass_loopLoopScheduler.add(importConditions(snapshot));
      double_pass_loopLoopScheduler.add(patch_2RoutineBegin(snapshot));
      double_pass_loopLoopScheduler.add(patch_2RoutineEachFrame());
      double_pass_loopLoopScheduler.add(patch_2RoutineEnd(snapshot));
      const mask_loop_3LoopScheduler = new Scheduler(psychoJS);
      double_pass_loopLoopScheduler.add(mask_loop_3LoopBegin(mask_loop_3LoopScheduler, snapshot));
      double_pass_loopLoopScheduler.add(mask_loop_3LoopScheduler);
      double_pass_loopLoopScheduler.add(mask_loop_3LoopEnd);
      double_pass_loopLoopScheduler.add(patch_1RoutineBegin(snapshot));
      double_pass_loopLoopScheduler.add(patch_1RoutineEachFrame());
      double_pass_loopLoopScheduler.add(patch_1RoutineEnd(snapshot));
      const mask_loop_4LoopScheduler = new Scheduler(psychoJS);
      double_pass_loopLoopScheduler.add(mask_loop_4LoopBegin(mask_loop_4LoopScheduler, snapshot));
      double_pass_loopLoopScheduler.add(mask_loop_4LoopScheduler);
      double_pass_loopLoopScheduler.add(mask_loop_4LoopEnd);
      double_pass_loopLoopScheduler.add(response_2RoutineBegin(snapshot));
      double_pass_loopLoopScheduler.add(response_2RoutineEachFrame());
      double_pass_loopLoopScheduler.add(response_2RoutineEnd(snapshot));
      double_pass_loopLoopScheduler.add(correct_mouseRoutineBegin(snapshot));
      double_pass_loopLoopScheduler.add(correct_mouseRoutineEachFrame());
      double_pass_loopLoopScheduler.add(correct_mouseRoutineEnd(snapshot));
      double_pass_loopLoopScheduler.add(double_pass_loopLoopEndIteration(double_pass_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var mask_loop_3;
function mask_loop_3LoopBegin(mask_loop_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    mask_loop_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'masks_cond.xlsx', '0:5'),
      seed: undefined, name: 'mask_loop_3'
    });
    psychoJS.experiment.addLoop(mask_loop_3); // add the loop to the experiment
    currentLoop = mask_loop_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisMask_loop_3 of mask_loop_3) {
      snapshot = mask_loop_3.getSnapshot();
      mask_loop_3LoopScheduler.add(importConditions(snapshot));
      mask_loop_3LoopScheduler.add(maskRoutineBegin(snapshot));
      mask_loop_3LoopScheduler.add(maskRoutineEachFrame());
      mask_loop_3LoopScheduler.add(maskRoutineEnd(snapshot));
      mask_loop_3LoopScheduler.add(mask_loop_3LoopEndIteration(mask_loop_3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function mask_loop_3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(mask_loop_3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function mask_loop_3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var mask_loop_4;
function mask_loop_4LoopBegin(mask_loop_4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    mask_loop_4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'masks_cond.xlsx', '0:5'),
      seed: undefined, name: 'mask_loop_4'
    });
    psychoJS.experiment.addLoop(mask_loop_4); // add the loop to the experiment
    currentLoop = mask_loop_4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisMask_loop_4 of mask_loop_4) {
      snapshot = mask_loop_4.getSnapshot();
      mask_loop_4LoopScheduler.add(importConditions(snapshot));
      mask_loop_4LoopScheduler.add(maskRoutineBegin(snapshot));
      mask_loop_4LoopScheduler.add(maskRoutineEachFrame());
      mask_loop_4LoopScheduler.add(maskRoutineEnd(snapshot));
      mask_loop_4LoopScheduler.add(mask_loop_4LoopEndIteration(mask_loop_4LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function mask_loop_4LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(mask_loop_4);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function mask_loop_4LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function double_pass_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(double_pass_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function double_pass_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var prac_patch_1Components;
function prac_patch_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_patch_1' ---
    t = 0;
    prac_patch_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    practice_patch_1.setImage(Patch_1_name);
    // Run 'Begin Routine' code from disable_mouse_3
    // ADDED THIS SNIPPET TO MAKE THE MOUSE INVISIBLE
    document.body.style.cursor='none';
    // keep track of which components have finished
    prac_patch_1Components = [];
    prac_patch_1Components.push(fixation_cross);
    prac_patch_1Components.push(practice_patch_1);
    prac_patch_1Components.push(Esc_exit_13);
    
    for (const thisComponent of prac_patch_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function prac_patch_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_patch_1' ---
    // get current time
    t = prac_patch_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_cross* updates
    if (t >= 0.0 && fixation_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_cross.tStart = t;  // (not accounting for frame time here)
      fixation_cross.frameNStart = frameN;  // exact frame index
      
      fixation_cross.setAutoDraw(true);
    }

    frameRemains = 0.0 + fixation_cross_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_cross.setAutoDraw(false);
    }
    
    // *practice_patch_1* updates
    if (t >= fixation_cross_duration && practice_patch_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_patch_1.tStart = t;  // (not accounting for frame time here)
      practice_patch_1.frameNStart = frameN;  // exact frame index
      
      practice_patch_1.setAutoDraw(true);
    }

    frameRemains = fixation_cross_duration + image_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practice_patch_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_patch_1.setAutoDraw(false);
    }
    
    // *Esc_exit_13* updates
    if (t >= 0.0 && Esc_exit_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_13.tStart = t;  // (not accounting for frame time here)
      Esc_exit_13.frameNStart = frameN;  // exact frame index
      
      Esc_exit_13.setAutoDraw(true);
    }

    frameRemains = 0.0 + exit_message_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Esc_exit_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Esc_exit_13.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of prac_patch_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_patch_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_patch_1' ---
    for (const thisComponent of prac_patch_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "prac_patch_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var maskComponents;
function maskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'mask' ---
    t = 0;
    maskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.060000);
    // update component parameters for each repeat
    mask_image.setImage(mask_name);
    // keep track of which components have finished
    maskComponents = [];
    maskComponents.push(mask_image);
    maskComponents.push(Esc_exit_14);
    
    for (const thisComponent of maskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function maskRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'mask' ---
    // get current time
    t = maskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *mask_image* updates
    if (t >= 0.0 && mask_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mask_image.tStart = t;  // (not accounting for frame time here)
      mask_image.frameNStart = frameN;  // exact frame index
      
      mask_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.06 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mask_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mask_image.setAutoDraw(false);
    }
    
    // *Esc_exit_14* updates
    if (t >= 0.0 && Esc_exit_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_14.tStart = t;  // (not accounting for frame time here)
      Esc_exit_14.frameNStart = frameN;  // exact frame index
      
      Esc_exit_14.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.06 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Esc_exit_14.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Esc_exit_14.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of maskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function maskRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'mask' ---
    for (const thisComponent of maskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var prac_patch_2Components;
function prac_patch_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_patch_2' ---
    t = 0;
    prac_patch_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    practice_patch_2.setImage(Patch_2_name);
    // keep track of which components have finished
    prac_patch_2Components = [];
    prac_patch_2Components.push(fixation_cross_3);
    prac_patch_2Components.push(practice_patch_2);
    prac_patch_2Components.push(Esc_exit_12);
    
    for (const thisComponent of prac_patch_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function prac_patch_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_patch_2' ---
    // get current time
    t = prac_patch_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_cross_3* updates
    if (t >= 0.0 && fixation_cross_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_cross_3.tStart = t;  // (not accounting for frame time here)
      fixation_cross_3.frameNStart = frameN;  // exact frame index
      
      fixation_cross_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + fixation_cross_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_cross_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_cross_3.setAutoDraw(false);
    }
    
    // *practice_patch_2* updates
    if (t >= fixation_cross_duration && practice_patch_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_patch_2.tStart = t;  // (not accounting for frame time here)
      practice_patch_2.frameNStart = frameN;  // exact frame index
      
      practice_patch_2.setAutoDraw(true);
    }

    frameRemains = fixation_cross_duration + image_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practice_patch_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_patch_2.setAutoDraw(false);
    }
    
    // *Esc_exit_12* updates
    if (t >= 0.0 && Esc_exit_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_12.tStart = t;  // (not accounting for frame time here)
      Esc_exit_12.frameNStart = frameN;  // exact frame index
      
      Esc_exit_12.setAutoDraw(true);
    }

    frameRemains = 0.0 + exit_message_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Esc_exit_12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Esc_exit_12.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of prac_patch_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_patch_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_patch_2' ---
    for (const thisComponent of prac_patch_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "prac_patch_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var gotValidClick;
var prac_responseComponents;
function prac_responseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_response' ---
    t = 0;
    prac_responseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from code
    /* Syntax Error: Fix Python code */
    // Run 'Begin Routine' code from enable_mouse_2
    // Added this snippet to make the mouse visible again
    document.body.style.cursor='auto';
    
    // keep track of which components have finished
    prac_responseComponents = [];
    prac_responseComponents.push(mouse_2);
    prac_responseComponents.push(response1disk_3);
    prac_responseComponents.push(response5disk_3);
    prac_responseComponents.push(response3disk_3);
    prac_responseComponents.push(response7disk_3);
    prac_responseComponents.push(text);
    prac_responseComponents.push(most_similar_3);
    prac_responseComponents.push(most_different_3);
    prac_responseComponents.push(Esc_exit_7);
    
    for (const thisComponent of prac_responseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
function prac_responseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_response' ---
    // get current time
    t = prac_responseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse_2* updates
    if (t >= 0.0 && mouse_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_2.tStart = t;  // (not accounting for frame time here)
      mouse_2.frameNStart = frameN;  // exact frame index
      
      mouse_2.status = PsychoJS.Status.STARTED;
      mouse_2.mouseClock.reset();
      prevButtonState = mouse_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [response1disk,response3disk,response5disk,response7disk]) {
            if (obj.contains(mouse_2)) {
              gotValidClick = true;
              mouse_2.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *response1disk_3* updates
    if (t >= 0.0 && response1disk_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response1disk_3.tStart = t;  // (not accounting for frame time here)
      response1disk_3.frameNStart = frameN;  // exact frame index
      
      response1disk_3.setAutoDraw(true);
    }

    
    // *response5disk_3* updates
    if (t >= 0.0 && response5disk_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response5disk_3.tStart = t;  // (not accounting for frame time here)
      response5disk_3.frameNStart = frameN;  // exact frame index
      
      response5disk_3.setAutoDraw(true);
    }

    
    // *response3disk_3* updates
    if (t >= 0.0 && response3disk_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response3disk_3.tStart = t;  // (not accounting for frame time here)
      response3disk_3.frameNStart = frameN;  // exact frame index
      
      response3disk_3.setAutoDraw(true);
    }

    
    // *response7disk_3* updates
    if (t >= 0.0 && response7disk_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response7disk_3.tStart = t;  // (not accounting for frame time here)
      response7disk_3.frameNStart = frameN;  // exact frame index
      
      response7disk_3.setAutoDraw(true);
    }

    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *most_similar_3* updates
    if (t >= 0.0 && most_similar_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      most_similar_3.tStart = t;  // (not accounting for frame time here)
      most_similar_3.frameNStart = frameN;  // exact frame index
      
      most_similar_3.setAutoDraw(true);
    }

    
    // *most_different_3* updates
    if (t >= 0.0 && most_different_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      most_different_3.tStart = t;  // (not accounting for frame time here)
      most_different_3.frameNStart = frameN;  // exact frame index
      
      most_different_3.setAutoDraw(true);
    }

    
    // *Esc_exit_7* updates
    if (t >= 0.0 && Esc_exit_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_7.tStart = t;  // (not accounting for frame time here)
      Esc_exit_7.frameNStart = frameN;  // exact frame index
      
      Esc_exit_7.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of prac_responseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var _mouseXYs;
var mousexpos;
var mouseypos;
var x11d;
var y11d;
var x12d;
var y12d;
var x13d;
var y13d;
var a1d;
var b1d;
var c1d;
var x21d;
var y21d;
var x22d;
var y22d;
var x23d;
var y23d;
var a2d;
var b2d;
var c2d;
var x31d;
var y31d;
var x32d;
var y32d;
var x33d;
var y33d;
var a3d;
var b3d;
var c3d;
var x41d;
var y41d;
var x42d;
var y42d;
var x43d;
var y43d;
var a4d;
var b4d;
var c4d;
var x51d;
var y51d;
var x52d;
var y52d;
var x53d;
var y53d;
var a5d;
var b5d;
var c5d;
var x61d;
var y61d;
var x62d;
var y62d;
var x63d;
var y63d;
var a6d;
var b6d;
var c6d;
var x71d;
var y71d;
var x72d;
var y72d;
var x73d;
var y73d;
var a7d;
var b7d;
var c7d;
var x81d;
var y81d;
var x82d;
var y82d;
var x83d;
var y83d;
var a8d;
var b8d;
var c8d;
var similarity;
function prac_responseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_response' ---
    for (const thisComponent of prac_responseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_2.getPos();
    _mouseButtons = mouse_2.getPressed();
    psychoJS.experiment.addData('mouse_2.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_2.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_2.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_2.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_2.rightButton', _mouseButtons[2]);
    if (mouse_2.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_2.clicked_name', mouse_2.clicked_name[0]);}
    // Run 'End Routine' code from code
    mousexpos = mouse.getPos()[0];
    mouseypos = mouse.getPos()[1];
    x11d = (a - (b / 2));
    y11d = (a + (b / 2));
    x12d = (a + (b / 2));
    y12d = (a + (b / 2));
    x13d = (a - (b / 2));
    y13d = (a - (b / 2));
    a1d = ((((y12d - y13d) * (mousexpos - x13d)) + ((x13d - x12d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    b1d = ((((y13d - y11d) * (mousexpos - x13d)) + ((x11d - x13d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    c1d = ((1 - a1d) - b1d);
    x21d = (a - (b / 2));
    y21d = (a - (b / 2));
    x22d = (a + (b / 2));
    y22d = (a + (b / 2));
    x23d = (a + (b / 2));
    y23d = (a - (b / 2));
    a2d = ((((y22d - y23d) * (mousexpos - x23d)) + ((x23d - x22d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    b2d = ((((y23d - y21d) * (mousexpos - x23d)) + ((x21d - x23d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    c2d = ((1 - a2d) - b2d);
    x31d = (a - (b / 2));
    y31d = (- (a - (b / 2)));
    x32d = (a + (b / 2));
    y32d = (- (a - (b / 2)));
    x33d = (a + (b / 2));
    y33d = (- (a + (b / 2)));
    a3d = ((((y32d - y33d) * (mousexpos - x33d)) + ((x33d - x32d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    b3d = ((((y33d - y31d) * (mousexpos - x33d)) + ((x31d - x33d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    c3d = ((1 - a3d) - b3d);
    x41d = (a - (b / 2));
    y41d = (- (a - (b / 2)));
    x42d = (a + (b / 2));
    y42d = (- (a + (b / 2)));
    x43d = (a - (b / 2));
    y43d = (- (a + (b / 2)));
    a4d = ((((y42d - y43d) * (mousexpos - x43d)) + ((x43d - x42d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    b4d = ((((y43d - y41d) * (mousexpos - x43d)) + ((x41d - x43d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    c4d = ((1 - a4d) - b4d);
    x51d = (- (a + (b / 2)));
    y51d = (- (a + (b / 2)));
    x52d = (- (a - (b / 2)));
    y52d = (- (a - (b / 2)));
    x53d = (- (a - (b / 2)));
    y53d = (- (a + (b / 2)));
    a5d = ((((y52d - y53d) * (mousexpos - x53d)) + ((x53d - x52d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    b5d = ((((y53d - y51d) * (mousexpos - x53d)) + ((x51d - x53d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    c5d = ((1 - a5d) - b5d);
    x61d = (- (a + (b / 2)));
    y61d = (- (a - (b / 2)));
    x62d = (- (a - (b / 2)));
    y62d = (- (a - (b / 2)));
    x63d = (- (a + (b / 2)));
    y63d = (- (a + (b / 2)));
    a6d = ((((y62d - y63d) * (mousexpos - x63d)) + ((x63d - x62d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    b6d = ((((y63d - y61d) * (mousexpos - x63d)) + ((x61d - x63d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    c6d = ((1 - a6d) - b6d);
    x71d = (- (a + (b / 2)));
    y71d = (a + (b / 2));
    x72d = (- (a - (b / 2)));
    y72d = (a - (b / 2));
    x73d = (- (a + (b / 2)));
    y73d = (a - (b / 2));
    a7d = ((((y72d - y73d) * (mousexpos - x73d)) + ((x73d - x72d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    b7d = ((((y73d - y71d) * (mousexpos - x73d)) + ((x71d - x73d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    c7d = ((1 - a7d) - b7d);
    x81d = (- (a + (b / 2)));
    y81d = (a + (b / 2));
    x82d = (- (a - (b / 2)));
    y82d = (a + (b / 2));
    x83d = (- (a - (b / 2)));
    y83d = (a - (b / 2));
    a8d = ((((y82d - y83d) * (mousexpos - x83d)) + ((x83d - x82d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    b8d = ((((y83d - y81d) * (mousexpos - x83d)) + ((x81d - x83d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    c8d = ((1 - a8d) - b8d);
    if (((((0 <= a1d) && (a1d <= 1)) && ((0 <= b1d) && (b1d <= 1))) && ((0 <= c1d) && (c1d <= 1)))) {
        similarity = 7;
    } else {
        if (((((0 <= a2d) && (a2d <= 1)) && ((0 <= b2d) && (b2d <= 1))) && ((0 <= c2d) && (c2d <= 1)))) {
            similarity = 6;
        } else {
            if (((((0 <= a3d) && (a3d <= 1)) && ((0 <= b3d) && (b3d <= 1))) && ((0 <= c3d) && (c3d <= 1)))) {
                similarity = 5;
            } else {
                if (((((0 <= a4d) && (a4d <= 1)) && ((0 <= b4d) && (b4d <= 1))) && ((0 <= c4d) && (c4d <= 1)))) {
                    similarity = 4;
                } else {
                    if (((((0 <= a5d) && (a5d <= 1)) && ((0 <= b5d) && (b5d <= 1))) && ((0 <= c5d) && (c5d <= 1)))) {
                        similarity = 3;
                    } else {
                        if (((((0 <= a6d) && (a6d <= 1)) && ((0 <= b6d) && (b6d <= 1))) && ((0 <= c6d) && (c6d <= 1)))) {
                            similarity = 2;
                        } else {
                            if (((((0 <= a7d) && (a7d <= 1)) && ((0 <= b7d) && (b7d <= 1))) && ((0 <= c7d) && (c7d <= 1)))) {
                                similarity = 1;
                            } else {
                                if (((((0 <= a8d) && (a8d <= 1)) && ((0 <= b8d) && (b8d <= 1))) && ((0 <= c8d) && (c8d <= 1)))) {
                                    similarity = 0;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    psychoJS.experiment.addData("similarity", similarity);
    psychoJS.experiment.addData("response_time", mouse.mouseClock.getTime());
    psychoJS.experiment.addData("Pass", 1);
    
    // the Routine "prac_response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var responsefeedback;
var responsefeedback1;
var resposne_feedbackComponents;
function resposne_feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'resposne_feedback' ---
    t = 0;
    resposne_feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from feedback_code
    if (((0 <= similarity) && (similarity <= 1))) {
        responsefeedback = `You selected ${similarity}`;
        responsefeedback1 = `${similarity} indicates you found the images very similar`;
    }
    if (((2 <= similarity) && (similarity <= 3))) {
        responsefeedback = `You selected ${similarity}`;
        responsefeedback1 = `${similarity} indicates you found the images similar`;
    }
    if (((4 <= similarity) && (similarity <= 5))) {
        responsefeedback = `You selected ${similarity}`;
        responsefeedback1 = `${similarity} indicates you found the images different`;
    }
    if (((6 <= similarity) && (similarity <= 7))) {
        responsefeedback = `You selected ${similarity}`;
        responsefeedback1 = `${similarity} indicates you found the images very different`;
    }
    
    text_55.setText(responsefeedback);
    text_56.setText(responsefeedback1);
    // keep track of which components have finished
    resposne_feedbackComponents = [];
    resposne_feedbackComponents.push(text_55);
    resposne_feedbackComponents.push(text_56);
    resposne_feedbackComponents.push(Esc_exit_8);
    
    for (const thisComponent of resposne_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function resposne_feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'resposne_feedback' ---
    // get current time
    t = resposne_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_55* updates
    if (t >= 0.0 && text_55.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_55.tStart = t;  // (not accounting for frame time here)
      text_55.frameNStart = frameN;  // exact frame index
      
      text_55.setAutoDraw(true);
    }

    frameRemains = 0.0 + response_feedback_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_55.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_55.setAutoDraw(false);
    }
    
    // *text_56* updates
    if (t >= 0.0 && text_56.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_56.tStart = t;  // (not accounting for frame time here)
      text_56.frameNStart = frameN;  // exact frame index
      
      text_56.setAutoDraw(true);
    }

    frameRemains = 0.0 + response_feedback_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_56.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_56.setAutoDraw(false);
    }
    
    // *Esc_exit_8* updates
    if (t >= 0.0 && Esc_exit_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_8.tStart = t;  // (not accounting for frame time here)
      Esc_exit_8.frameNStart = frameN;  // exact frame index
      
      Esc_exit_8.setAutoDraw(true);
    }

    frameRemains = 0.0 + response_feedback_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Esc_exit_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Esc_exit_8.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of resposne_feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function resposne_feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'resposne_feedback' ---
    for (const thisComponent of resposne_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "resposne_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var prac_correct_mouseComponents;
function prac_correct_mouseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_correct_mouse' ---
    t = 0;
    prac_correct_mouseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_12
    mouse_12.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    prac_correct_mouseComponents = [];
    prac_correct_mouseComponents.push(mouse_12);
    prac_correct_mouseComponents.push(response1disk_4);
    prac_correct_mouseComponents.push(response3disk_4);
    prac_correct_mouseComponents.push(response5disk_4);
    prac_correct_mouseComponents.push(response7disk_4);
    prac_correct_mouseComponents.push(text_52);
    prac_correct_mouseComponents.push(center_square_2);
    prac_correct_mouseComponents.push(most_similar_4);
    prac_correct_mouseComponents.push(most_different_4);
    prac_correct_mouseComponents.push(Esc_exit_9);
    
    for (const thisComponent of prac_correct_mouseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function prac_correct_mouseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_correct_mouse' ---
    // get current time
    t = prac_correct_mouseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse_12* updates
    if (t >= 0.0 && mouse_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_12.tStart = t;  // (not accounting for frame time here)
      mouse_12.frameNStart = frameN;  // exact frame index
      
      mouse_12.status = PsychoJS.Status.STARTED;
      mouse_12.mouseClock.reset();
      prevButtonState = mouse_12.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_12.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_12.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [center_square]) {
            if (obj.contains(mouse_12)) {
              gotValidClick = true;
              mouse_12.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *response1disk_4* updates
    if (t >= 0.0 && response1disk_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response1disk_4.tStart = t;  // (not accounting for frame time here)
      response1disk_4.frameNStart = frameN;  // exact frame index
      
      response1disk_4.setAutoDraw(true);
    }

    
    // *response3disk_4* updates
    if (t >= 0.0 && response3disk_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response3disk_4.tStart = t;  // (not accounting for frame time here)
      response3disk_4.frameNStart = frameN;  // exact frame index
      
      response3disk_4.setAutoDraw(true);
    }

    
    // *response5disk_4* updates
    if (t >= 0.0 && response5disk_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response5disk_4.tStart = t;  // (not accounting for frame time here)
      response5disk_4.frameNStart = frameN;  // exact frame index
      
      response5disk_4.setAutoDraw(true);
    }

    
    // *response7disk_4* updates
    if (t >= 0.0 && response7disk_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response7disk_4.tStart = t;  // (not accounting for frame time here)
      response7disk_4.frameNStart = frameN;  // exact frame index
      
      response7disk_4.setAutoDraw(true);
    }

    
    // *text_52* updates
    if (t >= 0.0 && text_52.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_52.tStart = t;  // (not accounting for frame time here)
      text_52.frameNStart = frameN;  // exact frame index
      
      text_52.setAutoDraw(true);
    }

    
    // *center_square_2* updates
    if (t >= 0.0 && center_square_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      center_square_2.tStart = t;  // (not accounting for frame time here)
      center_square_2.frameNStart = frameN;  // exact frame index
      
      center_square_2.setAutoDraw(true);
    }

    
    // *most_similar_4* updates
    if (t >= 0.0 && most_similar_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      most_similar_4.tStart = t;  // (not accounting for frame time here)
      most_similar_4.frameNStart = frameN;  // exact frame index
      
      most_similar_4.setAutoDraw(true);
    }

    
    // *most_different_4* updates
    if (t >= 0.0 && most_different_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      most_different_4.tStart = t;  // (not accounting for frame time here)
      most_different_4.frameNStart = frameN;  // exact frame index
      
      most_different_4.setAutoDraw(true);
    }

    
    // *Esc_exit_9* updates
    if (t >= 0.0 && Esc_exit_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_9.tStart = t;  // (not accounting for frame time here)
      Esc_exit_9.frameNStart = frameN;  // exact frame index
      
      Esc_exit_9.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of prac_correct_mouseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_correct_mouseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_correct_mouse' ---
    for (const thisComponent of prac_correct_mouseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_12.getPos();
    _mouseButtons = mouse_12.getPressed();
    psychoJS.experiment.addData('mouse_12.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_12.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_12.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_12.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_12.rightButton', _mouseButtons[2]);
    if (mouse_12.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_12.clicked_name', mouse_12.clicked_name[0]);}
    // the Routine "prac_correct_mouse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _space_press_continue_7_allKeys;
var begin_taskComponents;
function begin_taskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'begin_task' ---
    t = 0;
    begin_taskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_1
    // current position of the mouse:
    mouse_1.x = [];
    mouse_1.y = [];
    mouse_1.leftButton = [];
    mouse_1.midButton = [];
    mouse_1.rightButton = [];
    mouse_1.time = [];
    mouse_1.clicked_name = [];
    gotValidClick = false; // until a click is received
    space_press_continue_7.keys = undefined;
    space_press_continue_7.rt = undefined;
    _space_press_continue_7_allKeys = [];
    // keep track of which components have finished
    begin_taskComponents = [];
    begin_taskComponents.push(mouse_1);
    begin_taskComponents.push(begin_mouse_center);
    begin_taskComponents.push(Esc_exit_15);
    begin_taskComponents.push(space_press_continue_7);
    
    for (const thisComponent of begin_taskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function begin_taskRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'begin_task' ---
    // get current time
    t = begin_taskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse_1* updates
    if (t >= 0.0 && mouse_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_1.tStart = t;  // (not accounting for frame time here)
      mouse_1.frameNStart = frameN;  // exact frame index
      
      mouse_1.status = PsychoJS.Status.STARTED;
      mouse_1.mouseClock.reset();
      prevButtonState = mouse_1.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_1.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_1.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [center_square]) {
            if (obj.contains(mouse_1)) {
              gotValidClick = true;
              mouse_1.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_1.getPos();
          mouse_1.x.push(_mouseXYs[0]);
          mouse_1.y.push(_mouseXYs[1]);
          mouse_1.leftButton.push(_mouseButtons[0]);
          mouse_1.midButton.push(_mouseButtons[1]);
          mouse_1.rightButton.push(_mouseButtons[2]);
          mouse_1.time.push(mouse_1.mouseClock.getTime());
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *begin_mouse_center* updates
    if (t >= 0.0 && begin_mouse_center.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      begin_mouse_center.tStart = t;  // (not accounting for frame time here)
      begin_mouse_center.frameNStart = frameN;  // exact frame index
      
      begin_mouse_center.setAutoDraw(true);
    }

    
    // *Esc_exit_15* updates
    if (t >= 0.0 && Esc_exit_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_15.tStart = t;  // (not accounting for frame time here)
      Esc_exit_15.frameNStart = frameN;  // exact frame index
      
      Esc_exit_15.setAutoDraw(true);
    }

    
    // *space_press_continue_7* updates
    if (t >= 0.0 && space_press_continue_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_press_continue_7.tStart = t;  // (not accounting for frame time here)
      space_press_continue_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_press_continue_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_press_continue_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_press_continue_7.clearEvents(); });
    }

    if (space_press_continue_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_press_continue_7.getKeys({keyList: ['space'], waitRelease: false});
      _space_press_continue_7_allKeys = _space_press_continue_7_allKeys.concat(theseKeys);
      if (_space_press_continue_7_allKeys.length > 0) {
        space_press_continue_7.keys = _space_press_continue_7_allKeys[_space_press_continue_7_allKeys.length - 1].name;  // just the last key pressed
        space_press_continue_7.rt = _space_press_continue_7_allKeys[_space_press_continue_7_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of begin_taskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function begin_taskRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'begin_task' ---
    for (const thisComponent of begin_taskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_1.x) {  psychoJS.experiment.addData('mouse_1.x', mouse_1.x[0])};
    if (mouse_1.y) {  psychoJS.experiment.addData('mouse_1.y', mouse_1.y[0])};
    if (mouse_1.leftButton) {  psychoJS.experiment.addData('mouse_1.leftButton', mouse_1.leftButton[0])};
    if (mouse_1.midButton) {  psychoJS.experiment.addData('mouse_1.midButton', mouse_1.midButton[0])};
    if (mouse_1.rightButton) {  psychoJS.experiment.addData('mouse_1.rightButton', mouse_1.rightButton[0])};
    if (mouse_1.time) {  psychoJS.experiment.addData('mouse_1.time', mouse_1.time[0])};
    if (mouse_1.clicked_name) {  psychoJS.experiment.addData('mouse_1.clicked_name', mouse_1.clicked_name[0])};
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_press_continue_7.corr, level);
    }
    psychoJS.experiment.addData('space_press_continue_7.keys', space_press_continue_7.keys);
    if (typeof space_press_continue_7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_press_continue_7.rt', space_press_continue_7.rt);
        routineTimer.reset();
        }
    
    space_press_continue_7.stop();
    // the Routine "begin_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var patch_1Components;
function patch_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'patch_1' ---
    t = 0;
    patch_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    first_patch.setImage(Patch_1_name);
    // Run 'Begin Routine' code from disable_mouse
    // ADDED THIS SNIPPET TO MAKE THE MOUSE INVISIBLE
    document.body.style.cursor='none';
    // keep track of which components have finished
    patch_1Components = [];
    patch_1Components.push(fixation_cross_1);
    patch_1Components.push(first_patch);
    patch_1Components.push(Esc_exit_16);
    
    for (const thisComponent of patch_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function patch_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'patch_1' ---
    // get current time
    t = patch_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_cross_1* updates
    if (t >= 0.0 && fixation_cross_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_cross_1.tStart = t;  // (not accounting for frame time here)
      fixation_cross_1.frameNStart = frameN;  // exact frame index
      
      fixation_cross_1.setAutoDraw(true);
    }

    frameRemains = 0.0 + fixation_cross_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_cross_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_cross_1.setAutoDraw(false);
    }
    
    // *first_patch* updates
    if (t >= fixation_cross_duration && first_patch.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      first_patch.tStart = t;  // (not accounting for frame time here)
      first_patch.frameNStart = frameN;  // exact frame index
      
      first_patch.setAutoDraw(true);
    }

    frameRemains = fixation_cross_duration + image_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (first_patch.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      first_patch.setAutoDraw(false);
    }
    
    // *Esc_exit_16* updates
    if (t >= 0.0 && Esc_exit_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_16.tStart = t;  // (not accounting for frame time here)
      Esc_exit_16.frameNStart = frameN;  // exact frame index
      
      Esc_exit_16.setAutoDraw(true);
    }

    frameRemains = 0.0 + exit_message_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Esc_exit_16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Esc_exit_16.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of patch_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function patch_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'patch_1' ---
    for (const thisComponent of patch_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "patch_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var patch_2Components;
function patch_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'patch_2' ---
    t = 0;
    patch_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    second_patch.setImage(Patch_2_name);
    // Run 'Begin Routine' code from disable_mouse_2
    // ADDED THIS SNIPPET TO MAKE THE MOUSE INVISIBLE
    document.body.style.cursor='none';
    // keep track of which components have finished
    patch_2Components = [];
    patch_2Components.push(fixation_cross_2);
    patch_2Components.push(second_patch);
    patch_2Components.push(Esc_exit_17);
    
    for (const thisComponent of patch_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function patch_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'patch_2' ---
    // get current time
    t = patch_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_cross_2* updates
    if (t >= 0 && fixation_cross_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_cross_2.tStart = t;  // (not accounting for frame time here)
      fixation_cross_2.frameNStart = frameN;  // exact frame index
      
      fixation_cross_2.setAutoDraw(true);
    }

    frameRemains = 0 + fixation_cross_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_cross_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_cross_2.setAutoDraw(false);
    }
    
    // *second_patch* updates
    if (t >= fixation_cross_duration && second_patch.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      second_patch.tStart = t;  // (not accounting for frame time here)
      second_patch.frameNStart = frameN;  // exact frame index
      
      second_patch.setAutoDraw(true);
    }

    frameRemains = fixation_cross_duration + image_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (second_patch.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      second_patch.setAutoDraw(false);
    }
    
    // *Esc_exit_17* updates
    if (t >= 0.0 && Esc_exit_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_17.tStart = t;  // (not accounting for frame time here)
      Esc_exit_17.frameNStart = frameN;  // exact frame index
      
      Esc_exit_17.setAutoDraw(true);
    }

    frameRemains = 0.0 + exit_message_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Esc_exit_17.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Esc_exit_17.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of patch_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function patch_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'patch_2' ---
    for (const thisComponent of patch_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "patch_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trial_num_feedback;
var responseComponents;
function responseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'response' ---
    t = 0;
    responseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from code_4
    trialnumber = (trialnumber + 1);
    trial_num_feedback = `You have completed ${trialnumber} of ${alltrials} trials`;
    
    // Run 'Begin Routine' code from enable_mouse
    // Added this snippet to make the mouse visible again
    document.body.style.cursor='auto';
    
    // keep track of which components have finished
    responseComponents = [];
    responseComponents.push(mouse);
    responseComponents.push(response1disk);
    responseComponents.push(response3disk);
    responseComponents.push(response5disk);
    responseComponents.push(response7disk);
    responseComponents.push(text_23);
    responseComponents.push(most_similar);
    responseComponents.push(most_different);
    responseComponents.push(Esc_exit_10);
    
    for (const thisComponent of responseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function responseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'response' ---
    // get current time
    t = responseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [response1disk,response3disk,response5disk,response7disk]) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *response1disk* updates
    if (t >= 0.0 && response1disk.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response1disk.tStart = t;  // (not accounting for frame time here)
      response1disk.frameNStart = frameN;  // exact frame index
      
      response1disk.setAutoDraw(true);
    }

    
    // *response3disk* updates
    if (t >= 0.0 && response3disk.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response3disk.tStart = t;  // (not accounting for frame time here)
      response3disk.frameNStart = frameN;  // exact frame index
      
      response3disk.setAutoDraw(true);
    }

    
    // *response5disk* updates
    if (t >= 0.0 && response5disk.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response5disk.tStart = t;  // (not accounting for frame time here)
      response5disk.frameNStart = frameN;  // exact frame index
      
      response5disk.setAutoDraw(true);
    }

    
    // *response7disk* updates
    if (t >= 0.0 && response7disk.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response7disk.tStart = t;  // (not accounting for frame time here)
      response7disk.frameNStart = frameN;  // exact frame index
      
      response7disk.setAutoDraw(true);
    }

    
    // *text_23* updates
    if (t >= 0.0 && text_23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_23.tStart = t;  // (not accounting for frame time here)
      text_23.frameNStart = frameN;  // exact frame index
      
      text_23.setAutoDraw(true);
    }

    
    // *most_similar* updates
    if (t >= 0.0 && most_similar.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      most_similar.tStart = t;  // (not accounting for frame time here)
      most_similar.frameNStart = frameN;  // exact frame index
      
      most_similar.setAutoDraw(true);
    }

    
    // *most_different* updates
    if (t >= 0.0 && most_different.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      most_different.tStart = t;  // (not accounting for frame time here)
      most_different.frameNStart = frameN;  // exact frame index
      
      most_different.setAutoDraw(true);
    }

    
    // *Esc_exit_10* updates
    if (t >= 0.0 && Esc_exit_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_10.tStart = t;  // (not accounting for frame time here)
      Esc_exit_10.frameNStart = frameN;  // exact frame index
      
      Esc_exit_10.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of responseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function responseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'response' ---
    for (const thisComponent of responseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse.getPos();
    _mouseButtons = mouse.getPressed();
    psychoJS.experiment.addData('mouse.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse.rightButton', _mouseButtons[2]);
    if (mouse.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name[0]);}
    // Run 'End Routine' code from code_4
    mousexpos = mouse.getPos()[0];
    mouseypos = mouse.getPos()[1];
    x11d = (a - (b / 2));
    y11d = (a + (b / 2));
    x12d = (a + (b / 2));
    y12d = (a + (b / 2));
    x13d = (a - (b / 2));
    y13d = (a - (b / 2));
    a1d = ((((y12d - y13d) * (mousexpos - x13d)) + ((x13d - x12d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    b1d = ((((y13d - y11d) * (mousexpos - x13d)) + ((x11d - x13d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    c1d = ((1 - a1d) - b1d);
    x21d = (a - (b / 2));
    y21d = (a - (b / 2));
    x22d = (a + (b / 2));
    y22d = (a + (b / 2));
    x23d = (a + (b / 2));
    y23d = (a - (b / 2));
    a2d = ((((y22d - y23d) * (mousexpos - x23d)) + ((x23d - x22d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    b2d = ((((y23d - y21d) * (mousexpos - x23d)) + ((x21d - x23d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    c2d = ((1 - a2d) - b2d);
    x31d = (a - (b / 2));
    y31d = (- (a - (b / 2)));
    x32d = (a + (b / 2));
    y32d = (- (a - (b / 2)));
    x33d = (a + (b / 2));
    y33d = (- (a + (b / 2)));
    a3d = ((((y32d - y33d) * (mousexpos - x33d)) + ((x33d - x32d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    b3d = ((((y33d - y31d) * (mousexpos - x33d)) + ((x31d - x33d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    c3d = ((1 - a3d) - b3d);
    x41d = (a - (b / 2));
    y41d = (- (a - (b / 2)));
    x42d = (a + (b / 2));
    y42d = (- (a + (b / 2)));
    x43d = (a - (b / 2));
    y43d = (- (a + (b / 2)));
    a4d = ((((y42d - y43d) * (mousexpos - x43d)) + ((x43d - x42d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    b4d = ((((y43d - y41d) * (mousexpos - x43d)) + ((x41d - x43d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    c4d = ((1 - a4d) - b4d);
    x51d = (- (a + (b / 2)));
    y51d = (- (a + (b / 2)));
    x52d = (- (a - (b / 2)));
    y52d = (- (a - (b / 2)));
    x53d = (- (a - (b / 2)));
    y53d = (- (a + (b / 2)));
    a5d = ((((y52d - y53d) * (mousexpos - x53d)) + ((x53d - x52d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    b5d = ((((y53d - y51d) * (mousexpos - x53d)) + ((x51d - x53d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    c5d = ((1 - a5d) - b5d);
    x61d = (- (a + (b / 2)));
    y61d = (- (a - (b / 2)));
    x62d = (- (a - (b / 2)));
    y62d = (- (a - (b / 2)));
    x63d = (- (a + (b / 2)));
    y63d = (- (a + (b / 2)));
    a6d = ((((y62d - y63d) * (mousexpos - x63d)) + ((x63d - x62d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    b6d = ((((y63d - y61d) * (mousexpos - x63d)) + ((x61d - x63d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    c6d = ((1 - a6d) - b6d);
    x71d = (- (a + (b / 2)));
    y71d = (a + (b / 2));
    x72d = (- (a - (b / 2)));
    y72d = (a - (b / 2));
    x73d = (- (a + (b / 2)));
    y73d = (a - (b / 2));
    a7d = ((((y72d - y73d) * (mousexpos - x73d)) + ((x73d - x72d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    b7d = ((((y73d - y71d) * (mousexpos - x73d)) + ((x71d - x73d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    c7d = ((1 - a7d) - b7d);
    x81d = (- (a + (b / 2)));
    y81d = (a + (b / 2));
    x82d = (- (a - (b / 2)));
    y82d = (a + (b / 2));
    x83d = (- (a - (b / 2)));
    y83d = (a - (b / 2));
    a8d = ((((y82d - y83d) * (mousexpos - x83d)) + ((x83d - x82d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    b8d = ((((y83d - y81d) * (mousexpos - x83d)) + ((x81d - x83d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    c8d = ((1 - a8d) - b8d);
    if (((((0 <= a1d) && (a1d <= 1)) && ((0 <= b1d) && (b1d <= 1))) && ((0 <= c1d) && (c1d <= 1)))) {
        similarity = 7;
    } else {
        if (((((0 <= a2d) && (a2d <= 1)) && ((0 <= b2d) && (b2d <= 1))) && ((0 <= c2d) && (c2d <= 1)))) {
            similarity = 6;
        } else {
            if (((((0 <= a3d) && (a3d <= 1)) && ((0 <= b3d) && (b3d <= 1))) && ((0 <= c3d) && (c3d <= 1)))) {
                similarity = 5;
            } else {
                if (((((0 <= a4d) && (a4d <= 1)) && ((0 <= b4d) && (b4d <= 1))) && ((0 <= c4d) && (c4d <= 1)))) {
                    similarity = 4;
                } else {
                    if (((((0 <= a5d) && (a5d <= 1)) && ((0 <= b5d) && (b5d <= 1))) && ((0 <= c5d) && (c5d <= 1)))) {
                        similarity = 3;
                    } else {
                        if (((((0 <= a6d) && (a6d <= 1)) && ((0 <= b6d) && (b6d <= 1))) && ((0 <= c6d) && (c6d <= 1)))) {
                            similarity = 2;
                        } else {
                            if (((((0 <= a7d) && (a7d <= 1)) && ((0 <= b7d) && (b7d <= 1))) && ((0 <= c7d) && (c7d <= 1)))) {
                                similarity = 1;
                            } else {
                                if (((((0 <= a8d) && (a8d <= 1)) && ((0 <= b8d) && (b8d <= 1))) && ((0 <= c8d) && (c8d <= 1)))) {
                                    similarity = 0;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    psychoJS.experiment.addData("similarity", similarity);
    psychoJS.experiment.addData("response_time", mouse.mouseClock.getTime());
    psychoJS.experiment.addData("Pass", 1);
    psychoJS.experiment.addData("trialNumber", trialnumber);
    
    // the Routine "response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var correct_mouseComponents;
function correct_mouseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'correct_mouse' ---
    t = 0;
    correct_mouseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_11
    mouse_11.clicked_name = [];
    gotValidClick = false; // until a click is received
    trial_text_2.setText(trial_num_feedback);
    // keep track of which components have finished
    correct_mouseComponents = [];
    correct_mouseComponents.push(mouse_11);
    correct_mouseComponents.push(response1disk_2);
    correct_mouseComponents.push(response3disk_2);
    correct_mouseComponents.push(response5disk_2);
    correct_mouseComponents.push(response7disk_2);
    correct_mouseComponents.push(text_51);
    correct_mouseComponents.push(center_square);
    correct_mouseComponents.push(most_similar_2);
    correct_mouseComponents.push(most_different_2);
    correct_mouseComponents.push(trial_text_2);
    correct_mouseComponents.push(Esc_exit_11);
    
    for (const thisComponent of correct_mouseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function correct_mouseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'correct_mouse' ---
    // get current time
    t = correct_mouseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse_11* updates
    if (t >= 0.0 && mouse_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_11.tStart = t;  // (not accounting for frame time here)
      mouse_11.frameNStart = frameN;  // exact frame index
      
      mouse_11.status = PsychoJS.Status.STARTED;
      mouse_11.mouseClock.reset();
      prevButtonState = mouse_11.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_11.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_11.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [center_square]) {
            if (obj.contains(mouse_11)) {
              gotValidClick = true;
              mouse_11.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *response1disk_2* updates
    if (t >= 0.0 && response1disk_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response1disk_2.tStart = t;  // (not accounting for frame time here)
      response1disk_2.frameNStart = frameN;  // exact frame index
      
      response1disk_2.setAutoDraw(true);
    }

    
    // *response3disk_2* updates
    if (t >= 0.0 && response3disk_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response3disk_2.tStart = t;  // (not accounting for frame time here)
      response3disk_2.frameNStart = frameN;  // exact frame index
      
      response3disk_2.setAutoDraw(true);
    }

    
    // *response5disk_2* updates
    if (t >= 0.0 && response5disk_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response5disk_2.tStart = t;  // (not accounting for frame time here)
      response5disk_2.frameNStart = frameN;  // exact frame index
      
      response5disk_2.setAutoDraw(true);
    }

    
    // *response7disk_2* updates
    if (t >= 0.0 && response7disk_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response7disk_2.tStart = t;  // (not accounting for frame time here)
      response7disk_2.frameNStart = frameN;  // exact frame index
      
      response7disk_2.setAutoDraw(true);
    }

    
    // *text_51* updates
    if (t >= 0.0 && text_51.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_51.tStart = t;  // (not accounting for frame time here)
      text_51.frameNStart = frameN;  // exact frame index
      
      text_51.setAutoDraw(true);
    }

    
    // *center_square* updates
    if (t >= 0.0 && center_square.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      center_square.tStart = t;  // (not accounting for frame time here)
      center_square.frameNStart = frameN;  // exact frame index
      
      center_square.setAutoDraw(true);
    }

    
    // *most_similar_2* updates
    if (t >= 0.0 && most_similar_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      most_similar_2.tStart = t;  // (not accounting for frame time here)
      most_similar_2.frameNStart = frameN;  // exact frame index
      
      most_similar_2.setAutoDraw(true);
    }

    
    // *most_different_2* updates
    if (t >= 0.0 && most_different_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      most_different_2.tStart = t;  // (not accounting for frame time here)
      most_different_2.frameNStart = frameN;  // exact frame index
      
      most_different_2.setAutoDraw(true);
    }

    
    // *trial_text_2* updates
    if (t >= 0.0 && trial_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_text_2.tStart = t;  // (not accounting for frame time here)
      trial_text_2.frameNStart = frameN;  // exact frame index
      
      trial_text_2.setAutoDraw(true);
    }

    
    // *Esc_exit_11* updates
    if (t >= 0.0 && Esc_exit_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_11.tStart = t;  // (not accounting for frame time here)
      Esc_exit_11.frameNStart = frameN;  // exact frame index
      
      Esc_exit_11.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of correct_mouseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function correct_mouseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'correct_mouse' ---
    for (const thisComponent of correct_mouseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_11.getPos();
    _mouseButtons = mouse_11.getPressed();
    psychoJS.experiment.addData('mouse_11.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_11.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_11.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_11.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_11.rightButton', _mouseButtons[2]);
    if (mouse_11.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_11.clicked_name', mouse_11.clicked_name[0]);}
    // the Routine "correct_mouse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var response_2Components;
function response_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'response_2' ---
    t = 0;
    response_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from code_5
    trialnumber = (trialnumber + 1);
    trial_num_feedback = `You have completed ${trialnumber} of ${alltrials} trials`;
    
    // Run 'Begin Routine' code from enable_mouse_3
    // Added this snippet to make the mouse visible again
    document.body.style.cursor='auto';
    
    // keep track of which components have finished
    response_2Components = [];
    response_2Components.push(mouse_3);
    response_2Components.push(response1disk_5);
    response_2Components.push(response3disk_5);
    response_2Components.push(response5disk_5);
    response_2Components.push(response7disk_5);
    response_2Components.push(text_24);
    response_2Components.push(most_similar_5);
    response_2Components.push(most_different_5);
    response_2Components.push(Esc_exit_18);
    
    for (const thisComponent of response_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function response_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'response_2' ---
    // get current time
    t = response_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse_3* updates
    if (t >= 0.0 && mouse_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_3.tStart = t;  // (not accounting for frame time here)
      mouse_3.frameNStart = frameN;  // exact frame index
      
      mouse_3.status = PsychoJS.Status.STARTED;
      mouse_3.mouseClock.reset();
      prevButtonState = mouse_3.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_3.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_3.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [response1disk,response3disk,response5disk,response7disk]) {
            if (obj.contains(mouse_3)) {
              gotValidClick = true;
              mouse_3.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *response1disk_5* updates
    if (t >= 0.0 && response1disk_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response1disk_5.tStart = t;  // (not accounting for frame time here)
      response1disk_5.frameNStart = frameN;  // exact frame index
      
      response1disk_5.setAutoDraw(true);
    }

    
    // *response3disk_5* updates
    if (t >= 0.0 && response3disk_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response3disk_5.tStart = t;  // (not accounting for frame time here)
      response3disk_5.frameNStart = frameN;  // exact frame index
      
      response3disk_5.setAutoDraw(true);
    }

    
    // *response5disk_5* updates
    if (t >= 0.0 && response5disk_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response5disk_5.tStart = t;  // (not accounting for frame time here)
      response5disk_5.frameNStart = frameN;  // exact frame index
      
      response5disk_5.setAutoDraw(true);
    }

    
    // *response7disk_5* updates
    if (t >= 0.0 && response7disk_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response7disk_5.tStart = t;  // (not accounting for frame time here)
      response7disk_5.frameNStart = frameN;  // exact frame index
      
      response7disk_5.setAutoDraw(true);
    }

    
    // *text_24* updates
    if (t >= 0.0 && text_24.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_24.tStart = t;  // (not accounting for frame time here)
      text_24.frameNStart = frameN;  // exact frame index
      
      text_24.setAutoDraw(true);
    }

    
    // *most_similar_5* updates
    if (t >= 0.0 && most_similar_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      most_similar_5.tStart = t;  // (not accounting for frame time here)
      most_similar_5.frameNStart = frameN;  // exact frame index
      
      most_similar_5.setAutoDraw(true);
    }

    
    // *most_different_5* updates
    if (t >= 0.0 && most_different_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      most_different_5.tStart = t;  // (not accounting for frame time here)
      most_different_5.frameNStart = frameN;  // exact frame index
      
      most_different_5.setAutoDraw(true);
    }

    
    // *Esc_exit_18* updates
    if (t >= 0.0 && Esc_exit_18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Esc_exit_18.tStart = t;  // (not accounting for frame time here)
      Esc_exit_18.frameNStart = frameN;  // exact frame index
      
      Esc_exit_18.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of response_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function response_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'response_2' ---
    for (const thisComponent of response_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_3.getPos();
    _mouseButtons = mouse_3.getPressed();
    psychoJS.experiment.addData('mouse_3.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_3.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_3.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_3.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_3.rightButton', _mouseButtons[2]);
    if (mouse_3.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_3.clicked_name', mouse_3.clicked_name[0]);}
    // Run 'End Routine' code from code_5
    mousexpos = mouse.getPos()[0];
    mouseypos = mouse.getPos()[1];
    x11d = (a - (b / 2));
    y11d = (a + (b / 2));
    x12d = (a + (b / 2));
    y12d = (a + (b / 2));
    x13d = (a - (b / 2));
    y13d = (a - (b / 2));
    a1d = ((((y12d - y13d) * (mousexpos - x13d)) + ((x13d - x12d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    b1d = ((((y13d - y11d) * (mousexpos - x13d)) + ((x11d - x13d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    c1d = ((1 - a1d) - b1d);
    x21d = (a - (b / 2));
    y21d = (a - (b / 2));
    x22d = (a + (b / 2));
    y22d = (a + (b / 2));
    x23d = (a + (b / 2));
    y23d = (a - (b / 2));
    a2d = ((((y22d - y23d) * (mousexpos - x23d)) + ((x23d - x22d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    b2d = ((((y23d - y21d) * (mousexpos - x23d)) + ((x21d - x23d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    c2d = ((1 - a2d) - b2d);
    x31d = (a - (b / 2));
    y31d = (- (a - (b / 2)));
    x32d = (a + (b / 2));
    y32d = (- (a - (b / 2)));
    x33d = (a + (b / 2));
    y33d = (- (a + (b / 2)));
    a3d = ((((y32d - y33d) * (mousexpos - x33d)) + ((x33d - x32d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    b3d = ((((y33d - y31d) * (mousexpos - x33d)) + ((x31d - x33d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    c3d = ((1 - a3d) - b3d);
    x41d = (a - (b / 2));
    y41d = (- (a - (b / 2)));
    x42d = (a + (b / 2));
    y42d = (- (a + (b / 2)));
    x43d = (a - (b / 2));
    y43d = (- (a + (b / 2)));
    a4d = ((((y42d - y43d) * (mousexpos - x43d)) + ((x43d - x42d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    b4d = ((((y43d - y41d) * (mousexpos - x43d)) + ((x41d - x43d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    c4d = ((1 - a4d) - b4d);
    x51d = (- (a + (b / 2)));
    y51d = (- (a + (b / 2)));
    x52d = (- (a - (b / 2)));
    y52d = (- (a - (b / 2)));
    x53d = (- (a - (b / 2)));
    y53d = (- (a + (b / 2)));
    a5d = ((((y52d - y53d) * (mousexpos - x53d)) + ((x53d - x52d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    b5d = ((((y53d - y51d) * (mousexpos - x53d)) + ((x51d - x53d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    c5d = ((1 - a5d) - b5d);
    x61d = (- (a + (b / 2)));
    y61d = (- (a - (b / 2)));
    x62d = (- (a - (b / 2)));
    y62d = (- (a - (b / 2)));
    x63d = (- (a + (b / 2)));
    y63d = (- (a + (b / 2)));
    a6d = ((((y62d - y63d) * (mousexpos - x63d)) + ((x63d - x62d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    b6d = ((((y63d - y61d) * (mousexpos - x63d)) + ((x61d - x63d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    c6d = ((1 - a6d) - b6d);
    x71d = (- (a + (b / 2)));
    y71d = (a + (b / 2));
    x72d = (- (a - (b / 2)));
    y72d = (a - (b / 2));
    x73d = (- (a + (b / 2)));
    y73d = (a - (b / 2));
    a7d = ((((y72d - y73d) * (mousexpos - x73d)) + ((x73d - x72d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    b7d = ((((y73d - y71d) * (mousexpos - x73d)) + ((x71d - x73d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    c7d = ((1 - a7d) - b7d);
    x81d = (- (a + (b / 2)));
    y81d = (a + (b / 2));
    x82d = (- (a - (b / 2)));
    y82d = (a + (b / 2));
    x83d = (- (a - (b / 2)));
    y83d = (a - (b / 2));
    a8d = ((((y82d - y83d) * (mousexpos - x83d)) + ((x83d - x82d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    b8d = ((((y83d - y81d) * (mousexpos - x83d)) + ((x81d - x83d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    c8d = ((1 - a8d) - b8d);
    if (((((0 <= a1d) && (a1d <= 1)) && ((0 <= b1d) && (b1d <= 1))) && ((0 <= c1d) && (c1d <= 1)))) {
        similarity = 7;
    } else {
        if (((((0 <= a2d) && (a2d <= 1)) && ((0 <= b2d) && (b2d <= 1))) && ((0 <= c2d) && (c2d <= 1)))) {
            similarity = 6;
        } else {
            if (((((0 <= a3d) && (a3d <= 1)) && ((0 <= b3d) && (b3d <= 1))) && ((0 <= c3d) && (c3d <= 1)))) {
                similarity = 5;
            } else {
                if (((((0 <= a4d) && (a4d <= 1)) && ((0 <= b4d) && (b4d <= 1))) && ((0 <= c4d) && (c4d <= 1)))) {
                    similarity = 4;
                } else {
                    if (((((0 <= a5d) && (a5d <= 1)) && ((0 <= b5d) && (b5d <= 1))) && ((0 <= c5d) && (c5d <= 1)))) {
                        similarity = 3;
                    } else {
                        if (((((0 <= a6d) && (a6d <= 1)) && ((0 <= b6d) && (b6d <= 1))) && ((0 <= c6d) && (c6d <= 1)))) {
                            similarity = 2;
                        } else {
                            if (((((0 <= a7d) && (a7d <= 1)) && ((0 <= b7d) && (b7d <= 1))) && ((0 <= c7d) && (c7d <= 1)))) {
                                similarity = 1;
                            } else {
                                if (((((0 <= a8d) && (a8d <= 1)) && ((0 <= b8d) && (b8d <= 1))) && ((0 <= c8d) && (c8d <= 1)))) {
                                    similarity = 0;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    psychoJS.experiment.addData("similarity", similarity);
    psychoJS.experiment.addData("response_time", mouse.mouseClock.getTime());
    psychoJS.experiment.addData("Pass", 2);
    psychoJS.experiment.addData("trialNumber", trialnumber);
    
    // the Routine "response_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _space_exit_allKeys;
var end_of_experimentComponents;
function end_of_experimentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end_of_experiment' ---
    t = 0;
    end_of_experimentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    space_exit.keys = undefined;
    space_exit.rt = undefined;
    _space_exit_allKeys = [];
    // keep track of which components have finished
    end_of_experimentComponents = [];
    end_of_experimentComponents.push(thank_you);
    end_of_experimentComponents.push(space_exit);
    
    for (const thisComponent of end_of_experimentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function end_of_experimentRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_of_experiment' ---
    // get current time
    t = end_of_experimentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *thank_you* updates
    if (t >= 0.0 && thank_you.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thank_you.tStart = t;  // (not accounting for frame time here)
      thank_you.frameNStart = frameN;  // exact frame index
      
      thank_you.setAutoDraw(true);
    }

    
    // *space_exit* updates
    if (t >= 0.0 && space_exit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_exit.tStart = t;  // (not accounting for frame time here)
      space_exit.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_exit.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_exit.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_exit.clearEvents(); });
    }

    if (space_exit.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_exit.getKeys({keyList: ['space'], waitRelease: false});
      _space_exit_allKeys = _space_exit_allKeys.concat(theseKeys);
      if (_space_exit_allKeys.length > 0) {
        space_exit.keys = _space_exit_allKeys[_space_exit_allKeys.length - 1].name;  // just the last key pressed
        space_exit.rt = _space_exit_allKeys[_space_exit_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_of_experimentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_of_experimentRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_of_experiment' ---
    for (const thisComponent of end_of_experimentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_exit.corr, level);
    }
    psychoJS.experiment.addData('space_exit.keys', space_exit.keys);
    if (typeof space_exit.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_exit.rt', space_exit.rt);
        routineTimer.reset();
        }
    
    space_exit.stop();
    // the Routine "end_of_experiment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
