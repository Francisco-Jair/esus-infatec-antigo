<h1 align="center">
    <img alt="INFATEC" title="#INFATECEmpresa" src="https://infatec.net.br/templates/yootheme/cache/logo-infatec-92abd533.png" />
</h1>

<h4 align="center"> 
	🚧 Indicadores Previne 2022 1.0 🚀 em construção... 🚧
</h4>

<p align="center">
  <img alt="GitHub language count" src="https://icons.iconarchive.com/icons/cornmanthe3rd/plex/32/Other-python-icon.png">

  <img alt="Repository size" src="https://icons.iconarchive.com/icons/franksouza183/fs/32/Mimetypes-text-x-python-icon.png">

  	

</p>


## 💻 Sobre o projeto

🚀   Indicadores Previne 2022 1.0 Caxias - MA - Sistema como foco de analisar e gerar a partir
de dados,  tipos de informações relevante para avaliar o desempenho do serviço de saúde. 

O municipio poderar ter noção como é avaliada a  cidade, com relação ao serviço de saude, baseado nos indicadores. A baixo algumas funcionalidades:
- Realizar consultas
- Gerar Relatorios
- Analisar informações de maneira dinamica, atraves de graficos
- Gerar Graficos intuitivos 
- Ambiente amigavel e facil acesso
- Aplicação responsiva( se adapta a qualquer tamanho de dispositivo, Computadores e notebooks, SmartPhones e Tablets
- Impressao dos dados gerados
- Calculos dos indicadores

Abaixo os indicadores trabalhados:

1 - Proporção de gestantes com pelo menos seis consultas pré-natal realizadas, sendo a 1ª até a 12ª semana de gestação Avaliam-se os atendimentos realizados dos últimos 12 meses;<br>
2 - Proporção de gestantes com realização de exames para sífilis e HIV
Avaliam-se os atendimentos realizados dos últimos 12 meses;<br>
3 - Proporção de gestantes com atendimento odontológico realizado
Avaliam-se os atendimentos realizados dos últimos 12 meses;<br>
4 - Proporção de mulheres com coleta de citopatológico na APS
Avaliam-se os atendimentos realizados nos últimos 36 meses;<br>
5 - Proporção de crianças de um ano de idade vacinadas na APS contra difteria, tétano, coqueluche, hepatite B, infecções causadas por Haemophilus influenzae tipo B e poliomielite inativada;<br>
6 - Proporção de pessoas com hipertensão, com consulta e pressão arterial aferida no semestre;<br>
7 - Proporção de pessoas com diabetes, com consulta e hemoglobina glicada solicitada no semestre;<br>


Projeto desenvolvido pela Empresa INFATEC SOLUÇÕES TECNOLÓGICAS.
O Indicadores Previne 2022 1.0 é uma solução com foco de melhorar a gestao do municipio, baseado no desempenho do serviço de saúde.  .


## 🎨 Layout

design responsivo usa um layout flexível que se adapta a diferentes orientações ou tamanhos de janelas de visualização. 
Dessa forma, depedendo do dispostivio a aplicação não terá qualquer prejuízo na leitura das informações


## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python][python]
- [Django][django]
- [Django Rest Framework][djangorest]
- [Adminlte 3][adminlte]
- [Bootstrap][bootstrap]
- [JavaScript][javascript]

## 📝 Arquitetura do Projeto
O sistema esta baseado em MTV (Model, Template, View)Full Django.<br>
<strong>Model: </strong>Mapeamento do banco de dados para o projeto, pega as informações do Esus e faz com que a aplicação possa manipular a mesma;<br>
<strong>Template:</strong> Páginas para visualização de dados. aonde é dado toda a renderização do projeto, o front end propriamente dito. Para exibição e estilização da pages é usado a lib do bootstrap e javascript, para o B.I é usado o AdminLTE-3 e ChartJS;<br>
<strong>View: </strong>Lógica de negócio. É aqui é a onde que é determinado  toda a regra de negocio,calculos,tomadas de decisões, rotas e demais pontos de funcionamento que acontece no projeto.<br>
<strong> em tese o sistema funciona da seguinte forma: </strong><br>
O usuário do sistema solicita a geração dos indicadores de desempenho do Programa Previne Brasil, inserindo como parâmetros o tipo de indicador, o quadrimestre e o ano de avaliação. O sistema então extrai os dados e efetua a validação conforme critérios do Ministério da Saúde e, ao final, gera o indicador desejado. Os dados dos pacientes e atendimentos relativos ao indicador são salvos no banco de dados da apllicação, onde o gestor pode verificar, detalhadamente a produção das equipes de saúde do município.
 A figura abaixo mostra o funcionamento da mesma:<br>

<p align="center">
  <img alt="Arquitetura do projeto" src="https://fv9-6.failiem.lv/thumb_show.php?i=2suvw5bzt&view">
	

</p>

## 🚀 Como executar o projeto

Podemos considerar este projeto como sendo divido em quatro partes:
1. Uso do Esus (Sistema Esus) <br>
2. Uso do postgresql (banco de dados para consumo do Esus)<br>
3. Back end (Utilização dos comando python para rodar o server local)<br>
4. Utilizar o arquivo .env com sua devidas configurações<br>

💡primeiro ponto a se fazer é instalar o esus e postgresql

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:<br>
[Esus](https://sisaps.saude.gov.br/esus/), [Postgresql][postgres]. <br>
É necessario criar um banco de dados esus rodando localmente <br>
É necessario instalar as dependências ( para isso execute o arquivo requirements.txt)<br>

### ALTERNATIVA 1 - Executando o sistema na máquina local

É necessario criar o arquivo .env na raiz do projeto, apos criado inserir as seguintes informações e depois salvar :<br>
DEBUG=True<br>
SECRET_KEY=django-insecure-ilua_b85k-tjyv=3i7v5)p^_q%cfxs-tz0jlb%#1e8&$@tb@zh<br>
ALLOWED_HOSTS=127.0.0.1<br>
ESUS_DATABASE_URL=postgres://postgres:esus@localhost:5433/esus<br>

```bash
# abra um novo terminal e execute os comando a seguir para instalar as dependências:
$ pip install - r requirements.txt
# Todas as dependencias irão carregar e ser instaladas, após esse passo execute o servidor  e o gerenciador de tarefas qcluster em outra janela. com os 
#seguintes comandos:
$  python manage.py runserver
# o comando acima tem como foco executar o servidor. Após isso abra um novo terminal e execute o comando do qcluster:
$ python manage.py qcluster
# acesse o link http://127.0.0.1:8000/


```

### ALTERNATIVA 2 - Executando o sistema utilizando Docker

```bash
# abra um novo terminal e execute o comando a seguir para construir e executar os containers:
# (Sistema Operacional Linux)
$ docker-compose -f linux.yml up --build
# (Sistema Operacional Windows ou WSL)
$ docker-compose -f windows.yml up --build
# Na primeira execução do sistema é necessário criar um usuário para possibilitar o acesso. Quando o container estiver pronto, em outra janela do terminal execute o comando a seguir:
$ docker-compose exec web sh
# E depois:
$ python manage.py createsuperuser
# Em seguida, o sistema solicitará nome de usuário, email e senha. Insira conforme desejado.
# Acesse o link http://127.0.0.1:8000/ e faça login com os dados cadastrados no passo anterior.


```
## 📝 Licença

Este projeto está sob a Licença de software proprietário.

Desenvolvedores Responsaveis AJ 👋🏽 [Entre em contato!](https://www.facebook.com/aj.coostaa/) 👋🏽  Alberto [Entre em contato!](https://www.facebook.com/alb.romoc/)

[python]: https://www.python.org/
[django]: https://docs.djangoproject.com/en/4.0/
[djangorest]: https://www.django-rest-framework.org/
[adminlte]: https://adminlte.io/themes/v3/
[jre]: https://www.java.com/pt-BR/download/ie_manual.jsp?locale=pt_BR
[bootstrap]: https://getbootstrap.com/
[javascript]: https://developer.mozilla.org/pt-BR/docs/Web/JavaScript
[postgres]: https://www.postgresql.org/download/
