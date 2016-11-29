# Regressao nao parametrica

Este documento faz referencia ao codigo de regressao nao parametrica baseada em kernels

Este codigo foi feito em um modo evolutivo e contem varios exemplos de como utilizar as classes *example*, *example2*, *example3*

Geralmente os codigos necessitam de dados colhetados no Google Trends que se encontram na pasta //PrevisaodeEstoque/trends em formato *.csv*. Os scripts tambem geram *.csv* na pasta *predictions* que serao utlizados para popular o banco de dados as fases de aprendizado e previsao

## Requisitos
Para executar esse codigo, certifique-se que os seguintes pacotes estejam instalados:
- numpy
- scikit-learn
- matplotlib
- pandas

## Mock dataset
Para executar o algoritmo sobre uma base de dados pequena utilizada nas figuras do slide e do texto final entregue, execute

    $ python run_mock.py

o que mostrara um grafico da previsao de "dor de cabeca" por tempo para o estado de Sao Paulo. Este exemplo utiliza dados armazenados em *mock.csv*

## Full dataset
Para executar o codigo no dataset inteiro, execute

    $ python run.py

Esse codigo necessita dos *.csv* localizados em //PrevisaodeEstoque/trends

### Author
- Tiago Lobato Gimenes
