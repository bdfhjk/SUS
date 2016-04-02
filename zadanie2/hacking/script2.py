with open('output') as f:
    content = f.read().splitlines()

content = list(set(content))
content.sort()

for i in content:
    print i
