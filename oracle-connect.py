import oracledb

connection = oracledb.connect(
    user='sys',
    password='testpassword',
    host='localhost',
    sid='FREE',
    mode=oracledb.AUTH_MODE_SYSDBA
)

print(connection.instance_name)

cursor = connection.cursor()


def check_table_exists():
    cursor.execute("""
        create table if not exists training_data (
        name varchar(100),
        street varchar(200),
        no number
        )
    """)


def select(street):
    got_user_data = cursor.execute('select name, street, no from training_data where street=:1', [street])
    return got_user_data


def insert(user_data):
    check_table_exists()
    if isinstance(user_data, list):
        cursor.executemany("""
        insert into training_data (name, street, no) values (:1, :2, :3)""", user_data)
    else:
        cursor.execute("""
            insert into training_data (name, street, no) values (:1, :2, :3)""",
                       ('john', 'abc', 1)
                       )
    connection.commit()


johns = []

# generate test data
for i in range(100):
    johns.append(('john{}'.format(i), 'abc', i))

# insert generated bulk data
insert(johns)

# insert one entry
insert(('john', 'abc', 1))

# selecting and displaying all the entries with address abc
for selected_user_data in select('abc'):
    print(selected_user_data[0], selected_user_data[1], selected_user_data[2])
