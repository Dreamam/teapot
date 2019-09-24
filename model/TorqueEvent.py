# coding:utf-8


# 定义解析等号
def parse_equal(line):
    tokens = line.split("=")
    if 2 == len(tokens):
        tmp_dict = {tokens[0]: tokens[1]}
        return tmp_dict


# 添加前缀
def parse_equal_prefix(line, prefix):
    tokens = line.split("=")
    if 2 == len(tokens):
        tmp_dict = {prefix + tokens[0]: tokens[1]}
        return tmp_dict


# 资源列表前缀名
PREFIX = "Resource_List."


class TorqueEventFormat:
    # 用户名
    user = ''
    # 用户组名
    group = ''
    # 作业名
    job_name = ''
    # 队列名
    queue = ''
    # 作业提交时间
    c_time = 0
    # 作业开始排队时间
    q_time = 0
    # 作业排队结束时间
    e_time = 0
    # 作业开始执行时间
    start = 0
    # 作业拥有者
    owner = ''
    # 作业执行节点信息
    exec_host = ''
    # 资源申请列表-需要的节点数
    Resource_List_need_nodes = 0
    # 资源申请列表-需要的核数/节点
    Resource_List_need_ppn = 0
    # 资源列表-
    Resource_List_node_ct = 0
    # 资源列表 - 节点数
    Resource_List_nodes = 0
    # 资源列表 - 核数/节点
    Resource_List_ppn = 0
    # 资源列表 - 执行时长
    Resource_List_wall_time = ''
    # 会话
    session = 0
    # 总执行插槽
    total_execution_slots = 0
    # 独立节点数
    unique_node_count = 0
    # 作业结束时间
    end = 0
    # 作业结束状态
    Exit_status = 0
    # 资源使用 - CPU内核使用时间最大值
    resources_used_cpu_t = 240
    # 资源使用 - 能用使用
    resources_used_energy_used = 0
    # 资源使用 - 内存使用 kb
    resources_used_mem = ''
    # 资源使用 - 虚拟内存使用 kb
    resources_used_v_mem = ''
    # 资源使用 - 作业时间执行时长
    resources_used_wall_time = ''

    # 定义构造函数
    def __init__(self, event_detail):
        self.__parse__(event_detail)

    # 定义解析函数
    def __parse__(self, event_detail):
        event_dict = self.__convert_to_dict__(event_detail)
        if 'user' in event_dict.keys():
            self.user = event_dict['user']
        if 'group' in event_dict.keys():
            self.group = event_dict['group']
        if 'jobname' in event_dict.keys():
            self.job_name = event_dict['jobname']
        if 'queue' in event_dict.keys():
            self.queue = event_dict['queue']
        if 'ctime' in event_dict.keys():
            self.c_time = event_dict['ctime']
        if 'qtime' in event_dict.keys():
            self.q_time = event_dict['qtime']
        if 'etime' in event_dict.keys():
            self.e_time = event_dict['etime']
        if 'start' in event_dict.keys():
            self.start = event_dict['start']
        if 'owner' in event_dict.keys():
            self.owner = event_dict['owner']
        if 'exec_host' in event_dict.keys():
            self.exec_host = event_dict['exec_host']
        if 'Resource_List.neednodes' in event_dict.keys():
            self.Resource_List_need_nodes = event_dict['Resource_List.neednodes']
        if 'Resource_List.needppn' in event_dict.keys():
            self.Resource_List_need_ppn = event_dict['Resource_List.needppn']
        if 'Resource_List.nodect' in event_dict.keys():
            self.Resource_List_node_ct = event_dict['Resource_List.nodect']
        if 'Resource_List.nodes' in event_dict.keys():
            self.Resource_List_node_ct = event_dict['Resource_List.nodes']
        if 'Resource_List.ppn' in event_dict.keys():
            self.Resource_List_ppn = event_dict['Resource_List.ppn']
        if 'Resource_List.walltime' in event_dict.keys():
            self.Resource_List_wall_time = event_dict['Resource_List.walltime']
        if 'session' in event_dict.keys():
            self.session = event_dict['session']
        if 'total_execution_slots' in event_dict.keys():
            self.total_execution_slots = event_dict['total_execution_slots']
        if 'unique_node_count' in event_dict.keys():
            self.unique_node_count = event_dict['unique_node_count']
        if 'end' in event_dict.keys():
            self.end = event_dict['end']
        if 'Exit_status' in event_dict.keys():
            self.Exit_status = event_dict['Exit_status']
        if 'resources_used.cput' in event_dict.keys():
            self.resources_used_cpu_t = event_dict['resources_used.cput']
        if 'resources_used.energy_used' in event_dict.keys():
            self.resources_used_energy_used = event_dict['resources_used.energy_used']
        if 'resources_used.mem' in event_dict.keys():
            self.resources_used_mem = event_dict['resources_used.mem']
        if 'resources_used.vmem' in event_dict.keys():
            self.resources_used_v_mem = event_dict['resources_used.vmem']
        if 'resources_used.walltime' in event_dict.keys():
            self.resources_used_wall_time = event_dict['resources_used.walltime']

    def __convert_to_dict__(self, event_detail):
        split_tokens = event_detail.split(" ")
        # print(split_tokens)
        event_dict = {}
        for token in split_tokens:
            tmp_tokens = token.split("=")
            # print(tmp_tokens)
            if len(tmp_tokens) == 2:
                # print(tmp_tokens[0] + " : ", tmp_tokens[1])
                event_dict[tmp_tokens[0]] = tmp_tokens[1]
            if len(tmp_tokens) == 3:
                if self.__parse_nodes_ppn__(token):
                    event_dict.update(self.__parse_nodes_ppn__(token))
                    # print(tmp_tokens[2])
        return event_dict

    # 定义解析节点数和核数的函数
    def __parse_nodes_ppn__(self, resource_nodes_ppn):
        node_ppn_dict = {}
        tokens = resource_nodes_ppn.split(":")
        if 2 == len(tokens):
            tmp_dict_1 = parse_equal(tokens[0])
            node_ppn_dict.update(tmp_dict_1)
            if 'need' in tokens[0]:
                tmp_dict_2 = parse_equal_prefix(tokens[1], PREFIX + 'need')
                node_ppn_dict.update(tmp_dict_2)
            else:
                tmp_dict_2 = parse_equal_prefix(tokens[1], PREFIX)
                node_ppn_dict.update(tmp_dict_2)
            return node_ppn_dict
