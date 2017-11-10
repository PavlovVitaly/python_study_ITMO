from flask import (
    request, redirect, url_for, render_template
)
from pony.orm import db_session

from . import app
from .forms import CustomerForm
from .models import Customer


@app.route('/customer/register', methods=['GET', 'POST'])
def customer_register():
    form = CustomerForm(request.form)

    if form.validate_on_submit():
        with db_session:
            customer = Customer(email=form.email.data,
                                pasword=form.pasword.data,
                                name=form.name.data,
                                country=form.country.data,
                                address=form.address.data)
        return redirect(url_for('customer_show', customer_id=customer.id))

    return render_template('customer/register.html', form=form)


@app.route('/customer/<int:customer_id>')
def customer_show(customer_id):
    return 'Покупатель с ID {}'.format(customer_id)
