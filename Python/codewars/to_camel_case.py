def to_camel_case(text):
    if not text:
        return text
    s = text.replace("-", " ").replace("_", " ")
    s = s.split(' ')
    return f"{s[0]}{''.join(i.capitalize() for i in s[1:])}"


def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s