import pandas as pd 
import matplotlib.pyplot as plt

pd.set_option('display.float_format', lambda x: '%.3f' % x)
ax = plt.subplots()
#Step one: Loaded in data 
df = pd.read_csv('https://health.data.ny.gov/resource/5dtw-tffi.csv?$query=SELECT%0A%20%20%60hospital_service_area%60%2C%0A%20%20%60hospital_county%60%2C%0A%20%20%60facility_name%60%2C%0A%20%20%60age_group%60%2C%0A%20%20%60gender%60%2C%0A%20%20%60race%60%2C%0A%20%20%60ethnicity%60%2C%0A%20%20%60discharge_year%60%2C%0A%20%20%60length_of_stay%60%2C%0A%20%20%60type_of_admission%60%2C%0A%20%20%60total_charges%60%2C%0A%20%20%60total_costs%60%2C%0A%20%20%60zip_code_3_digits%60%2C%0A%20%20%60operating_certificate_number%60%2C%0A%20%20%60permanent_facility_id%60%2C%0A%20%20%60patient_disposition%60%2C%0A%20%20%60ccsr_diagnosis_code%60%2C%0A%20%20%60ccsr_diagnosis_description%60%2C%0A%20%20%60ccsr_procedure_code%60%2C%0A%20%20%60ccsr_procedure_description%60%2C%0A%20%20%60apr_drg_code%60%2C%0A%20%20%60apr_drg_description%60%2C%0A%20%20%60apr_mdc_code%60%2C%0A%20%20%60apr_mdc_description%60%2C%0A%20%20%60apr_severity_of_illness_code%60%2C%0A%20%20%60apr_severity_of_illness%60%2C%0A%20%20%60apr_risk_of_mortality%60%2C%0A%20%20%60apr_medical_surgical%60%2C%0A%20%20%60payment_typology_1%60%2C%0A%20%20%60payment_typology_2%60%2C%0A%20%20%60payment_typology_3%60%2C%0A%20%20%60birth_weight%60%2C%0A%20%20%60emergency_department_indicator%60%0AWHERE%20caseless_one_of(%60hospital_service_area%60%2C%20%22Long%20Island%22)')

#Step 2 Confirm have all data needed
df['age_group'].head()
df['gender'].head()
df['length_of_stay'].head()
df['type_of_admission'].head()
df['total_charges'].head()
df['total_costs'].head()
df['discharge_year'].head()
df['ethnicity'].head()
df['race'].head()

#Step 3

#length_of_stay 
convert_stay = df['length_of_stay'].apply(lambda x : x.replace('+',''))
convert_stay = pd.to_numeric(convert_stay,errors = 'coerce')
convert_stay.describe([.25, .5, .75])


convert_total_cost = df['total_costs'].apply(lambda x : x.replace(',',''))
convert_total_cost = pd.to_numeric(convert_total_cost,errors = 'coerce')
convert_total_cost.describe([.25, .5, .75])

convert_total_charges = df['total_charges'].apply(lambda x : x.replace(',',''))
convert_total_charges = pd.to_numeric(convert_total_charges,errors = 'coerce')
convert_total_charges.describe([.25, .5, .75])

#Step 4
age_group = df['age_group']
age_group.value_counts()
age_group.value_counts().plot.bar(xlabel ='age_group',ylabel ='counts')
plt.savefig('bar_plot_age_group.png')
plt.show()

gender = df['gender']
gender.value_counts()
gender.value_counts().plot.bar(ylabel='count')
plt.savefig('bar_plot_gender.png')
plt.show()

type_of_admission = df['type_of_admission']
type_of_admission.value_counts()
type_of_admission.value_counts().plot.bar(ylabel='count')
plt.savefig('bar_plot_type_of_admission.png')
plt.show()

#Step 5
length_of_stay = df['length_of_stay']
length_of_stay.value_counts()
length_of_stay.value_counts().plot.hist(xlabel ='length_of_stay',ylabel ='counts')
plt.savefig('histogram_length_of_stay.png')
plt.show()

length_of_stay = df['length_of_stay']
length_of_stay.value_counts()
length_of_stay.value_counts().plot.hist(xlabel ='length_of_stay',ylabel ='counts')
plt.savefig('histogram_length_of_stay.png')
plt.show()