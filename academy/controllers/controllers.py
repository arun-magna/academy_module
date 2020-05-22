# -*- coding: utf-8 -*-
# from odoo import http


# class academy_module(http.Controller):
#     @http.route('/academy_module/academy_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy_module/academy_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy_module.listing', {
#             'root': '/academy_module/academy_module',
#             'objects': http.request.env['academy_module.academy_module'].search([]),
#         })

#     @http.route('/academy_module/academy_module/objects/<model("academy_module.academy_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy_module.object', {
#             'object': obj
#         })
