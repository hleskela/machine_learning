import monkdata as m
import dtree as dtree

print("Assignment 1:")
print("Entropy of MONK-1:", dtree.entropy(m.monk1))
print("Entropy of MONK-2:", dtree.entropy(m.monk2))
print("Entropy of MONK-3:", dtree.entropy(m.monk3))

print("Assignment 2:")

print("{:3} {:<23} {:<23} {:<23}".format("#", "MONK-1", "MONK-2", "MONK-3"))
for at in m.attributes:
    print("{:3} {:<23} {:<23} {:<23}".format(at.name, dtree.averageGain(m.monk1, at),dtree.averageGain(m.monk2, at),dtree.averageGain(m.monk3, at)))
