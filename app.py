import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Matheus | Automações Inteligentes",
    layout="wide"
)

# --- SIDEBAR DE NAVEGAÇÃO ---
st.sidebar.title("Hub de Projetos | Matheus")
st.sidebar.markdown("Escolha uma seção:")

projeto = st.sidebar.radio(
    "Navegação:",
    ["Início / Sobre Mim", "Robô de Processamento de Dados", "Organização de Planilhas"]
)

st.sidebar.divider()
st.sidebar.info("📩 **Contato:** \n\n"
"[Meu LinkedIn](https://www.linkedin.com/in/matheus-batista-ab791727a/)\n\n" 
"[matheusbatista1006@gmail.com](mailto:matheusbatista1006@gmail.com?subject=Contato%20via%20Portfólio%20-%20Matheus%20Batista)"
)

# --- ÁREA PRINCIPAL ---

if projeto == "Início / Sobre Mim":
    col_foto, col_texto = st.columns([1, 2.5])

    with col_foto:
        # Colocar minha foto futuramente
        # st.image("prints/minha_foto.jpg", use_container_width=True)
        st.write("### Matheus")
        st.caption("Desenvolvedor Python focado em Automação")

    with col_texto:
        st.title("Olá, eu sou o Matheus!")
        st.markdown("""
        Apaixonado por criar soluções que devolvem o tempo para as pessoas. Meu foco é **transformar processos manuais lentos em sistemas automáticos de alta performance.**
        
        ### O que eu faço?
        Desenvolvo ferramentas personalizadas para empresas e profissionais que precisam de:
        - **Web Scraping:** Extração de dados inteligentes em larga escala.
        - **Automação de Sistemas:** Integração entre planilhas, sites e bancos de dados.
        - **Otimização de Fluxos:** Redução de erros humanos e aumento de velocidade operacional.
        
        ### Por que contratar minhas soluções?
        Diferente de scripts simples, eu entrego **softwares resilientes**: com tratamento de erros, logs detalhados, proteção contra quedas de internet e bancos de dados profissionais (SQLite).
        
        **Navegue pelo menu lateral para ver minhas tecnologias em ação!**
        """)
        
        st.divider()
        st.write("### Minhas principais tecnologias:")
        st.code("Python | Playwright | Pandas | SQL | Asyncio | Streamlit | Logging")

elif projeto == "Robô de Processamento de Dados":
    st.title("Robô de Processamento de Dados")
    st.subheader("Automação inteligente para tarefas repetitivas em sites e sistemas.")
    
    st.markdown("""
    ### Automação de Processamento de Dados
    Desenvolvi esse robô para **otimizar fluxos operacionais**, eliminando gargalos manuais e garantindo 100% de integridade nos dados.
    
    **Fluxo de Trabalho:**
    1.  **Leitura:** Extração automatizada de dados de 1.000 clientes via planilha.
    2.  **Integração:** Inserção precisa das informações em plataforma web.
    3.  **Processamento:** Captura de respostas e dados gerados pelo sistema.
    4.  **Consolidação:** Atualização final da planilha com os novos dados processados.
    
    *Operação contínua, sem interrupções e à prova de erros de digitação.*
    """)

    # --- SEÇÃO DE VÍDEOS ---
    st.divider()

    # Vídeo Normal
    st.write("### Execução Padrão")
    st.write("Aqui o robô trabalha de forma otimizada, processando as informações diretamente no sistema.")
    st.video("videos/projeto1/video_normal.mp4")

    st.divider()

    # Vídeo Demonstrativo
    st.write("### Visualização do Trabalho")
    st.write("Neste modo, você consegue ver o robô interagindo com o site em tempo real, exatamente como uma pessoa faria, mas com a velocidade de uma máquina.")
    st.video("videos/projeto1/video_demonstracao.mp4")

    st.divider()

    # Vídeo Modo Mudo
    st.write("### Modo Silencioso")
    st.write("Aqui o robô trabalha de forma silenciosa e focada apenas nos dados essenciais, economizando tempo e recursos do computador.")
    st.video("videos/projeto1/video_mudo.mp4")

    st.divider()

    # Vídeo Modo Mudo Total
    st.write("### Modo Mudo Absoluto")
    st.write("O modo menos custoso possível. O robô elimina qualquer distração visual para processar grandes volumes de dados.")
    st.video("videos/projeto1/video_mudo_total.mp4")

    st.divider()

    # Vídeo Checkpoint
    st.write("## Proteção contra Quedas e Interrupções")
    st.write("Se a internet cair ou o computador desligar, o robô é inteligente o suficiente para saber onde parou. Ele nunca processa o mesmo dado duas vezes, evitando erros e perda de tempo.")
    st.video("videos/projeto1/video_checkpoint.mp4")

    st.divider()

    # Print dos Logs
    st.write("### Relatório de Atividades (Logs)")
    st.write("O programa gera um histórico detalhado de tudo o que foi feito. Assim, você tem total controle e transparência sobre cada ação realizada pelo robô.")
    st.image("prints/projeto1/print_logs.jpg", caption="Exemplo do histórico de processamento do sistema")

    st.divider()

    # Print do resultado
    st.write("### Resultado Final")
    st.write("No final, o programa cria uma pasta chamada resultados, onde o sistema insere o resultado final das operações.")

    
    col1, col2, col_grade = st.columns([1, 1, 1.2])

    with col1:
        st.image("prints/projeto1/print_resultados.jpg", caption="Resultado final das operações - Visão 1", use_container_width=True)

    with col2:
        st.image("prints/projeto1/print_resultados2.jpg", caption="Resultado final das operações - Visão 2", use_container_width=True)

    with col_grade:
        st.write("<p style='text-align: center; font-weight: bold;'>Comprovações Detalhadas</p>", unsafe_allow_html=True)
        g_fila1 = st.columns(3)
        g_fila1[0].image("prints/projeto1/prova1.jpg", use_container_width=True)
        g_fila1[1].image("prints/projeto1/prova2.jpg", use_container_width=True)
        g_fila1[2].image("prints/projeto1/prova3.jpg", use_container_width=True)
        
        g_fila2 = st.columns(3)
        g_fila2[0].image("prints/projeto1/prova4.jpg", use_container_width=True)
        g_fila2[1].image("prints/projeto1/prova5.jpg", use_container_width=True)
        g_fila2[2].image("prints/projeto1/prova6.jpg", use_container_width=True)

elif projeto == "Organização de Planilhas":
    st.title("Consolidação Inteligente de Dados")
    st.subheader("Automação para unificação e tratamento de grandes volumes de arquivos CSV/Excel.")
    
    st.markdown("""
    ### Inteligência e Governança de Dados
    Este sistema foi desenvolvido para resolver o problema de dispersão de informações em múltiplos arquivos. Ele automatiza a leitura, o tratamento e a união de bases de dados, garantindo que nenhum dado seja perdido no processo.
    
    **Funcionalidades Principais:**
    1.  **Processamento em Lote:** Capacidade de ler todos os arquivos de um diretório em segundos.
    2.  **Seleção Granular:** Opção para o usuário escolher manualmente quais arquivos devem compor a base final.
    3.  **Padronização Automática:** O sistema identifica colunas correspondentes e unifica os formatos de dados.
    4.  **Exportação Consolidada:** Gera um arquivo final único, pronto para análise em BI ou relatórios gerenciais.
    5.  **Junção de Dados:** Clientes que possuem o mesmo ID terão seus dados mesclados, onde o salário será alterado para o total.
    """)

    st.divider()

    # --- SEÇÃO DE VÍDEOS PROJETO 2 ---
    st.write("### Processamento de Diretório Completo")
    st.write("Demonstração do sistema varrendo uma pasta inteira, identificando os arquivos compatíveis e realizando a união automática.")
    st.video("videos/projeto2/video_pasta_inteira.mp4")

    st.divider()

    st.write("### Processamento por Seleção de Arquivos")
    st.write("Demonstração da flexibilidade do sistema, permitindo que o operador selecione apenas os arquivos específicos que deseja consolidar.")
    st.video("videos/projeto2/video_selecao_arquivos.mp4")

    st.divider()

    # --- RELATÓRIOS E COMPROVAÇÕES ---
    st.write("### Rastreabilidade e Logs")
    st.write("Assim como no robô de processamento, este sistema gera logs de auditoria que confirmam quais arquivos foram lidos e se houve alguma inconsistência na estrutura das planilhas.")
    st.image("prints/projeto2/print_logs_planilhas.png", caption="Log de auditoria do processamento de dados")

    st.divider()

    st.write("### Validação do Resultado Final")
    st.write("Comparação direta entre os arquivos de origem e o arquivo consolidado. A imagem comprova que a estrutura de colunas e a contagem de linhas permanecem íntegras após a unificação.")
    
    # Seção de Provas e Validação de Dados
    st.write("### Validação de Integridade e Resultados")
    st.write("Abaixo, a comprovação da união dos dados brutos em arquivos consolidados, mantendo a precisão das informações.")
    
    col_origem, col_resultado = st.columns([1, 1])
    
    with col_origem:
        st.write("**Arquivos de Origem (Input)**")
        st.image("prints/projeto2/dados1.png", caption="Base de Dados 01 (CSV)", use_container_width=True)
        st.image("prints/projeto2/dados2.png", caption="Base de Dados 02 (CSV)", use_container_width=True)
        st.image("prints/projeto2/dados3.png", caption="Base de Dados 03 (CSV)", use_container_width=True)
        
    with col_resultado:
        st.write("**Arquivos Consolidados (Output)**")
        
        # Prova 1: Junção Total
        st.image("prints/projeto2/juncao1.png", caption="Junção Total: Processamento de todos os arquivos do diretório.", use_container_width=True)
        st.info("O arquivo acima demonstra a unificação completa das três bases de origem em um único registro mestre.")
        
        st.divider()
        
        # Prova 2: Junção Parcial (Seleção Granular)
        st.image("prints/projeto2/juncao2.png", caption="Junção Parcial: Processamento seletivo (apenas dados1 e dados2).", use_container_width=True)
        st.info("Demonstração da funcionalidade de seleção granular, onde apenas os arquivos específicos escolhidos pelo usuário foram processados.")

    st.divider()
    st.caption("A estrutura de colunas e a soma de valores (ID/Salário) foram validadas automaticamente pelo motor de processamento.")

# --- RODAPÉ ---
st.markdown("---")
st.caption("Desenvolvido por Matheus Batista | Python & Automação")