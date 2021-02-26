BEGIN {
    # init the varibles for counting
    packet_drop1 = 0;
    packet_sent1 = 0;
    packet_drop2 = 0;
    packet_sent2 = 0;
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

if (source_node=="0" && flow_type=="tcp" && net_action=="+") {
    packet_sent1++;
}

if (source_node=="1" && flow_type=="tcp" && net_action=="+") {
    packet_sent2++;
}

if (flow_id=="1" && flow_type=="tcp" && net_action == "d"){
    packet_drop1++;
}

if (flow_id=="2" && flow_type=="tcp" && net_action == "d"){
    packet_drop2++;
}

}

END {
    printf(packet_drop1/packet_sent1);
    printf("\n");
    printf(packet_drop2/packet_sent2);
    printf("\n");
    #printf(packet_drop);
}
