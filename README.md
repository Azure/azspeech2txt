Azure Speech to Text
====================

This [MLHub](https://mlhub.ai) package provides a quick introduction
to the pre-built Speech to Text model provided through Azure's
Cognitive Services. This service takes an audio signal and transcribes
it to return the text.

In addition to the demonstration this package provides a collection of
commands that turn the service into a useful command line tool for
transcribing from the microphone or from an audio file.

A free Azure subscription allowing up to 5,000 transactions per month
is available from https://azure.microsoft.com/free/. Once set up visit
https://ms.portal.azure.com and Create a resource under AI and Machine
Learning called Speech Services. Once created you can access the web
API subscription key and endpoint from the portal. This will be
prompted for in the demo.

This package is part of the [Azure on
MLHub](https://github.com/Azure/mlhub) repository. Please note that
these Azure models, unlike the MLHub models in general, use *closed
source services* which have no guarantee of ongoing availability and
do not come with the freedom to modify and share.

Visit the github repository for more details:
<https://github.com/Azure/azspeech2txt>

The Python code is based on the [Azure Speech Services Quick Start for
Python](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstart-python).

Usage
-----

- To install mlhub (Ubuntu 18.04 LTS)

```console
$ pip3 install mlhub
```

- To install and configure the demo:

```console
$ ml install   azspeech2txt
$ ml configure azspeech2txt
```

Command Line Tools
------------------

In addition to the *demo* presented below, the *azspeech2txt* package
provides a number of useful command line tools.

*Listen*

The *listen* command will listen for an utterance from the computer microphone
for up to 15 seconds and then transcribe it to standard output.

```console
$ ml listen azspeech2txt
The machine learning hub is useful for demonstrating capability of 
models as well as providing command line tools.
```

*Transcribe*

The *transcribe* command takes an audio file and transcribes it to
standard output. For large audio files this can take some time.

```console
$ ml transcribe azspeech2txt harvard.wav
The stale smell of old beer lingers it takes heat to bring out the odor.
A cold dip restore's health and Zest, a salt pickle taste fine with
Ham tacos, Al Pastore are my favorite a zestful food is the hot cross bun.
```

The audio file comes from Github:
https://github.com/realpython/python-speech-recognition/raw/master/audio_files/harvard.wav

Demonstration
-------------

```console
$ ml demo azspeech2txt 

====================
Azure Speech to Text
====================

Welcome to a demo of the pre-built models for Speech to Text provided
through Azure's Cognitive Services. This cloud service accepts audio
and then converts that into text which it returns locally.

The following file has been found and is assumed to contain
an Azure Speech Services subscription key and region. We will load 
the file and use this information.

    /home/kt/.mlhub/azspeech2txt/private.py

Say something...

> Recognized: Welcome to a demo of the prebuilt models for speech to
> text provided through azure's cognitive services. This cloud service 
> accepts audio and then converts that into text, which it returns locally.

Thank you for exploring the 'azspeech2txt' model.
```

As you can see I read the first paragraph from the screen and the
Azure Speech to Text service was quite accurate in its
transcription. If the accuracy for the particular accent is good then
it is quite suitable, for example, to be used as a dictation tool.

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

# Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
