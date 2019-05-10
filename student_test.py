from students import *
import consts


def test_student():
    factory = giveStudentFacroty('Bot', 'DIHT', 2)
    student = factory.createUnit()
    assert student.faculty == 'DIHT'
    assert type(student.intelect) == int
    assert type(student.friendliness) == int
    assert type(student.luck) == int
    assert type(student.oratory) == int
    assert student.sex in ('man', 'not man')


for i in range(10000):
    test_student()
