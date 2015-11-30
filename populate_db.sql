INSERT INTO patientmodel_table
    (pk, name, address, phone, blood_type, height, weight, birthdate) VALUES
    (1, 'Matheus Portela', 'SQN 214 bloco J', '3321-3030', 'A+',
        '1.71', '56.0', '1994-01-11');
INSERT INTO patientmodel_table
    (pk, name, address, phone, blood_type, height, weight, birthdate) VALUES
    (2, 'Ana Bárbara', 'SQN 315 bloco E', '3321-8181', 'A-',
        '1.60', '63.0', '1992-12-07');
INSERT INTO patientmodel_table
    (pk, name, address, phone, blood_type, height, weight, birthdate) VALUES
    (3, 'Harry Potter', 'Gryffindor Dorms', 'Edwiges', 'O+',
        '1.65', '60.0', '1991-07-31');

INSERT INTO surgerytypemodel_table
    (pk, name, specialty, description) VALUES
    (1, 'Catarata', 'Oftalmologia', 'Remoção de catarata');
INSERT INTO surgerytypemodel_table
    (pk, name, specialty, description) VALUES
    (2, 'Cardiovascular', 'Cardiologia', 'Inserção de stent');
INSERT INTO surgerytypemodel_table
    (pk, name, specialty, description) VALUES
    (3, 'AVC', 'Neurologia', 'Intervenção pós-AVC');

INSERT INTO surgerymodel_table
    (pk, surgery_date, patient_pk, employee_pk, surgery_type_pk) VALUES
    (1, '2010-10-10', 1, NULL, 2);
INSERT INTO surgerymodel_table
    (pk, surgery_date, patient_pk, employee_pk, surgery_type_pk) VALUES
    (2, '2011-11-11', 3, NULL, 1);
INSERT INTO surgerymodel_table
    (pk, surgery_date, patient_pk, employee_pk, surgery_type_pk) VALUES
    (3, '2012-12-12', 3, NULL, 3);