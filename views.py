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

@app.route('/surgery_types', methods=['GET'])
def surgery_types():
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