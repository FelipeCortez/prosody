import sys
import re
import subprocess
import random
import json
from collections import OrderedDict
from typing import List

def flatten(lst: list):
    return [item for sublist in lst for item in sublist]

class Phone():
    def __init__(
            self,
            phone_sampa: str,
            phone_mbrola: str,
            duration: int,
            pitch_changes: list
    ):
        self.phone_sampa = phone_sampa
        self.phone_mbrola = phone_mbrola
        self.duration = duration
        self.pitch_changes = pitch_changes

    def as_line(self):
        return "{} {} {}".format(
            self.phone_mbrola,
            self.duration,
            " ".join([str(item) for item in flatten(self.pitch_changes)])
        )

class Sentence():
    def __init__(self, phones: List[Phone]=None):
        if phones is None:
            self.phones = []
        else:
            self.phones = phones

    def mbrola_phones(self):
        return [phone.phone_mbrola for phone in self.phones]

    def dictify(self):
        return [vars(phone) for phone in self.phones]

    def __repr__(self):
        return "\n".join([phone.as_line() for phone in self.phones])


class Converter():
    def __init__(self):
        self.load_sampa_mbrola()
        self.load_durations()

    def load_sampa_mbrola(self):
        equivs = {}
        with open("sampa_mbrola.tbl") as f:
            for line in f:
                k, v, _ = line.split()
                equivs[k] = v

        self.equivs = OrderedDict(
            sorted(equivs.items(), key=lambda t: -len(t[0])))

    def load_durations(self):
        durations = {}
        with open("durations.tbl") as f:
            for line in f:
                k, v = line.split()
                durations[k] = v

        self.durations = durations

    def convert_phoneme(self, sentence: str) -> tuple:
        """Returns first phone from the sentence"""

        if sentence[0] == " ":
            return ("_", 1)
        elif self.equivs:
            # s is a special case, needs to peek next
            if sentence[0] == "s":
                if sentence[1] in "aeiou&":
                    return ("s", 1)

            for equiv in self.equivs.items():

                if re.match(re.escape(equiv[0]), sentence):
                    # print("match:", equiv[0], phoneme, "=", equiv[1])
                    return (equiv[1], len(equiv[0]))

        # print("didn't match", phoneme)
        return (phoneme[0], 1)

    def get_duration(self, phoneme: str) -> int:
        if self.durations and phoneme in self.durations:
            return self.durations[phoneme]
        else:
            return 100

    def convert_sentence(self, input_str: str) -> Sentence:
        sentence = Sentence()
        sentence.phones.append(Phone(" ", "_", 150, [[50, 150]]))

        ignored = ["@", "\n", ",", "'", "^", ";"]
        # ' is a stress marker, should be important later

        sampa = self.text_to_sampa(input_str)
        sampa = sampa.replace("'", "")
        print(";; ", sampa)

        while sampa:
            if sampa[0] not in ignored:
                converted = self.convert_phoneme(sampa)
                phone_sampa = sampa[:converted[1]]
                sampa = sampa[converted[1]:]

                duration = self.get_duration(converted[0])
                phone = Phone(
                    phone_sampa = phone_sampa,
                    phone_mbrola = converted[0],
                    duration = int(duration),
                    pitch_changes = [[50, 150]] # percentage, Hz
                )

                sentence.phones.append(phone)
            else:
                sampa = sampa[1:]

        sentence.phones.append(Phone(" ", "_", 150, [[50, 150]]))
        return sentence

    def text_to_sampa(self, sentence: str) -> str:
        espeak_str = "espeak-ng -v pt-br '{}' -x -q".format(sentence)

        p = subprocess.Popen(espeak_str, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        output = output.decode("utf-8")
        output = output.replace("\n", "").strip()
        return output


if __name__ == "__main__":
    converter = Converter()

    for line in sys.stdin:
        print(";;", line)
        print(converter.convert_sentence(line))
