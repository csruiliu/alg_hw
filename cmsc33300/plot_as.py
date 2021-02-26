import matplotlib.pyplot as plt
import numpy as np

def plot_plr_single():
    outpath = '/home/ruiliu/Development/NSD-Homework/exp2-plr.pdf'
    cbr = np.arange(1,11,1)
    plr_reno = [0, 0, 0, 0, 0, 0, 0, 0, 0.0238724, 0.127984]
    plr_newreno = [0, 0, 0, 0, 0, 0, 0, 0, 0.0234083, 0.134126]
    plr_vegas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.108216]
    
    plt.figure(figsize=(5, 3.4), dpi=100)
    plt.plot(cbr, plr_reno, marker='^', markersize=6, linewidth=2, linestyle=':', label='Reno')
    plt.plot(cbr, plr_newreno, marker='o', markersize=5, linewidth=1.5,  label='NewReno')
    plt.plot(cbr, plr_vegas, marker='*', markersize=8, linewidth=1.5, linestyle='--', label='Vegas')
    plt.tick_params(axis='y',direction='in',labelsize=16) 
    plt.tick_params(axis='x',direction='in',bottom='False',labelsize=16)
    plt.xticks(np.arange(1,11,1))
    plt.yticks(np.arange(0,0.2,0.05))
    plt.xlabel('CBR (Mbps)', fontsize=18)
    plt.ylabel('Average Packet Loss Rate \n (Number of packets lost per second)', fontsize=11)
    plt.legend(fontsize=14)
    plt.grid(linestyle='--')
    plt.tight_layout()
    plt.savefig(outpath, format='pdf', bbox_inches='tight', pad_inches=0.05)

def plot_tp_single():
    outpath = '/home/ruiliu/Development/NSD-Homework/exp2-tp.pdf'
    cbr = np.arange(1,11,1)
    plr_reno = [2.64941, 2.6494, 2.6494, 2.64927, 2.64927, 2.64926, 2.64071, 1.99735, 0.956125, 0.263341]
    plr_newreno = [2.64941, 2.6494, 2.6494, 2.64927, 2.64695, 2.64926, 2.64071, 1.99735, 1.00444, 0.263017]
    plr_vegas = [2.54871, 2.54389, 2.54385, 2.54384, 2.54673, 2.54361, 2.53533, 1.99369, 0.99968, 0.199109]
    
    plt.figure(figsize=(5, 3.4), dpi=100)
    
    plt.plot(cbr, plr_reno, marker='^', markersize=6, linewidth=2, linestyle=':', label='Reno')
    plt.plot(cbr, plr_newreno, marker='o', markersize=5, linewidth=1.5,  label='NewReno')
    plt.plot(cbr, plr_vegas, marker='*', markersize=8, linewidth=1.5, linestyle='--', label='Vegas')
    plt.tick_params(axis='y',direction='in',labelsize=16) 
    plt.tick_params(axis='x',direction='in',bottom='False',labelsize=16)
    plt.xticks(np.arange(1,11,1))
    plt.yticks([0,1,2,3],('0','1','2','3'))
    plt.xlabel('CBR (Mbps)', fontsize=18)
    plt.ylabel('Average Packet Loss Rate \n (Number of packets lost per second)', fontsize=11)
    plt.legend(fontsize=14)
    plt.grid(linestyle='--')
    plt.tight_layout()
    plt.savefig(outpath, format='pdf', bbox_inches='tight', pad_inches=0.05)

def plr_reno_reno():
    outpath = '/home/ruiliu/Development/NSD-Homework/exp1-plr-reno-reno.pdf'
    cbr = np.arange(1,11,1)
    plr_reno1 = [0, 0, 0, 0, 0, 0, 0, 0.00897049, 0.044403, 0.531304]
    plr_reno2 = [0, 0, 0, 0, 0, 0, 0, 0.00751701, 0.0481184, 0.261469]
    
    plt.figure(figsize=(5, 3.4), dpi=100)
    plt.plot(cbr, plr_reno1, marker='^', markersize=6, linewidth=2, linestyle=':', label='Reno N0-N4')
    plt.plot(cbr, plr_reno2, marker='o', markersize=5, linewidth=1.5,  label='Reno N1-N5')
    plt.tick_params(axis='y',direction='in',labelsize=16) 
    plt.tick_params(axis='x',direction='in',bottom='False',labelsize=16)
    plt.xticks(np.arange(1,11,1))
    plt.yticks(np.arange(0,0.5,0.1))
    plt.xlabel('CBR (Mbps)', fontsize=18)
    plt.ylabel('Average Packet Loss Rate \n (Number of packets lost per second)', fontsize=11)
    plt.legend(fontsize=14)
    plt.grid(linestyle='--')
    plt.tight_layout()
    plt.savefig(outpath, format='pdf', bbox_inches='tight', pad_inches=0.05)

def plr_newreno_reno():
    outpath = '/home/ruiliu/Development/NSD-Homework/exp1-plr-newreno-reno.pdf'
    cbr = np.arange(1,11,1)
    plr_reno1 = [0, 0, 0, 0, 0, 0, 0, 0.000706964, 0.0437622, 0.464286]
    plr_reno2 = [0, 0, 0, 0, 0, 0, 0, 0.0301353, 0.0494973, 0.128707]
    
    plt.figure(figsize=(5, 3.4), dpi=100)
    plt.plot(cbr, plr_reno1, marker='^', markersize=6, linewidth=2, linestyle=':', label='New Reno N0-N4')
    plt.plot(cbr, plr_reno2, marker='o', markersize=5, linewidth=1.5,  label='Reno N1-N5')
    plt.tick_params(axis='y',direction='in',labelsize=16) 
    plt.tick_params(axis='x',direction='in',bottom='False',labelsize=16)
    plt.xticks(np.arange(1,11,1))
    plt.yticks(np.arange(0,0.7,0.1))
    plt.xlabel('CBR (Mbps)', fontsize=18)
    plt.ylabel('Average Packet Loss Rate \n (Number of packets lost per second)', fontsize=11)
    plt.legend(fontsize=14)
    plt.grid(linestyle='--')
    plt.tight_layout()
    plt.savefig(outpath, format='pdf', bbox_inches='tight', pad_inches=0.05)

def plr_vegas_vegas():
    outpath = '/home/ruiliu/Development/NSD-Homework/exp1-plr-vegas-vegas.pdf'
    cbr = np.arange(1,11,1)
    plr_reno1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.110393]
    plr_reno2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.18799]
    
    plt.figure(figsize=(5, 3.4), dpi=100)
    plt.plot(cbr, plr_reno1, marker='^', markersize=6, linewidth=2, linestyle=':', label='Vegas N0-N4')
    plt.plot(cbr, plr_reno2, marker='o', markersize=5, linewidth=1.5,  label='Vegas N1-N5')
    plt.tick_params(axis='y',direction='in',labelsize=16) 
    plt.tick_params(axis='x',direction='in',bottom='False',labelsize=16)
    plt.xticks(np.arange(1,11,1))
    plt.yticks(np.arange(0,0.7,0.1))
    plt.xlabel('CBR (Mbps)', fontsize=18)
    plt.ylabel('Average Packet Loss Rate \n (Number of packets lost per second)', fontsize=11)
    plt.legend(fontsize=14)
    plt.grid(linestyle='--')
    plt.tight_layout()
    plt.savefig(outpath, format='pdf', bbox_inches='tight', pad_inches=0.05)

def plr_newreno_vegas():
    outpath = '/home/ruiliu/Development/NSD-Homework/exp1-plr-newreno-vegas.pdf'
    cbr = np.arange(1,11,1)
    plr_reno1 = [0, 0, 0, 0, 0, 0, 0, 0.000252653, 0.0198885, 0.134353]
    plr_reno2 = [0, 0, 0, 0, 0, 0, 0, 0.000950119, 0.0174825, 0.368421]
    
    plt.figure(figsize=(5, 3.4), dpi=100)
    plt.plot(cbr, plr_reno1, marker='^', markersize=6, linewidth=2, linestyle=':', label='New Reno N0-N4')
    plt.plot(cbr, plr_reno2, marker='o', markersize=5, linewidth=1.5,  label='Vegas N1-N5')
    plt.tick_params(axis='y',direction='in',labelsize=16) 
    plt.tick_params(axis='x',direction='in',bottom='False',labelsize=16)
    plt.xticks(np.arange(1,11,1))
    plt.yticks(np.arange(0,0.7,0.1))
    plt.xlabel('CBR (Mbps)', fontsize=18)
    plt.ylabel('Average Packet Loss Rate \n (Number of packets lost per second)', fontsize=11)
    plt.legend(fontsize=14)
    plt.grid(linestyle='--')
    plt.tight_layout()
    plt.savefig(outpath, format='pdf', bbox_inches='tight', pad_inches=0.05)


def tp_newreno_vegas():
    outpath = '/home/ruiliu/Development/NSD-Homework/exp1-tp-newreno-vegas.pdf'
    cbr = np.arange(1,11,1)
    tp1 = [2.64657, 2.64663, 2.64661, 2.64415, 2.54314, 2.25575, 2.0228, 1.66165, 0.782179, 0.261207]
    tp2 = [2.54099, 2.54085, 2.54067, 2.5387, 2.44149, 1.73466, 0.972229, 0.339762, 0.295004, 0.0104226]
    
    plt.figure(figsize=(5, 3.4), dpi=100)
    plt.plot(cbr, tp1, marker='^', markersize=6, linewidth=2, linestyle=':', label='New Reno N0-N4')
    plt.plot(cbr, tp2, marker='o', markersize=5, linewidth=1.5,  label='Vegas N1-N5')
    plt.tick_params(axis='y',direction='in',labelsize=16) 
    plt.tick_params(axis='x',direction='in',bottom='False',labelsize=16)
    plt.xticks(np.arange(1,11,1))
    plt.yticks([0,1,2,3])
    plt.xlabel('CBR (Mbps)', fontsize=18)
    plt.ylabel('Average Throughput (Mbps)', fontsize=14)
    plt.legend(fontsize=14)
    plt.grid(linestyle='--')
    plt.tight_layout()
    plt.savefig(outpath, format='pdf', bbox_inches='tight', pad_inches=0.05)



def tp_reno_reno():
    outpath = '/home/ruiliu/Development/NSD-Homework/exp1-tp-reno-reno.pdf'
    cbr = np.arange(1,11,1)
    tp1 = [2.64228, 2.64228, 2.64226, 2.64224, 2.49415, 1.9964, 1.63454, 0.992893, 0.517005, 0.531304]
    tp2 = [2.64221, 2.64213, 2.64205, 2.64205, 2.49404, 1.99621, 1.6343, 1.05421, 0.518585, 0.261469]
    
    plt.figure(figsize=(5, 3.4), dpi=100)
    plt.plot(cbr, tp1, marker='^', markersize=6, linewidth=2, linestyle=':', label='Reno N0-N4')
    plt.plot(cbr, tp2, marker='o', markersize=5, linewidth=1.5,  label='Reno N1-N5')
    plt.tick_params(axis='y',direction='in',labelsize=16) 
    plt.tick_params(axis='x',direction='in',bottom='False',labelsize=16)
    plt.xticks(np.arange(1,11,1))
    plt.yticks([0,1,2,3])
    plt.xlabel('CBR (Mbps)', fontsize=18)
    plt.ylabel('Average Throughput (Mbps)', fontsize=14)
    plt.legend(fontsize=14)
    plt.grid(linestyle='--')
    plt.tight_layout()
    plt.savefig(outpath, format='pdf', bbox_inches='tight', pad_inches=0.05)

def tp_newreno_reno():
    outpath = '/home/ruiliu/Development/NSD-Homework/exp1-tp-newreno-reno.pdf'
    cbr = np.arange(1,11,1)
    tp1 = [2.64228, 2.64228, 2.64226, 2.64224, 2.49415, 1.9964, 1.63454, 1.66194, 0.61458, 0.531304]
    tp2 = [2.64221, 2.64213, 2.64205, 2.64205, 2.49404, 1.99621, 1.6343, 0.397184, 0.412812, 0.261469]
    
    plt.figure(figsize=(5, 3.4), dpi=100)
    plt.plot(cbr, tp1, marker='^', markersize=6, linewidth=2, linestyle=':', label='New Reno N0-N4')
    plt.plot(cbr, tp2, marker='o', markersize=5, linewidth=1.5,  label='Reno N1-N5')
    plt.tick_params(axis='y',direction='in',labelsize=16) 
    plt.tick_params(axis='x',direction='in',bottom='False',labelsize=16)
    plt.xticks(np.arange(1,11,1))
    plt.yticks([0,1,2,3])
    plt.xlabel('CBR (Mbps)', fontsize=18)
    plt.ylabel('Average Throughput (Mbps)', fontsize=14)
    plt.legend(fontsize=14)
    plt.grid(linestyle='--')
    plt.tight_layout()
    plt.savefig(outpath, format='pdf', bbox_inches='tight', pad_inches=0.05)

def tp_vegas_vegas():
    outpath = '/home/ruiliu/Development/NSD-Homework/exp1-tp-vegas-vegas.pdf'
    cbr = np.arange(1,11,1)
    tp1 = [2.54553, 2.54323, 2.54352, 2.54352, 2.49042, 1.88453, 1.49625, 1.05292, 0.710998, 0.155565]
    tp2 = [2.5454, 2.54303, 2.54279, 2.54277, 2.4902, 2.1019, 1.49539, 0.94373, 0.710386, 0.17573]
    
    plt.figure(figsize=(5, 3.4), dpi=100)
    plt.plot(cbr, tp1, marker='^', markersize=6, linewidth=2, linestyle=':', label='Vegas N0-N4')
    plt.plot(cbr, tp2, marker='o', markersize=5, linewidth=1.5,  label='Vegas N1-N5')
    plt.tick_params(axis='y',direction='in',labelsize=16) 
    plt.tick_params(axis='x',direction='in',bottom='False',labelsize=16)
    plt.xticks(np.arange(1,11,1))
    plt.yticks([0,1,2,3])
    plt.xlabel('CBR (Mbps)', fontsize=18)
    plt.ylabel('Average Throughput (Mbps)', fontsize=14)
    plt.legend(fontsize=14)
    plt.grid(linestyle='--')
    plt.tight_layout()
    plt.savefig(outpath, format='pdf', bbox_inches='tight', pad_inches=0.05)

def tp_queue():
    outpath = '/home/ruiliu/Development/NSD-Homework/exp3-tp.pdf'
    time_slot = np.arange(1,21,1)
    tp_reno_droptail = [1.173440, 1.335520, 1.389547, 1.418640, 1.434432, 1.292427, 1.171977, 1.098280, 1.027093, 0.980128, 0.922793, 0.892347, 0.868505, 0.824297, 0.808725, 0.843460, 0.881939, 0.916142, 0.947183, 0.974704]
    tp_reno_red = [1.173440, 1.273120, 1.309120, 1.333360, 1.359552, 1.224480, 1.106606, 1.032760, 0.969778, 0.928544, 0.877411, 0.851440, 0.812185, 0.791611, 0.765461, 0.780540, 0.813911, 0.844960, 0.872303, 0.899408]
    tp_sack_droptail = [1.173440, 1.335520, 1.389547, 1.418640, 1.434432, 1.299360, 1.193371, 1.105560, 1.040036, 0.985120, 0.942458, 0.905520, 0.874905, 0.848069, 0.821483, 0.856460, 0.894664, 0.928160, 0.958131, 0.985520]
    tp_sack_red = [1.173440, 1.264800, 1.295253, 1.341680, 1.347904, 1.224480, 1.117303, 1.030680, 0.969778, 0.920224, 0.880436, 0.848667, 0.824985, 0.800526, 0.774891, 0.787300, 0.829082, 0.858364, 0.884564, 0.908144]
    
    
    plt.figure(figsize=(8, 3.5), dpi=100)
    plt.plot(time_slot, tp_reno_droptail, marker='^', markersize=4, linewidth=1, linestyle=':', label='Reno-DropTail')
    plt.plot(time_slot, tp_reno_red, marker='o', markersize=4, linewidth=1,  label='Reno-RED')
    plt.plot(time_slot, tp_sack_droptail, marker='*', markersize=4, linewidth=1, linestyle='--', label='SACK-DropTail')
    plt.plot(time_slot, tp_sack_red, marker='+', markersize=4, linewidth=1, linestyle='-.', label='SACK-RED')
    
    x1, y1 = [5, 15], [1.5, 1.5]
    x2, y2 = [5, 5], [1.47, 1.52]
    x3, y3 = [15, 15], [1.47, 1.52]
    
    plt.plot(x1, y1, 'k-')
    plt.plot(x2, y2, 'k-')
    plt.plot(x3, y3, 'k-')
    plt.text(8.1, 1.42, 'CBR flow added', fontsize=12)
    
    plt.tick_params(axis='y',direction='in',labelsize=16) 
    plt.tick_params(axis='x',direction='in',bottom='False',labelsize=16)
    plt.xticks(np.arange(1,21,1))
    plt.yticks(np.arange(0.8,1.6,0.2))
    plt.xlabel('Time (second)', fontsize=18)
    plt.ylabel('Average Throughput (Mbps)', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(linestyle='--')
    plt.tight_layout()
    plt.savefig(outpath, format='pdf', bbox_inches='tight', pad_inches=0.05)


def tp_udp():
    outpath = '/home/ruiliu/Development/NSD-Homework/exp4-tp-udp.pdf'
    time_slot = np.arange(1,21,1)
    udp1_red = [2.16, 2.32, 2.24, 2.1, 2.032, 2.133333, 1.954286, 2.07, 2.053333, 1.944, 1.869091, 1.84, 1.846154, 1.834286, 1.834667, 1.83, 1.887059, 1.844444, 1.818947, 1.816]
    udp2_red = [0, 0.8, 1.2, 1.36, 1.44, 1.493333, 1.68, 1.56, 1.52, 1.44, 1.410909, 1.42, 1.384615, 1.388571, 1.392, 1.395, 1.312941, 1.328889, 1.338947, 1.364]
    udp3_red = [0, 0, 0.146667, 0.37, 0.48, 0.433333, 0.48, 0.54, 0.626667, 0.852, 0.978182, 1.02, 1.064615, 1.088571, 1.096000, 1.11, 1.145882, 1.175556, 1.2, 1.186]

    udp1_droptail = [2.160000,2.320000,2.240000,2.100000,2.016000,1.986667,1.897143,1.800000,1.804444,1.848000,1.934545,1.966667,1.993846,1.954286,1.920000,1.880000,1.854118,1.795556,1.751579,1.716000]
    udp2_droptail = [0.000000,0.800000,1.200000,1.360000,1.440000,1.480000,1.542857,1.640000,1.635556,1.592000,1.563636,1.533333,1.532308,1.560000,1.605333,1.635000,1.661176,1.684444,1.717895,1.736000]
    udp3_droptail = [0.000000,0.000000,0.146667,0.370000,0.504000,0.586667,0.674286,0.730000,0.760000,0.792000,0.760000,0.776667,0.769231,0.791429,0.797333,0.817500,0.825882,0.871111,0.890526,0.912000]


    plt.figure(figsize=(8, 4), dpi=100)
    plt.plot(time_slot, udp1_red, marker='^', color='green', markersize=4, linewidth=1, linestyle=':', label='UDP1-RED')
    plt.plot(time_slot, udp2_red, marker='o', color='green', markersize=4, linewidth=1, linestyle='-.', label='UDP2-RED')
    plt.plot(time_slot, udp3_red, marker='*', color='green', markersize=4, linewidth=1, linestyle='--', label='UDP3-RED')
    
    plt.plot(time_slot, udp1_droptail, marker='^', color='red', markersize=4, linewidth=1, linestyle=':', label='UDP1-DropTail')
    plt.plot(time_slot, udp2_droptail, marker='o', color='red', markersize=4, linewidth=1, linestyle='-.', label='UDP2-DropTail')
    plt.plot(time_slot, udp3_droptail, marker='*', color='red', markersize=4, linewidth=1, linestyle='--', label='UDP3-DropTail')
 
    
    plt.tick_params(axis='y',direction='in',labelsize=16) 
    plt.tick_params(axis='x',direction='in',bottom='False',labelsize=16)
    plt.xticks(np.arange(1,21,1))
    plt.yticks(np.arange(0,2.5,0.4))
    plt.xlabel('Time (0.1 second)', fontsize=18)
    plt.ylabel('Average Throughput (Mbps)', fontsize=14)
    plt.legend(loc='lower right', ncol=2, fontsize=12)
    plt.grid(linestyle='--')
    plt.tight_layout()
    plt.savefig(outpath, format='pdf', bbox_inches='tight', pad_inches=0.05)


def lat_udp():
    outpath = '/home/ruiliu/Development/NSD-Homework/exp4-lat-udp.pdf'
    time_slot = np.arange(1,21,1)
    udp1_red = [0.000083,0.000198,0.000337,0.000510,0.000770,0.001139,0.001280,0.001738,0.001996,0.002108,0.002156,0.002224,0.002320,0.002420,0.002580,0.002768,0.003061,0.003186,0.003311,0.003484]
    udp2_red = [0.000000,0.000108,0.000288,0.000555,0.000879,0.001264,0.001811,0.001923,0.002201,0.002309,0.002374,0.002460,0.002525,0.002660,0.002804,0.002996,0.002996,0.003241,0.003461,0.00370]
    udp3_red = [0.000000,0.000000,0.000076,0.000293,0.000499,0.000592,0.000802,0.001106,0.001462,0.002101,0.002281,0.002403,0.002553,0.002729,0.002923,0.003177,0.003550,0.003904,0.004201,0.004359]

    udp1_droptail = [0.000084,0.000200,0.000340,0.000515,0.000748,0.001083,0.001337,0.001588,0.001996,0.002516,0.003105,0.003643,0.004141,0.004458,0.004775,0.005036,0.005388,0.005502,0.005699,0.005940]
    udp2_droptail = [0.000000,0.000094,0.000251,0.000483,0.000767,0.001115,0.001589,0.002182,0.002553,0.002860,0.003230,0.003496,0.003938,0.004439,0.005006,0.005599,0.006042,0.006631,0.007164,0.007683]
    udp3_droptail = [0.000000,0.000000,0.000095,0.000366,0.000701,0.001153,0.001813,0.002319,0.002823,0.003399,0.003599,0.004182,0.004574,0.005156,0.005661,0.006175,0.006676,0.007588,0.008190,0.008799]


    plt.figure(figsize=(8, 4), dpi=100)
    plt.plot(time_slot, udp1_red, marker='^', color='green', markersize=4, linewidth=1, linestyle=':', label='UDP1-RED')
    plt.plot(time_slot, udp2_red, marker='o', color='green', markersize=4, linewidth=1, linestyle='-.', label='UDP2-RED')
    plt.plot(time_slot, udp3_red, marker='*', color='green', markersize=4, linewidth=1, linestyle='--', label='UDP3-RED')
    
    plt.plot(time_slot, udp1_droptail, marker='^', color='red', markersize=4, linewidth=1, linestyle=':', label='UDP1-DropTail')
    plt.plot(time_slot, udp2_droptail, marker='o', color='red', markersize=4, linewidth=1, linestyle='-.', label='UDP2-DropTail')
    plt.plot(time_slot, udp3_droptail, marker='*', color='red', markersize=4, linewidth=1, linestyle='--', label='UDP3-DropTail')
 
    
    plt.tick_params(axis='y',direction='in',labelsize=16) 
    plt.tick_params(axis='x',direction='in',bottom='False',labelsize=16)
    plt.xticks(np.arange(1,21,1))
    #plt.yticks(np.arange(0,1.1,0.2))
    plt.xlabel('Time (0.1 second)', fontsize=18)
    plt.ylabel('Latency', fontsize=18)
    plt.legend(fontsize=12)
    plt.grid(linestyle='--')
    plt.tight_layout()
    plt.savefig(outpath, format='pdf', bbox_inches='tight', pad_inches=0.05)

if __name__ == "__main__":
    #plot_plr_single()
    #plot_tp_single()
    #plr_reno_reno()
    #plr_newreno_reno()
    #plr_vegas_vegas()
    #plr_newreno_vegas()
    #tp_newreno_vegas()
    #tp_reno_reno()
    #tp_newreno_reno()
    #tp_vegas_vegas()
    #tp_queue()
    tp_udp()
    lat_udp()