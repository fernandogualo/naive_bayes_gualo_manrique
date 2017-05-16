# -*- coding: utf-8 -*-


from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
import csv
import io

from preprocess import Preprocess

dengue_features_train_file = '../data/dengue_features_train.csv'
dengue_labels_train_file = '../data/dengue_labels_train.csv'
dengue_features_test_file = '../data/dengue_features_test.csv'

dengue_train_data = []
dengue_train_result = []
dengue_test_data = []
dengue_test_result = []
selected_attributes = []

#Limpieza de datos y selección de los atributos necesarios
for i in range(4, 23):
	selected_attributes.append(i)

Preprocess.cleanFile(dengue_features_train_file)
Preprocess.cleanFile(dengue_labels_train_file)
Preprocess.cleanFile(dengue_features_test_file)

#Apertura de los ficheros .csv limpios y se guardan en estructuras de datos    
with io.open(dengue_features_train_file + '.cleaned', newline = '') as csvfile:
    csv_dftrain_reader = csv.reader(csvfile, delimiter = ',', quotechar = "'", quoting = csv.QUOTE_ALL, skipinitialspace = True)
    for row in csv_dftrain_reader:
    	dengue_train_data.append([float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]), float(row[11]), float(row[12]), float(row[13]), float(row[14]), float(row[15]), float(row[16]), float(row[17]), float(row[18]), float(row[19]), float(row[20]), float(row[21]), float(row[22])])

with io.open(dengue_labels_train_file + '.cleaned', newline = '') as csvfile:
    csv_dltrain_reader = csv.reader(csvfile, delimiter = ',', quotechar = "'", quoting = csv.QUOTE_ALL, skipinitialspace = True)
    for row in csv_dltrain_reader:
        dengue_train_result.append(float(row[3]))

with io.open(dengue_features_test_file + '.cleaned', newline = '') as csvfile:
    csv_dftest_reader = csv.reader(csvfile, delimiter = ',', quotechar = "'", quoting = csv.QUOTE_ALL, skipinitialspace = True)
    for row in csv_dftest_reader:
        dengue_test_data.append([float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]), float(row[11]), float(row[12]), float(row[13]), float(row[14]), float(row[15]), float(row[16]), float(row[17]), float(row[18]), float(row[19]), float(row[20]), float(row[21]), float(row[22])])

# Crear los clasificadores
model_G = GaussianNB()
model_M = MultinomialNB()
model_B = BernoulliNB()

# Entrenamiento de los modelos creados
model_G.fit(dengue_train_data, dengue_train_result)
model_B.fit(dengue_train_data, dengue_train_result)

# Predecir con los dato de test
predicted_G = model_G.predict(dengue_test_data)
predicted_B = model_B.predict(dengue_test_data)

print("-----------Modelo Gaussiano -----------")
print(predicted_G)
print("-----------Modelo Bernoulli -----------")
print(predicted_B)

