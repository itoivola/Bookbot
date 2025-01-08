file = "books/frankenstein.txt"
def count_words(content):
    return len(content.split())

def count_chars(content):
    chars = list(content.lower())
    charcount = {} 
    for char in chars:
        if char in charcount:
            charcount[char] += 1
        else:
            charcount[char] = 1
    return charcount

def sorthelper(dict):
    sortable = []
    for k in dict:
        sortable.append({"character": k, "sum": dict[k]})
    return sortable

def sort_on(dict):
    return dict["sum"]

def report(charcount):
    print(f"--- Begin report of {file} ---")
    print(f"{count_words(file_contents)} words in the document")
    print("")

    for dict in charcount:
        if dict["character"].isalpha():
            print(f"The {dict["character"]} was found {dict["sum"]} times")

    print("--- End report ---")


with open(file) as f:
    file_contents = f.read()

charcount = sorthelper(count_chars(file_contents))
charcount.sort(reverse=True, key=sort_on)

report(charcount)
