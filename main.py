def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{wc(file_contents)} words found in the document")
        print()

        charDict = charCount(file_contents)
        charList = sorted(charDict.items(), key=lambda x: x[1], reverse=True)
        for item in charList:
            print(f"The '{item[0]}' character was found {item[1]} times")

        print("--- End report ---")


def wc(str):
    return len(str.split())


def charCount(str):
    dict = {}

    for c in str:
        if not c.isalpha():
            continue

        c = c.lower()

        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1

    return dict


main()
