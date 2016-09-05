# coding: utf-8
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from datetime import date
from datetime import datetime
from openerp.report import report_sxw
from openerp.tools.translate import _
from openerp.osv import fields, osv
from openerp import tools

class IslrResCompany(osv.osv):
    _inherit = "res.company"

    #~ def _get_image(self, cr, uid, ids, name, args, context=None):
        #~ result = dict.fromkeys(ids, False)
        #~ for obj in self.browse(cr, uid, ids, context=context):
            #~ result[obj.id] = tools.image_get_resized_images(obj.signature_logo)
            #~ print '********',result
        #~ return result
#~ 
    #~ def _set_image(self, cr, uid, id, name, value, args, context=None):
        #~ return self.write(cr, uid, [id], {'signature_logo': tools.image_resize_image_big(value)}, context=context)

    _columns = {
        'signature_logo': fields.binary("Sello",help="Sello digital de la compañía"),
        #~ 'signature_logo_medium': fields.function(_get_image, fnct_inv=_set_image,
            #~ string="Image (auto-resized to 128x128):", type="binary", multi="_get_image",
            #~ store = {
                #~ 'res.company': (lambda self, cr, uid, ids, c={}: ids, ['signature_logo'], 10),
            #~ }),
        #~ 'signature_logo_small': fields.function(_get_image, fnct_inv=_set_image,
            #~ string="Image (auto-resized to 64x64):", type="binary", multi="_get_image",
            #~ store = {
                #~ 'res.company': (lambda self, cr, uid, ids, c={}: ids, ['signature_logo'], 10),
            #~ }),
    }
