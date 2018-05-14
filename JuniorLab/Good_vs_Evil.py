good = "707 423 584 293 572 62"
evil = "135 864 981 626 15 152 121"

def goodvsevil(good, evil):
    good_score = [1,2,3,3,4,10]
    evil_score = [1,2,2,2,3,5,10]
    good = [int(x) * y for x,y in zip(good.split(' '),good_score)]
    evil = [int(x) * y for x,y in zip(evil.split(' '),evil_score)]
    answer = sum(good) - sum(evil)
    if answer > 0:
        return "Battle Result: Good triumphs over Evil"
    elif answer < 0:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"

print(goodvsevil(good,evil))
