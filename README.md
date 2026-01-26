# Estatistica-Basica

## Capitulo 2

### Resumo de Dados:

Tabela 2.1 com informaçÕes de 36 empregados da seção de orçamentos da Companhia MB

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>N</th>
      <th>Estado Civil</th>
      <th>Grau de Instrução</th>
      <th>N de Filhos</th>
      <th>Salario (x Sal Min)</th>
      <th>Anos</th>
      <th>Meses</th>
      <th>Região de Procedência</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>solteiro</td>
      <td>ensino fundamental</td>
      <td>NaN</td>
      <td>4.00</td>
      <td>26</td>
      <td>3</td>
      <td>interior</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>casado</td>
      <td>ensino fundamental</td>
      <td>1.0</td>
      <td>4.56</td>
      <td>32</td>
      <td>10</td>
      <td>capital</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>casado</td>
      <td>ensino fundamental</td>
      <td>2.0</td>
      <td>5.25</td>
      <td>36</td>
      <td>5</td>
      <td>capital</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>solteiro</td>
      <td>ensino médio</td>
      <td>NaN</td>
      <td>5.73</td>
      <td>20</td>
      <td>10</td>
      <td>outra</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>solteiro</td>
      <td>ensino fundamental</td>
      <td>NaN</td>
      <td>6.26</td>
      <td>40</td>
      <td>7</td>
      <td>outra</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>casado</td>
      <td>ensino fundamental</td>
      <td>0.0</td>
      <td>6.66</td>
      <td>28</td>
      <td>0</td>
      <td>interior</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>solteiro</td>
      <td>ensino fundamental</td>
      <td>NaN</td>
      <td>6.86</td>
      <td>41</td>
      <td>0</td>
      <td>interior</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>solteiro</td>
      <td>ensino fundamental</td>
      <td>NaN</td>
      <td>7.39</td>
      <td>43</td>
      <td>4</td>
      <td>capital</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>casado</td>
      <td>ensino médio</td>
      <td>1.0</td>
      <td>7.59</td>
      <td>34</td>
      <td>10</td>
      <td>capital</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>solteiro</td>
      <td>ensino médio</td>
      <td>NaN</td>
      <td>7.44</td>
      <td>23</td>
      <td>6</td>
      <td>outra</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>casado</td>
      <td>ensino médio</td>
      <td>2.0</td>
      <td>8.12</td>
      <td>33</td>
      <td>6</td>
      <td>interior</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>solteiro</td>
      <td>ensino fundamental</td>
      <td>NaN</td>
      <td>8.46</td>
      <td>27</td>
      <td>11</td>
      <td>capital</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>solteiro</td>
      <td>ensino médio</td>
      <td>NaN</td>
      <td>8.74</td>
      <td>37</td>
      <td>5</td>
      <td>outra</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>casado</td>
      <td>ensino fundamental</td>
      <td>3.0</td>
      <td>8.95</td>
      <td>44</td>
      <td>2</td>
      <td>outra</td>
    </tr><br>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>casado</td>
      <td>ensino médio</td>
      <td>0.0</td>
      <td>9.13</td>
      <td>30</td>
      <td>5</td>
      <td>interior</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>solteiro</td>
      <td>ensino médio</td>
      <td>NaN</td>
      <td>9.35</td>
      <td>38</td>
      <td>8</td>
      <td>outra</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>casado</td>
      <td>ensino médio</td>
      <td>1.0</td>
      <td>9.77</td>
      <td>31</td>
      <td>7</td>
      <td>capital</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>casado</td>
      <td>ensino fundamental</td>
      <td>2.0</td>
      <td>9.80</td>
      <td>39</td>
      <td>7</td>
      <td>outra</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>solteiro</td>
      <td>superior</td>
      <td>NaN</td>
      <td>10.53</td>
      <td>25</td>
      <td>8</td>
      <td>interior</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>solteiro</td>
      <td>ensino médio</td>
      <td>NaN</td>
      <td>10.76</td>
      <td>37</td>
      <td>4</td>
      <td>interior</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>casado</td>
      <td>ensino médio</td>
      <td>1.0</td>
      <td>11.06</td>
      <td>30</td>
      <td>9</td>
      <td>outra</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>solteiro</td>
      <td>ensino médio</td>
      <td>NaN</td>
      <td>11.59</td>
      <td>34</td>
      <td>2</td>
      <td>capital</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>solteiro</td>
      <td>ensino fundamental</td>
      <td>NaN</td>
      <td>12.00</td>
      <td>41</td>
      <td>0</td>
      <td>outra</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>casado</td>
      <td>superior</td>
      <td>0.0</td>
      <td>12.79</td>
      <td>26</td>
      <td>1</td>
      <td>outra</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>casado</td>
      <td>ensino médio</td>
      <td>2.0</td>
      <td>13.23</td>
      <td>32</td>
      <td>5</td>
      <td>interior</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>casado</td>
      <td>ensino médio</td>
      <td>2.0</td>
      <td>13.60</td>
      <td>35</td>
      <td>0</td>
      <td>outra</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>solteiro</td>
      <td>ensino fundamental</td>
      <td>NaN</td>
      <td>13.85</td>
      <td>46</td>
      <td>7</td>
      <td>outra</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>casado</td>
      <td>ensino médio</td>
      <td>0.0</td>
      <td>14.69</td>
      <td>29</td>
      <td>8</td>
      <td>interior</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
      <td>casado</td>
      <td>ensino médio</td>
      <td>5.0</td>
      <td>14.71</td>
      <td>40</td>
      <td>6</td>
      <td>interior</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>casado</td>
      <td>ensino médio</td>
      <td>2.0</td>
      <td>15.99</td>
      <td>35</td>
      <td>10</td>
      <td>capital</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31</td>
      <td>solteiro</td>
      <td>superior</td>
      <td>NaN</td>
      <td>16.22</td>
      <td>31</td>
      <td>5</td>
      <td>outra</td>
    </tr>
    <tr>
      <th>31</th>
      <td>32</td>
      <td>casado</td>
      <td>ensino médio</td>
      <td>1.0</td>
      <td>16.61</td>
      <td>36</td>
      <td>4</td>
      <td>interior</td>
    </tr>
    <tr>
      <th>32</th>
      <td>33</td>
      <td>casado</td>
      <td>superior</td>
      <td>3.0</td>
      <td>17.26</td>
      <td>43</td>
      <td>7</td>
      <td>capital</td>
    </tr>
    <tr>
      <th>33</th>
      <td>34</td>
      <td>solteiro</td>
      <td>superior</td>
      <td>NaN</td>
      <td>18.75</td>
      <td>33</td>
      <td>7</td>
      <td>capital</td>
    </tr>
    <tr>
      <th>34</th>
      <td>35</td>
      <td>casado</td>
      <td>ensino médio</td>
      <td>2.0</td>
      <td>19.40</td>
      <td>48</td>
      <td>11</td>
      <td>capital</td>
    </tr>
    <tr>
      <th>35</th>
      <td>36</td>
      <td>casado</td>
      <td>superior</td>
      <td>3.0</td>
      <td>23.30</td>
      <td>42</td>
      <td>2</td>
      <td>interior</td>
    </tr>
  </tbody>
</table>
</div>

#### 2.1 Tipos de variáveis

Variaveis qualitativas nominais: Estadfo Civil, Região de Procedência
<br>Variaveis qualitativas ordinais: Grau de Instrução
<br>Variaveis quantitativas discretas: Número de Filhos, anos, meses
<br>variaveis quantitativas contínuas: Salario

![alt text](image.png)

#### 2.2 Distribuições de Frequências

Aqui podemos descobrir a ocorrencia das possíveis realizações de uma variavel. Abaixo a frequencia da variavel Grau de Instrução:<br><br>
Tabela 2.2 Frequencias e porcentagens dos 36 empregados da seção de orçamentos da Companhia MB segundo o grau de instrução

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Frequência</th>
      <th>Proporção</th>
      <th>Porcentagem %</th>
    </tr>
    <tr>
      <th>Grau de Instrução</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ensino médio</th>
      <td>18.0</td>
      <td>0.500000</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>ensino fundamental</th>
      <td>12.0</td>
      <td>0.333333</td>
      <td>33.333333</td>
    </tr>
    <tr>
      <th>superior</th>
      <td>6.0</td>
      <td>0.166667</td>
      <td>16.666667</td>
    </tr>
    <tr>
      <th>Total</th>
      <td>36.0</td>
      <td>1.000000</td>
      <td>100.000000</td>
    </tr>
  </tbody>
</table>
</div>

<br>Tabela 2.3 Frequancias e porcentagens dos 4000 empregados da Companhia MB, segundo grau de instrução.<br>

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Frequência</th>
      <th>Porcentagem</th>
    </tr>
    <tr>
      <th>Grau de Instrução</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Fundamental</th>
      <td>1650.0</td>
      <td>32.5</td>
    </tr>
    <tr>
      <th>Médio</th>
      <td>1020.0</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>Superior</th>
      <td>1330.0</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>Total</th>
      <td>4000.0</td>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
</div>

<br> Tabela 2.4 frequencia de faixas de salario

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Frequência</th>
      <th>Porcentagem %</th>
    </tr>
    <tr>
      <th>Faixa Salarial</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>[4, 8)</th>
      <td>10.0</td>
      <td>27.777778</td>
    </tr>
    <tr>
      <th>[8, 12)</th>
      <td>12.0</td>
      <td>33.333333</td>
    </tr>
    <tr>
      <th>[12, 16)</th>
      <td>8.0</td>
      <td>22.222222</td>
    </tr>
    <tr>
      <th>[16, 20)</th>
      <td>5.0</td>
      <td>13.888889</td>
    </tr>
    <tr>
      <th>[20, 24)</th>
      <td>1.0</td>
      <td>2.777778</td>
    </tr>
    <tr>
      <th>Total</th>
      <td>36.0</td>
      <td>100.000000</td>
    </tr>
  </tbody>
</table>
</div>