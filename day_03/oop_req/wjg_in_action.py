from wordjumblegame_oop import wordjumblegame

p1 = wordjumblegame("Achal")
p2 = wordjumblegame("Rohit")
p3 = wordjumblegame("Saritha")


p = [p1, p2, p3]
for player in p:
    player.run()

for player in p:
    player.showresults()