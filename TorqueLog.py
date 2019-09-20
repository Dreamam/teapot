# coding:utf-8


class TorqueLogFormat:  # Torque日志基本格式实体类
    # 时间戳
    time_stamp = 0

    # 事件标记：
    # A - 系统放弃执行作业
    # C - 作业已设置检查点并保持
    # D - 作业已被删除
    # E - 作业已退出，可能是作业计算完毕退出或中途出错退出
    # Q - 作业已递交或者排队中
    # R - 试图返回作业
    # S - 试图开始一个新作业
    # T - 试图从检查点重启作业
    event_marker = ''

    # 作业号
    job_num = 0

    # 事件详情
    event_detail = ''

    # 定义构造函数
    def __init__(self, per_log):
        self.parse(per_log)

    # 解析每行Torque日志
    def parse(self, per_log):
        tokens = per_log.split(";")
        if len(tokens) == 4:
            self.time_stamp = tokens[0]
            self.event_marker = tokens[1]
            self.job_num = tokens[2]
            self.event_detail = tokens[3]
