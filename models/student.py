from odoo import models, fields, api


class Student(models.Model):
    _name = 'academy.student'
    _description = 'Academy: Student Model'

    first_name = fields.Char(string='FirstName')
    last_name = fields.Char(string='LastName')
    major = fields.Char(string='Major')
    arrears = fields.Boolean()
    grade = fields.Char(default='-')
    advisor = fields.Many2one('res.partner', string='Advisor')
    course_ids = fields.One2many('academy.course', 'student', string='Course')
    course_count = fields.Integer(string='Course Count', compute='get_course_count')

    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')],
                              string='Status',
                              default='active')

    def get_course_count(self):
        self.course_count = len(self.course_ids)

    def set_active(self):
        self.status = 'active'

    def set_inactive(self):
        self.status = 'inactive'
        template_id = self.env.ref('academy_module.student_email_template').id
        print(f"Template ID: {template_id}")
        if template_id:
            email_template = self.env['mail.template'].browse(template_id)
            print(f"Email Template: {email_template}")
            email_template.send_mail(self.id, force_send=True,
                                   raise_exception=True,
                                   email_values={'email_to':self.advisor.email})


class Course(models.Model):
    _name = 'academy.course'
    _description = 'Academy: Course Model'

    name = fields.Char(string='Course Name')
    student = fields.Many2one('academy.student', string='Student')
    course_sequence = fields.Char(string='Sequence')

    @api.model
    def create(self, vals_list):
        print(f"Inside the create method of {self._name} that's being overridden")
        print(f"Values: {vals_list}")
        print(vals_list['name'])
        vals_list['course_sequence'] = self.env['ir.sequence'].next_by_code('course.sequence')
        result = super(Course, self).create(vals_list)
        return result

    def write(self, vals):
        print(f"Inside the write method of {self._name} that's being overridden")
        result = super(Course, self).write(vals)
        return result

    def unlink(self):
        print("Inside the unlink method that's being overridden")
        result = super(Course, self).unlink()
        return result

