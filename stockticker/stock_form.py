from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, PasswordField, SubmitField, BooleanField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class StockForm(FlaskForm): #Inherits from FlaskForm
	
	assetType = SelectField('Type of asset', 
							choices=[('stock', 'Stock'), 
									 ('crypto', 'Crypto'),
									 ('bond', 'Bond',),
									 ('material', 'Raw Material')],
							validate_choice=True
							)
	country = SelectField('Country', choices=["Sweden", "USA"], default=1)
	ticker = SelectField('Ticker', 
							validators=[DataRequired()]
							)
	name = StringField('Name')
	amount = FloatField('Amount owned',
						validators=[DataRequired()]
						)
	datePurchased = DateField('Date purchased (YYYY-MM-DD)',
							 validators=[DataRequired()]
							 )
	submit = SubmitField('Add asset')

