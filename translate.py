#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse

lst = {
    "`": "_",
    "1": "ๅ",
    "2": "/",
    "3": "-",
    "4": "ภ",
    "5": "ถ",
    "6": "ุ",
    "7": "ึ",
    "8": "ค",
    "9": "ต",
    "0": "จ",
    "-": "ข",
    "=": "ช",
    "q": "ๆ",
    "w": "ไ",
    "e": "ำ",
    "r": "พ",
    "t": "ะ",
    "y": "ั",
    "u": "ี",
    "i": "ร",
    "o": "น",
    "p": "ย",
    "[": "บ",
    "]": "ล",
    "\\": "ฃ",
    "a": "ฟ",
    "s": "ห",
    "d": "ก",
    "f": "ด",
    "g": "เ",
    "h": "้",
    "j": "่",
    "k": "า",
    "l": "ส",
    ";": "ว",
    "'": "ง",
    "z": "ผ",
    "x": "ป",
    "c": "แ",
    "v": "อ",
    "b": "ิ",
    "n": "ื",
    "m": "ท",
    ",": "ม",
    ".": "ใ",
    "/": "ฝ",
    "~": "%",
    "!": "+",
    "@": "๑",
    "#": "๒",
    "$": "๓",
    "%": "๔",
    "^": "ู",
    "&": "฿",
    "*": "๕",
    "(": "๖",
    ")": "๗",
    "_": "๘",
    "+": "๙",
    "Q": "๐",
    "W": "\"",
    "E": "ฎ",
    "R": "ฑ",
    "T": "ธ",
    "Y": "ํ",
    "U": "๊",
    "I": "ณ",
    "O": "ฯ",
    "P": "ญ",
    "{": "ฐ",
    "}": ",",
    "|": "ฅ",
    "A": "ฤ",
    "S": "ฆ",
    "D": "ฏ",
    "F": "โ",
    "G": "ฌ",
    "H": "็",
    "J": "๋",
    "K": "ษ",
    "L": "ศ",
    ":": "ซ",
    "\"": ".",
    "Z": "(",
    "X": ")",
    "C": "ฉ",
    "V": "ฮ",
    "B": "ฺ",
    "N": "์",
    "M": "?",
    "<": "ฒ",
    ">": "ฬ",
    "?": "ฦ"
}


class BrainNotFoundError(FileNotFoundError):
    pass


class UserIsTooDumpError(BrainNotFoundError):
    pass


def _main_(args):
    word = args.word
    lang = args.language
    if lang not in ['th', 'en', 't', 'e']:
        raise UserIsTooDumpError('Dude, you must enter language as one of (th, en, t, e)')
    output = ''
    if lang in ['en', 'e']:
        for char in word:
            output += lst[char]
    else:
        for char in word:
            output += list(lst.keys())[list(lst.values()).index(char)]
    print(output)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='translate thai kedmani to')
    argparser.add_argument('-w', '--word', help='word to translate')
    argparser.add_argument('-l', '--language', help='input language(t or e)')

    args = argparser.parse_args()
    _main_(args)
