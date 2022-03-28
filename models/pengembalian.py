from odoo import api, fields, models

class Pengembalian(models.Model):
    _name = 'wedding.pengembalian'
    _description = 'Pengembalian Barang'

    name = fields.Char(string='Name')    
    order_id = fields.Many2one(comodel_name='wedding.order', string='No Order')
    nama_penyewa = fields.Char(compute='_compute_nama_penyewa', string='Nama Penyewa')
    
    @api.depends('order_id')
    def _compute_nama_penyewa(self):
        for record in self:
            # record.nama_penyewa = self.env['wedding.order'].search([('id', '=', record.order_id.id)]).mapped('pemesan.name').name
            record.nama_penyewa = record.order_id.pemesan.name
    
    tgl_pengembalian = fields.Date(string='', default=fields.Date.today())
    
    tagihan = fields.Char(compute='_compute_tagihan', string='Tagihan')
    
    @api.depends('order_id')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.order_id.total
    
    @api.model
    def create(self,vals):
        record = super(Pengembalian, self).create(vals)
        if record.tgl_pengembalian:
            self.env['wedding.order'].search([('id','=',record.order_id.id)]).write({'sudah_kembali':True})
            self.env["wedding.akunting"].create({'kredit' : record.tagihan, 'name': record.name})
            return record

    def unlink(self):
        for wiku in self:
            self.env['wedding.order'].search([('id','=',wiku.order_id.id)]).write({'sudah_kembali':False})
        record = super(Pengembalian, self).unlink()

     