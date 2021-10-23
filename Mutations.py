def mutate_string(a, position, character):
    l=list(a)
    l[position]=character
    a="".join(l)
    return a
