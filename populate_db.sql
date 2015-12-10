INSERT INTO patientmodel_table
    (pk, name, address, phone, blood_type, height, weight, birthdate) VALUES
    (1, 'Harry Potter', 'Gryffindor Male Dormitory', '3321-3030', 'A+',
        '1.71', '56.0', '1994-01-11');
INSERT INTO patientmodel_table
    (pk, name, address, phone, blood_type, height, weight, birthdate) VALUES
    (2, 'Hermione Granger', 'Gryffindor Female Dormitory', '3321-8181', 'A-',
        '1.60', '63.0', '1992-12-07');
INSERT INTO patientmodel_table
    (pk, name, address, phone, blood_type, height, weight, birthdate) VALUES
    (3, 'Albus Dumbledore', 'Headmaster Room', '2222-1232', 'O+',
        '1.65', '60.0', '1991-07-31');

INSERT INTO materialsmodel_table
    (pk, name, usage, units, price, priority) VALUES
    (1, 'Gaze', 'Curativos', 100, 1.50, 1);
INSERT INTO materialsmodel_table
    (pk, name, usage, units, price, priority) VALUES
    (2, 'Seringa', 'Vacinas', 250, 2.00, 4);
INSERT INTO materialsmodel_table
    (pk, name, usage, units, price, priority) VALUES
    (3, 'Bisturi', 'Cirurgia', 15, 10.00, 2);

INSERT INTO medicinemodel_table
    (pk, name, type, description, units, price, priority) VALUES
    (4, 'Aspirina', 'Analgésico', 'Alívio de dor', 42, 3.45, 1);
INSERT INTO medicinemodel_table
    (pk, name, type, description, units, price, priority) VALUES
    (5, 'Novalgina', 'Anti-Térmico', 'Tratamento de febre', 27, 1.10, 2);
INSERT INTO medicinemodel_table
    (pk, name, type, description, units, price, priority) VALUES
    (6, 'Paracetamol', 'Bactericida', 'Tratamento contra infecções', 3, 6.00, 10);

INSERT INTO diagnosismodel_table
    (pk, disease, treatment) VALUES
    (1, 'Gripe', 'Repouso por 7 dias');
INSERT INTO diagnosismodel_table
    (pk, disease, treatment) VALUES
    (2, 'Câncer', 'Quimioterapia');
INSERT INTO diagnosismodel_table
    (pk, disease, treatment) VALUES
    (3, 'Dengue', 'Internação em UTI');

INSERT INTO surgerytypemodel_table
    (pk, name, specialty, description) VALUES
    (1, 'Catarata', 'Oftalmologia', 'Remoção de catarata');
INSERT INTO surgerytypemodel_table
    (pk, name, specialty, description) VALUES
    (2, 'Cardiovascular', 'Cardiologia', 'Inserção de stent');
INSERT INTO surgerytypemodel_table
    (pk, name, specialty, description) VALUES
    (3, 'AVC', 'Neurologia', 'Intervenção pós-AVC');

INSERT INTO pharmacymodel_table
    (pk, address, phone, funds, inventory_pk) VALUES
    (1, 'Rua dos Alfeneiros', '9292-0101', 30000.00, NULL);
INSERT INTO pharmacymodel_table
    (pk, address, phone, funds, inventory_pk) VALUES
    (2, 'St. Mungus', '7273-0101', 50000.00, NULL);
INSERT INTO pharmacymodel_table
    (pk, address, phone, funds, inventory_pk) VALUES
    (3, 'Hogsmeade', '8877-2233', 1000.00, NULL);

INSERT INTO hospitalmodel_table
    (pk, name, address, phone, funds, inventory_pk) VALUES
    (1, 'HRAN', 'Asa Norte', '3333-0001', 90000.00, NULL);
INSERT INTO hospitalmodel_table
    (pk, name, address, phone, funds, inventory_pk) VALUES
    (2, 'HRAS', 'Asa Sul', '3333-0002', 30000.00, NULL);
INSERT INTO hospitalmodel_table
    (pk, name, address, phone, funds, inventory_pk) VALUES
    (3, 'HRT', 'Asa Taguatinga', '3333-0003', 60000.00, NULL);

INSERT INTO departmentmodel_table
    (pk, name, hospital_pk) VALUES
    (1, 'Enfermagem', 1);
INSERT INTO departmentmodel_table
    (pk, name, hospital_pk) VALUES
    (2, 'Cirurgia', 3);
INSERT INTO departmentmodel_table
    (pk, name, hospital_pk) VALUES
    (3, 'Pronto-Socorro', 2);

INSERT INTO employeemodel_table
    (pk, name, birthdate, type, position, specialty, address, phone, wage,
        contract_date, picture, department_pk, boss) VALUES
    (1, 'Madam Pomfrey', '1970-01-01', 'Médico', 'Diretor', 'Cirurgia',
        'Ala Hospitalar', '0022-1122', 4000.00, '2001-07-07', NULL, 1, NULL);
INSERT INTO employeemodel_table
    (pk, name, birthdate, type, position, specialty, address, phone, wage,
        contract_date, picture, department_pk, boss) VALUES
    (2, 'Minerva McGonnagal', '1960-01-01', 'Administrador', 'Contador',
        'Departamento de Finanças', 'Contabilidade', '0022-1123', 10000.00,
        '2002-01-01', NULL, 3, NULL);
INSERT INTO employeemodel_table
    (pk, name, birthdate, type, position, specialty, address, phone, wage,
        contract_date, picture, department_pk, boss) VALUES
    (3, 'Rubeus Hagrid', '1980-01-01', 'Advogado', 'Procurador', 'Advocacia',
        'Departamento Jurídico', '0022-1124', 11000.00, '2003-07-07', NULL, 1,
        NULL);

INSERT INTO surgerymodel_table
    (pk, surgery_date, patient_pk, surgery_type_pk, general_surgeon_pk,
        co_surgeon_pk, assistant_surgeon_pk, inventory_pk) VALUES
    (1, '2010-10-10', 1, 2, 1, 2, 3, NULL);
INSERT INTO surgerymodel_table
    (pk, surgery_date, patient_pk, surgery_type_pk, general_surgeon_pk,
        co_surgeon_pk, assistant_surgeon_pk, inventory_pk) VALUES
    (2, '2011-11-11', 3, 1, 3, 2, 1, NULL);
INSERT INTO surgerymodel_table
    (pk, surgery_date, patient_pk, surgery_type_pk, general_surgeon_pk,
        co_surgeon_pk, assistant_surgeon_pk, inventory_pk) VALUES
    (3, '2012-12-12', 3, 3, 2, 1, 3, NULL);

INSERT INTO appointmentmodel_table
    (pk, appointment_date, patient_pk, employee_pk, hospital_pk) VALUES
    (1, '2015-07-07', 1, 1, 2);
INSERT INTO appointmentmodel_table
    (pk, appointment_date, patient_pk, employee_pk, hospital_pk) VALUES
    (2, '2015-08-07', 3, 3, 2);
INSERT INTO appointmentmodel_table
    (pk, appointment_date, patient_pk, employee_pk, hospital_pk) VALUES
    (3, '2015-09-07', 2, 2, 1);

INSERT INTO prescriptionmodel_table
    (pk, dosage, appointment_pk) VALUES
    (1, '2 vezes ao dia', 3);
INSERT INTO prescriptionmodel_table
    (pk, dosage, appointment_pk) VALUES
    (2, '1 vez por semana', 2);
INSERT INTO prescriptionmodel_table
    (pk, dosage, appointment_pk) VALUES
    (3, '10 mL toda manhã', 1);

INSERT INTO prescriptionmedicinemodel_table VALUES (1, 2);
INSERT INTO prescriptionmedicinemodel_table VALUES (2, 1);
INSERT INTO prescriptionmedicinemodel_table VALUES (3, 1);

INSERT INTO employeeappointmentmodel_table VALUES (1, 1);
INSERT INTO employeeappointmentmodel_table VALUES (2, 3);
INSERT INTO employeeappointmentmodel_table VALUES (3, 2);

INSERT INTO diagnosisappointmentmodel_table VALUES (1, 2);
INSERT INTO diagnosisappointmentmodel_table VALUES (2, 2);
INSERT INTO diagnosisappointmentmodel_table VALUES (3, 1);

INSERT INTO diagnosispatientmodel_table VALUES (1, 1);
INSERT INTO diagnosispatientmodel_table VALUES (2, 2);
INSERT INTO diagnosispatientmodel_table VALUES (3, 3);

INSERT INTO diagnosismedicinemodel_table VALUES (1, 3);
INSERT INTO diagnosismedicinemodel_table VALUES (2, 3);
INSERT INTO diagnosismedicinemodel_table VALUES (2, 2);

INSERT INTO hospitalemployeemodel_table VALUES (1, 1);
INSERT INTO hospitalemployeemodel_table VALUES (2, 1);
INSERT INTO hospitalemployeemodel_table VALUES (3, 1);

INSERT INTO surgerynursemodel_table VALUES (1, 3);
INSERT INTO surgerynursemodel_table VALUES (2, 1);
INSERT INTO surgerynursemodel_table VALUES (3, 1);

INSERT INTO departmentemployeemodel_table VALUES (1, 3);
INSERT INTO departmentemployeemodel_table VALUES (2, 1);
INSERT INTO departmentemployeemodel_table VALUES (3, 2);