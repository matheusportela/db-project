/*
 * Entity relations
 */
CREATE TABLE IF NOT EXISTS patientmodel_table (
    pk SERIAL PRIMARY KEY,
    name TEXT,
    address TEXT,
    phone TEXT,
    birthdate DATE,
    weight REAL,
    height REAL,
    blood_type TEXT);

CREATE TABLE IF NOT EXISTS inventorymodel_table (
    pk SERIAL PRIMARY KEY,
    units NUMERIC,
    price REAL,
    priority NUMERIC);

CREATE TABLE IF NOT EXISTS materialsmodel_table (
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
    description TEXT);

CREATE TABLE IF NOT EXISTS pharmacymodel_table (
    pk SERIAL PRIMARY KEY,
    address TEXT,
    phone TEXT,
    cashier TEXT,
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
    hospital_pk INT REFERENCES hospitalmodel_table(pk));

CREATE TABLE IF NOT EXISTS employeemodel_table (
    pk SERIAL PRIMARY KEY,
    name TEXT, /* Not in ERM */
    birthdate DATE,
    type TEXT,
    position TEXT,
    specialty TEXT,
    address TEXT,
    phone TEXT,
    wage REAL,
    contract_date DATE,
    picture BYTEA,
    department_pk INT REFERENCES departmentmodel_table(pk),
    boss INT REFERENCES employeemodel_table(pk));

CREATE TABLE IF NOT EXISTS surgerymodel_table (
    pk SERIAL PRIMARY KEY,
    surgery_date DATE,
    patient_pk INT REFERENCES patientmodel_table(pk),
    surgery_type_pk INT REFERENCES surgerytypemodel_table(pk),
    general_surgeon_pk INT REFERENCES employeemodel_table(pk),
    co_surgeon_pk INT REFERENCES employeemodel_table(pk),
    assistant_surgeon_pk INT REFERENCES employeemodel_table(pk),
    inventory_pk INT REFERENCES inventorymodel_table(pk));

CREATE TABLE IF NOT EXISTS appointmentmodel_table (
    pk SERIAL PRIMARY KEY,
    appointment_data DATE,
    patient_pk INT REFERENCES patientmodel_table(pk),
    employee_pk INT REFERENCES employeemodel_table(pk),
    hospital_pk INT REFERENCES hospitalmodel_table(pk));

CREATE TABLE IF NOT EXISTS prescriptionmodel_table (
    pk SERIAL PRIMARY KEY,
    dosage TEXT,
    appointment_pk INT REFERENCES appointmentmodel_table(pk));

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

CREATE TABLE IF NOT EXISTS surgerynursemodel_table (
    surgery_pk INT REFERENCES surgerymodel_table(pk),
    nurse_pk INT REFERENCES employeemodel_table(pk),
    PRIMARY KEY (surgery_pk, nurse_pk));

CREATE TABLE IF NOT EXISTS departmentemployeemodel_table (
    department_pk INT REFERENCES departmentmodel_table(pk),
    employee_pk INT REFERENCES employeemodel_table(pk),
    PRIMARY KEY (department_pk, employee_pk));