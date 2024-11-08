print('acesso a mensagens da empresa para gerentes, analistas e estagiarios')
print('dia da semana do acesso: (0)domingo,(1)segunda-feira,(2)terça-feira,(3)quarta-feira,(4)quinta-feira,(5)sexta-feira,(6)sabado')
funcionarios= ["gerente","analista","estagiario"]
dias=['domingo','segunda-feira','terça-feira','quarta-feira','quinta-feira','sexta-feira','sabado']
acesso=input('digite seu cargo: ')
dia_do_acesso=input('digite o dia da semana: ')

class funcionario:
    def __init__(self,cargo):
        self.cargo=cargo

class gerente(funcionario):
    def dia (self,dias_da_semana):
        if(acesso == 'gerente' and dia_do_acesso == dias[0:]):
            print ('Acesso permitido', acesso)
        return

class analista(funcionario):
    def dia (self):
        if(acesso == 'analista' and dia_do_acesso in dias[1:6]):
            print('acesso permitido ',acesso)
        else:
            print('acesso negado')
        return

class estagiario(funcionario):
    def dia (self, dia_do_acesso):
        if (acesso == estagiario and dia_do_acesso in dias[1:6]):
            print('acesso permitido ',acesso)
        else:
            print('acesso negado')
        return


