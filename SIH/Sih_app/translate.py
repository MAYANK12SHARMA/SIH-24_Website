import requests, uuid, json
import azure.cognitiveservices.speech as speechsdk

# Add your key and endpoint
key = "9257553e89ae411c893a771aabbf5359"
endpoint = "https://api.cognitive.microsofttranslator.com"
location = "centralindia"

# List of languages (this is a subset, you can add more)
def langcode(lang):
    languages = {
    "Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar",
    "Armenian": "hy", "Assamese": "as", "Azerbaijani (Latin)": "az", "Bangla": "bn",
    "Bashkir": "ba", "Basque": "eu", "Bhojpuri": "bho", "Bodo": "brx", "Bosnian (Latin)": "bs",
    "Bulgarian": "bg", "Cantonese (Traditional)": "yue", "Catalan": "ca",
    "Chinese (Literary)": "lzh", "Chinese Simplified": "zh-Hans", "Chinese Traditional": "zh-Hant",
    "Shona": "sn", "Croatian": "hr", "Czech": "cs", "Danish": "da", "Dari": "prs",
    "Divehi": "dv", "Dogri": "doi", "Dutch": "nl", "English": "en", "Estonian": "et",
    "Faroese": "fo", "Fijian": "fj", "Filipino": "fil", "Finnish": "fi", "French": "fr",
    "French (Canada)": "fr-ca", "Galician": "gl", "Georgian": "ka", "German": "de",
    "Greek": "el", "Gujarati": "gu", "Haitian Creole": "ht", "Hausa": "ha",
    "Hebrew": "he", "Hindi": "hi", "Hmong Daw (Latin)": "mww", "Hungarian": "hu",
    "Icelandic": "is", "Igbo": "ig", "Indonesian": "id", "Inuinnaqtun": "ikt",
    "Inuktitut": "iu", "Inuktitut (Latin)": "iu-Latn", "Irish": "ga", "Italian": "it",
    "Japanese": "ja", "Kannada": "kn", "Kashmiri": "ks", "Kazakh": "kk", "Khmer": "km",
    "Kinyarwanda": "rw", "Klingon (Latin)": "tlh-Latn", "Klingon (plqaD)": "tlh-Piqd",
    "Konkani": "gom", "Korean": "ko", "Kurdish (Central)": "ku", "Kurdish (Northern)": "kmr",
    "Kyrgyz (Cyrillic)": "ky", "Lao": "lo", "Latvian": "lv", "Lithuanian": "lt",
    "Lingala": "ln", "Lower Sorbian": "dsb", "Luganda": "lug", "Macedonian": "mk",
    "Maithili": "mai", "Malagasy": "mg", "Malay (Latin)": "ms", "Malayalam": "ml",
    "Maltese": "mt", "Maori": "mi", "Marathi": "mr", "Mongolian (Cyrillic)": "mn-Cyrl",
    "Mongolian (Traditional)": "mn-Mong", "Nepali": "ne", "Norwegian": "nb", "Nyanja": "ny",
    "Odia": "or", "Pashto": "ps", "Polish": "pl", "Portuguese (Brazil)": "pt-BR",
    "Portuguese (Portugal)": "pt-PT", "Punjabi": "pa", "Quechua": "qu", "Romanian": "ro",
    "Russian": "ru", "Samoan": "sm", "Sanskrit": "sa", "Serbian (Cyrillic)": "sr-Cyrl",
    "Serbian (Latin)": "sr-Latn", "Sesotho": "st", "Shona": "sn", "Sindhi": "sd",
    "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", "Somali": "so", "Spanish": "es",
    "Sundanese (Latin)": "su", "Swahili": "sw", "Swati": "ss", "Swedish": "sv",
    "Tajik": "tg", "Tamil": "ta", "Tatar": "tt", "Telugu": "te", "Thai": "th",
    "Tigrinya": "ti", "Tswana": "tn", "Turkish": "tr", "Turkmen": "tk", "Ukrainian": "uk",
    "Urdu": "ur", "Uzbek (Cyrillic)": "uz-Cyrl", "Uzbek (Latin)": "uz-Latn", "Vietnamese": "vi",
    "Xhosa": "xh", "Yoruba": "yo", "Zulu": "zu"
    }
    
    for i,j in languages.items():
        if i == str(lang):
            return j
        



languages = {
    "Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar",
    "Armenian": "hy", "Assamese": "as", "Azerbaijani (Latin)": "az", "Bangla": "bn",
    "Bashkir": "ba", "Basque": "eu", "Bhojpuri": "bho", "Bodo": "brx", "Bosnian (Latin)": "bs",
    "Bulgarian": "bg", "Cantonese (Traditional)": "yue", "Catalan": "ca",
    "Chinese (Literary)": "lzh", "Chinese Simplified": "zh-Hans", "Chinese Traditional": "zh-Hant",
    "Shona": "sn", "Croatian": "hr", "Czech": "cs", "Danish": "da", "Dari": "prs",
    "Divehi": "dv", "Dogri": "doi", "Dutch": "nl", "English": "en", "Estonian": "et",
    "Faroese": "fo", "Fijian": "fj", "Filipino": "fil", "Finnish": "fi", "French": "fr",
    "French (Canada)": "fr-ca", "Galician": "gl", "Georgian": "ka", "German": "de",
    "Greek": "el", "Gujarati": "gu", "Haitian Creole": "ht", "Hausa": "ha",
    "Hebrew": "he", "Hindi": "hi", "Hmong Daw (Latin)": "mww", "Hungarian": "hu",
    "Icelandic": "is", "Igbo": "ig", "Indonesian": "id", "Inuinnaqtun": "ikt",
    "Inuktitut": "iu", "Inuktitut (Latin)": "iu-Latn", "Irish": "ga", "Italian": "it",
    "Japanese": "ja", "Kannada": "kn", "Kashmiri": "ks", "Kazakh": "kk", "Khmer": "km",
    "Kinyarwanda": "rw", "Klingon (Latin)": "tlh-Latn", "Klingon (plqaD)": "tlh-Piqd",
    "Konkani": "gom", "Korean": "ko", "Kurdish (Central)": "ku", "Kurdish (Northern)": "kmr",
    "Kyrgyz (Cyrillic)": "ky", "Lao": "lo", "Latvian": "lv", "Lithuanian": "lt",
    "Lingala": "ln", "Lower Sorbian": "dsb", "Luganda": "lug", "Macedonian": "mk",
    "Maithili": "mai", "Malagasy": "mg", "Malay (Latin)": "ms", "Malayalam": "ml",
    "Maltese": "mt", "Maori": "mi", "Marathi": "mr", "Mongolian (Cyrillic)": "mn-Cyrl",
    "Mongolian (Traditional)": "mn-Mong", "Nepali": "ne", "Norwegian": "nb", "Nyanja": "ny",
    "Odia": "or", "Pashto": "ps", "Polish": "pl", "Portuguese (Brazil)": "pt-BR",
    "Portuguese (Portugal)": "pt-PT", "Punjabi": "pa", "Quechua": "qu", "Romanian": "ro",
    "Russian": "ru", "Samoan": "sm", "Sanskrit": "sa", "Serbian (Cyrillic)": "sr-Cyrl",
    "Serbian (Latin)": "sr-Latn", "Sesotho": "st", "Shona": "sn", "Sindhi": "sd",
    "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", "Somali": "so", "Spanish": "es",
    "Sundanese (Latin)": "su", "Swahili": "sw", "Swati": "ss", "Swedish": "sv",
    "Tajik": "tg", "Tamil": "ta", "Tatar": "tt", "Telugu": "te", "Thai": "th",
    "Tigrinya": "ti", "Tswana": "tn", "Turkish": "tr", "Turkmen": "tk", "Ukrainian": "uk",
    "Urdu": "ur", "Uzbek (Cyrillic)": "uz-Cyrl", "Uzbek (Latin)": "uz-Latn", "Vietnamese": "vi",
    "Xhosa": "xh", "Yoruba": "yo", "Zulu": "zu"
    }

def translate_text(input_language,text, target_language):
    # input_language = langcode(input_language)
    print(input_language)   
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from':input_language,
        # 'to': [langcode(target_language)]
        'to': [target_language]
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{'text': text}]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    
    # Extract the translation
    translation = response[0]["translations"][0]['text']
    return translation


