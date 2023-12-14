import cmath

import numpy as np
import matplotlib.pyplot as plt

class QuestionNo1:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def A(self):
        return self.a + self.d

    def B(self):
        return self.a / self.d

    def C(self):
        resultA = self.a * self.b
        resultB = self.c * self.d
        return resultA, resultB

    def D(self):
        result = {
            "Bilangan real z1": self.a.real,
            "Bilangan real z2": self.b.real,
            "Bilangan Imag z3": self.c.imag,
            "Bilangan Imag z4": self.d.imag
        }
        return result

    def E(self):
        result = {
            "Hasil z1": self.a.conjugate(),
            "Hasil z3": self.c.conjugate(),
            "Hasil z2": self.b.conjugate()
        }
        return result

    def F(self):
        result = {
            "Hasil z1": abs(self.a),
            "Hasil z3": abs(self.c)
        }
        return result


a = complex(-1, 3)
b = complex(0, 5)
c = complex(2, 0)
d = complex(-1, -1)

question = QuestionNo1(a, b, c, d)
print(f"(A). z1 + z2 = {question.A()}")
print(f"(B). z1 / z4 = {question.B()}")
print(f"(c). z1 * z2, z1 * z4 = {question.C()}")
print(question.D())
print(question.E())
print(question.F())

z1_matrix = np.array([[-1, -3], [3, -1]])
z4_vector = np.array([-1, -1])

# z1z4
result_z1z4 = np.dot(z1_matrix, z4_vector)
print("z1z4 =", result_z1z4)  # Output: z1z4 = [ 2 -5]

# z4z1
z4_matrix = np.array([[-1, -1], [-1, 3]])
z1_vector = np.array([-1, 3])
result_z4z1 = np.dot(z4_matrix, z1_vector)
print("z4z1 =", result_z4z1)  # Output: z4z1 = [ 2 -5]

# z2z4
z2_matrix = np.array([[0, -5], [5, 0]])
result_z2z4 = np.dot(z2_matrix, z4_vector)
print("z2z4 =", result_z2z4)  # Output: z2z4 = [-5 -5]

def to_polar(z):
    magnitude = abs(z)
    angle = cmath.phase(z)
    angle_deg = angle * 180 / cmath.pi  # Mengonversi sudut ke dalam derajat
    return magnitude, angle_deg

# Bilangan kompleks
z1 = 1 + 1j
z2 = -0.5 - 0.4j
z3 = 3 - 2j
z4 = 3
z5 = -1j

# Mengubah ke bentuk polar
polar_z1 = to_polar(z1)
polar_z2 = to_polar(z2)
polar_z3 = to_polar(z3)
polar_z4 = to_polar(complex(z4))  # Mengonversi ke bilangan kompleks jika bentuknya bilangan bulat
polar_z5 = to_polar(z5)

# Menampilkan hasil
print(f"z1 dalam bentuk polar: {polar_z1}")
print(f"z2 dalam bentuk polar: {polar_z2}")
print(f"z3 dalam bentuk polar: {polar_z3}")
print(f"z4 dalam bentuk polar: {polar_z4}")
print(f"z5 dalam bentuk polar: {polar_z5}")

points = np.array([1 + 1j, 2 + 1j, 2 + 2j, 1 + 2j, 1.5 + 1.5j, 1.5 + 0.5j])

# Plot titik-titik "E"
plt.figure(figsize=(5, 5))
plt.plot(points.real, points.imag, 'bo-', label='Letter "E" Points')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Plot of Letter "E" Points')
plt.grid(True)
plt.legend()
plt.show()

# Contoh operasi aritmatika kompleks pada titik-titik
complex_number = 1/3 + 1j/2  # atau complex_number = 1 - 1j
result_multiply = points * complex_number
print("Hasil perkalian dengan bilangan kompleks:", result_multiply)

# Contoh transformasi dengan fungsi non-linear, misalnya pengkuadratan
result_square = points ** 2
print("Hasil transformasi dengan fungsi kuadrat:", result_square)