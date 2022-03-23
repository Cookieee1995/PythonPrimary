class rec: pass

rec.name = 'Bob'
rec.age = 40

print(rec.name)

x = rec()
y = rec()

print(x.name,y.name)

x.name = 'Sue'
print(rec.name,x.name,y.name)

print(list(rec.__dict__.keys()))
print(list(name for name in rec.__dict__ if not name.startswith('_')))
print(list(x.__dict__.keys()))
print(list(y.__dict__.keys()))