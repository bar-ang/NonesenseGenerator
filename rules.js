{
    "SPEECH" : [
        ["SENTENCE"],
        ["QUESTION"]
    ],

    "SENTENCE" : [
        ["SIMPLE_SENTENCE"],
        ["SENTENCE", "COMMA", "CONJUNCTION", "SIMPLE_SENTENCE"]
    ],

    "QUESTION" : [
        ["YES_NO_QUESTION", "QUESTION_MARK"],
        ["WH_QUESTION", "QUESTION_MARK"]
    ],

    "WH_QUESTION" : [
        ["INTERROGATIVE", "YES_NO_QUESTION"]
    ],

    "YES_NO_QUESTION" : [
        ["BE", "SUBJECT", "STATIVE"]
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
        ["ARTICLE", "ADJECTIVE", "NOUN"],
        ["ARTICLE", "ADJECTIVE", "NOUN", "THAT", "ACTION"]
    ],

    "ACTION" : [
        ["VERB"],
        ["VERB", "OBJECT"],
        ["VERB", "ADVERB", "OBJECT"],
        ["VERB", "OBJECT", "ADVERB"],
        ["STATIVE"]
    ],

    "STATIVE" : [
        ["BE", "ADJECTIVE"],
        ["BE", "OBJECT"]
    ]
}

