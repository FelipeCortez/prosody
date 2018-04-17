import sys


class Converter():
    def __init__(self):
        self.load_sampa_mbrola()
        self.load_durations()

    def load_sampa_mbrola(self):
        equivs = {}
        with open("sampa-mbrola.tbl") as f:
            for line in f:
                v, k, _ = line.split()
                equivs[k] = v

        self.equivs = equivs

    def load_durations(self):
        durations = {}
        with open("durations.tbl") as f:
            for line in f:
                k, v = line.split()
                durations[k] = v

        self.durations = durations

    def convert_phoneme(self, phoneme: str):
        # não é _tão_ simples assim
        # fazer lookahead com regex
        # regras am, em, etc etc
        # s pode ser s (antes de vogal) ou s2 (antes de consoante)
        if self.equivs and phoneme in self.equivs:
            return self.equivs[phoneme]
        else:
            return phoneme

    def get_duration(self, phoneme: str) -> int:
        if self.durations and phoneme in self.durations:
            return self.durations[phoneme]
        else:
            return 100

    def convert_sentence(self, input_str):
        result = ["_ 50 50 150"]
        forbidden = ["\n", ",", "'"]

        input_str = input_str.strip()

        for phoneme in input_str:
            if phoneme not in forbidden:
                mbrola_line = "{} {} {} {}".format(
                    self.convert_phoneme(phoneme),
                    str(self.get_duration(phoneme)),
                    "50",
                    "150"
                )

                result.append(mbrola_line)

        result.append("_ 50 50 150")
        return "\n".join(result)


if __name__ == "__main__":
    converter = Converter()
    for line in sys.stdin:
        # print(line)
        print(converter.convert_sentence(line))
