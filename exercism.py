def response(hey_bob):
    hey_bob = " ".join(hey_bob.split())

    if hey_bob == "":
        return "Fine. Be that way!"
    if hey_bob == hey_bob.upper() != hey_bob.lower() and hey_bob[-1] == '?':
        return "Calm down, I know what I'm doing!"
    if hey_bob[-1] == '?':
        return "Sure."
    if hey_bob == hey_bob.upper() != hey_bob.lower():
        return "Whoa, chill out!"
    return "Whatever."

print(response('The   fox jumped   over    the log.'))
