def bin_to_dec(binary):
    result = 0
    for i in range(len(str(binary))):
        result += (int(str(binary)[-(i + 1)]) * 2) ** i
        print(result)


bin_to_dec(11011)
