
import ast

ripeList="ripe-vps"
result="theresult"
falsa="Ghost_VP_ID"
ID_list=[]
finalFile="final_report"
listProbes=[]
infoProbes=[]

def loadprobes():
    temp_list_probes=[]
    temp_information_probes={}

    pathVPs=ripeList

    for line in open(pathVPs,'r').readlines():
        if line.startswith("#"): #skip header and comments
            continue

        hostname,latitude,longitude,country = line.strip().split("\t")
        temp_list_probes.append(hostname)
        temp_information_probes[hostname]=[latitude,longitude,country]
    return (",".join(temp_list_probes),temp_information_probes) #building the list


def retrieveResult(infoProbes,result_data):
        #o status?

        numVpAnswer=0
        numVpFail=0
        totalRtt = 0
        numLatencyresultment = 0
        numVpTimeout = 0
        print result_data
        #result=ast.literal_eval(result_data)
        print("Number of answers: %s" % len(result_data))

        result=result_data
        VP = result["prb_id"]
        print VP
        try:
            ttl=result["ttl"]
        except:
            print result
            ttl=-1
        IO_file=open(str(result["msm_id"]), 'a')
        numVpAnswer += 1
        #result_rtt=dict(result["result"])
        """
        if result["result"].has_key("rtt"):
            totalRtt += int(result["rtt"])
            numLatencyresultment += 1
    #       IO_file.write(str(VP)+"\t"+str(infoProbes[str(VP)][0])+"\t"+str(infoProbes[str(VP)][1])+"\t"+str(result["rtt"])+"\t"+str(ttl)+"\t"+infoProbes[str(VP)][2]+"\n")
            #IO_file.write(str(VP)+"\t"+str(infoProbes[str(VP)][0])+"\t"+str(infoProbes[str(VP)][1])+"\t"+str(result["rtt"])+"\t"+str(ttl)+"\t"+infoProbes[str(VP)][2]+"\n")
            a=infoProbes[infoProbes.keys()[0]]
            print a
            IO_file.write(str(VP)+"\t"+str(infoProbes[a][0])+"\t"+str(infoProbes[a][1])+"\t"+str(result["rtt"])+"\t"+str(ttl)+"\t"+infoProbes[a][2]+"\n")
        """
        #print result["result"][0]
        #print result["result"]
        #print result["result"]["rt"]
        #if result["result"].has_key["rt"]:
        #    print result["result"]["rt"]
        #    print "hola holita"

        if result["result"][0].has_key("rtt"):
            #dict = {k:v for k,v in (x.split(':') for x in result["result"]) }
            #totalRtt += int(result["rtt"])
            numLatencyresultment += 1
    #       IO_file.write(str(VP)+"\t"+str(infoProbes[str(VP)][0])+"\t"+str(infoProbes[str(VP)][1])+"\t"+str(result["rtt"])+"\t"+str(ttl)+"\t"+infoProbes[str(VP)][2]+"\n")
            #IO_file.write(str(VP)+"\t"+str(infoProbes[str(VP)][0])+"\t"+str(infoProbes[str(VP)][1])+"\t"+str(result["rtt"])+"\t"+str(ttl)+"\t"+infoProbes[str(VP)][2]+"\n")
            a=infoProbes[infoProbes.keys()[0]]
            print a
            IO_file.write(str(VP)+"\t"+str(infoProbes[str(VP)][0])+"\t"+str(infoProbes[str(VP)][1])+"\t"+str(result["result"][0]["rtt"])+"\t"+str(ttl)+"\t"+infoProbes[str(VP)][2]+"\n")
            #IO_file.write(str(VP)+"\t"+str(a[0])+"\t"+str(a[1])+"\t"+str(result["result"][0]["rtt"])+"\t"+str(ttl)+"\t"+a[2]+"\n")

        elif result["result"][0].has_key("error"):
            numVpFail += 1
        elif result["result"][0].has_key("x"):
            numVpTimeout += 1
        else:
            print ("Error in the resultment: result has no field rtt, or x or error")
        IO_file.close()
