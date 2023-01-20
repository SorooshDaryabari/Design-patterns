def alphabets_upto(letter):
    for i in range(65, ord(letter)+1):
        yield chr(i)


if __name__ == "__main__":
    alphabets_upto_K = alphabets_upto("K")
    alphabets_upto_M = alphabets_upto("M")

    for alpha in alphabets_upto_K:
        print(alpha, end=" ")

    print()

    for alpha in alphabets_upto_M:
        print(alpha, end=" ")
