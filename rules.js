RULES = {
        Var.SENTENCE : [
            [Var.IMPARATIVE_SENTENCE],
            [Var.IMPARATIVE_SENTENCE],
            [Var.IMPARATIVE_SENTENCE],
            [Var.QUESTION],
        ],

        Var.IMPARATIVE_SENTENCE : [
            [Var.SIMPLE_SENTENCE],
            [Var.SIMPLE_SENTENCE, Var.COMMA, Var.CONJUNCTION, Var.IMPARATIVE_SENTENCE]
        ],

        Var.QUESTION : [
            [Var.SIMPLE_QUESTION, Var.QUESTION_MARK],
        ],

        Var.SIMPLE_QUESTION : [
            [Var.QUESTION_VERB, Var.SUBJECT, Var.VERB_PHRASE],
        ],

        Var.SIMPLE_SENTENCE : [
            [Var.SUBJECT, Var.VERB_PHRASE],
        ],

        Var.VERB_PHRASE : [
            [Var.VERB],
            [Var.NOT_CLAUSE, Var.VERB]
        ],

        Var.VERB : [
            [Var.TRANSITIVE_VERB, Var.OBJECT],
            [Var.INTRANSITIVE_VERB],
            [Var.TRANSITIVE_VERB, Var.OBJECT, Var.ADVERB],
            [Var.INTRANSITIVE_VERB, Var.ADVERB],
            [Var.ADVERB, Var.TRANSITIVE_VERB, Var.OBJECT],
        ],

        Var.SUBJECT : [
            [Var.NOUN_PHRASE],
            [Var.PRONOUN],
        ],

        Var.OBJECT : [
            [Var.NOUN_PHRASE],
        ],

        Var.NOUN_PHRASE : [
            [Var.ARTICLE, Var.NOUN],
            [Var.ARTICLE, Var.ADJECTIVE, Var.NOUN],
        ],
}

