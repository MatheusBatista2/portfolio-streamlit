import streamlit as st

st.set_page_config(
    page_title="Matheus | Automações Inteligentes",
    layout="wide"
)

if "idioma" not in st.session_state:
    st.session_state.idioma = "Português"

idioma_opcoes = {
    "Português": ["Português", "Inglês"],
    "Inglês": ["Portuguese", "English"]
}

idioma_labels = list(idioma_opcoes[st.session_state.idioma])
idioma_index = 0 if st.session_state.idioma == "Português" else 1

escolha = st.sidebar.selectbox("Idioma / Language", idioma_labels, index=idioma_index)

if st.session_state.idioma == "Português":
    if escolha == "Inglês":
        st.session_state.idioma = "Inglês"
        st.rerun()
else:
    if escolha == "Portuguese":
        st.session_state.idioma = "Português"
        st.rerun()

idioma = st.session_state.idioma

if idioma == "Português":
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

    if projeto == "Início / Sobre Mim":
        col_foto, col_texto = st.columns([1, 2.5])

        with col_foto:
            st.write("### Matheus")
            st.caption("Desenvolvedor Python focado em Automação")

        with col_texto:
            st.title("Olá, eu sou o Matheus!")
            st.markdown("""
            **Crio ferramentas para automatizar o que toma tempo do seu time, como por exemplo: extração de dados, integração entre sistemas e processamento em lote.**
            
            ### O que eu faço?
            Desenvolvo ferramentas personalizadas para empresas e profissionais que precisam de:
            - **Web Scraping:** Extração de dados inteligentes em larga escala.
            - **Automação de Sistemas:** Integração entre planilhas, sites e bancos de dados.
            - **Otimização de Fluxos:** Redução de erros humanos e aumento de velocidade operacional.
            
            ### Por que contratar minhas soluções?
            Diferente de scripts simples, eu entrego ferramentas completas com tratamento de erros, logs detalhados, checkpoint contra quedas e banco de dados SQLite para rastreabilidade total.
            
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
        Desenvolvi esse robô para **automatizar o processo**, eliminando gargalos manuais e reduzindo drasticamente falhas de digitação e perda de dados no processo.
        
        **Fluxo de Trabalho:**
        1.  **Leitura:** Extração automatizada de dados de 1.000 clientes via planilha.
        2.  **Integração:** Inserção precisa das informações em plataforma web.
        3.  **Processamento:** Captura de respostas e dados gerados pelo sistema.
        4.  **Consolidação:** Atualização final da planilha com os novos dados processados.
        
        *Operação contínua, sem interrupções, eliminando erros de digitação do processo.*
        """)

        st.divider()
        st.write("### Execução Padrão")
        st.write("Aqui o robô trabalha de forma otimizada, processando as informações diretamente no sistema.")
        st.video("videos/projeto1/video_normal.mp4")

        st.divider()
        st.write("### Visualização do Trabalho")
        st.write("Neste modo, você consegue ver o robô interagindo com o site em tempo real, exatamente como uma pessoa faria, mas com a velocidade de uma máquina.")
        st.video("videos/projeto1/video_demonstracao.mp4")

        st.divider()
        st.write("### Modo Silencioso")
        st.write("Aqui o robô trabalha de forma silenciosa e focada apenas nos dados essenciais, economizando tempo e recursos do computador.")
        st.video("videos/projeto1/video_mudo.mp4")

        st.divider()
        st.write("### Modo Mudo Absoluto")
        st.write("O modo menos custoso possível. O robô elimina qualquer distração visual para processar grandes volumes de dados.")
        st.video("videos/projeto1/video_mudo_total.mp4")

        st.divider()
        st.write("## Proteção contra Quedas e Interrupções")
        st.write("Se a internet cair ou o computador desligar, o robô retoma de onde parou automaticamente. Ele nunca processa o mesmo dado duas vezes, evitando erros e perda de tempo.")
        st.video("videos/projeto1/video_checkpoint.mp4")

        st.divider()
        st.write("### Relatório de Atividades (Logs)")
        st.write("O programa gera um histórico detalhado de tudo o que foi feito. Assim, você tem total controle e transparência sobre cada ação realizada pelo robô.")
        st.image("prints/projeto1/print_logs.jpg", caption="Exemplo do histórico de processamento do sistema")

        st.divider()
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
        ### O que esse sistema faz?
        Este sistema foi desenvolvido para resolver o problema de dispersão de informações em múltiplos arquivos. Ele automatiza a leitura, o tratamento e a união de bases de dados, garantindo que nenhum dado seja perdido no processo.
        
        **Funcionalidades Principais:**
        1.  **Processamento em Lote:** Capacidade de ler todos os arquivos de um diretório em segundos.
        2.  **Seleção Manual:** Opção para o usuário escolher manualmente quais arquivos devem compor a base final.
        3.  **Padronização Automática:** O sistema identifica colunas correspondentes e unifica os formatos de dados.
        4.  **Exportação Consolidada:** Gera um arquivo final único, pronto para análise em BI ou relatórios gerenciais.
        5.  **Junção de Dados:** Clientes que possuem o mesmo ID terão seus dados mesclados, onde o salário será alterado para o total.
        """)

        st.divider()
        st.write("### Processamento de Diretório Completo")
        st.write("Demonstração do sistema varrendo uma pasta inteira, identificando os arquivos compatíveis e realizando a união automática.")
        st.video("videos/projeto2/video_pasta_inteira.mp4")

        st.divider()
        st.write("### Processamento por Seleção de Arquivos")
        st.write("Demonstração da flexibilidade do sistema, permitindo que o operador selecione apenas os arquivos específicos que deseja consolidar.")
        st.video("videos/projeto2/video_selecao_arquivos.mp4")

        st.divider()
        st.write("### Rastreabilidade e Logs")
        st.write("Assim como no robô de processamento, este sistema gera logs de auditoria que confirmam quais arquivos foram lidos e se houve alguma inconsistência na estrutura das planilhas.")
        st.image("prints/projeto2/print_logs_planilhas.png", caption="Log de auditoria do processamento de dados")

        st.divider()
        st.write("### Validação do Resultado Final")
        st.write("Comparação direta entre os arquivos de origem e o arquivo consolidado. A imagem comprova que a estrutura de colunas e a contagem de linhas permanecem íntegras após a unificação.")
        st.write("Abaixo, a comprovação da união dos dados brutos em arquivos consolidados, mantendo a precisão das informações.")
        
        col_origem, col_resultado = st.columns([1, 1])
        
        with col_origem:
            st.write("**Arquivos de Origem (Input)**")
            st.image("prints/projeto2/dados1.png", caption="Base de Dados 01 (CSV)", use_container_width=True)
            st.image("prints/projeto2/dados2.png", caption="Base de Dados 02 (CSV)", use_container_width=True)
            st.image("prints/projeto2/dados3.png", caption="Base de Dados 03 (CSV)", use_container_width=True)
            
        with col_resultado:
            st.write("**Arquivos Consolidados (Output)**")
            st.image("prints/projeto2/juncao1.png", caption="Junção Total: Processamento de todos os arquivos do diretório.", use_container_width=True)
            st.info("O arquivo acima demonstra a unificação completa das três bases de origem em um único registro mestre.")
            st.divider()
            st.image("prints/projeto2/juncao2.png", caption="Junção Parcial: Processamento seletivo (apenas dados1 e dados2).", use_container_width=True)
            st.info("Demonstração da funcionalidade de seleção manual, onde apenas os arquivos específicos escolhidos pelo usuário foram processados.")

        st.divider()
        st.caption("A estrutura de colunas e a soma de valores (ID/Salário) foram validadas automaticamente pelo motor de processamento.")

    st.markdown("---")
    st.caption("Desenvolvido por Matheus Batista | Python & Automação")

else:
    st.sidebar.title("Project Hub | Matheus")
    st.sidebar.markdown("Choose a section:")

    projeto = st.sidebar.radio(
        "Navigation:",
        ["Home / About Me", "Data Processing Robot", "Spreadsheet Organization"]
    )

    st.sidebar.divider()
    st.sidebar.info("📩 **Contact:** \n\n"
    "[My LinkedIn](https://www.linkedin.com/in/matheus-batista-ab791727a/)\n\n" 
    "[matheusbatista1006@gmail.com](mailto:matheusbatista1006@gmail.com?subject=Contact%20via%20Portfolio%20-%20Matheus%20Batista)"
    )

    if projeto == "Home / About Me":
        col_foto, col_texto = st.columns([1, 2.5])

        with col_foto:
            st.write("### Matheus")
            st.caption("Python Developer focused on Automation")

        with col_texto:
            st.title("Hi, I'm Matheus!")
            st.markdown("""
            **I build tools to automate what takes up your team's time, such as: data extraction, system integration and batch processing.**
            
            ### What I do
            I develop custom tools for companies and professionals who need:
            - **Web Scraping:** Large-scale intelligent data extraction.
            - **System Automation:** Integration between spreadsheets, websites, and databases.
            - **Workflow Optimization:** Reduction of human error and increased operational speed.
            
            ### Why choose my solutions?
            Unlike simple scripts, I deliver complete tools with error handling, detailed logs, checkpoint against outages and SQLite database for full traceability.
            
            **Use the side menu to see my technologies in action!**
            """)
            
            st.divider()
            st.write("### Core stack:")
            st.code("Python | Playwright | Pandas | SQL | Asyncio | Streamlit | Logging")

    elif projeto == "Data Processing Robot":
        st.title("Data Processing Robot")
        st.subheader("Intelligent automation for repetitive tasks in sites and systems.")
        
        st.markdown("""
        ### Data Processing Automation
        I developed this robot to **automate the process**, eliminating manual bottlenecks and drastically reducing typing errors and data loss.
        
        **Workflow:**
        1.  **Reading:** Automated data extraction of 1,000 customers via spreadsheet.
        2.  **Integration:** Precise insertion of information into the web platform.
        3.  **Processing:** Capturing responses and data generated by the system.
        4.  **Consolidation:** Final spreadsheet update with the new processed data.
        
        *Continuous operation, without interruptions, eliminating typing errors from the process.*
        """)

        st.divider()
        st.write("### Standard Execution")
        st.write("Here the robot works in an optimized way, processing information directly in the system.")
        st.video("videos/projeto1/video_normal.mp4")

        st.divider()
        st.write("### Work Visualization")
        st.write("In this mode, you can see the robot interacting with the site in real-time, exactly as a person would, but with the speed of a machine.")
        st.video("videos/projeto1/video_demonstracao.mp4")

        st.divider()
        st.write("### Silent Mode")
        st.write("Here the robot works silently, focusing only on essential data, saving time and computer resources.")
        st.video("videos/projeto1/video_mudo.mp4")

        st.divider()
        st.write("### Absolute Mute Mode")
        st.write("The least resource-intensive mode possible. The robot removes any visual distraction to process large volumes of data.")
        st.video("videos/projeto1/video_mudo_total.mp4")

        st.divider()
        st.write("## Protection against Outages and Interruptions")
        st.write("If the internet goes down or the computer shuts off, the robot resumes from where it left off automatically. It never processes the same data twice, avoiding errors and time loss.")
        st.video("videos/projeto1/video_checkpoint.mp4")

        st.divider()
        st.write("### Activity Report (Logs)")
        st.write("The program generates a detailed history of everything performed. This gives you total control and transparency over every action the robot takes.")
        st.image("prints/projeto1/print_logs.jpg", caption="Example of the system's processing history")

        st.divider()
        st.write("### Final Result")
        st.write("Finally, the program creates a results folder, where the system saves the final outcome of the operations.")

        col1, col2, col_grade = st.columns([1, 1, 1.2])

        with col1:
            st.image("prints/projeto1/print_resultados.jpg", caption="Final result of operations - View 1", use_container_width=True)

        with col2:
            st.image("prints/projeto1/print_resultados2.jpg", caption="Final result of operations - View 2", use_container_width=True)

        with col_grade:
            st.write("<p style='text-align: center; font-weight: bold;'>Detailed Proof</p>", unsafe_allow_html=True)
            g_fila1 = st.columns(3)
            g_fila1[0].image("prints/projeto1/prova1.jpg", use_container_width=True)
            g_fila1[1].image("prints/projeto1/prova2.jpg", use_container_width=True)
            g_fila1[2].image("prints/projeto1/prova3.jpg", use_container_width=True)
            
            g_fila2 = st.columns(3)
            g_fila2[0].image("prints/projeto1/prova4.jpg", use_container_width=True)
            g_fila2[1].image("prints/projeto1/prova5.jpg", use_container_width=True)
            g_fila2[2].image("prints/projeto1/prova6.jpg", use_container_width=True)

    elif projeto == "Spreadsheet Organization":
        st.title("Intelligent Data Consolidation")
        st.subheader("Automation for merging and cleaning large volumes of CSV/Excel files.")
        
        st.markdown("""
        ### What does this system do?
        This system was developed to solve the problem of information scattered across multiple files. It automates the reading, cleaning, and merging of databases, minimizing data lost throughout the process.
        
        **Main Features:**
        1.  **Batch Processing:** Ability to read all files in a directory in seconds.
        2.  **Manual Selection:** Option for the user to manually choose which files should make up the final base.
        3.  **Automatic Standardization:** The system identifies matching columns and unifies data formats.
        4.  **Consolidated Export:** Generates a single final file, ready for BI analysis or management reports.
        5.  **Data Merging:** Customers with the same ID will have their data merged, where the salary is updated to the total.
        """)

        st.divider()
        st.write("### Full Directory Processing")
        st.write("Demonstration of the system scanning an entire folder, identifying compatible files, and performing automatic merging.")
        st.video("videos/projeto2/video_pasta_inteira.mp4")

        st.divider()
        st.write("### Processing by File Selection")
        st.write("Demonstration of system flexibility, allowing the operator to select only specific files for consolidation.")
        st.video("videos/projeto2/video_selecao_arquivos.mp4")

        st.divider()
        st.write("### Traceability and Logs")
        st.write("Just like the processing robot, this system generates audit logs confirming which files were read and if there were any structural inconsistencies.")
        st.image("prints/projeto2/print_logs_planilhas.png", caption="Data processing audit log")

        st.divider()
        st.write("### Final Result Validation")
        st.write("Direct comparison between source files and the consolidated file. The image proves that column structure and row count remain intact after merging.")
        st.write("Below is the proof of merging raw data into consolidated files while maintaining information accuracy.")
        
        col_origem, col_resultado = st.columns([1, 1])
        
        with col_origem:
            st.write("**Source Files (Input)**")
            st.image("prints/projeto2/dados1.png", caption="Database 01 (CSV)", use_container_width=True)
            st.image("prints/projeto2/dados2.png", caption="Database 02 (CSV)", use_container_width=True)
            st.image("prints/projeto2/dados3.png", caption="Database 03 (CSV)", use_container_width=True)
            
        with col_resultado:
            st.write("**Consolidated Files (Output)**")
            st.image("prints/projeto2/juncao1.png", caption="Full Merge: Processing all files in the directory.", use_container_width=True)
            st.info("The file above demonstrates the complete unification of the three source bases into a single master record.")
            st.divider()
            st.image("prints/projeto2/juncao2.png", caption="Partial Merge: Selective processing (only data1 and data2).", use_container_width=True)
            st.info("Demonstration of manual selection, where only the files chosen by the user were processed.")

        st.divider()
        st.caption("Column structure and value totals (ID/Salary) were automatically validated by the processing engine.")

    st.markdown("---")
    st.caption("Developed by Matheus Batista | Python & Automation")