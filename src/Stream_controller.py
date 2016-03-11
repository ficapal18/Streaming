
from ripe.atlas.cousteau import AtlasStream
import os, subprocess,time,json
import Handler
import ast






global infoProbes,listProbes,ID_list
ripeList="ripe-vps"
result="theresult"
falsa="Ghost_VP_ID"
ID_list=[]
finalFile="final_report"
listProbes=[]
infoProbes=[]






#st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

question=raw_input("Do you have the ID list? (y/n)")
if question=="n":
    print "Checking IP List"
    FNULL = open(os.devnull, 'w')
    subprocess.call("./program.sh", shell=True,stdout=FNULL,stderr=subprocess.STDOUT)

    print "1st step finished, IDs are available"

file_ip=open(result,"r")
#file_falsa=open(falsa,"r")
ts = time.time()
for i, line in enumerate(file_ip):
    line_parts=line.split("/")
    current_ID=line_parts[-2]
    ID_list.append(current_ID)
    IO_file=open(""+ID_list[i],'a')
    IO_file.write("#hostname	latitude	longitude	rtt[ms]	ttl	country\n")
    #IO_file.write("#hostname	latitude	longitude	country\n")
    IO_file.write("#ripeID measurement:\t"+str(current_ID)+"\n")
    url="https://atlas.ripe.net/api/v1/measurement/"+ID_list[i]+"/result/"
    print url
    IO_file.close()


listProbes,infoProbes=Handler.loadprobes()


def on_result_response(*args):
    """
    Function that will be called every time we receive a new result.
    Args is a tuple, so you should use args[0] to access the real message.
    """
    print args[0]
    #result_data = json.dumps(args[0])
    #result_data=ast.literal_eval(args[0])
    #result_data = json.load(args[0])
    Handler.retrieveResult(infoProbes,args[0])

atlas_stream = AtlasStream()
atlas_stream.connect()
# Measurement results
channel = "result"
# Bind function we want to run with every result message received
atlas_stream.bind_channel(channel, on_result_response)
# Subscribe to new stream for 1001 measurement results
#stream_parameters = {"msm": ID_list,"startTime": ts}
#ID_list.append(1001)
print ID_list

ID_list = map(int, ID_list)
#ID_list=(1001)

#ID_list.append('1001')

stream_parameters = {"msm":ID_list[0]}
atlas_stream.start_stream(stream_type="result",**stream_parameters)

# Probe's connection status results
channel = "probe"
atlas_stream.bind_channel(channel, on_result_response)
#stream_parameters = {"prb": (12605,13663,850),"startTime": ts,"enrichProbes": True}
#,"start_time":1456948500
stream_parameters = {"startTime": 1457600000}
atlas_stream.start_stream(stream_type="probestatus", **stream_parameters)

# Timeout all subscriptions after 5 secs. Leave seconds empty for no timeout.
# Make sure you have this line after you start *all* your streams
atlas_stream.timeout(seconds=120)
# Shut down everything
atlas_stream.disconnect()








