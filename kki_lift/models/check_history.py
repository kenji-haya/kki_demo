from odoo import models, fields, api
from datetime import datetime


class kki_lift_check_history(models.Model):
    _name = 'kki_lift.history'
    _description = 'kki_lift.history'

    name = fields.Char("name")
    check_date = fields.Date("check date", required="True", default=datetime.today())
    lift_id = fields.Many2one("kki_lift.lift", "Forklift")
    image = fields.Binary('image')
    fork_1 = fields.Boolean('[フォーク］亀裂や曲がりがないか')
    back_1 = fields.Boolean('[バックレスト］亀裂や曲がりがないか')
    chain_1 = fields.Boolean('[チェーン］亀裂や曲がりがないか')
    mast_1 = fields.Boolean('[マスト］亀裂や曲がりがないか')
    tire_1 = fields.Boolean('[タイヤ］亀裂や曲がりがないか')
    handle_1 = fields.Boolean('[ハンドル］亀裂や曲がりがないか')
    handle_2 = fields.Boolean('[ハンドル] 著しい遊びまたはガタツキがないか')
    break_1 = fields.Boolean('[ブレーキペダル] ブレーキの効きが充分か')
    horn_1 = fields.Boolean('[ホーン・バックブザー] 正常か')
    volt_meter_1 = fields.Boolean('[ボルトメーター 規定量か')
    cooling_water = fields.Boolean('[冷却水] 規定量か。水がこぼれていないか')
    oil_1 = fields.Boolean('[油] 規定量か。油は落ちていないか')
    battery = fields.Boolean('[バッテリー] 規定量か。バッテリー液がこぼれていないか')


