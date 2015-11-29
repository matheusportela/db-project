#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import traceback

from flask import Flask, request, render_template, Response

import models

app = Flask(__name__)

@app.route('/')
def index_view():
    try:
        return render_template('index.html')
    except:
        return traceback.format_exc()

@app.route('/surgery_types', methods=['GET', 'POST'])
def surgery_types_view():
    if request.method == 'GET':
        try:
            return render_template('surgery_type_create.html')
        except:
            return traceback.format_exc()
    elif request.method == 'POST':
        try:
            st = models.SurgeryTypeModel(
                pk=int(request.form['pk']),
                name=request.form['name'],
                specialty=request.form['specialty'],
                description=request.form['description'])
            st.create()
            response = Response(response='Success', status=200)
            return response
        except:
            return traceback.format_exc()

@app.route('/surgery_type/<int:pk>', methods=['GET', 'PATCH', 'DELETE'])
def surgery_type_view(pk):
    if request.method == 'GET':
        try:
            surgery_type = models.SurgeryTypeModel(pk=pk)
            surgery_type.load()
            return render_template('surgery_type_details.html',
                surgery_type=surgery_type)
        except:
            return traceback.format_exc()
    elif request.method == 'PATCH':
        return 'ECHO: PATCH\n'
    elif request.method == 'DELETE':
        return 'ECHO: DELETE\n'

if __name__ == '__main__':
    app.run()