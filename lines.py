import glob
files = glob.glob("*.py")
del files[files.index("lines.py")]
ct = 0
for f in files:
	ct += len(open(f).read().split("\n"))
print(ct)