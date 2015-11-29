/*
 * Entity relations
 */
CREATE TABLE IF NOT EXISTS patientmodel_table (
    pk SERIAL PRIMARY KEY,
    name TEXT,
    address TEXT,
    phone TEXT,
    blood_type TEXT,
    height REAL,
    weight REAL,
    birthdate DATE);

CREATE TABLE IF NOT EXISTS inventorymodel_table (
    pk SERIAL PRIMARY KEY,
    units NUMERIC,
    price REAL,
    priority NUMERIC);

CREATE TABLE IF NOT EXISTS toolmodel_table (
    pk SERIAL PRIMARY KEY,
    name TEXT,
    usage TEXT) INHERITS (inventorymodel_table);

CREATE TABLE IF NOT EXISTS medicinemodel_table (
    pk SERIAL PRIMARY KEY,
    name TEXT,
    type TEXT,
    description TEXT) INHERITS (inventorymodel_table);

CREATE TABLE IF NOT EXISTS diagnosismodel_table (
    pk SERIAL PRIMARY KEY,
    treatment TEXT,
    disease TEXT);

CREATE TABLE IF NOT EXISTS surgerytypemodel_table (
    pk SERIAL PRIMARY KEY,
    name TEXT,
    specialty TEXT,
    description TEXT,
    patient_pk INT REFERENCES patientmodel_table(pk),
    surgery_type_pk INT REFERENCES surgerytypemodel_table(pk),
    employee_pk INT REFERENCES employeemodel_table(pk));

CREATE TABLE IF NOT EXISTS pharmacymodel_table (
    pk SERIAL PRIMARY KEY,
    address TEXT,
    phone TEXT,
    cashier1 TEXT,
    cashier2 TEXT,
    inventory_pk INT REFERENCES inventorymodel_table(pk));

CREATE TABLE IF NOT EXISTS hospitalmodel_table (
    pk SERIAL PRIMARY KEY,
    name TEXT,
    address TEXT,
    phone TEXT,
    cashier TEXT,
    inventory_pk INT REFERENCES inventorymodel_table(pk));

CREATE TABLE IF NOT EXISTS departmentmodel_table (
    pk SERIAL PRIMARY KEY,
    name TEXT,
    boss TEXT,
    hospital_pk INT REFERENCES hospitalmodel_table(pk));

CREATE TABLE IF NOT EXISTS surgerymodel_table (
    pk SERIAL PRIMARY KEY,
    surgery_date DATE,
    surgery_type_pk INT REFERENCES surgerytypemodel_table(pk));

CREATE TABLE IF NOT EXISTS appointmentmodel_table (
    pk SERIAL PRIMARY KEY,
    appointment_data DATE,
    patient_pk INT REFERENCES patientmodel_table(pk),
    hospital_pk INT REFERENCES hospitalmodel_table(pk));

CREATE TABLE IF NOT EXISTS prescriptionmodel_table (
    pk SERIAL PRIMARY KEY,
    prescription_date DATE,
    appointment_pk INT REFERENCES appointmentmodel_table(pk));

CREATE TABLE IF NOT EXISTS employeemodel_table (
    pk SERIAL PRIMARY KEY,
    name TEXT, /* Not in ERM */
    birthdate DATE,
    phone TEXT,
    address TEXT,
    type TEXT,
    position TEXT,
    special_age NUMERIC, /* What is this? */
    wage REAL,
    picture BYTEA,
    department_pk INT REFERENCES departmentmodel_table(pk));

/*
 * Many-to-many relations
 */
CREATE TABLE IF NOT EXISTS prescriptionmedicinemodel_table (
    prescription_pk INT REFERENCES prescriptionmodel_table(pk),
    medicine_pk INT REFERENCES medicinemodel_table(pk),
    PRIMARY KEY (prescription_pk, medicine_pk));

CREATE TABLE IF NOT EXISTS employeeappointmentmodel_table (
    employee_pk INT REFERENCES employeemodel_table(pk),
    appointment_pk INT REFERENCES appointmentmodel_table(pk),
    PRIMARY KEY (employee_pk, appointment_pk));

CREATE TABLE IF NOT EXISTS diagnosisappointmentmodel_table (
    diagnosis_pk INT REFERENCES diagnosismodel_table(pk),
    appointment_pk INT REFERENCES appointmentmodel_table(pk),
    PRIMARY KEY (diagnosis_pk, appointment_pk));

CREATE TABLE IF NOT EXISTS diagnosispatientmodel_table (
    diagnosis_pk INT REFERENCES diagnosismodel_table(pk),
    patient_pk INT REFERENCES patientmodel_table(pk),
    PRIMARY KEY (diagnosis_pk, patient_pk));

CREATE TABLE IF NOT EXISTS diagnosismedicinemodel_table (
    diagnosis_pk INT REFERENCES diagnosismodel_table(pk),
    medicine_pk INT REFERENCES medicinemodel_table(pk),
    PRIMARY KEY (diagnosis_pk, medicine_pk));

CREATE TABLE IF NOT EXISTS hospitalemployeemodel_table (
    hospital_pk INT REFERENCES hospitalmodel_table(pk),
    employee_pk INT REFERENCES employeemodel_table(pk),
    PRIMARY KEY (hospital_pk, employee_pk));

CREATE TABLE IF NOT EXISTS surgeryinventorymodel_table (
    surgery_pk INT REFERENCES surgerymodel_table(pk),
    inventory_pk INT REFERENCES inventorymodel_table(pk),
    PRIMARY KEY (surgery_pk, inventory_pk));