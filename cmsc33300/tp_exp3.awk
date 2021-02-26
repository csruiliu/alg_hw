BEGIN {
    # init the varibles for counting
    recv_size = 0
    trans_size = 0
    start_time = 0
    j = 1
    for (i=0; i < 20; i++) {
        end_time[i] = j
        j++
    }
    
    lastpackettime = 0
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


if (source_node=="0") {
    if (net_action=="+") {
        recv_size += packet_size
    }
}

if (net_action=="r" && end_node=="4" && flow_id=="1"){
    for (k = 0; k < 20; k++) {
        if (end_time[k] > net_time) {
            recv_size_store[k] += packet_size
        }
    }
}


}

END {
    end_time[j] = lastpackettime
    recv_size_store[j] = recv_size
    for (i=0;i<20;i++) {
        th = (recv_size_store[i]*8)/(end_time[i] - start_time)/1000000;
        printf("Time:%f RecvdSize:%f Throughput:%f\n", end_time[i],recv_size_store[i],th)
    }
    
}