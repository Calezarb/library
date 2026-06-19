# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"
    _order = "name"

    name = fields.Char(
        string="Name",
        required=True,
    )

    _sql_constraints = [
        ("name_uniq",
         "unique(name)",
         "A category with this name already exists!"
        ),
    ]
