import glob
files = glob.glob("*.py")
ct = 0
for f in files:
	ct += len(open(f).read().split("\n"))
print(ct)