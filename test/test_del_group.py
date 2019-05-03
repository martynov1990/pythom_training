from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="111", header="111", footer="111"))
    app.group.delete_first_group()
