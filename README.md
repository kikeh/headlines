Headlines
========

This is a basic Python program that prints newspaper headlines. Besides it also uses a very simple sentiment analysis of those headlines for measuring the general mood of the news.

## Requirements

*headlines* has been developed for Python 2.7 (for now). It will surely be improved for Python 3 soon.

## Usage

Basic ways of using *headlines*:

#### Sentiment analysis only (default)

```
python headlines.py
```

#### Sentiment analysis, headlines and newspaper (by name or id)

```
python headlines.py -n <num_headlines> -p <newspaper>
```

Based on a list with info about different newspapers, it is possible to check the news choosing it.

Supported now:

| Newspaper      | Simple name     |    ID# |
| -------------- | --------------- | :----: |
| El Mundo       | elmundo         |      0 |
| 20 Minutos     | 20minutos       |      1 |

## Example

This command will output the sentiment analysis and the first 10 headlines of '20 Minutos':

```
python headlines.py -n 10 -p 20minutos
```

Output:

```
Matches:
  0 out of 9 matches are good
  9 out of 9 matches are bad
Headlines: 
  Good    : 0
  Bad     : 9
  Moderate: 131
Headlines are 100.00% negative.

[1] El Consejo de Estado apoya la impugnación del 9-N por unanimidad
[2] Javier Tebas: "Si la votación es libre, Cristiano no gana los premios de la Liga"
[3] Tim Cook, el jefe de Apple, se declara gay en una carta: "Estoy orgulloso de serlo"
[4] Joan Laporta no descarta presentarse a las próximas elecciones del Barça
[5] Cinco consejos para evitar perder el tiempo
[6] Expediente sancionador a Mediaset y Atresmedia por exceso de publicidad
[7] El Congreso aprueba la 'ley Lassalle' entre críticas de "chapuza" y "desastre"
[8] Sor Cristina: "El programa de 'La Voz' me ha servido para hacer llegar un mensaje divino"
[9] Los Giants de San Francisco ganan las Series Mundiales de béisbol
[10] Las Comunidades deben 1.330 millones de euros a empresas de tecnología sanitaria
```
