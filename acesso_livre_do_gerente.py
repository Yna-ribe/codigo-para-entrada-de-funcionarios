print('Sistema de controle de acesso do escritório para: gerentes, estagiario e secretario')
cargo_do_funcionario=input('qual seu cargo? ')
dia_da_semana=input('qual o dia da semana? ')
for i in range(3):
    while(cargo_do_funcionario != "gerente" or "estagiario" or "secretario"):
        print('acesso negado, tente outra vez, você só tem {i}tentativas'
if(cargo_do_funcionario == 'gerente'):
    print ('Acesso permitido',cargo_do_funcionario)
elif(dia_da_semana == 'sabado' or dia_da_semana == 'domingo'):
    print("Acesso negado", cargo_do_funcionario)
else:
    print ('Acesso permitido',cargo_do_funcionario)
