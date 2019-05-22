from model.group import Group


def test_edit_first_group(app):
    group = Group(name="", header="", footer="")
    if app.group.count() == 0:
        app.group.create(Group(name="111", header="111", footer="111"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(group)
    group.id = old_groups[0].id
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
