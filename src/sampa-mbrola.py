def load_sampa_mbrola():
    equivs = {}
    with open("sampa-mbrola.phonemes") as f:
        for line in f:
            k, v = line.split()
            equivs[k] = v
            print(k, v)
    return equivs


if __name__ == "__main__":
    load_sampa_mbrola()
