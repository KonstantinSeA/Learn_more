db_name = input()
global_init(db_name)
session = create_session()
for user in session.query(User).filter(User.address == 'module_1',
                                       User.speciality.notlike('%engineer%'),
                                       User.position.notlike('%engineer%')):
    print(user.id)
