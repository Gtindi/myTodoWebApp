def longest_string(glist):
    if len(glist) == 1:
        return len(glist[0])
    else:
        return max(len(glist[0]), longest_string(glist[1:]))
print(longest_string(['exam', 'an', 'test', 'fry']))
print(longest_string(['pan']))
print(longest_string(['can', 'pan', 'tan', 'ban', 'fan']))
print(longest_string(['an', 'exam', 'fan', 'banana', 'banana']))