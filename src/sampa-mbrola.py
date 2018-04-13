import sys

class Converter():
    def __init__(self):
        self.load_sampa_mbrola()

    def load_sampa_mbrola(self):
        equivs = {}
        with open("sampa-mbrola.phonemes") as f:
            for line in f:
                v, k = line.split()
                equivs[k] = v

        self.equivs = equivs

    def convert_phoneme(self, phoneme: str):
        if self.equivs and phoneme in self.equivs:
            return self.equivs[phoneme]
        else:
            return phoneme

    def convert_sentence(self, input_str):
        result = ["_"]
        forbidden = [
            "\n",
            ",",
            "'"
        ]

        input_str = input_str.strip()

        for phoneme in input_str:
            if phoneme not in forbidden:
                result.append(self.convert_phoneme(phoneme))

        result.append("_")
        return "\n".join(result)

if __name__ == "__main__":
    converter = Converter()
    for line in sys.stdin:
        print(line)
        print(converter.convert_sentence(line))
