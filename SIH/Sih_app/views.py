from django.shortcuts import render
from .translate import translate_text
from .forms import TranslateForm
import azure.cognitiveservices.speech as speechsdk
import json
from django.http import JsonResponse

def index(request):
    result = None
    form = TranslateForm()

    if request.method == 'POST':
        form = TranslateForm(request.POST)
        if form.is_valid():
            input_language = form.cleaned_data['input_language']
            text = form.cleaned_data['text']
            target_language = form.cleaned_data['target_language']
            result = translate_text(input_language, text, target_language)

    return render(request, 'index.html', {'form': form, 'result': result})

def recognize_speech(request):
    if request.method == 'POST':
        try:
            text = recognize_from_microphone()
            return JsonResponse({'text': text})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription='9b3e0e85ccad4bc0b61e7d6b5b3d841f', region='centralindia')
    speech_config.speech_recognition_language = "hi-IN"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        return "No speech could be recognized."
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        return f"Speech Recognition canceled: {cancellation_details.reason}. Error details: {cancellation_details.error_details}"

