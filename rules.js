{
        "SENTENCE" : [
            ["IMPARATIVE_SENTENCE"],
            ["IMPARATIVE_SENTENCE"],
            ["IMPARATIVE_SENTENCE"],
            ["QUESTION"]
        ],
        
        "IMPARATIVE_SENTENCE" : [
            ["SIMPLE_SENTENCE"],
            ["SIMPLE_SENTENCE", "COMMA", "CONJUNCTION", "IMPARATIVE_SENTENCE"]
        ],

        "QUESTION" : [
            ["SIMPLE_QUESTION", "QUESTION_MARK"]
        ],

        "SIMPLE_QUESTION" : [
            ["QUESTION_VERB", "SUBJECT", "VERB_PHRASE"]
        ],

        "SIMPLE_SENTENCE" : [
            ["SUBJECT", "VERB_PHRASE"]
        ],

        "VERB_PHRASE" : [
            ["VERB"],
            ["NOT_CLAUSE", "VERB"]
        ],

        "VERB" : [
            ["TRANSITIVE_VERB", "OBJECT"],
            ["INTRANSITIVE_VERB"],
            ["TRANSITIVE_VERB", "OBJECT", "ADVERB"],
            ["INTRANSITIVE_VERB", "ADVERB"],
            ["ADVERB", "TRANSITIVE_VERB", "OBJECT"]
        ],

        "SUBJECT" : [
            ["NOUN_PHRASE"],
            ["PRONOUN"]
        ],

        "OBJECT" : [
            ["NOUN_PHRASE"]
        ],

        "NOUN_PHRASE" : [
            ["ARTICLE", "NOUN"],
            ["ARTICLE", "ADJECTIVE", "NOUN"]
        ]
}

