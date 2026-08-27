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
