import student
import mary

x = student.a["code"]
y = student.b["code"]
z = student.b["age"]
j = student.a["student"]
k = student.a["father"]

print(x)
print(y)
print(z)
print(j)
print(k)

for i in range(len(student.f)):
	print(i, student.f[i])

for i in range(len(mary.a)):
	print(i, mary.a[i])