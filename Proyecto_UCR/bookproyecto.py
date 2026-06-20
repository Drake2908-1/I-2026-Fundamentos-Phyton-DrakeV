class letras:
    def __init__ (self,mayusculas, minusculas,):
        self.mayusculas = mayusculas
        self.minusculas = minusculas
        self.letras = []

    def agregar_letras (self,letras):
        self.letras.append(letras)

    def eliminar_letra  (self, letras):
        for letras_en_lista in self.letras:
          if  letras_en_lista == letras:
              self.letras.remove(letras_en_lista)
          break

a = letras ("A", "a")
b = letras ("B", "b")
c = letras ("C", "c")
d = letras ("D", "d")
e = letras ("E", "e")
f = letras ("F", "f")
g = letras ("G", "g")
h = letras ("H", "h")
i= letras ("I", "i")
j = letras ("J", "j")
k = letras ("K", "k")
l = letras ("L", "l")
m = letras ("M", "m")
n = letras ("N", "n")
ñ = letras ("Ñ", "ñ")
o = letras ("O", "o")
p = letras ("P", "p")
q = letras ("Q", "q")
r = letras ("R", "r")
s = letras ("S", "s")
t = letras ("T", "t")
u = letras ("U", "u")
v = letras ("V", "v")
w = letras ("W", "w")
x = letras ("X", "x")
y = letras ("Y", "y")
z = letras ("Z", "z")

a.agregar_letras("A")
b.agregar_letras("B")
c.agregar_letras("C")
d.agregar_letras("D")
e.agregar_letras("E")
f.agregar_letras("F")
g.agregar_letras("G")
h.agregar_letras("H")
i.agregar_letras("I")
j.agregar_letras("J")
k.agregar_letras("K")
l.agregar_letras("L")
m.agregar_letras("M")
n.agregar_letras("N")
ñ.agregar_letras("Ñ")
o.agregar_letras("O")
p.agregar_letras("P")
q.agregar_letras("Q")
r.agregar_letras("R")
s.agregar_letras("S")
t.agregar_letras("T")
u.agregar_letras("U")
v.agregar_letras("V")
w.agregar_letras("W")
x.agregar_letras("X")
y.agregar_letras("Y")
z.agregar_letras("Z")

letra=str(input("Inserte la letra:"))
letras = letras(letra.upper(), letra.lower())

print("sugerencia";Sugerencia)











        
              
