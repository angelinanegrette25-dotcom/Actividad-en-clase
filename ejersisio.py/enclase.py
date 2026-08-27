from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Colaborador:
    username: str
    email: str


@dataclass
class Proyecto:
    nombre: str
    lenguaje: str
    colaboradores: list[Colaborador] = field(default_factory=list)

    def agregar_colaborador(self, colaborador: Colaborador) -> None:
        if self.tiene_colaborador(colaborador.username):
            print("Aviso: el colaborador ya existe.")
        else:
            self.colaboradores.append(colaborador)

    def tiene_colaborador(self, username: str) -> bool:
        for colaborador in self.colaboradores:
            if colaborador.username == username:
                return True
        return False

    def listar_colaboradores(self) -> list[Colaborador]:
        return self.colaboradores

    def __str__(self) -> str:
        return (
            f"Proyecto: {self.nombre} "
            f"[{self.lenguaje}] — {len(self.colaboradores)} colaborador(es)"
        )


class GestorProyectos:

    def __init__(self) -> None:
        self.proyectos: list[Proyecto] = []

    def registrar_proyecto(self, proyecto: Proyecto) -> None:

        if self.buscar_proyecto(proyecto.nombre) is not None:
            print("Aviso: el proyecto ya existe.")
        else:
            self.proyectos.append(proyecto)

    def buscar_proyecto(self, nombre: str) -> Proyecto | None:

        for proyecto in self.proyectos:
            if proyecto.nombre == nombre:
                return proyecto
        return None

    def listar_proyectos(self) -> list[Proyecto]:
        return self.proyectos



ana = Colaborador(username="ana_dev", email="ana@mail.com")
luis = Colaborador(username="luis99", email="luis@mail.com")
sofia = Colaborador(username="sofiaml", email="sofia@mail.com")


p1 = Proyecto(nombre="InventarioApp", lenguaje="Python")
p1.agregar_colaborador(ana)
p1.agregar_colaborador(luis)
p1.agregar_colaborador(ana)

p2 = Proyecto(nombre="WebStore", lenguaje="JavaScript")
p2.agregar_colaborador(sofia)


print(p1)
print(p2)


print(p1.tiene_colaborador("ana_dev"))
print(p1.tiene_colaborador("sofiaml"))

gestor = GestorProyectos()
gestor.registrar_proyecto(p1)
gestor.registrar_proyecto(p2)
gestor.registrar_proyecto(p1)

encontrado = gestor.buscar_proyecto("WebStore")
print(encontrado)

no_existe = gestor.buscar_proyecto("OtroProyecto")
print(no_existe)

print(len(gestor.listar_proyectos()))