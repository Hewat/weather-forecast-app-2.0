## Descrição de como foi construir o backend em Python

1 - Instalação do PIP package manager e do framework Flask

Instalei o PIP package manager e utilizei o framework Flask para criar as rotas de API. Também é necessário iniciar o ambiente virtual que criei com o comando na pasta backend ```source weather-forecast-app-env/bin/activate```

2 - Chamada às APIs da OpenWeatherMap

No arquivo app.py criei duas chamadas nas APIs da https://openweathermap.org/, uma para a API de 5 dias/3 em 3 horas e outra para as informações de tempo do instante atual.

3 - Criação de um dicionário com os dados da API

Executando essas duas chamadas foi criado um dicionário weather com os dados que a aplicação necessita, conforme abaixo.

```weather = {
"city": forecast_data["city"]["name"],
"country": forecast_data["city"]["country"],
"current_weather": current_weather_data,
"forecast": forecast_data["list"],
}
```

4 - Criação do banco de dados SQLite

Criei o arquivo ```database.py```, o qual cria a tabela no banco sqLite com os dados de tempo do instante atual (prefixo 'current_weather') e de previsão do tempo (prefixo 'forecast')

5 - Tratamento dos dados e inserção no banco de dados

No mesmo arquivo ```database.py``` é feito um tratamento com os dados provenientes do dicionário weather, separando cada dado e iterando cada linha para poder ser inserido no banco de dados corretanmente.

6 - Criação das rotas de API

Foram então criadas duas rotas utilizando o Flask, uma ```/search``` com input de parametro com a cidade que deseja buscar e armazena os dados na tabela ```'weather'``` do banco de dados e a outra ```/history``` que busca no banco de dados o histórico que foi salvo nas buscas anteriores.

7 - Teste do backend

7.1) Instale primeiramente o python. Se já tiver instalado, utilize ```python3 --version``` para checar a versão. Se não, instale a última versão 3.x de https://www.python.org/

7.1) Verifique se o package manager PIP está instalado com o comando ```python3 -m pip --version```. Se não, siga as instruções em https://packaging.python.org/en/latest/tutorials/installing-packages/#

7.2) Iniciar o ambiente virtual na pasta backend ```source weather-forecast-app-env/bin/activate```

7.3) Instalar as dependencias necessárias na mesma pasta conforme abaixo, utilizando o gerenciador de pacotes PIP. 

flask: pip install Flask
flask_cors: pip install flask_cors
requests: pip install requests

Os outros módulos utilizados (os, json, datetime, sqlite3) necessários para o projeto já estão inclusos.

7.4) Finalmente, Para testar o backend basta rodar o comando 'python3 app.py' dentro da pasta 'backend', que será iniciado o servidor na porta 5000. Então basta fazer uma chamada no Postman, por exemplo, com uma URL do tipo ```http://localhost:5000/search?city=São Paulo```. Você verá que a API trará o JSON com o retorno e também salvará todos os dados, um a um, no banco.

## Descrição de como foi construir parcialmente o frontend com React e Javascript

1 - Utilização do create-react-app

utilizei a base de projeto react do ```create-react-app```, que fornece já uma estrutura e instala módulos como o ```react```, ```react-dom``` e ```react-script``` para testar a aplicação em tempo real.

2 - Criação do campo de texto e do botão

Comecei criando um campo de texto e um botão. Ao preencher o campo de texto e apertar o botão, é chamada uma função ```handleSubmit``` que irá fazer a busca na rota ```/search``` fornecida pelo backend da aplicação e armazenar em um estado ```weatherData```.

3 - Criação dos componentes WeatherCard e Forecast

Criei o componente ```WeatherCard```, para conter os cards com os dados resumidos de cada dia e o componente ```Forecast```, para conter os dados detalhados ao clicar em um ```WeatherCard```.

4 - Teste do frontend

Para testar é necessário utilizar ```npm start```, que iniciará um servidor na porta 3000. Foi utilizada uma biblioteca de CORS para permitir a comunicação entre o backend e o frontend que estão em portas diferentes. Lembrando que o servidor backend precisa estar rodando também na porta 5000 com o comando 'python3 app.py'.

5 - Dificuldades e pontos a serem melhorados
A medida que fui trabalhando nos componentes e testando, os dados foram corretamente requisitados do backend, porém tive muitos problemas com as instalações dos módulos e não consegui renderizar novamente devido ao erro persistente de conflito nos módulos. Entrego então o projeto parcialmente.
