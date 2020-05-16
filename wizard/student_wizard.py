
from odoo import models, fields, api, _

class StudentWizard(models.TransientModel):
    _name = 'student.wizard'
    _description = 'Student Wizard'

    grade = fields.Char()

    def set_grade(self):
        print("In set_grade() method...")
        print('Student', self.env.context)
        student_id = self.env.context.get('active_id')

        self.env['academy.student'].browse(student_id).write({'grade': self.grade})
