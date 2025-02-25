import string

sentence = input ("Enter a sentence: ").strip()
if not sentence:
    print("Please enter a vaild sentence!")
else:
    cleaned_sentence = sentence.translate(
        str.maketrans('', '', string.punctuation))
    words =cleaned_sentence.split()
    word_count = len(words)

    print("\n📌 Processed Sentence:", cleaned_sentence)
    print("🔤 Words List:", words)
    print("🔢 Total Words:", word_count)
