from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, request, logging, jsonify, send_file, send_from_directory
from .models import createGraph, drawGraph
from io import BytesIO
import base64
import re
import os

module = Blueprint('graph', __name__)

@module.route('/_create_picture', methods=['POST'])
def create_picture():
    if request.method == 'POST':
        nodesDictionary = request.get_json()

        drawGraph(createGraph(nodesDictionary))
        #return send_from_directory("images", filename)

        root_dir = os.path.dirname(os.getcwd())
        return send_from_directory(os.path.join(root_dir, 'static', 'img'), 'result.png')
#        send_file('app/static/img/', attachment_filename='result.png')
