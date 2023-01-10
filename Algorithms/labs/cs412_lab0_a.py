"""
    name: Brandon Quinn

"""
# 1. I used a dictionary to hold onto the words and their definitions
# 2. I used .update, .get, and .keys
# 3. update: O(1), get: O(1), keys: I read online in python 3 that it is O(1)
# 4. I think it would be what we discussed in class O(m + n)
# 5. My algorithm works because it translates the words based off their
# definitions correctly (although it was hard to tell for the one with 10000
# lines of input).

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    dict_log = {}
    message = ""
    count = 0
    translation = ""
    # your code here
    n = int(input())
    lines = [input().split(" ") for _ in range(n + 1)]
    for line in lines:
        if count != n:
            if line[1] not in dict_log.keys():
                dict_log.update({line[1]: line[0]})
        else:
            message = line
        count += 1
    for word in message:
        if word not in dict_log:
            translation += "??? "
        else:
            translation += dict_log.get(word)
            translation += " "
    print(translation)


if __name__ == "__main__":
    main()
