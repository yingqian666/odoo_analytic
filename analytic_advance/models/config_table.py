import logging
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class ConfigTable(models.Model):
    _name = "field.config.table"

    model_name = fields.Many2one('ir.model',string="系统模型")
    field_name = fields.Many2one('ir.model.fields',string="系统字段",domain="[('model_id','=',model_name)]")
    name = fields.Char(string="自定义字段名称")

    @api.onchange("field_name")
    def _onchange_field_name(self):
        for recond in self:
            if recond.model_name and recond.field_name:
                recond.name = recond.model_name.name + '-' + recond.field_name.name
