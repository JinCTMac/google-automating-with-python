def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    # 1. splits text into words
    lower_text = file_contents.lower()
    split_text = lower_text.split()

    # 2. removing punctuation, stopwords and counting words into dict
    freq_dict = {}

    for word in split_text:
        word = word.lower()
        if word in punctuations:
            split_text.remove(word)
        elif word in uninteresting_words:
            split_text.remove(word)
        else:
            if word not in freq_dict:
                freq_dict[word] = 1
            else:
                freq_dict[word] += 1
    return freq_dict

print(calculate_frequencies("wow Wow Wow wow this is a really cool text wow this text is so cool poggers nice to lmao any all just few wow this can't be good great jumpy nice boy"))
