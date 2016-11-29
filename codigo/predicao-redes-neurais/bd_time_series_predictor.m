clear all;
clc;


%load time series - eacho series in a column
time_series = csvread('csvSintomasCeara.csv',1,1);
%time_series = dengue_SP;
time_series_size = [670 670 670 670 670];
num_series = 5;
%values to predict
num_predictions = 100;
num_sintoma = 5
%for num_sintoma=1 : num_series
    
    delete_temp_files;
    
%   achar coeficiente de autocorrelacao
    auto_correlacao = calc_cor(time_series(:,num_sintoma));
    
    %pegar o numero de entradas de acordo com o coeficiente de
    %autocorrelacao
    num_inputs = find(auto_correlacao<0.3,1);
    
    %seta o limite maximo de inputs da rede
    if(isempty(num_inputs))
       num_inputs=20; 
    end
    %checa se a série temporal é praticamente só zeros
    soma = sum(time_series(:,num_sintoma));
    if(soma<5)
        num_sintoma
       %continue;
    end
    
    %pega a série temporal relevante
    S = time_series(1:time_series_size(num_sintoma),num_sintoma);
    %S = time_series;
    %S = S / norm(S);
    %cria o conjunto de treinamento a partir da serie temporal
    for k=1 : time_series_size(num_sintoma) - num_inputs
       for j=1 : num_inputs
          X(k,j) = S(k+j-1);
       end
    end
    %coloca a coluna de bias da rede neural
    X = [X ones(length(X(:,1)),1)]
    %aqui ja temos a serie temporal normalizada e o conjunto de treinamento
    %X já montado.
    %Agora vamos separar os k folds para treinamento, validação e testes
    num_neurons_hidden_layer = time_series_size(num_sintoma)/(5*(num_inputs+1));
    gen_k_folds;
    %iniciar treinamento
    nn1h_k_folds;
    
    %neural networks trained
    %now we need to generate a prediction
    saida = time_series(1:time_series_size(num_sintoma),num_sintoma);
    %S = S / norm(S);
    for cur_prediction = 1 : num_predictions
        for fold = 1 : 10
            
            %load weights
            load(strcat('w1v',sprintf('%d',fold)));
            load(strcat('w2v',sprintf('%d',fold)));
            %get size of the time series
            last_index = size(saida);
            last_index = last_index(1);
            
            %get input as the n last numbers from the time series
            input = saida(last_index(1)-length(w1(1,:))+1:last_index);
            %transpose arrays
            input = input';
           
            
            %rodar a rede neural nos dados input
            Srn(fold) = [tanh(input*w1') ones(1,1)]*w2';
            
        end
        
        %tomar a predicao como resultado do ensemble
        prediction = ceil(mean(Srn));
        
        
        prediction
        clear Srn;
        %atualizar a série temporal para a próxima predição
        saida = vertcat(saida,prediction);
        
    end
    
    %A saída do ensemble para este sintoma é enviada para este csv
    csvwrite('saida.csv',saida')
%end
