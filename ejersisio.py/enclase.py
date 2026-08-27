from dataclasses import dataclass, field


@dataclass
class Colaborador:
    username: str
    email: str

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
                f"[{self.lenguaje}] — {len(self.colaboradores)} colaboradores"
            )


class GestorProyectos:

    def __init__(self) -> None:
        self.proyectos: list[Proyecto] = []

    def registrar_proyecto(self, proyecto: Proyecto) -> None:

        if self.buscar_proyecto(proyecto.nombre) is not None:
            print("Aviso: el proyecto ya existe.")
        else:
            self.proyectos.append(proyecto)
