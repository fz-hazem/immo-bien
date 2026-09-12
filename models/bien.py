from odoo import fields, models

class Bien(models.Model):
    _name = "immo.bien"
    _description = "Bien immobilier"

    name = fields.Char(string="Titre", required=True)
    reference = fields.Char(string="Référence", required=True)
    prix_demande = fields.Float(string="Prix demandé", required=True)
    prix_vente = fields.Float(string="Prix de vente")
    surface = fields.Integer(string="Surface (m²)")
    etat = fields.Selection([
        ("dispo", "Disponible"),
        ("offre", "Offre reçue"),
        ("vendu", "Vendu"),
    ], default="dispo")