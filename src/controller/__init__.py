from database.db import Session


def insert_record(obj: any) -> None:
    Session.add(obj)
    Session.commit()


def insert_records(*obj: any) -> None:
    for i in obj:
        Session.add(i)
    Session.commit()


def get_records(query: any) -> list[any]:
    query_result = Session.execute(query).all()
    result = []

    for i in query_result:
        result.append(i[0])

    return result


def get_one_record(query: any) -> any:
    result = Session.execute(query).first()

    if result:
        return result[0]
    else:
        return None
