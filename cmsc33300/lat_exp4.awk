BEGIN {
    # init the varibles for counting
    recv_size = 0;
    trans_size = 0;
    start_time = 0;
    packet_counts1 = 0;
    packet_counts2 = 0;
    packet_counts3 = 0;
    l = 0.1;
    for (k=0; k < 20; k++) {
        end_time[k] = l;
        l=l+0.1;
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

for (i=0; i<20; i++) {
    if (end_time[i] > net_time) {
        if (net_action=="+" && flow_id=="1"){
            send_time1[seq_no] = net_time;
        }

        if (net_action=="r" && flow_id=="1") {
            recv_time1[seq_no] = net_time;
            if (recv_time1[seq_no] > send_time1[seq_no]){
                delay1 = recv_time1[seq_no] - send_time1[seq_no]
                packet_counts1++
                total_delay1[i] += delay1
            }  
        }

        if (net_action=="+" && flow_id=="2"){
            send_time2[seq_no] = net_time;
        }

        if (net_action=="r" && flow_id=="2") {
            recv_time2[seq_no] = net_time;
            if (recv_time2[seq_no] > send_time2[seq_no]){
                delay2 = recv_time2[seq_no] - send_time2[seq_no]
                packet_counts2++
                total_delay2[i] += delay2
            }  
        }

        if (net_action=="+" && flow_id=="3"){
            send_time3[seq_no] = net_time;
        }

        if (net_action=="r" && flow_id=="3") {
            recv_time3[seq_no] = net_time;
            if (recv_time3[seq_no] > send_time3[seq_no]){
                delay3 = recv_time3[seq_no] - send_time3[seq_no]
                packet_counts3++
                total_delay3[i] += delay3
            }  
        }
    }
}

}

END {
    for (j=0;j<20;j++) {
        lat1 = total_delay1[j]/packet_counts1;
        lat2 = total_delay2[j]/packet_counts2;
        lat3 = total_delay3[j]/packet_counts3;
        #printf("Time:%f Throughput:%f, %f, %f\n", end_time[j],lat1,lat2,lat3)
        printf("%f,", lat1)
    }
    
}