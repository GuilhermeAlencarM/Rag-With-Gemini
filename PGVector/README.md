# Execução

Para iniciar a aplicação, é necessário instalar os requirements do arquivo `requirements.txt`:
`pip install -r requirements.txt`

# Obter a imagem da extensão do pgvector com PostgreSQL

`docker pull pgvector/pgvector:pg16`

# Criação do container

Após a criação da imagem, crie um container especificando a senha e o nome do banco de dados:
`docker run -d --name pgvector -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_DB=postgres -p 5432:5432 pgvector/pgvector:pg16`

Em seguida, execute o arquivo de configuração na pasta config chamado database para a criação da extensão pgvector:

`python config/database.py`

Por fim, execute o comando para inicialização da api:

`uvicorn main:app --reload`
