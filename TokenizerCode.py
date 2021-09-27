# Aqui segue um pequeno código para ajudar na parte lógica de pessoas
# que gostariam de tokenizar algum texto ou DataFram(df) que desejarem.

# Nesse primeiro trecho, iremos importar o NLTK, especificamente os dados.
# Além dele, usaremos o Pandas para poder carregar nosso df.
# O ultimo import é relativo a comandos e consultas relativas ao nosso sistema
# operacional. No meu caso, utilizo do windows 10
import nltk.data
import pandas as pd
import os

# Aqui carregamos os tokenizadores de frases em inglês e português.
tokenizer_english = nltk.data.load('nltk:tokenizers/punkt/english.pickle');
tokenizer_portuguese = nltk.data.load('nltk:tokenizers/punkt/portuguese.pickle');

# Aqui nós carregamos nosso dataSet em formato CSV,
# se seu caso for diferente, apenas adeque esse carregamento :)
df_english = pd.read_csv('dataSet_2320.csv');
df_portuguese = pd.read_csv('dataSet_5000.csv');

# Apenas duas variáveis sendo inicializadas em formato de lista
listCV = [];
listCVTokenized = [];

# Afim de evitar erros na escrita dos diretórios e/ou arquivos
# adicionei aqui todas as strings possíveis e diretórios que
# estaremos trabalhando.

# O método "os.getcwd()" nos trás o diretório atual que este arquivo
# python. Então todas as pastas e arquivos serão criados no mesmo
# diretório que este arquivo estiver
basePath = str(os.getcwd());
folderBR = 'text_by_tokenizer_portuguese';
folderEN = 'text_by_tokenizer_english';
pathFolderBR = '{}\\text_by_tokenizer_portuguese'.format(basePath);
pathFolderEN = '{}\\text_by_tokenizer_english'.format(basePath);
diretoryCentralBR = os.path.join(basePath, folderBR);
diretoryCentralEN = os.path.join(basePath, folderEN);
originalText = 'textCV.txt';
tokenizedText = 'textTokenized.txt';
i = 0;

# Função para utilizar o tokenizador que carregamos.
# Para evitar confusão, eu apenas adicionei uma string 
# como parâmetro para saber qual dos dois serem utilizados
def tokenizing(text,language):
    if (language == 'br'):
        return tokenizer_portuguese.tokenize(text);
    elif(language == 'en'):
        return tokenizer_english.tokenize(text);

# Função para pegar cada linha do dataset em
# formato de string e utilizar o tokenizer
# salvando em arquivos o texto original e o
# tokenizado
def generateTokenizedBR(i):
    try:
        textCV = str(df_portuguese['cv_text'][i]);
        textTokenized = tokenizing(textCV);
        os.chdir(pathFolderBR);
        createFolder = os.path.join(os.getcwd(),"{}".format(i));
        os.mkdir(createFolder);
        directoryWithFolder = "{}\\{}".format(diretoryCentralBR,i);
        fileTextCV = open("{}\\{}".format(directoryWithFolder,originalText), "x", encoding = 'utf-8');
        fileTextCV.write(textCV);
        fileTextCV.close();
        fileTextTokenized = open("{}\\{}".format(directoryWithFolder,tokenizedText), "x", encoding = 'utf-8');
        for item in textTokenized:
            fileTextTokenized.write(item+"\n");
        fileTextTokenized.close();
    except:
        pass

# Mesma função de cima, apenas com
# a mudança do idioma
def generateTokenizedEN(i):
    try:
        textCV = str(df_english['cv_text'][i]);
        textTokenized = tokenizing(textCV);
        os.chdir(pathFolderEN);
        createFolder = os.path.join(os.getcwd(),"{}".format(i));
        os.mkdir(createFolder);
        directoryWithFolder = "{}\\{}".format(diretoryCentralEN,i);
        fileTextCV = open("{}\\textCV.txt".format(directoryWithFolder), "x", encoding = 'utf-8');
        fileTextCV.write(textCV);
        fileTextCV.close();
        fileTextTokenized = open("{}\\textTokenized.txt".format(directoryWithFolder), "x", encoding = 'utf-8');
        for item in textTokenized:
            fileTextTokenized.write(item+"\n");
        fileTextTokenized.close();
    except:
        pass

# Verificação se a pasta criada existe ou não.
# Lembrando que eu fiz apenas verificando as pastas
# ainda não adicionei uma verificação para os arquivos
# então caso já tenha gerado alguma vez, recomendo que
# delete os arquivos ou a pasta contendo os arquivos
# para que o código possa funcionar sem ocorrer uma exception
if(os.path.exists(folderBR) and os.path.exists(folderEN)):
    for i in range(100):
        generateTokenizedBR(i);
        generateTokenizedEN(i);
else:
    os.mkdir(diretoryCentralBR);
    os.mkdir(diretoryCentralEN);
    for i in range(100):   
        generateTokenizedBR(i);
        generateTokenizedEN(i);