from consts import *


def hit1(st, ex, hiter):
    div_subject = 1
    if ex.subject == st.subject:
        div_subject = 0
    if hiter == 'student':
        hit = 5 * div_subject + max(1, st.intelect - ex.knowlege) * (st.luck + max_stat) // max_stat + max(0,
                                                                                                           st.oratory - ex.alcohol_liking) * ex.friendliness // max_stat
        ex.health -= hit
        ex.stats['health'] = ex.health
    else:
        hit = 2 * div_subject + max(0, ex.knowlege - st.intelect) * (max_stat - st.luck) // max_stat + max(0,
                                                                                                           ex.alcohol_liking - st.oratory) * ex.friendliness // max_stat
        st.health -= hit
        st.stats['health'] = st.health


def hit2(st, ex, hiter):
    div_sex = 1
    div_subject = 1
    if self.sex == student.sex:
        div_sex = 0
    if self.subject == student.subject:
        div_subject = 0
    if hiter == 'student':
        hit = max(0,
                  div_subject + div_sex + st.intellect - ex.knowlege + st.luck + st.oratory - ex.alcohol_liking + ex.friendliness)
        ex.health -= hit
        ex.stats['health'] = ex.health
    else:
        hit = max(0, div_subject + div_sex + ex.knowlege - st.intellect - st.luck +
                  ex.alcohol_liking - st.oratory + ex.friendliness)
        st.health -= hit
        st.stats['health'] = st.health


def hill1(unit1, unit2):
    if unit1.type == unit2.type:
        unit2.health += 3 * unit1.oratory + 2 * unit2.oratory
    elif unit1.type != 'student' and unit2.type != 'student':
        unit2.health += unit1.friendliness + unit2.friendliness
    unit2.stats['health'] = unit2.health
