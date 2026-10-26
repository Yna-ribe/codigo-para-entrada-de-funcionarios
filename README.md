## Implementação do Protótipo em Python

O repositório conta com um protótipo inicial em script Python para validar a lógica de triagem e o fluxo de decisão do sistema de controle de acesso. 

### Fluxo de Validação do Script:
* **Entrada de Dados:** O sistema solicita o cargo do funcionário e o dia atual da semana.
* **Validação de Perfil:** Verifica se o cargo informado pertence a um dos três grupos cadastrados (Gerente, Analista ou Estagiário).
* **Filtro Temporal:** Aplica restrições de calendário, garantindo o bloqueio de acessos em fins de semana para cargos operacionais, enquanto mantém o acesso do perfil administrativo (Gerente) liberado de forma diária.
