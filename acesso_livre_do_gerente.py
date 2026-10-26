print('Sistema de controle de acesso do escritório para: gerentes, estagiario e analista')

# Lista de cargos válidos para verificação rápida
cargos_validos = ["gerente", "estagiario", "analista"]

cargo_do_funcionario = input('qual seu cargo? ').strip().lower()
dia_da_semana = input('qual o dia da semana? ').strip().lower()

# Corrigido: Verifica se o cargo NÃO está na lista de cadastrados
if cargo_do_funcionario not in cargos_validos:
    # Corrigido: Exibe de 3 até 1 tentativas restantes usando f-string
    for i in range(3, 0, -1):
        print(f'Acesso negado, tente outra vez, você só tem {i} tentativas')
else:
    # Fluxo principal de permissões
    if cargo_do_funcionario == 'gerente':
        print('Acesso permitido, bem-vindo', cargo_do_funcionario)
        
    elif dia_da_semana == 'sabado' or dia_da_semana == 'domingo':
        # Bloqueia analistas e estagiários no fim de semana
        print("Acesso negado para o cargo:", cargo_do_funcionario)
        
    else:
        # Permite analistas e estagiários em dias úteis
        print('Acesso permitido, bem-vindo', cargo_do_funcionario)
