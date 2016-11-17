wget http://api.worldbank.org/v2/en/indicator/SI.POV.GINI?downloadformat=csv -O data.zip
unzip data.zip
mv API_SI.POV.GINI_DS2_en_csv_v2.csv data.csv
rm Meta*
rm data.zip
python lala.py
rm data.csv
