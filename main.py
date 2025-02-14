def main():
    with open("books/frankenstein.txt") as f:
        file_contents=f.read()
        wordlist = file_contents.split()
        word_count = len(wordlist)
        print(word_count)
        char_counted= char_count(file_contents)

        sortiert = sortiere_den_dreck(char_counted)
        print(sortiert)
        result_print(word_count,sortiert)

def char_count(file_content):
    dict = {}
    file_content = file_content.lower()
    for char in file_content:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def sortiere_den_dreck(dict):
    dreckliste_fuer_dreck_dictionary = []
    for key, value in dict.items():
        if key.isalpha():
            dreckliste_fuer_dreck_dictionary.append({"letter": key, "num": value})

    dreckliste_fuer_dreck_dictionary.sort(reverse=True,key=sort_on)

    return dreckliste_fuer_dreck_dictionary


def result_print(wort_anzahl , zeichen_liste):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wort_anzahl}  words found in the document")
    for element in zeichen_liste:
        print(f"The {element['letter']} character was found {element['num']} times")
    print("--- End report ---")

        

#main
main()