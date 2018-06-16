from math import sqrt

def intsint(labels: list, key: float = 150.0, range: float = 1.0):
    if labels[0] not in ["T", "M", "B"]:
        raise ValueError("First item in list can't be relative")

    freq_t = key * sqrt(2 ** range)
    freq_m = key
    freq_b = key / sqrt(2 ** range)

    freqs = []

    for idx, l in enumerate(labels):
        if l == "T":
            freqs.append(freq_t)
        elif l == "M":
            freqs.append(freq_m)
        elif l == "B":
            freqs.append(freq_b)
        elif l == "H":
            freqs.append(sqrt(freqs[idx - 1] * freq_t))
        elif l == "S":
            freqs.append(freqs[idx - 1])
        elif l == "L":
            freqs.append(sqrt(freqs[idx - 1] * freq_b))
        elif l == "U":
            freqs.append(sqrt(freqs[idx - 1] * sqrt(freqs[idx - 1] * freq_t)))
        elif l == "D":
            freqs.append(sqrt(freqs[idx - 1] * sqrt(freqs[idx - 1] * freq_b)))

    return freqs

seq = list("TSLLSUHBU")
print(intsint(seq))
