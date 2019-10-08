drop database if exists bill;
create database bill;
use bill;

create table if not exists t_log
(
 log_id varchar(255) primary key,
 event_marker varchar(10) not null,
 job_num varchar(64) not null,
 event_detail varchar(2048) not null
 )engine=InnoDB default charset=utf8;

create table if not exists t_event
(
 log_id varchar(255) primary key,
 user varchar(255),
 `group` varchar(255),
 job_name varchar(255),
 queue varchar(255),
 c_time varchar(255),
 q_time varchar(255),
 e_time varchar(255),
 start varchar(255),
 owner varchar(255),
 exec_host varchar(255),
 Resource_List_need_nodes varchar(255),
 Resource_List_need_ppn varchar(255),
 Resource_List_node_ct varchar(255),
 Resource_List_nodes varchar(255),
 Resource_List_ppn varchar(255),
 Resource_List_wall_time varchar(255),
 session varchar(255),
 total_execution_slots varchar(255),
 unique_node_count varchar(255),
 end varchar(255),
 Exit_status varchar(255),
 resources_used_cpu_t varchar(255),
 resources_used_energy_used varchar(255),
 resources_used_mem varchar(255),
 resources_used_v_mem varchar(255),
 resources_used_wall_time varchar(255) 
)engine=InnoDB default charset=utf8;