# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_galeria_patient(models.Model):
    _name = 'medical.galeria.patient'
    _description = 'medical galeria patient'
    _rec_name = 'medical_galeria_patient'

    nombre = fields.Char()
    fecha = fields.Char()
    fotoantes = fields.Char()
    fotoahora = fields.Char()

   