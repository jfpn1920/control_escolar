class Profesor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
    def mostrar(self):
        print(f"profesor: {self.nombre} | especialidad: {self.especialidad}")
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar(self):
        print(f"estudiante: {self.nombre} | edad: {self.edad}")
class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"estudiante {estudiante.nombre} asignado al curso {self.nombre}.\n")
    def mostrar_curso(self):
        print(f"\ncurso: {self.nombre}")
        print(f"profesor: {self.profesor.nombre}")
        print("estudiantes inscritos:")
        
        if not self.estudiantes:
            print("   no hay estudiantes inscritos.")
        else:
            for estudiante in self.estudiantes:
                print(f"   - {estudiante.nombre} ({estudiante.edad} años)")
        print()
class ControlEscolar:
    def __init__(self):
        self.cursos = []
    def agregar_curso(self, curso):
        self.cursos.append(curso)
    def mostrar_cursos(self):
        if not self.cursos:
            print("no hay cursos registrados.\n")
        else:
            for curso in self.cursos:
                curso.mostrar_curso()
    def buscar_curso(self, nombre):
        for curso in self.cursos:
            if curso.nombre.lower() == nombre.lower():
                return curso
        return None
def menu():
    sistema = ControlEscolar()
    prof1 = Profesor("ana lopez", "matemáticas")
    prof2 = Profesor("carlos perez", "programacion")
    curso1 = Curso("algebra", prof1)
    curso2 = Curso("python basico", prof2)
    sistema.agregar_curso(curso1)
    sistema.agregar_curso(curso2)
    while True:
        print(" sistema de control escolar")
        print("1. mostrar cursos")
        print("2. asignar estudiante a curso")
        print("3. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            sistema.mostrar_cursos()
        elif opcion == "2":
            nombre_est = input("ingrese nombre del estudiante: ")
            try:
                edad_est = int(input("ingrese edad del estudiante: "))
            except ValueError:
                print("edad invalida.\n")
                continue
            nombre_curso = input("ingrese nombre del curso: ")
            curso = sistema.buscar_curso(nombre_curso)
            if curso:
                estudiante = Estudiante(nombre_est, edad_est)
                curso.agregar_estudiante(estudiante)
            else:
                print("curso no encontrado.\n")
        elif opcion == "3":
            print("saliendo del sistema...")
            break
        else:
            print("opcion invalida.\n")
menu()