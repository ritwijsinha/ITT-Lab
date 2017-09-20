import string
mail = "\nDear <name>,\n\nThis is a sample email. Unfortunately, I do not have enough shits to give.\nBest of luck for whatever.\n\nRegards,\nRitwij\n\n\n"
names = ["MaybeRitwij","AlmostRitwij","NotRitwij"]
for i in names:
	print string.replace(mail,"<name>",i)