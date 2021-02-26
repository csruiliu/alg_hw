BEGIN {
    # init the varibles for counting
    recv_size = 0;
    trans_size = 0;
    start_time = 0;
    j = 0.1;
    for (i=0; i < 20; i++) {
        end_time[i] = j;
        j=j+0.1;
    }
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


if (net_action=="r" && flow_id=="1"){
    for (k = 0; k < 20; k++) {
        if (end_time[k] > net_time) {
            recv_size_store1[k] += packet_size;
        }
    }
}

if (net_action=="r" && flow_id=="2"){
    for (k = 0; k < 20; k++) {
        if (end_time[k] > net_time) {
            recv_size_store2[k] += packet_size;
        }
    }
}


if (net_action=="r" && flow_id=="3"){
    for (k = 0; k < 20; k++) {
        if (end_time[k] > net_time) {
            recv_size_store3[k] += packet_size;
        }
    }
}

}

END {
    for (i=0;i<20;i++) {
        th1 = (recv_size_store1[i]*8)/(end_time[i] - start_time)/1000000;
        th2 = (recv_size_store2[i]*8)/(end_time[i] - start_time)/1000000;
        th3 = (recv_size_store3[i]*8)/(end_time[i] - start_time)/1000000;
        #printf("Time:%f Throughput:%f, %f, %f\n", end_time[i],th1,th2,th3);
        printf("%f,", th3);
    }
    
}