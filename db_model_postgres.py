from start import db


class Link(db.Model):
	dino_link = db.Column(db.String(200), primary_key = True)
	website = db.Column(db.String(200))

	def __init__(self, website, dino_link):
		self.website = website
		self.dino_link

	def set_link(website, dino_link):
		new_link = Link(website, dino_link)
		db.session.add(link)
		db.session.commit()

	def get_link(short_link):
		return Link.query.filter_by(dino_link = short_link).first()
