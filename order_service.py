from models import Order

def create_order(user_id, amount, notifier, logger, db, user_repository):
    # obtiene el email desde el repositorio recibido (puede ser real, fake o stub)
    email = user_repository.get_user_email(user_id)
    logger.log(f'Creating order for {email}')

    # valida que el monto sea positivo antes de crear la orden
    if amount <= 0:
        raise ValueError("Invalid amount")

    order = Order(user_email=email, amount=amount, status='CREATED')

    # registra la orden en la sesion y la persiste en la base de datos
    db.add(order)
    db.commit()

    notifier.send(email, 'Order created')
    return order
