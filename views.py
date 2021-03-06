#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback

from flask import Flask, request, redirect, render_template

import models

app = Flask(__name__)

@app.route('/')
def index_view():
    try:
        return render_template('index.html')
    except:
        return traceback.format_exc()

###########
# PATIENT #
###########
@app.route('/patients', methods=['GET'])
def patient_view():
    if request.method == 'GET':
        try:
            patient_list = models.PatientModel.all()
            return render_template('patient_list.html',
                patient_list=patient_list)
        except:
            return traceback.format_exc()

@app.route('/patient/create', methods=['GET', 'POST'])
def patients_create_view():
    if request.method == 'GET':
        try:
            return render_template('patient_create.html')
        except:
            return traceback.format_exc()
    elif request.method == 'POST':
        try:
            patient = models.PatientModel(pk=int(request.form['pk']))
            patient.name = request.form['name']
            patient.address = request.form['address']
            patient.phone = request.form['phone']
            patient.blood_type = request.form['blood_type']
            patient.height = float(request.form['height'])
            patient.weight = float(request.form['weight'])
            patient.birthdate = request.form['birthdate']
            patient.create()
            return redirect('/patient/%d' % patient.pk, code=302)
        except:
            return traceback.format_exc()

@app.route('/patient/<int:pk>', methods=['GET'])
def patient_details_view(pk):
    if request.method == 'GET':
        try:
            patient = models.PatientModel(pk=pk)
            patient.load()
            return render_template('patient_details.html',
                patient=patient)
        except:
            return traceback.format_exc()

@app.route('/patient/<int:pk>/edit', methods=['GET', 'POST'])
def patient_edit_view(pk):
    if request.method == 'GET':
        try:
            patient = models.PatientModel(pk=pk)
            patient.load()
            return render_template('patient_edit.html',
                patient=patient)
        except:
            return traceback.format_exc()
    elif request.method == 'POST':
        try:
            patient = models.PatientModel(pk=pk)
            patient.name = request.form['name']
            patient.address = request.form['address']
            patient.phone = request.form['phone']
            patient.blood_type = request.form['blood_type']
            patient.height = float(request.form['height'])
            patient.weight = float(request.form['weight'])
            patient.birthdate = request.form['birthdate']
            patient.save()
            return redirect('/patient/%d' % patient.pk, code=302)
        except:
            return traceback.format_exc()

@app.route('/patient/<int:pk>/delete', methods=['GET'])
def patient_delete_view(pk):
    if request.method == 'GET':
        try:
            patient = models.PatientModel(pk=pk)
            patient.delete()
            return redirect('/patients', code=302)
        except:
            return traceback.format_exc()

#############
# SURGERIES #
#############
@app.route('/surgeries', methods=['GET'])
def surgeries_view():
    if request.method == 'GET':
        try:
            surgery_list = models.SurgeryModel.all()
            return render_template('surgery_list.html',
                surgery_list=surgery_list)
        except:
            return traceback.format_exc()

@app.route('/surgery/create', methods=['GET', 'POST'])
def surgeries_create_view():
    if request.method == 'GET':
        try:
            return render_template('surgery_create.html')
        except:
            return traceback.format_exc()
    elif request.method == 'POST':
        try:
            surgery = models.SurgeryModel(pk=int(request.form['pk']))
            surgery.surgery_date = request.form['surgery_date']
            surgery.patient_pk = int(request.form['patient_pk']) if request.form['patient_pk'] else None
            surgery.surgery_type_pk = int(request.form['surgery_type_pk']) if request.form['surgery_type_pk'] else None
            surgery.general_surgeon_pk = int(request.form['general_surgeon_pk']) if request.form['general_surgeon_pk'] else None
            surgery.co_surgeon_pk = int(request.form['co_surgeon_pk']) if request.form['co_surgeon_pk'] else None
            surgery.assistant_surgeon_pk = int(request.form['assistant_surgeon_pk']) if request.form['assistant_surgeon_pk'] else None
            surgery.inventory_pk = int(request.form['inventory_pk']) if request.form['inventory_pk'] else None
            surgery.create()
            return redirect('/surgery/%d' % surgery.pk, code=302)
        except:
            return traceback.format_exc()

@app.route('/surgery/<int:pk>', methods=['GET'])
def surgery_details_view(pk):
    if request.method == 'GET':
        try:
            surgery = models.SurgeryModel(pk=pk)
            surgery.load()
            return render_template('surgery_details.html',
                surgery=surgery)
        except:
            return traceback.format_exc()

@app.route('/surgery/<int:pk>/edit', methods=['GET', 'POST'])
def surgery_edit_view(pk):
    if request.method == 'GET':
        try:
            surgery = models.SurgeryModel(pk=pk)
            surgery.load()
            return render_template('surgery_edit.html',
                surgery=surgery)
        except:
            return traceback.format_exc()
    elif request.method == 'POST':
        try:
            surgery = models.SurgeryModel(pk=pk)
            surgery.surgery_date = request.form['surgery_date']
            surgery.patient_pk = int(request.form['patient_pk']) if request.form['patient_pk'] else None
            surgery.surgery_type_pk = int(request.form['surgery_type_pk']) if request.form['surgery_type_pk'] else None
            surgery.general_surgeon_pk = int(request.form['general_surgeon_pk']) if request.form['general_surgeon_pk'] else None
            surgery.co_surgeon_pk = int(request.form['co_surgeon_pk']) if request.form['co_surgeon_pk'] else None
            surgery.assistant_surgeon_pk = int(request.form['assistant_surgeon_pk']) if request.form['assistant_surgeon_pk'] else None
            surgery.inventory_pk = int(request.form['inventory_pk']) if request.form['inventory_pk'] else None
            surgery.save()
            return redirect('/surgery/%d' % surgery.pk, code=302)
        except:
            return traceback.format_exc()

@app.route('/surgery/<int:pk>/delete', methods=['GET'])
def surgery_delete_view(pk):
    if request.method == 'GET':
        try:
            surgery = models.SurgeryModel(pk=pk)
            surgery.delete()
            return redirect('/surgeries', code=302)
        except:
            return traceback.format_exc()

#################
# SURGERY TYPES #
#################
@app.route('/surgery_types', methods=['GET'])
def surgery_types_view():
    if request.method == 'GET':
        try:
            surgery_type_list = models.SurgeryTypeModel.all()
            return render_template('surgery_type_list.html',
                surgery_type_list=surgery_type_list)
        except:
            return traceback.format_exc()

@app.route('/surgery_type/create', methods=['GET', 'POST'])
def surgery_types_create_view():
    if request.method == 'GET':
        try:
            return render_template('surgery_type_create.html')
        except:
            return traceback.format_exc()
    elif request.method == 'POST':
        try:
            surgery_type = models.SurgeryTypeModel(
                pk=int(request.form['pk']),
                name=request.form['name'],
                specialty=request.form['specialty'],
                description=request.form['description'])
            surgery_type.create()
            return redirect('/surgery_type/%d' % surgery_type.pk, code=302)
        except:
            return traceback.format_exc()

@app.route('/surgery_type/<int:pk>', methods=['GET'])
def surgery_type_details_view(pk):
    if request.method == 'GET':
        try:
            surgery_type = models.SurgeryTypeModel(pk=pk)
            surgery_type.load()
            return render_template('surgery_type_details.html',
                surgery_type=surgery_type)
        except:
            return traceback.format_exc()

@app.route('/surgery_type/<int:pk>/edit', methods=['GET', 'POST'])
def surgery_type_edit_view(pk):
    if request.method == 'GET':
        try:
            surgery_type = models.SurgeryTypeModel(pk=pk)
            surgery_type.load()
            return render_template('surgery_type_edit.html',
                surgery_type=surgery_type)
        except:
            return traceback.format_exc()
    elif request.method == 'POST':
        try:
            surgery_type = models.SurgeryTypeModel(pk=pk)
            surgery_type.name = request.form['name']
            surgery_type.specialty = request.form['specialty']
            surgery_type.description = request.form['description']
            surgery_type.save()
            return redirect('/surgery_type/%d' % surgery_type.pk, code=302)
        except:
            return traceback.format_exc()

@app.route('/surgery_type/<int:pk>/delete', methods=['GET'])
def surgery_type_delete_view(pk):
    if request.method == 'GET':
        try:
            surgery_type = models.SurgeryTypeModel(pk=pk)
            surgery_type.delete()
            return redirect('/surgery_types', code=302)
        except:
            return traceback.format_exc()

if __name__ == '__main__':
    app.run()