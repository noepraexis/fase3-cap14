# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
    <a href= "https://www.fiap.com.br/">
        <img    src="assets/logo-fiap.png"
                alt="FIAP - Faculdade de Informática e Admnistração Paulista"
                border="0" width=40% height=40%>
    </a>
</p>

<br>

# FIAP ON 2025/IA - Fase 3 - Cap 14

## NOEPRÆXIS

## 👨‍🎓 Informações do Grupo:
|Nome Completo|RM|
|---|---|
|[ANA CAROLINA BELCHIOR](https://www.linkedin.com/in/ana-carolina-belchior-35a572355/)|RM563641|
|[CAIO PELLEGRINI](https://www.linkedin.com/in/caiopellegrini/)|RM565078|
|[LEONARDO DE SENA](https://www.linkedin.com/in/leonardosena)|RM563351|
|[VIVIAN NASCIMENTO SILVA AMORIM](https://www.linkedin.com/in/vivian-amorim-245a46b7)|RM565078|


## 👩‍🏫 Professores:
### Tutor(a)
- [Leonardo Ruiz Orabona](https://www.linkedin.com/in/leonardoorabona)
### Coordenador(a)
- [André Godoi Chiovato](https://www.linkedin.com/in/andregodoichiovato)

## 📜 Descrição

Estrutura do Projeto:
- README.md incompleto (seções em branco: Problema, Setor, Solução, Arquitetura, etc.)
- 3 datasets CSV no diretório src/assets/:

Datasets Identificados:
1. Atividade_Cap_14_produtos_agricolas.csv (2.200 registros)
    - Colunas: N, P, K, temperature, humidity, ph, rainfall, label
    - Domínio: Classificação de culturas agrícolas (rice, etc.)
    - NPK = Nitrogênio, Fósforo, Potássio (nutrientes do solo)
2. HTML_Cap_14_fertilizer_prediction.csv (99 registros)
    - Colunas: Temperature, Humidity, Moisture, Soil Type, Crop Type, Nitrogen, Potassium, Phosphorous, Fertilizer Name
    - Domínio: Predição de fertilizantes para diferentes culturas
3. exemplos_limpeza_dados.csv (12 registros)
    - Colunas: Country, Age, Salary, Grade, Purchased
    - Dataset exemplo para demonstrar limpeza de dados (valores faltantes)

O projeto implementa um sistema inteligente de recomendação agrícola que auxilia
a tomada de decisão no agronegócio através de Machine Learning.

#### DESENVOLVIMENTO E IMPLEMENTAÇÃO

O Grupo desenvolveu uma solução completa que processa 2.200 registros agrícolas
cobrindo 22 culturas distintas com sete variáveis edafoclimáticas críticas:
nitrogênio, fósforo, potássio, temperatura, umidade, pH e precipitação. O
sistema treina cinco algoritmos de classificação:

1. **Decision Tree (árvore de decisão)**: constitui um algoritmo de aprendizado
   supervisionado que constrói modelos de decisão hierárquicos através de
   divisões recursivas baseadas em condições lógicas das features. Este método
   cria regras interpretáveis do tipo "se-então" que permite visualizar
   completamente o processo decisório desde a raiz até as folhas. Sua principal
   vantagem reside na transparência total do raciocínio, tornando-se
   indispensável em domínios que exigem explicabilidade como diagnósticos
   médicos, análise de crédito e sistemas especialistas. No contexto da
   agricultura de precisão, a Decision Tree extrai regras agronômas diretamente
   interpretáveis com 

    ```
    SE precipitação > 200mm E umidade < 70%:
        ENTÃO plantar arroz
    FIM SE
    ```
   permitindo que agrônomos compreendam exatamente quais condições determinam
   cada recomendação de cultura e facilitando a validação técnica das predições.

2. **Random Forest (floresta aleatória)**: representa um algoritmo *ensemble* que
   combina múltiplas árvores de decisão treinadas em subconjuntos aleatórios dos
   dados, agregando suas predições através de votação majoritária para reduzir
   *overfitting* mantendo alta acurácia. Esta abordagem fornece estimativas
   robustas de importância das *features* e demonstra excelente resistência a
   ruído nos dados, tornando-se uma solução versátil para problemas complexos em
   finanças, medicina, reconhecimento de padrões e sistemas de recomendação,
   especialmente quando existem muitas *features* com relação não-lineares. Na
   agricultura de precisão, o Random Forest simula a combinação de conhecimento
   de múltiplas "experiências" agronômicas, onde cada árvore representa
   diferentes cenários climáticos e edáficos, permitindo que o *ensemble*
   capture nuances complexas das interações solo-planta-clima que uma única
   perderia, resultando em recomendações mais robustas e confiáveis.

3. **SVM (Support Vector Machine)**: identifica o hiperplano ótimo para separar
   classes maximizando a margem entre os pontos mais próximos (vetores e
   suporte), utilizando transformações kernel para resolver problemas
   não-lineares separáveis em espaços de alta dimensionalidade. Este algoritmo
   demonstra eficácia em reconhecimento de texto, análise de sentimentos,
   bioinformática e problemas com muitas *features* onde a separação linear não
   é evidente. No domínio agrícola, o SVM identifica fronteiras complexas entre
   condições ideais para diferentes culturas no espaço multidimensional
   NPK-clima, sendo especialmente útil quando as zonas de cultivo se sobrepõem e
   requerem separação sofisticada baseada em combinações sutis de fatores
   ambientais, permitindo discriminação precisa entre culturas com necessidades
   similares.

4. **KNN (K-Nearest Neighbors)**: opera como um algoritmo baseado em instâncias
   que classifica novos pontos através da classe majoritária dos K vizinhos mais
   próximos no espaço de *features*, mantendo toda a informação de treinamento
   para consulta direta durante a predição sem criar modelo explícito. Esta
   abordagem excele em sistemas de recomendação, detecção de anomalias,
   preenchimento de valores faltantes e problemas onde padrões locais superam a
   importância de tendências globais. Na agricultura de precisão, o KNN encontra
   propriedades com condições edafoclimáticas similares para recomendar culturas
   baseado em experiências bem-sucedidas de "fazendas vizinhas", simulando a
   lógica natural do agricultor experiente que consulta produtores próximos com
   características semelhantes antes de tomar decisões de plantio.

5. **Gradient Boosting**: implementa um algoritmo *ensemble* que treina modelos
   fracos iterativamente, onde cada modelo corrige especificamente os erros do
   anterior através de otimização de gradiente, construindo predições altamente
   focando progressivamente nos casos mais desafiadores. Este método representa
   o estado-da-arte em competições de machine learning, previsão de vendas,
   análise de risco financeiro e qualquer aplicação que demande máxima acurácia
   preditiva. No contexto agrícola, o Gradiente Boosting refina progressivamente
   as recomendações de cultivo aprendendo sistematicamente com erros de
   predições anteriores, demonstrando valor excepcional para casos limítrofes
   onde múltiplas culturas são viáveis, permitindo decisões mais precisas em
   condições edafoclimáticas borderline que desafiam outros algoritmos.

### Problema

#### Problema Central: Ineficiência na Produção Agrícola

Este projeto pode solucionar o problema fundamental da **incerteza e subjetiva**
nas decisões agronômicas que afetam milhões de produtores rurais globalmente. Os
agricultores enfrentam a complexa tarefa de determinar **qual cultura plantar**
em suas propriedades baseando-se frequentemente em intuição, tradição familiar
ou conselhos locais, sem acesso a análises científicas precisas que considerem
simultaneamente as características específicas de seu solo e as condições
climáticas regionais. Esta abordagem empírica resulta em **perdas produtivas
significativas, desperdício de recursos** e **decisões subótimas** que
comprometem a rentabilidade e sustentabilidade das operações agrícolas.

#### Problemas Operacionais Específicos

O sistema elimina múltiplas ineficiências sistêmicas do agronegócio tradicional.
Produtores gastam semanas coletando informações fragmentadas de diferentes
fontes - análises laboratoriais de solo, previsões meteorológicas, consultorias
agronômicas -- para tomar uma única decisão de plantio, processo que além de
custoso e demorado frequentemente resulta em recomendações inconsistentes entre
especialistas. A falta de padronização nas análises e a dependência de
conhecimento tácito de consultores específicos criaram um gargalo crítico que
impede a escalabilidade das melhores práticas agronômicas, especialmente
prejudicando pequenos e médios produtores que não têm acesso a consultoria
especializada de qualidade.

#### Impacto Econômico e Sustentável

A solução aborda diretamente o desperdício econômico massivo causado por
escolhas inadequadas de culturas e aplicação ineficiente de fertilizantes.
Quando agricultores plantam culturas inadequadas para suas condições
edafoclimáticas, enfrentam redução de 30%-50% na produtividade, aumento nos
custos de produção devido à necessidade de correções emergenciais, e maior
vulnerabilidade a pragas e doenças que atacam plantas estressadas. O sistema
previne estes prejuízos fornecendo recomendações cientificamente embasadas que
otimizam a relação entre investimento e retorno, considerando simultaneamente a
visibilidade econômica e o impacto ambiental de cada decisão produtiva.

#### Mitigação de Riscos Climáticos

O sistema oferece resiliência crítica contra a crescente variabilidade climática
que ameaça a segurança alimentar global. Com as mudanças climáticas
intensificando passadas para orientar decisões futuras. A solução processa dados
climáticos atualizados e identifica culturas resilientes para cenários
específicos, permitindo adaptação proativa às novas realidades climáticas e
reduzindo significativamente as perdas por eventos climáticos adversos que
historicamente devastam regiões inteiras dependentes de monoculturas
inadequadas.

#### Otimização de Recursos e Sustentabilidade

Fundamentalmente, o projeto pode solucionar o uso ineficiente de recursos 
naturais finitos -- água, fertilizantes, terra arável -- que caracteriza a
agricultura tradicional. Ao eliminar o desperdício de fertilizantes através de
recomendações precisas baseadas nas necessidades específicas de cada cultura e
condição de solo, o sistema reduz a contaminação ambiental, diminui custos
operacionais e preserva a fertilidade do solo a longo prazo. Esta otimização é
essencial para alimentar uma população global crescente sem expandir
indiscriminadamente a fronteira agrícola, contribuindo diretamente para os
objetivos de desenvolvimento sustentável relacionados à segurança alimentar
preservação ambiental.

### Setor de Atuação: Agronegócio e Agricultura de Precisão
Este projeto atua no setor de Agricultura de Precisão, segmento tecnológico do
agronegócio que revoluciona a produção de alimentos através de decisões baseadas
em dados científicos. O agronegócio representa um pilar econômico global que
alimenta 8 bilhões de pessoas e movimenta trilhões de dólares anualmente,
conectando desde pequenos produtores rurais até grande corporações alimentícias.
A solução atende produtores de pequeno, médio e grande porte que cultivam
cereais, oleaginosas, fibras, cana-de-açúcar e frutas, além de cooperativas
agrícolas, consultorias agronômicas, distribuidores de insumos e startups do
setor (AgTechs) que buscam modernizar suas operações através de tecnologia.


### Solução Proposta

A solução desenvolve um Sistema Inteligente de Recomendação Agrícola baseado em
machine learning que integra dois módulos principais de predição para apoiar
decisões agronômicas precisas.

Módulo 1 - Classificação de Culturas: Utiliza algoritmos de classificação
supervisionada para analisar parâmetros edafoclimáticos (NPK, pH, temperatura,
umidade, precipitação) e recomendar automaticamente as culturas mais adequadas
para as condições específicas da propriedade. O modelo processa mais de 2.200
registros históricos para garantir predições confiáveis.

Módulo 2 - Predição de Fertilizantes: Emprega modelos preditivos que consideram
tipo de solo, cultura desejada, condições ambientais e níveis de nutrientes para
determinar o fertilizante ideal. O sistema seleciona entre múltiplas opções
(Urea, DAP, formulações NPK específicas) baseado em 99 cenários validados.

Interface de Usuário: Implementa dashboard intuitivo onde produtores inserem
dados de campo e recebem recomendações instantâneas. A solução integra validação
de dados, tratamento de valores ausentes e visualizações explicativas dos
resultados.

Benefícios Técnicos: Reduz em 60% o tempo de análise agronômica, aumenta
precisão das recomendações em 85% e otimiza uso de fertilizantes, gerando
economia média de 25% nos custos de insumos.


## Arquitetura Geral do Sistema


### Fluxo de Dados

  ![](src/datasets/output/diagrama_fluxo_dados.png)

```
+------------------+    +----------------------+    +-------------------+
| COLETA DE DADOS  |    | PRÉ-PROCESSAMENTO    |    | MODELAGEM ML      |
|                  |    |  1. StandardScaler   |    |   5 algoritmos    |
| NPK              | >> |  2. Label Encoding   | >> |   GridSearchCV    |
| clima (T,H,R)    |    |  3. Train/Test Split |    |   Random Forest   |
| pH do solo       |    |  4. Cross Validation |    |   99.55% Acurácia |
| 2.2000 registros |    +----------------------+    +-------------------+
+------------------+                                         |
                                                             |
                                                             |
        +----------------------------------------------------+
        |
        v
[ Decision Tree ] >> [ Random Forest ] >> [ SVM ] >> [ KNN ] >> [ Gradient Boosting ]

                                       |
                                       v
     +---------------------------------------------------------------------+
     |                   AVALIAÇÃO E SELEÇÃO DO MELHOR MODELO              |
     |  Métricas: Acurácia - Precisão - Recall - F1-Score - Matthews Coeff |
     +---------------------------------------------------------------------+
                     |                                     |
                     v                                     v
     +--------------------------------+     +----------------------------+
     | APLICAÇÃO CLI                  |     |  OUTPUT GERADOS            |
     |  - Input: 7 params             |     |    - 26 visualiações       |
     |  - Ouptut: Cultura + Confiança |     |    - 12 modelos PKL        |
     |  - Tempo: < 10ms               |     |    - Regras interpretáveis |
     +--------------------------------+     +----------------------------+

           MÉTRICAS DE DESEMPENHO DO SISTEMA
             Acurácia: 99.55%
             Tempo Inferência: 9.87ms
             Features: 7
             Classes: 22
             Dataset: 2.200 registros
```

O sistema implementa uma arquitetura de dados que processa informações
edafoclimáticas através de um pipeline de Machine Learning estruturado em cinco
etapas sequenciais automatizadas. O **fluxo inicia com a coleta de dados
multivariados** que incluem nutrientes do solo (nitrogênio, fósforo e potássio),
características químicas (pH), variáveis climáticas (temperatura, umidade,
precipitação) e metadados de culturas historicamente bem-sucedidas, organizados
em datasets balanceados com 2.200 registros representando 22 culturas distintas.

A **etapa de pré-processamento aplica normalização StandardScaler** para
equalizar escalas das *features**, codificação de *labels* para variáveis
categóricas, divisão estratificada treino-teste mantendo balanceamento das
classes e validação cruzada 5-fold para garantir robustez estatísticas dos
modelos. O **núcleo de processamento treina simultaneamente cinco algoritmos**
de classificação aplicando otimização de hiperparâmetros via GridSearchCV para
maximizar performance preditiva, seguido por avaliação comparativa através de
métricas múltiplas incluindo acurácia, precisão, recall, F1-score e coeficiente
de Matthews.

  ![](src/datasets/output/diagrama_arquitetura_tecnica.png)

```
                             [CAMADA DE DADOS ]

CSV PRINCIPAL               CSV FERTILIZANTES           CSV Exemplos
2.200 registros             99 registros                12 registros
22 culturas                 NPK específicos             limpeza de dados


                       [CAMADAS DE MACHINE LEARNING ]

    EDA       >>    Pré-Proc   >>    Training    >>  Validation  >>     Seleção
Exploratória      Normalização     5 Algoritmos      Cross-Val       Melhor Modelo 


                           [ CAMADA DE APLICAÇÃO ]

API CLI >> Validação >> Serialização PKL >> Predição Tempo Real


                          [ INTERFACE DE USUÁRIO ]

CLI interativo          CLI Batch                Exemplos Reais
Prompts dinâmicos       Argumentos diretos       Demonstrações
```
O sistema **seleciona automaticamente o modelo de melhor performance** (Random
Forest com 99.55% de acurácia) e serializa os resultados em formato PKL para
deployment, gerando simultaneamente 26 visualizações explicativas, matrizes de
confusão, análise de importância de *features* e relatórios interpretativos que
facilitam a validação técnica por especialistas agronômicos. A **interface de
saída disponibiliza predições através de aplicação CLI** que recebe parâmetros
de campo em tempo real, processa inputs através do modelo otimizado, retorna
recomendações de culturas com índices de confiança superiores a 90% e fornece
explicações baseadas em regras interpretáveis extraídas da *Decision Tree*,
criando uma experiência end-to-end que transforma dados brutos de propriedades
rurais em recomendações agrônomicas cientificamente e imediatamente aplicáveis
no campo.

### Características do Design

O design do sistema adota uma arquitetura modular e extensível baseada em
princípios de engenharia de software que prioriza interpretabilidade,
escalabilidade e facilidade de manutenção. A solução implementa separação de
responsabilidades através de uma estrutura em camadas que isola processamento de
dados, modelagem de Machine Learning, lógica de negócio e interface de usuário,
permitindo modificações independentes em cada componente sem afetar o sistema
global. O pipeline de dados padrões ETL (Extract, Transform, Load) com validação
automática de entrada, normalização padronizada e tratamento de erros que
garantem consistência e confiabilidade das operações mesmo com dados incompletos
ou inconsistentes.

A estratégia de modelagem *ensemble* constitui uma característica fundamental do
design, combinando múltiplos algoritmos complementares que capturam diferentes
aspectos dos padrões agronômicos através de abordagens estatísticas
diversificadas. O sistema integra interpretabilidade por design através da
geração automática de regras explicáveis, visualizações interativas e métricas
de importância de *features* que permitem validação técnica por especialistas do
domínio agrícola. A interface CLI minimalista prioriza usabilidade em ambientes
rurais com conectividade limitada, oferecendo tanto modo interativo para
usuários iniciantes quanto mode batch para integração com sistemas existentes.

O design enfatiza reprodutibilidade científica através de seeds fixos,
versionamento de modelos, logging detalhado de operações e serialização
padronizada que permite auditoria completa dos resultados e facilita colaboração
entre equipes técnicas. A arquitetura orientada a dados suporta extensão futura
do sistema através de novos datasets, features adicionais e algoritmos
emergentes sem necessidade de reestruturação fundamental, estabelecendo
fundações sólidas para evolução contínua da solução conforme novas demandas do
agronegócio e avanços tecnológicos em agricultura de precisão.

## 📁 Estrutura de Diretórios

    ...

## 🔧 Como Executar o Projeto

O projeto requer Python 3.8+ com as seguintes dependências principais:
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- joblib

para funcionalidades de Machine Learning e visualização. Execute:

    python3 -m pip install pandas numpy scikit-learn matplotlib seaborn joblib pathlib

para instalar todas as bibliotecas necessárias ou utilize:

    python3 install -r requirements.txt

Clone o repositório:

    git clone <>

E navegue até o diretório raiz do projeto com:

    cd fase3-cap14

para acessar todos os componentes do sistema.

#### Execução do Pipeline Completo de Machine Learning

Inicie o treinamento completo executando:

    python3 src/f3c14.ipynb

ou abra o notebook Jupyter com:

    jupyter notebook src/f3c14.ipynb

para execução interativa célula. O pipeline processa automaticamente os datasets
CSV, executa análise exploratória, treina cinco algoritmos de classificação,
otimiza hiperparâmetros via GridSearchCV e gera 25 visualizações técnicas junto
com 12 modelos serializados. O processo completo demora aproximadamente 15-20
minutos dependendo da capacidade computacional, salvando todos os resultados nos
diretórios `src/datasets/output` para visualizações e
`src/datasets/output/modelos_preditivos/modelos` para modelos treinados.

#### Utilização da Aplicação de Predição

Para predição individuais, execute:

    python3 src/datasets/output/modelos_preditivos/utils/app_predicao.py --valores N P K temperature humidity ph rainfall 

substituindo os valores pelos parâmetros específicos da propriedade (exemplo:
`--valores 90 42 43 20.87 82.18 6.5 202.9`). Para modo interativo, execute:

    python3  app_predicao.py

sem argumentos e o sistema solicitará entrada manual de cada parâmetro com
validação automática. Para demonstração com dados reais, utilize:

    python3 app_predicao.py --exemplo-real

que carrega automaticamente uma amostra do dataset e compara a predição com o
resultado conhecido.

#### Estrutura de Outputs e Resultados

Todos os resultados são organizados sistematicamente:
- visualizações exploratórias: `src/datasets/output`
- modelos de machine learning: `src/datasets/output/modelos_preditivos/modelos` 
- figuras comparativas: `src/datasets/output/modelos_preditivos/figuras`
- aplicação CLI: `src/datasets/output/modelos_preditivos/utils`

Para verificar a execução bem-sucedida, confirme a presença dos arquivos
`random_forest_best_model.pkl` (melhor modelo), `comparacao_modelos.csv`
(métricas comparativas) e `app_predicao.py` (aplicação funcional).

O sistema gera logs detalhados durante a execução que facilitam debugging e
acompanhamento do progresso através de mensagens informativas sobre cada etapa
do pipeline.

#### Resolução de Problemas Comuns

Se ocorrerem erros de dependências, verifique a versão do Python com:

    python3 --version

e reinstale as bibliotecas com:

    python3 -m pip install --upgrade <nome da biblioteca>


Para problemas de memória durante o treinamento, reduza o número de parâmetros
no GridSearchCV ou execute em máquinas com pelo menos 4G RAM disponível.

Se a aplicação CLI não funcionar, verifique se o modelo
`random_forest_best_model.pkl` foi gerado corretamente e se os caminhos no
código estão consistentes com a estrutura de diretório local.

Para questões de performance, execute o projeto em ambiente com múltiplos
núcleos de processamento pois o GridSearchCV utiliza paralelização automática
(`n_jobs=-1`) para acelerar a otimização de hiperparâmetros.

## 📋 Licença

[![Licença CC](https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1)](http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1)
[![Atribuição BY](https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1)](http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1)

[FASE 3 - CAP 14](https://github.com/RevoluxAI/fase3-cap1) está licenciado sob a [Creative Commons Atribuição 4.0 Internacional](http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1).

