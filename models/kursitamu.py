from odoo import api, fields, models

class KursiTamu(models.Model):
    _name = 'wedding.kursitamu'
    _description = 'Data Tentang Kursi Tamu Dan Harganya'

    name = fields.Char(string='Name')
    tipe = fields.Selection(string='Tipe Kursi', 
    selection=[('plastik','Plastik'), ('stainles','Stainles')])
    stok = fields.Integer(string='Stok Kursi')
    harga = fields.Integer(string='Harga Sewa Per Unit')
    
