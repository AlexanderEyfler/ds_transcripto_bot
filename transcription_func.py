from string import punctuation

TRANSCRIPTION_SYMBOLS = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ë': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TS',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ь': '',
    'Ы': 'Y',
    'Ъ': 'IE',
    'Э': 'E',
    'Ю': 'IU',
    'Я': 'IA',
}

def transcription(fio: str) -> str:
    cleaned_text = ''.join(let for let in fio if let not in punctuation)
    buffer_list = []

    for word in cleaned_text.upper().split(' '):
        buffer_string = ''
        for letter in word:
            buffer_string += TRANSCRIPTION_SYMBOLS[letter]
        buffer_list.append(buffer_string)

    return ' '.join(x.capitalize() for x in buffer_list)
    