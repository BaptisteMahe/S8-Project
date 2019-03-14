from réseau import Reseau

res = Reseau()
res.set_error(1)

# res.print_data()

res.set_couche(4)
res.add_all_neurone([3, 5, 7, 3])
res.create_reseau()

# res.print_all()
""" test basique
res.learn([1, 0, 1], [1, 1, 0])
res.learn([1, 0, 0], [0, 0, 0])
res.learn([0, 0, 0], [1, 0, 1])
res.learn([1, 1, 1], [1, 1, 1])
"""

for i in [0, 1]:
    for j in [0, 1]:
        for k in [0, 1]:
            res.learn([i, j, k], [0, 0, 0])

res.print_all()

res.parcourir([1, 1, 1])

res.print_last_couche()
"""
    optimisation du for i in range...
"""
