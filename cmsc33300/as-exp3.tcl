set ns [new Simulator]

set tcpvar1 [lindex $argv 0]
set queuevar1 [lindex $argv 1]

#set nf [open as_out.nam w]
#$ns namtrace-all $nf

set tf [open as_exp3_out.tr w]
$ns trace-all $tf

proc finish {} {
    global ns tf
    $ns flush-trace
    #close $nf
    close $tf
    #exec nam as_out.nam &
    exit 0
}

#create 6 nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]

#create links and form the network topology
$ns duplex-link $n2 $n3 1.5Mb 10ms $queuevar1
$ns duplex-link $n0 $n2 10Mb 10ms $queuevar1
$ns duplex-link $n1 $n2 10Mb 10ms $queuevar1
$ns duplex-link $n3 $n4 10Mb 10ms $queuevar1
$ns duplex-link $n3 $n5 10Mb 10ms $queuevar1

#for better layout 
$ns duplex-link-op $n2 $n3 orient right
$ns duplex-link-op $n0 $n2 orient right-down 
$ns duplex-link-op $n1 $n2 orient right-up 
$ns duplex-link-op $n3 $n4 orient right-up 
$ns duplex-link-op $n3 $n5 orient right-down

#create tcp1, attach agenet to n0 and sink at n4 
set tcp1 [new Agent/TCP/$tcpvar1]
$tcp1 set fid_ 1
$ns attach-agent $n0 $tcp1
if {$tcpvar1=="Sack1"} {
    set sink1 [new Agent/TCPSink/Sack1]
} else {
    set sink1 [new Agent/TCPSink]
}

$ns attach-agent $n4 $sink1
$ns connect $tcp1 $sink1

#create ftp1 as traffic for tcp1
set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1
$ftp1 set packet_size_ 1000
$ftp1 set type_ FTP

#create udp1, attach agenet to n1 and sink at n5
set udp1 [new Agent/UDP]
$udp1 set fid_ 2
$ns attach-agent $n1 $udp1
set null1 [new Agent/Null] 
$ns attach-agent $n5 $null1
$ns connect $udp1 $null1

#create CBR as the traffic for udp1
set cbr1 [new Application/Traffic/CBR]
$cbr1 attach-agent $udp1
$cbr1 set type_ CBR
$cbr1 set packet_size_ 500
$cbr1 set rate_ 1Mb
$cbr1 set random_ false

$ns at 0.0 "$ftp1 start"
$ns at 20.0 "$ftp1 stop"

$ns at 5.0 "$cbr1 start"
$ns at 15.0 "$cbr1 stop"

$ns at 20.1 "finish"
$ns run