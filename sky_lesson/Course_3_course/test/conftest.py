# coding=utf8
import pytest
import Course_3_course.run


@pytest.fixture()
def test():
    app = run.app
    return app.test()