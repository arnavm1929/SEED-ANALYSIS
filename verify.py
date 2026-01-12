def count(folder):
    import os
    return sum(len(files) for _,_,files in os.walk(folder))

print("TRAIN =", count("VegSeedsBD/train"))
print("VAL   =", count("VegSeedsBD/val"))
print("TEST  =", count("VegSeedsBD/test"))
