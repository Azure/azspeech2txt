# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# ml transcribe azspeech2txt <path>

import os
import sys
import time
import argparse

import azure.cognitiveservices.speech as speechsdk

from mlhub.utils import get_cmd_cwd

option_parser = argparse.ArgumentParser(add_help=False)

option_parser.add_argument(
    'path',
    help='path to audio file')

args = option_parser.parse_args()

# Defaults.

KEY_FILE = "private.py"
DEFAULT_REGION = "southeastasia"

subscription_key = None
region = DEFAULT_REGION

# Prompt the user for the key and region and save into private.py for
# future runs of the model. The contents of that file is:
#
# subscription_key = "a14d...ef24"
# region = "southeastasia"

if os.path.isfile(KEY_FILE) and os.path.getsize(KEY_FILE) != 0:
    exec(open(KEY_FILE).read())
else:
    sys.stdout.write("Please enter your Speech Services subscription key []: ")
    subscription_key = input()

    sys.stdout.write("Please enter your region [southeastasia]: ")
    region = input()
    if len(region) == 0: region = DEFAULT_REGION

    if len(subscription_key) > 0:
        assert subscription_key
        ofname = open(KEY_FILE, "w")
        ofname.write("""subscription_key = "{}"
region = "{}"
    """.format(subscription_key, region))
        ofname.close()

        print("""
I've saved that information into the file:

        """ + os.getcwd() + "/" + KEY_FILE)

# Create a callback to terminate the transcription once the full audio
# has been transcribed.

done = False

def stop_cb(evt):
    """Callback to stop continuous recognition upon receiving an event `evt`"""
    speech_recognizer.stop_continuous_recognition()
    global done
    done = True

# Create an instance of a speech config with the provided subscription
# key and service region. Then create an audio configuration to load
# the audio from file rather than from microphone. A sample audio file
# is available as harvard.wav from:
#
# https://github.com/realpython/python-speech-recognition/raw/master/
# audio_files/harvard.wav
#
# A recognizer is then created with the given settings.

pth = os.path.join(get_cmd_cwd(), args.path)

speech_config     = speechsdk.SpeechConfig(subscription=subscription_key,
                                           region=region)
audio_config      = speechsdk.audio.AudioConfig(use_default_microphone=False,
                                                filename=pth)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,
                                               audio_config=audio_config)

# We connect callbacks to the events fired by the speech
# recognizer. Most are commented out as examples here to allow tracing
# if you are interested in exploring the interactions with the server.
#
# speech_recognizer.recognizing.connect(lambda evt:
#                                       print('RECOGNIZING: {}'.format(evt)))
# speech_recognizer.session_started.connect(lambda evt:
#                                           print('STARTED: {}'.format(evt)))
# speech_recognizer.session_stopped.connect(lambda evt:
#                                           print('STOPPED {}'.format(evt)))
# speech_recognizer.canceled.connect(lambda evt:
#                                    print('CANCELED {}'.format(evt)))

# This callback provides the actual transcription.

speech_recognizer.recognized.connect(lambda evt:
                                     print('{}'.format(evt.result.text)))

# Stop continuous recognition on either session stopped or canceled
# events.

speech_recognizer.session_stopped.connect(stop_cb)
speech_recognizer.canceled.connect(stop_cb)

# Start continuous speech recognition, and then perform
# recognition. For long-running recognition we use
# start_continuous_recognition().

speech_recognizer.start_continuous_recognition()
while not done:
    time.sleep(.5)

