violations=["kl-08-av-2794",
            "kl-08-av-4970",
            "kl-01-av-14",
            "kl-01-av-1",
            "kl-01-av-12",
            "tn-01-av-1",
            "ghz-01-avo-1",
            "klo-01-ac0-10"
            ]

from re import *
rule="[k][l][-][0-9]{2}[-][a-z]{2}[-][0-9]{4}"
for num in violations:
    matcher=fullmatch(rule,num)
    if matcher!=None:
        print(num)


tweets="What a game, hats off both teams. Well done @benstokes38 @patcummins30 you have bought test cricket back  to life. love test cricket @TheBarmyArmy @cricketAus @ECB_cricket"
from re import *
rule="[@][a-zA-Z0-9_]*"
matcher=finditer(rule,tweets)
for m in matcher:
    print(m.group())
    