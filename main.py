import prettytable 

from schedule import Schedule
from genetic import GeneticOptimize


def vis(schedule):
    """visualization Class Schedule.

    Arguments:
        schedule: List, Class Schedule
    """
    col_labels = ['week/slot', '1', '2', '3', '4', '5']
    table_vals = [[i + 1, '', '', '', '', ''] for i in range(5)]

    table = prettytable.PrettyTable(col_labels, hrules=prettytable.ALL)

    for s in schedule:
        weekDay = s.weekDay
        slot = s.slot
        text = 'course: {} \n class: {} \n room: {} \n teacher: {}'.format(s.courseId, s.classId, s.roomId, s.teacherId)
        table_vals[weekDay - 1][slot] = text

    for row in table_vals:
        table.add_row(row)

    print(table)


if __name__ == '__main__':
    schedules = []

    '''
    # add schedule
    schedules.append(Schedule(201, 1201, 11101))
    schedules.append(Schedule(201, 1201, 11101))
    schedules.append(Schedule(202, 1201, 11102))
    schedules.append(Schedule(202, 1201, 11102))
    schedules.append(Schedule(203, 1201, 11103))
    schedules.append(Schedule(203, 1201, 11103))
    schedules.append(Schedule(206, 1201, 11106))
    schedules.append(Schedule(206, 1201, 11106))

    schedules.append(Schedule(202, 1202, 11102))
    schedules.append(Schedule(202, 1202, 11102))
    schedules.append(Schedule(204, 1202, 11104))
    schedules.append(Schedule(204, 1202, 11104))
    schedules.append(Schedule(206, 1202, 11106))
    schedules.append(Schedule(206, 1202, 11106))

    schedules.append(Schedule(203, 1203, 11103))
    schedules.append(Schedule(203, 1203, 11103))
    schedules.append(Schedule(204, 1203, 11104))
    schedules.append(Schedule(204, 1203, 11104))
    schedules.append(Schedule(205, 1203, 11105))
    schedules.append(Schedule(205, 1203, 11105))
    schedules.append(Schedule(206, 1203, 11106))
    schedules.append(Schedule(206, 1203, 11106))
    
    '''

    '''
    # Courses
    201 - ISP688
    202 - ISP611
    203 - ISP623
    204 - TXC501
    205 - ISP610
    206 - CSP600

    # Classes
    1201 - CS2595A
    1202 - CS2595B
    1203 - CS2595C

    # Lecturers
    11101 - Dr Mastura 
    11102 - Dr Zaki
    11103 - Dr Nurzeatul
    11104 - Dr ...
    11105 - Madam Farah
    11106 - Prof Azlinah
    '''
    # add schedule
    schedules.append(Schedule('ISP688', 'CS2595A', 'Dr Mastura'))
    schedules.append(Schedule('ISP688', 'CS2595A', 'Dr Mastura'))
    schedules.append(Schedule('ISP611', 'CS2595A', 'Dr Zaki'))
    schedules.append(Schedule('ISP611', 'CS2595A', 'Dr Zaki'))
    schedules.append(Schedule('ISP623', 'CS2595A', 'Dr Nurzeatul'))
    schedules.append(Schedule('ISP623', 'CS2595A', 'Dr Nurzeatul'))
    schedules.append(Schedule('CSP600', 'CS2595A', 'Prof Azlinah'))
    schedules.append(Schedule('CSP600', 'CS2595A', 'Prof Azlinah'))

    schedules.append(Schedule('ISP611', 'CS2595B', 'Dr Zaki'))
    schedules.append(Schedule('ISP611', 'CS2595B', 'Dr Zaki'))
    schedules.append(Schedule('TXC501', 'CS2595B', 'Dr ...'))
    schedules.append(Schedule('TXC501', 'CS2595B', 'Dr ...'))
    schedules.append(Schedule('CSP600', 'CS2595B', 'Prof Azlinah'))
    schedules.append(Schedule('CSP600', 'CS2595B', 'Prof Azlinah'))

    schedules.append(Schedule('ISP623', 'CS2595C', 'Dr Nurzeatul'))
    schedules.append(Schedule('ISP623', 'CS2595C', 'Dr Nurzeatul'))
    schedules.append(Schedule('TXC501', 'CS2595C', 'Dr ...'))
    schedules.append(Schedule('TXC501', 'CS2595C', 'Dr ...'))
    schedules.append(Schedule('ISP610', 'CS2595C', 'Madam Farah'))
    schedules.append(Schedule('ISP610', 'CS2595C', 'Madam Farah'))
    schedules.append(Schedule('CSP600', 'CS2595C', 'Prof Azlinah'))
    schedules.append(Schedule('CSP600', 'CS2595C', 'Prof Azlinah'))

    # optimization
    ga = GeneticOptimize(popsize=50, elite=10, maxiter=500)
    res = ga.evolution(schedules, 3)

    # visualization
    vis_res = []
    for r in res:
        if r.classId == 'CS2595A':
            vis_res.append(r)
    vis(vis_res)

