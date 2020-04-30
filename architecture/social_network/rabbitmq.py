import sys
import os
import json
import make_arch as march 

# memcached
def main():
	# read path
	recvTm = march.make_time_model("expo", [3000])
	respTm = None

	# currently do not test the epoll_stage model
	stage = march.make_stage(stage_name = "rabbitmq", pathId = 0, pathStageId = 0, stageId = 0, blocking = False, batching = False, socket = False, 
		epoll = False, ngx = False, net = True, chunk = False, recvTm = recvTm, respTm = respTm, cm = None, criSec = False, threadLimit = None, 
		scaleFactor = 0.0)

	path = march.make_code_path(pathId = 0, prob = None, stages=[stage], priority = None)

	# memcached
	rabbitmq = march.make_micro_service(servType = "micro_service", servName = "rabbitmq", bindConn = True, paths = [path], 
		baseFreq = 2600, curFreq = 2600)

	with open("./json/microservice/rabbitmq.json", "w+") as f:
		json.dump(rabbitmq, f, indent=2)


if __name__ == "__main__":
	main()