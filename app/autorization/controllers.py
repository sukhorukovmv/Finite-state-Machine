from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, request, logging, jsonify
from functools import wraps

module = Blueprint('autorization', __name__)
