"""
Residencies Blueprint - Handles all residency/visa program routes
"""
from flask import Blueprint

residencies = Blueprint(
    'residencies',
    __name__,
    url_prefix='/residencies',
    template_folder='templates',
    static_folder='static'
)

from . import routes
