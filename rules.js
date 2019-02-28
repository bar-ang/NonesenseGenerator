{
    "SPEECH" : [
        ["SENTENCE"],
        ["QUESTION"]
    ],

    "SENTENCE" : [
        ["SIMPLE_SENTENCE"],
        ["SENTENCE", "COMMA", "CONJUNCTION", "SIMPLE_SENTENCE"]
    ],

    "SIMPLE_SENTENCE" : [
        ["SUBJECT", "ACTION"]
    ],

    "SUBJECT" : [
        ["NOUN_PHRASE"]
    ],

    "OBJECT" : [
        ["NOUN_PHRASE"]
    ],

    "NOUN_PHRASE" : [
        ["ARTICLE", "NOUN"],
        ["ARTICLE", "ADJECTIVE", "NOUN"]
    ],

    "ACTION" : [
        ["VERB"],
        ["VERB", "OBJECT"],
        ["VERB", "ADVERB", "OBJECT"],
        ["VERB", "OBJECT", "ADVERB"]
    ]
}

