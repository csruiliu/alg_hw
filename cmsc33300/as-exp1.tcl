set ns [new Simulator]

set tcpvar1 [lindex $argv 0]
set tcpvar2 [lindex $argv 1]
set cbrrate [lindex $argv 2]

#set nf [open as_out.nam w]
#$ns namtrace-all $nf

set tf [open as_out.tr w]
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
$ns duplex-link $n2 $n3 10Mb 10ms DropTail
$ns duplex-link $n0 $n2 10Mb 10ms DropTail
$ns duplex-link $n1 $n2 10Mb 10ms DropTail
$ns duplex-link $n3 $n4 10Mb 10ms DropTail
$ns duplex-link $n3 $n5 10Mb 10ms DropTail

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
set sink1 [new Agent/TCPSink]
$ns attach-agent $n4 $sink1
$ns connect $tcp1 $sink1

#create tcp2, attach agenet to n1 and sink at n5
set tcp2 [new Agent/TCP/$tcpvar2]
$tcp2 set fid_ 2
$ns attach-agent $n1 $tcp2
set sink2 [new Agent/TCPSink]
$ns attach-agent $n5 $sink2
$ns connect $tcp2 $sink2

#create ftp1 as traffic for tcp1
set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1
$ftp1 set type_ FTP

#create ftp2 as traffic for tcp2
set ftp2 [new Application/FTP]
$ftp2 attach-agent $tcp2
$ftp2 set type_ FTP

#create udp1, attach agenet to n2 and sink at n3
set udp1 [new Agent/UDP]
$ns attach-agent $n2 $udp1
set null1 [new Agent/Null] 
$ns attach-agent $n3 $null1
$ns connect $udp1 $null1

#create CBR as the traffic for udp1
set cbr1 [new Application/Traffic/CBR]
$cbr1 attach-agent $udp1
$cbr1 set packet_size_ 1000
$cbr1 set rate_ $cbrrate
$cbr1 set random_ false

$ns at 1.0 "$ftp1 start"
$ns at 100.0 "$ftp1 stop"

$ns at 1.0 "$ftp2 start"
$ns at 100.0 "$ftp2 stop"

$ns at 1.0 "$cbr1 start"
$ns at 100.0 "$cbr1 stop"

$ns at 100.1 "finish"
$ns run