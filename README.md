# Cobertura
Realize através de scripts python a cobertura de sua infraestrutura. Faça o python trabalhar por você.

### O que pode ser feito com o Cobertura?
Atualmente ferramentas de monitoramento de sistemas como (Zabbix) não tem soluções completas para serviços específicos.
Dentre vários serviços podemos indicar o (Redis), elencando nesta problemática vários itens:
- Existe algum item do cluster danificado?
- Quais items estão como primary ou replica?
- Está sendo acessado via SSH?
- O serviço está ativo?
- Cluster está funcional? Leitura e gravação de chaves?
- Quais erros encontrados? Quais possíveis dicas para solução?
![Screenshot_20220630_125821](https://user-images.githubusercontent.com/26276218/176724085-a6ea671f-e5ac-4e9b-a95e-427806416a82.png)

### Onde ficam os scripts?
Ficam na pasta [scripts](scripts) contendo até template html. A ideia é que cada caixinha seja um script como mostra a imagem abaixo:
![Screenshot_20220630_130034](https://user-images.githubusercontent.com/26276218/176724336-030d5702-c393-4449-8662-a5db4677fcce.png)

### Como instalar?
```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Como rodar?
Após instalar e reiniciar o VSCode para reconhecer as dependências, é possível abrir o arquivo "cobertura.py" e rodar pelo menu "Run" > "Run without debugging (ctrl + f5)"

### Python e frameworks utilizados
- Python 3.9.7
- Bootstrap v5.2.0-beta1
- Bootstrap Icons v1.8.3
- jQuery v3.6.0 Slim

### Pacotes do Python neste exemplo
- flask
- requests
- paramiko
- redis
