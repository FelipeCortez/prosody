import sys
import re
import subprocess
from collections import OrderedDict


class Converter():
    def __init__(self):
        self.load_sampa_mbrola()
        self.load_durations()

    def load_sampa_mbrola(self):
        equivs = {}
        with open("sampa-mbrola.tbl") as f:
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

    def convert_phoneme(self, phoneme: str):
        if phoneme[0] == " ":
            return ("_", 1)
        elif self.equivs:
            for equiv in self.equivs.items():
                if re.match(re.escape(equiv[0]), phoneme):
                    # print("match:", equiv[0], phoneme, "=", equiv[1])
                    return (equiv[1], len(equiv[0]))

        # print("didn't match", phoneme)
        return (phoneme[0], 1)

    def get_duration(self, phoneme: str) -> int:
        if self.durations and phoneme in self.durations:
            return self.durations[phoneme]
        else:
            return 100

    def convert_sentence(self, input_str: str) -> str:
        result = ["_ 50 50 150"]
        ignored = ["@", "\n", ",", "'", "^", ";"]
        # ' is a stress marker, should be important later

        sampa = self.text_to_sampa(input_str)
        sampa = sampa.replace("'", "")
        print(";; ", sampa)

        while sampa:
            if sampa[0] not in ignored:
                converted = self.convert_phoneme(sampa)
                sampa = sampa[converted[1]:]

                mbrola_line = "{} {} {} {}".format(
                    converted[0], str(self.get_duration(converted[0])), "50", "150")

                # print(sampa)
                result.append(mbrola_line)
            else:
                sampa = sampa[1:]

        result.append("_ 50 50 150")
        return "\n".join(result)

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
