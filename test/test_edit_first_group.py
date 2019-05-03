from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="111", header="111", footer="111"))
    app.group.edit_first_group()
