print('Sistema de controle de acesso do escritório')
cargo_do_funcionario=input('qual seu cargo? ')
dia_da_semana=input('qual o dia da semana? ')
acesso = cargo_do_funcionario + dia_da_semana
 
if (cargo_do_funcionario == 'gerente') and (dia_da_semana == 'segunda-feira'):
    print ('acesso permitido',cargo_do_funcionario,',todas as segundas-feiras')
else:
    print('acesso negado para esse sistema')
if (cargo_do_funcionario == 'analista') and (dia_da_semana == 'terça-feira'):
    print('acesso permitido',cargo_do_funcionario,',todas as terças-feiras')
else:
    print('acesso negado para esse sistema')
 
if (cargo_do_funcionario == 'estagiario') and (dia_da_semana == 'quarta-feira'):
    print('acesso permitido',cargo_do_funcionario,',todas as quartas-feiras')
else:
    print('acesso negado para esse sistema')