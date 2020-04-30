import sys
import os
import json
import make_arch as march

def main():
	sched = march.make_service_sched("CMT", [1, [20]], None)
	load_balancer = march.make_serv_inst(servName = "load_balancer", servDomain = "", instName = "load_balancer", 
		modelName = "load_balancer", sched = sched, machId = 0)
        services = [load_balancer]

	sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	nginx = march.make_serv_inst(servName = "nginx", servDomain = "", instName = "nginx", 
		modelName = "nginx", sched = sched, machId = 1)
        services.append(nginx)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	media_frontend = march.make_serv_inst(servName = "media_frontend", servDomain = "", instName = "media_frontend", 
		modelName = "media_frontend", sched = sched, machId = 2)
        services.append(media_frontend)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	unique_id = march.make_serv_inst(servName = "unique_id", servDomain = "", instName = "unique_id", 
		modelName = "unique_id", sched = sched, machId = 3)
        services.append(unique_id)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	url_shorten = march.make_serv_inst(servName = "url_shorten", servDomain = "", instName = "url_shorten", 
		modelName = "url_shorten", sched = sched, machId = 4)
        services.append(url_shorten)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	media = march.make_serv_inst(servName = "media", servDomain = "", instName = "media", 
		modelName = "media", sched = sched, machId = 5)
        services.append(media)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	text = march.make_serv_inst(servName = "text", servDomain = "", instName = "text", 
		modelName = "text", sched = sched, machId = 6)
        services.append(text)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	user_tag = march.make_serv_inst(servName = "user_tag", servDomain = "", instName = "user_tag", 
		modelName = "user_tag", sched = sched, machId = 7)
        services.append(user_tag)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	recommender = march.make_serv_inst(servName = "recommender", servDomain = "", instName = "recommender", 
		modelName = "recommender", sched = sched, machId = 8)
        services.append(recommender)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	read_home_timeline = march.make_serv_inst(servName = "read_home_timeline", servDomain = "", instName = "read_home_timeline", 
		modelName = "read_home_timeline", sched = sched, machId = 9)
        services.append(read_home_timeline)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	compose_post = march.make_serv_inst(servName = "compose_post", servDomain = "", instName = "compose_post", 
		modelName = "compose_post", sched = sched, machId = 10)
        services.append(compose_post)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	user = march.make_serv_inst(servName = "user", servDomain = "", instName = "user", 
		modelName = "user", sched = sched, machId = 11)
        services.append(user)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	social_graph = march.make_serv_inst(servName = "social_graph", servDomain = "", instName = "social_graph", 
		modelName = "social_graph", sched = sched, machId = 12)
        services.append(social_graph)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	search = march.make_serv_inst(servName = "search", servDomain = "", instName = "search", 
		modelName = "search", sched = sched, machId = 13)
        services.append(search)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	post_storage = march.make_serv_inst(servName = "post_storage", servDomain = "", instName = "post_storage", 
		modelName = "post_storage", sched = sched, machId = 14)
        services.append(post_storage)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	user_timeline = march.make_serv_inst(servName = "user_timeline", servDomain = "", instName = "user_timeline", 
		modelName = "user_timeline", sched = sched, machId = 15)
        services.append(user_timeline)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	rabbitmq = march.make_serv_inst(servName = "rabbitmq", servDomain = "", instName = "rabbitmq", 
		modelName = "rabbitmq", sched = sched, machId = 16)
        services.append(rabbitmq)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	write_home_timeline = march.make_serv_inst(servName = "write_home_timeline", servDomain = "", instName = "write_home_timeline", 
		modelName = "write_home_timeline", sched = sched, machId = 17)
        services.append(write_home_timeline)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	memcached_0 = march.make_serv_inst(servName = "memcached_0", servDomain = "", instName = "memcached_0", 
		modelName = "memcached", sched = sched, machId = 18)
        services.append(memcached_0)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	memcached_1 = march.make_serv_inst(servName = "memcached_1", servDomain = "", instName = "memcached_1", 
		modelName = "memcached", sched = sched, machId = 19)
        services.append(memcached_1)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	redis_0 = march.make_serv_inst(servName = "redis_0", servDomain = "", instName = "redis_0", 
		modelName = "redis", sched = sched, machId = 20)
        services.append(redis_0)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	redis_1 = march.make_serv_inst(servName = "redis_1", servDomain = "", instName = "redis_1", 
		modelName = "redis", sched = sched, machId = 21)
        services.append(redis_1)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	memcached_2 = march.make_serv_inst(servName = "memcached_2", servDomain = "", instName = "memcached_2", 
		modelName = "memcached", sched = sched, machId = 22)
        services.append(memcached_2)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	memcached_3 = march.make_serv_inst(servName = "memcached_3", servDomain = "", instName = "memcached_3", 
		modelName = "memcached", sched = sched, machId = 23)
        services.append(memcached_3)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	mongodb_0 = march.make_serv_inst(servName = "mongodb_0", servDomain = "", instName = "mongodb_0", 
		modelName = "mongodb", sched = sched, machId = 24)
        services.append(mongodb_0)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	mongodb_1 = march.make_serv_inst(servName = "mongodb_1", servDomain = "", instName = "mongodb_1", 
		modelName = "mongodb", sched = sched, machId = 25)
        services.append(mongodb_1)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	mongodb_2 = march.make_serv_inst(servName = "mongodb_2", servDomain = "", instName = "mongodb_2", 
		modelName = "mongodb", sched = sched, machId = 26)
        services.append(mongodb_2)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	mongodb_3 = march.make_serv_inst(servName = "mongodb_3", servDomain = "", instName = "mongodb_3", 
		modelName = "mongodb", sched = sched, machId = 27)
        services.append(mongodb_3)

        sched = march.make_service_sched("CMT", [4, [20,21,22,23]], None)
	mongodb_4 = march.make_serv_inst(servName = "mongodb_4", servDomain = "", instName = "mongodb_4", 
		modelName = "mongodb", sched = sched, machId = 28)
        services.append(mongodb_4)

	edge_0 = march.make_edge(src = "load_balancer", targ = "nginx", bidir = False)
        edges = [edge_0]

        edge_1 = march.make_edge(src = "load_balancer", targ = "media_frontend", bidir = False)
        edges.append(edge_1)

        edge_2 = march.make_edge(src = "media_frontend", targ = "media", bidir = False)
        edges.append(edge_2)

        edge_3 = march.make_edge(src = "media_frontend", targ = "memcached_3", bidir = True)
        edges.append(edge_3)

        edge_4 = march.make_edge(src = "media_frontend", targ = "mongodb_4", bidir = True)
        edges.append(edge_4)

        edge_5 = march.make_edge(src = "nginx", targ = "unique_id", bidir = False)
        edges.append(edge_5)

        edge_6 = march.make_edge(src = "nginx", targ = "url_shorten", bidir = False)
        edges.append(edge_6)

        edge_7 = march.make_edge(src = "nginx", targ = "read_home_timeline", bidir = False)
        edges.append(edge_7)

        edge_8 = march.make_edge(src = "nginx", targ = "search", bidir = False)
        edges.append(edge_8)

        edge_9 = march.make_edge(src = "nginx", targ = "media", bidir = False)
        edges.append(edge_9)

        edge_10 = march.make_edge(src = "nginx", targ = "post_storage", bidir = False)
        edges.append(edge_10)

        edge_11 = march.make_edge(src = "nginx", targ = "text", bidir = False)
        edges.append(edge_11)

        edge_12 = march.make_edge(src = "nginx", targ = "social_graph", bidir = False)
        edges.append(edge_12)

        edge_13 = march.make_edge(src = "nginx", targ = "user_tag", bidir = False)
        edges.append(edge_13)

        edge_14 = march.make_edge(src = "nginx", targ = "recommender", bidir = False)
        edges.append(edge_14)

        edge_15 = march.make_edge(src = "unique_id", targ = "compose_post", bidir = False)
        edges.append(edge_15)

        edge_16 = march.make_edge(src = "url_shorten", targ = "compose_post", bidir = False)
        edges.append(edge_16)

        edge_17 = march.make_edge(src = "media", targ = "compose_post", bidir = False)
        edges.append(edge_17)

        edge_18 = march.make_edge(src = "text", targ = "compose_post", bidir = False)
        edges.append(edge_18)

        edge_19 = march.make_edge(src = "nginx", targ = "user", bidir = True)
        edges.append(edge_19)

        edge_20 = march.make_edge(src = "recommender", targ = "user", bidir = False)
        edges.append(edge_20)

        edge_21 = march.make_edge(src = "read_home_timeline", targ = "memcached_1", bidir = True)
        edges.append(edge_21)

        edge_22 = march.make_edge(src = "read_home_timeline", targ = "mongodb_1", bidir = True)
        edges.append(edge_22)

        edge_23 = march.make_edge(src = "read_home_timeline", targ = "post_storage", bidir = False)
        edges.append(edge_23)

        edge_24 = march.make_edge(src = "read_home_timeline", targ = "redis_1", bidir = False)
        edges.append(edge_24)

        edge_25 = march.make_edge(src = "compose_post", targ = "post_storage", bidir = False)
        edges.append(edge_25)

        edge_26 = march.make_edge(src = "compose_post", targ = "user_timeline", bidir = False)
        edges.append(edge_26)

        edge_27 = march.make_edge(src = "compose_post", targ = "rabbitmq", bidir = False)
        edges.append(edge_27)

        edge_28 = march.make_edge(src = "user", targ = "compose_post", bidir = False)
        edges.append(edge_28)

        edge_29 = march.make_edge(src = "user", targ = "memcached_0", bidir = True)
        edges.append(edge_29)

        edge_30 = march.make_edge(src = "user", targ = "mongodb_0", bidir = True)
        edges.append(edge_30)

        edge_31 = march.make_edge(src = "social_graph", targ = "user", bidir = False)
        edges.append(edge_31)

        edge_32 = march.make_edge(src = "social_graph", targ = "memcached_2", bidir = True)
        edges.append(edge_32)

        edge_33 = march.make_edge(src = "social_graph", targ = "mongodb_3", bidir = True)
        edges.append(edge_33)

        edge_34 = march.make_edge(src = "search", targ = "mongodb_1", bidir = True)
        edges.append(edge_34)

        edge_35 = march.make_edge(src = "post_storage", targ = "memcached_1", bidir = True)
        edges.append(edge_35)

        edge_36 = march.make_edge(src = "post_storage", targ = "mongodb_1", bidir = True)
        edges.append(edge_36)

        edge_37 = march.make_edge(src = "user_timeline", targ = "post_storage", bidir = False)
        edges.append(edge_37)

        edge_38 = march.make_edge(src = "user_timeline", targ = "redis_0", bidir = True)
        edges.append(edge_38)

        edge_39 = march.make_edge(src = "user_timeline", targ = "mongodb_2", bidir = True)
        edges.append(edge_39)

        edge_40 = march.make_edge(src = "rabbitmq", targ = "write_home_timeline", bidir = False)
        edges.append(edge_40)

        edge_41 = march.make_edge(src = "write_home_timeline", targ = "redis_1", bidir = True)
        edges.append(edge_41)

        edge_42 = march.make_edge(src = "write_home_timeline", targ = "social_graph", bidir = False)
        edges.append(edge_42)

	graph = march.make_cluster(services = services, edges = edges, netLat = 65000)

	with open("./json/graph.json", "w+") as f:
		json.dump(graph, f, indent=2)

if __name__ == "__main__":
	main()