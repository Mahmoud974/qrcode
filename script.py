import pyqrcode

# Informations de contact pour le QR code vCard
nom = "Dupont"
prenom = "Jean"
telephone = "+33123456789"
email = "jean.dupont@example.com"
adresse = "123 Rue de Paris, 75000 Paris, France"
entreprise = "Entreprise XYZ"
site_web = "https://www.entreprisexyz.com"

# Format vCard avec les informations de contact
vcard = f"""
BEGIN:VCARD
VERSION:3.0
FN:{prenom} {nom}
N:{nom};{prenom};;;
ORG:{entreprise}
TEL:{telephone}
EMAIL:{email}
ADR:;;{adresse}
URL:{site_web}
END:VCARD
"""

# Génération du QR code avec les informations de contact
contact_qr = pyqrcode.create(vcard)
contact_qr.png("contact_vcard_qrcode.png", scale=8)

print("QR code généré avec les coordonnées de contact.")
