import sys
import os
import json
import make_arch as march

def main():
	sched = march.make_service_sched("CMT", [8, [20,21,22,23,24,25,26,27]], None)
	frontend = march.make_serv_inst(servName = "frontend", servDomain = "", instName = "frontend", 
		modelName = "frontend", sched = sched, machId = 0)

	sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	search = march.make_serv_inst(servName = "search", servDomain = "", instName = "search", 
		modelName = "search", sched = sched, machId = 1)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	geo = march.make_serv_inst(servName = "geo", servDomain = "", instName = "geo", 
		modelName = "geo", sched = sched, machId = 2)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	rate = march.make_serv_inst(servName = "rate", servDomain = "", instName = "rate", 
		modelName = "rate", sched = sched, machId = 3)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	profile = march.make_serv_inst(servName = "profile", servDomain = "", instName = "profile", 
		modelName = "profile", sched = sched, machId = 4)

	services = [frontend, search, geo, rate, profile]

	edge_0 = march.make_edge(src = "frontend", targ = "search", bidir = False)
        edge_1 = march.make_edge(src = "search", targ = "rate", bidir = False)
        edge_2 = march.make_edge(src = "search", targ = "geo", bidir = False)
        edge_3 = march.make_edge(src = "frontend", targ = "profile", bidir = False)

	edges = [edge_0, edge_1, edge_2, edge_3]

	graph = march.make_cluster(services = services, edges = edges, netLat = 65000)

	with open("./json/graph.json", "w+") as f:
		json.dump(graph, f, indent=2)

if __name__ == "__main__":
	main()