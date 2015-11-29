CREATE TABLE IF NOT EXISTS surgerytypemodel_table (
    pk SERIAL PRIMARY KEY,
    name TEXT,
    specialty TEXT,
    description TEXT);

CREATE TABLE IF NOT EXISTS surgerymodel_table (
    pk SERIAL PRIMARY KEY,
    surgery_date DATE,
    surgery_type_pk SERIAL REFERENCES surgerytypemodel_table(pk));

CREATE TABLE IF NOT EXISTS pharmacymodel_table (
    pk SERIAL PRIMARY KEY,
    address TEXT,
    phone TEXT,
    cashier1 TEXT,
    cashier2 TEXT);