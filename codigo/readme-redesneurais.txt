O código para predição de séries temporais utiliza o toolbox do professor Von Zuben da
Faculdade de Engenharia Elétrica e Computação da Unicamp. Tal toolbox foi modificado
para permitir sua automação.

O arquivo db_time_series_predictor contém um script de automação do processo utilizado.
Nele são calculados os coeficientes de autocorrelação de cada série e um ensemble de
redes neurais então é treinado para predizer um número de valores futuros para a série.

A pasta simpleESN contém um toolbox para treinamento e testes de redes neurais de
estado eco.