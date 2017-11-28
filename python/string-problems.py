def is_pal_perm(S):
    d = {}
    for char in S:
        if char in d:
            d[char] = d[char] + 1
        else:
            d[char] = 1

    has_seen_odd = False

    for char in d:
        if d[char] % 2 == 1:
            if has_seen_odd:
                return False
            has_seen_odd = True

    return True

# Check to see if the second string is one edit away from the first. An edit can be:
#   * Replace: exchange one character from the first
#   * Delete:  remove one character from the first
#   * Add:     add one character to the first
def one_edit_away(first, second):
    def edit_replace(first, second):
        seen_different = False
        for i in range(len(first)):
            if first[i] != second[i]:
                if seen_different:
                    return False
                seen_different = True
        return seen_different

    def edit_add(first, second):
        offset = 0
        for i in range(len(second)):
            if first[i - offset] != second[i]:
                if offset > 0:
                    return False
                offset += 1
        return True

    # Put the functions in a dict and use default is false
    if len(first) == len(second):
        return edit_replace(first, second)
    elif len(first) == len(second) - 1:
        return edit_add(second, first)
    elif len(first) == len(second) + 1:
        return edit_add(first, second)
    return False

print one_edit_away('helo', 'hello')
