import sys
import os
import json
import make_arch as march 


def main():
	# path 0: memcached cache hit
	nodeList = []

	node_0 = march.make_serv_path_node(servName = "load_balancer", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 0, needSync = False, syncNodeId = None, childs = [1])
	nodeList.append(node_0)

	node_1 = march.make_serv_path_node(servName = "nginx", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 1, needSync = False, syncNodeId = None, childs = [2,3,4,5,6])
	nodeList.append(node_1)

	node_2 = march.make_serv_path_node(servName = "media", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 2, needSync = False, syncNodeId = None, childs = [7])
	nodeList.append(node_2)

        node_3 = march.make_serv_path_node(servName = "unique_id", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 3, needSync = False, syncNodeId = None, childs = [7])
	nodeList.append(node_3)

        node_4 = march.make_serv_path_node(servName = "url_shorten", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 4, needSync = False, syncNodeId = None, childs = [7])
	nodeList.append(node_4)

        node_5 = march.make_serv_path_node(servName = "text", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 5, needSync = False, syncNodeId = None, childs = [7])
	nodeList.append(node_5)

        node_6 = march.make_serv_path_node(servName = "user", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 6, needSync = False, syncNodeId = None, childs = [7])
	nodeList.append(node_6)

        node_7 = march.make_serv_path_node(servName = "compose_post", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 7, needSync = False, syncNodeId = None, childs = [8,11,14])
	nodeList.append(node_7)

        node_8 = march.make_serv_path_node(servName = "post_storage", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 8, needSync = False, syncNodeId = None, childs = [9,10])
	nodeList.append(node_8)

        node_9 = march.make_serv_path_node(servName = "memcached_1", servDomain = "", codePath = 1, startStage = 0, endStage = -1, 
		nodeId = 9, needSync = False, syncNodeId = None, childs = [20])
	nodeList.append(node_9)

        node_10 = march.make_serv_path_node(servName = "mongodb_1", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 10, needSync = False, syncNodeId = None, childs = [20])
	nodeList.append(node_10)

        node_11 = march.make_serv_path_node(servName = "user_timeline", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 11, needSync = False, syncNodeId = None, childs = [12,13])
	nodeList.append(node_11)

        node_12 = march.make_serv_path_node(servName = "redis_0", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 12, needSync = False, syncNodeId = None, childs = [20])
	nodeList.append(node_12)

        node_13 = march.make_serv_path_node(servName = "mongodb_2", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 13, needSync = False, syncNodeId = None, childs = [20])
	nodeList.append(node_13)

        node_14 = march.make_serv_path_node(servName = "rabbitmq", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 14, needSync = False, syncNodeId = None, childs = [15])
	nodeList.append(node_14)

        node_15 = march.make_serv_path_node(servName = "write_home_timeline", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 15, needSync = False, syncNodeId = None, childs = [16,17])
	nodeList.append(node_15)

        node_16 = march.make_serv_path_node(servName = "redis_1", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 16, needSync = False, syncNodeId = None, childs = [20])
	nodeList.append(node_16)

        node_17 = march.make_serv_path_node(servName = "social_graph", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 17, needSync = False, syncNodeId = None, childs = [18,19])
	nodeList.append(node_17)

        node_18 = march.make_serv_path_node(servName = "memcached_2", servDomain = "", codePath = 1, startStage = 0, endStage = -1, 
		nodeId = 18, needSync = False, syncNodeId = None, childs = [20])
	nodeList.append(node_18)

        node_19 = march.make_serv_path_node(servName = "mongodb_3", servDomain = "", codePath = 0, startStage = 0, endStage = -1, 
		nodeId = 19, needSync = False, syncNodeId = None, childs = [20])
	nodeList.append(node_19)

        node_20 = march.make_serv_path_node(servName = "client", servDomain = "", codePath = -1, startStage = 0, endStage = -1, 
		nodeId = 20, needSync = False, syncNodeId = None, childs = [])
	nodeList.append(node_20)

	path_memc_hit = march.make_serv_path(pathId = 0, entry = 0, prob = 100, nodes = nodeList)


	paths = [path_memc_hit]

	with open("./json/path.json", "w+") as f:
		json.dump(paths, f, indent=2)

if __name__ == "__main__":
	main()