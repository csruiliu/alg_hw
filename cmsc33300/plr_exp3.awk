BEGIN {
    # init the varibles for counting
    packet_drop = 0;
    packet_sent = 0;
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

if (flow_id=="1" && source_node=="2" && end_node=="3" && net_action=="+") {
    packet_sent++;
}

if (flow_id=="1" && net_action=="d"){
    packet_drop++;
}
}

END {
    printf(packet_drop/packet_sent);
    printf("\n")
    #printf(packet_drop);
}
