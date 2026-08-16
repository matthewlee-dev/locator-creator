def test_create_locator_expects_locator_created():
    # Arrange
    from maya import cmds

    from locatorcreator.example import create_locator

    # Act
    test_loc = create_locator("foo")

    # Assert
    assert cmds.objExists(test_loc)
