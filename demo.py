# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# This demo is based on the Azure Cognitive Services Speech to Text Quick Start

print("""==============
Speech to Text
==============

Welcome to a demo of the pre-built models for Speech to Text provided
through Azure's Cognitive Services. This cloud service accepts audio
and then converts that into text which it returns locally.
""")

# Defaults.

KEY_FILE = "private.py"
DEFAULT_REGION = "southeastasia"

subscription_key = None
region = DEFAULT_REGION

# Import the required libraries.

import os
import sys
import azure.cognitiveservices.speech as speechsdk

#from textwrap import fill

# Prompt the user for the key and region and save into private.py for
# future runs of the model. The contents of that file is:
#
# subscription_key = "a14d...ef24"
# region = "southeastasia"

if os.path.isfile(KEY_FILE) and os.path.getsize(KEY_FILE) != 0:
    print("""The following file has been found and is assumed to contain
an Azure Speech Services subscription key and region. We will load 
the file and use this information.

    """ + os.getcwd() + "/" + KEY_FILE)
    exec(open(KEY_FILE).read())
else:
    print("""An Azure resource is required to access this service (and to run this
demo). See the README for details of a free subscription. Then you can
provide the key and the region information here.
""")
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

print("""
Say something...
""")

########################################################################
#
# Following is the code that does the actual work, creating an
# instance of a speech config with the specified subscription key and
# service region, then creating a recognizer with the given settings,
# and then performing recognition. recognize_once() returns when the
# first utterance has been recognized, so it is suitable only for
# single shot recognition like command or query. For long-running
# recognition, use start_continuous_recognition() instead, or if you
# want to run recognition in a non-blocking manner, use
# recognize_once_async().

speech_config     = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
result            = speech_recognizer.recognize_once()

#
########################################################################

# Checks result.

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
