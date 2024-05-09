short_form={'CU':'see you',
            ':-)':"I’m happy",
            ':-(':"l’m unhappy",
            ';-)':'wink',
            ':-P':'stick out my tongue',
            '(~,~)':'sleepy',
            'TA':'totally awesome',
            'CCC':'Canadian Computing Competition',
            'CUZ':'because',
            'TY':'thank-you',
            'YW':"you’re welcome",
            'TTYL':'talk to you later'}

while True:
    short=input()

    if short in short_form:
        print(short_form[short])
        if short=='TTYL':
            break
    else:
        print(short)