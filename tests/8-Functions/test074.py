def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return kwargs['prefix'] + word
    elif "suffix" in kwargs:
        return word + kwargs['suffix']
    return word


print(combine_words("child", suffix="ish"))
print(combine_words("child", prefix="man"))
