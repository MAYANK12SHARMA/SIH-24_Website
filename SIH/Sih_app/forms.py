from django import forms

class TranslateForm(forms.Form):
    text = forms.CharField(label='Enter Text', max_length=1000)
    
    language_choices = [
        ("af", "Afrikaans"), ("sq", "Albanian"), ("am", "Amharic"), ("ar", "Arabic"),
        ("hy", "Armenian"), ("as", "Assamese"), ("az", "Azerbaijani (Latin)"), ("bn", "Bangla"),
        ("ba", "Bashkir"), ("eu", "Basque"), ("bho", "Bhojpuri"), ("brx", "Bodo"), ("bs", "Bosnian (Latin)"),
        ("bg", "Bulgarian"), ("yue", "Cantonese (Traditional)"), ("ca", "Catalan"),
        ("lzh", "Chinese (Literary)"), ("zh-Hans", "Chinese Simplified"), ("zh-Hant", "Chinese Traditional"),
        ("sn", "Shona"), ("hr", "Croatian"), ("cs", "Czech"), ("da", "Danish"), ("prs", "Dari"),
        ("dv", "Divehi"), ("doi", "Dogri"), ("nl", "Dutch"), ("en", "English"), ("et", "Estonian"),
        ("fo", "Faroese"), ("fj", "Fijian"), ("fil", "Filipino"), ("fi", "Finnish"), ("fr", "French"),
        ("fr-ca", "French (Canada)"), ("gl", "Galician"), ("ka", "Georgian"), ("de", "German"),
        ("el", "Greek"), ("gu", "Gujarati"), ("ht", "Haitian Creole"), ("ha", "Hausa"),
        ("he", "Hebrew"), ("hi", "Hindi"), ("mww", "Hmong Daw (Latin)"), ("hu", "Hungarian"),
        ("is", "Icelandic"), ("ig", "Igbo"), ("id", "Indonesian"), ("ikt", "Inuinnaqtun"),
        ("iu", "Inuktitut"), ("iu-Latn", "Inuktitut (Latin)"), ("ga", "Irish"), ("it", "Italian"),
        ("ja", "Japanese"), ("kn", "Kannada"), ("ks", "Kashmiri"), ("kk", "Kazakh"), ("km", "Khmer"),
        ("rw", "Kinyarwanda"), ("tlh-Latn", "Klingon (Latin)"), ("tlh-Piqd", "Klingon (plqaD)"),
        ("gom", "Konkani"), ("ko", "Korean"), ("ku", "Kurdish (Central)"), ("kmr", "Kurdish (Northern)"),
        ("ky", "Kyrgyz (Cyrillic)"), ("lo", "Lao"), ("lv", "Latvian"), ("lt", "Lithuanian"),
        ("ln", "Lingala"), ("dsb", "Lower Sorbian"), ("lug", "Luganda"), ("mk", "Macedonian"),
        ("mai", "Maithili"), ("mg", "Malagasy"), ("ms", "Malay (Latin)"), ("ml", "Malayalam"),
        ("mt", "Maltese"), ("mi", "Maori"), ("mr", "Marathi"), ("mn-Cyrl", "Mongolian (Cyrillic)"),
        ("mn-Mong", "Mongolian (Traditional)"), ("ne", "Nepali"), ("nb", "Norwegian"), ("ny", "Nyanja"),
        ("or", "Odia"), ("ps", "Pashto"), ("pl", "Polish"), ("pt-BR", "Portuguese (Brazil)"),
        ("pt-PT", "Portuguese (Portugal)"), ("pa", "Punjabi"), ("qu", "Quechua"), ("ro", "Romanian"),
        ("ru", "Russian"), ("sm", "Samoan"), ("sa", "Sanskrit"), ("sr-Cyrl", "Serbian (Cyrillic)"),
        ("sr-Latn", "Serbian (Latin)"), ("st", "Sesotho"), ("sn", "Shona"), ("sd", "Sindhi"),
        ("si", "Sinhala"), ("sk", "Slovak"), ("sl", "Slovenian"), ("so", "Somali"), ("es", "Spanish"),
        ("su", "Sundanese (Latin)"), ("sw", "Swahili"), ("ss", "Swati"), ("sv", "Swedish"),
        ("tg", "Tajik"), ("ta", "Tamil"), ("tt", "Tatar"), ("te", "Telugu"), ("th", "Thai"),
        ("ti", "Tigrinya"), ("tn", "Tswana"), ("tr", "Turkish"), ("tk", "Turkmen"), ("uk", "Ukrainian"),
        ("ur", "Urdu"), ("uz-Cyrl", "Uzbek (Cyrillic)"), ("uz-Latn", "Uzbek (Latin)"), ("vi", "Vietnamese"),
        ("xh", "Xhosa"), ("yo", "Yoruba"), ("zu", "Zulu")
    ]
    input_language = forms.ChoiceField(label="Select input Language", choices=language_choices)
    target_language = forms.ChoiceField(label="Select target Language", choices=language_choices)
    
