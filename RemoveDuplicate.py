def rem_duplicates(s):
    final = []
    for n in s:
        if n not in final:
            final.append(n)
    return final
print(rem_duplicates([1,2,3,4,3,5,7,7]))
