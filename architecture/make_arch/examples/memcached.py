import sys
import os
import json
import make_arch as march 

# memcached
def main():
	# read path
	recvTm = march.make_time_model("expo", [1.5])
	respTm = None
	epoll_stage = march.make_stage(stage_name = "epoll", pathId = 0, pathStageId = 0, stageId = 0, blocking = False, batching = True, socket = False, 
		net = False, chunk = False, recvTm = recvTm, respTm = respTm, cm = None, criSec = False, threadLimit = None)

	recvTm = march.make_time_model("expo", [4.0])
	respTm = None
	socket_stage = march.make_stage(stage_name = "socket", pathId = 0, pathStageId = 1, stageId = 1, blocking = False, batching = True, socket = True, 
		net = False, chunk = False, recvTm = recvTm, respTm = respTm, cm = None, criSec = False, threadLimit = None)

	recvTm = march.make_time_model("expo", [0.1])
	respTm = None
	read_stage = march.make_stage(stage_name = "proc_read", pathId = 0, pathStageId = 2, stageId = 2, blocking = False, batching = False, socket = False, 
		net = False, chunk = False, recvTm = recvTm, respTm = respTm, cm = None, criSec = False, threadLimit = None)

	recvTm = march.make_time_model("expo", [4.5])
	respTm = None
	send_stage = march.make_stage(stage_name = "send", pathId = 0, pathStageId = 3, stageId = 3, blocking = False, batching = False, socket = False, 
		net = True, chunk = False, recvTm = recvTm, respTm = respTm, cm = None, criSec = False, threadLimit = None)

	read_path = march.make_code_path(pathId = 0, prob = 1.0, stages=[epoll_stage, socket_stage, read_stage, send_stage], priority = None)

	# write path
	recvTm = march.make_time_model("expo", [1.5])
	respTm = None
	epoll_stage = march.make_stage(stage_name = "epoll", pathId = 1, pathStageId = 0, stageId = 0, blocking = False, batching = True, socket = False, 
		net = False, chunk = False, recvTm = recvTm, respTm = respTm, cm = None, criSec = False, threadLimit = None)

	recvTm = march.make_time_model("expo", [4.0])
	respTm = None
	socket_stage = march.make_stage(stage_name = "socket", pathId = 1, pathStageId = 1, stageId = 1, blocking = False, batching = True, socket = True, 
		net = False, chunk = False, recvTm = recvTm, respTm = respTm, cm = None, criSec = False, threadLimit = None)

	recvTm = march.make_time_model("expo", [0.1])
	respTm = None
	write_stage = march.make_stage(stage_name = "proc_write", pathId = 1, pathStageId = 2, stageId = 4, blocking = False, batching = False, socket = False, 
		net = False, chunk = False, recvTm = recvTm, respTm = respTm, cm = None, criSec = False, threadLimit = None)

	recvTm = march.make_time_model("expo", [4.5])
	respTm = None
	send_stage = march.make_stage(stage_name = "send", pathId = 1, pathStageId = 3, stageId = 3, blocking = False, batching = False, socket = False, 
		net = True, chunk = False, recvTm = recvTm, respTm = respTm, cm = None, criSec = False, threadLimit = None)

	write_path = march.make_code_path(pathId = 1, prob = 0.0, stages=[epoll_stage, socket_stage, write_stage, send_stage], priority = None)


	# memcached
	memcached = march.make_micro_service(servType = "micro_service", servName = "memcached", bindConn = True, paths = [read_path, write_path])

	with open("./json/microservice/memcached.json", "w+") as f:
		json.dump(memcached, f, indent=2)


if __name__ == "__main__":
	main();