#python slicing
name="purnima"
print(name[::-1])
print(name[1:5])
print(name[::-2])


#split and join
sentence="my name is Purnima"
sp=sentence.split()
print(sp)
jo=' '.join(sp)


#find word in sentence:
if "name" in sentence:
    print("word found!")
print(sentence.find("name"))

print("python" in sentence)

text="I love Java"
print(text.replace("Jave","Python"))