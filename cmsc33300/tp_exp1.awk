BEGIN {
    # init the varibles for counting
    recv_size1 = 0
    recv_size2 = 0
    trans_size = 0
    start_time = 1.0
    end_time1 = 0
    end_time2 = 0
}

{
net_action = $1;
net_time = $2;
source_node = $3;
end_node = $4;
flow_type = $5;
packet_size = $6;
flow_id = $8;
source_port = $9;
end_port = $10;
seq_no = $11;
packet_id = $12;


if (flow_id=="1" && net_action == "r" && end_node =="4"){
    recv_size1 += packet_size;
    end_time1 = net_time
}

if (flow_id=="2" && net_action == "r" && end_node =="5"){
    recv_size2 += packet_size;
    end_time2 = net_time
}

}

END {
    th1 = (recv_size1*8)/(end_time1 - start_time)/1000000;
    th2 = (recv_size2*8)/(end_time2 - start_time)/1000000;
    printf(th1"\n");
    printf(th2"\n");
    
    #printf(packet_drop);
}
