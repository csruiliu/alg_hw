BEGIN {
    # init the varibles for counting
    recv_size = 0
    trans_size = 0
    start_time = 1.0
    end_time = 0
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
    recv_size += packet_size;
    end_time = net_time
}
}

END {
    th = (recv_size*8)/(end_time - start_time)/1000000;
    printf(th"\n");
    #printf(end_time)
    #printf("\n")
    #printf(packet_drop);
}