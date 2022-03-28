from crypt import methods
from odoo import http, fields, models
from odoo.http import request
import json

class KursiTamuCon(http.Controller):
    @http.route(['/kursitamu','/kursitamu/<int:idnya>'], type='json', auth='public', methods=['GET'], csrf=True)
    def getKursiTamu(self,idnya=None, **kwargs):
        value = []
        if not idnya:
            kursi = request.env['wedding.kursitamu'].search([])
            for k in kursi:
                value.append({  "id": k.id,
                                "namakursi":k.name,
                                "tipe_bahan": k.tipe,
                                "stok_tersedia" : k.stok,
                                "harga_sewa" : k.harga})
            return json.dumps(value)
            
        else:
            kursiid = request.env['wedding.kursitamu'].search([('id','=',idnya)])
            for k in kursiid:
                value.append({  "id": k.id,
                                "namakursi":k.name,
                                "tipe_bahan": k.tipe,
                                "stok_tersedia" : k.stok,
                                "harga_sewa" : k.harga})
            return json.dumps(value)
