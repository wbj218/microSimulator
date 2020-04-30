#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <stdio.h>

#include "cluster_parser.hh"
#include "cluster.hh"
#include "client.hh"

std::string sched_dec_file = "./sched_test/sched_decision.txt";
std::string stats_output_file = "./sched_test/simulated_stats.txt";

// return true if decision is ready
bool get_sched_decision(int cur_round, std::unordered_map<std::string, unsigned>& freq_set) {
	std::ifstream dec_file(sched_dec_file);
	if(!dec_file) {
		// std::cout << "cannot open " << sched_dec_file << std::endl;
		return false;
	}
	char buffer[512];
	unsigned load_balancer = 0;
	unsigned nginx = 0;
	unsigned media = 0;
	unsigned unique_id = 0;
	unsigned url_shorten = 0;
        unsigned text = 0;
        unsigned user = 0;
        unsigned compose_post = 0;
        unsigned post_storage = 0;
        unsigned memcached_1 = 0;
        unsigned mongodb_1 = 0;
        unsigned user_timeline = 0;
        unsigned redis_0 = 0;
        unsigned mongodb_2 = 0;
        unsigned rabbitmq = 0;
        unsigned write_home_timeline = 0;
        unsigned redis_1 = 0;
        unsigned social_graph = 0;
        unsigned memcached_2 = 0;
        unsigned mongodb_3 = 0;
	int sched_round = -1;
	while(!dec_file.eof()) {
		dec_file.getline(buffer, 512);
		//sscanf(buffer, "frontend: %u; geo: %u; profile: %u; rate: %u; search: %u; cur_round: %d", &frontend, &geo, &profile, &rate, &search, &sched_round);
                sscanf(buffer, "load_balancer: %u; nginx: %u; media: %u; unique_id: %u; url_shorten: %u; text: %u; user: %u; compose_post: %u; post_storage: %u; memcached_1: %u; mongodb_1: %u; user_timeline: %u; redis_0: %u; mongodb_2: %u; rabbitmq: %u; write_home_timeline: %u; redis_1: %u; social_graph: %u; memcached_2: %u; mongodb_3: %u; cur_round: %d", \
                &load_balancer, &nginx, &media, &unique_id, &url_shorten, &text, &user, &compose_post, &post_storage, &memcached_1, &mongodb_1, &user_timeline, &redis_0, &mongodb_2, &rabbitmq, &write_home_timeline, &redis_1, &social_graph, &memcached_2, &mongodb_3, &sched_round);
	}
	dec_file.close();
	if(sched_round != cur_round) {
		//printf("sched_round = %d, cur_round = %d\n", sched_round, cur_round);
		//printf("frontend: %u; geo: %u; profile: %u; rate: %u; search: %u;\n", frontend, geo, profile, rate, search);
		return false;
	} else {
		freq_set["load_balancer"] = load_balancer;
		freq_set["nginx"] = nginx;
		freq_set["media"] = media;
		freq_set["unique_id"] = unique_id;
		freq_set["url_shorten"] = url_shorten;
                freq_set["text"] = text;
                freq_set["user"] = user;
                freq_set["compose_post"] = compose_post;
                freq_set["post_storage"] = post_storage;
                freq_set["memcached_1"] = memcached_1;
                freq_set["mongodb_1"] = mongodb_1;
                freq_set["user_timeline"] = user_timeline;
                freq_set["redis_0"] = redis_0;
                freq_set["mongodb_2"] = mongodb_2;
                freq_set["rabbitmq"] = rabbitmq;
                freq_set["write_home_timeline"] = write_home_timeline;
                freq_set["redis_1"] = redis_1;
                freq_set["social_graph"] = social_graph;
                freq_set["memcached_2"] = memcached_2;
                freq_set["mongodb_3"] = mongodb_3;
		return true;
	}
}

void output_stats(int cur_round, Time end2end_tail, Time load_balancer_tail, Time nginx_tail, Time media_tail, Time unique_id_tail, Time url_shorten_tail, \
Time text_tail, Time user_tail, Time compose_post_tail, Time post_storage_tail, Time memcached_1_tail, Time mongodb_1_tail, Time user_timeline_tail, \
Time redis_0_tail, Time mongodb_2_tail, Time rabbitmq_tail, Time write_home_timeline_tail, Time redis_1_tail, Time social_graph_tail, Time memcached_2_tail, \
Time mongodb_3_tail, uint64_t cur_qps) {
	std::ofstream stats_file(stats_output_file);
	if(!stats_file) {
		std::cout << "cannot open " << sched_dec_file << std::endl;
		exit(-1);
	}

	std::cout << "output stats" << std::endl;
	stats_file << "end2end: " << end2end_tail << "; load_balancer: " << load_balancer_tail << "; nginx :" << nginx_tail << "; media :" << media_tail << "; unique_id :" << unique_id_tail << "; url_shorten :" << url_shorten_tail 
        << "; text :" << text_tail << "; user :" << user_tail << "; compose_post :" << compose_post_tail << "; post_storage :" << post_storage_tail << "; memcached_1 :" << memcached_1_tail << "; mongodb_1 :" << mongodb_1_tail 
        << "; user_timeline :" << user_timeline_tail << "; redis_0 :" << redis_0_tail << "; mongodb_2 :" << mongodb_2_tail << "; rabbitmq :" << rabbitmq_tail << "; write_home_timeline :" << write_home_timeline_tail << "; redis_1 :" << redis_1_tail
        << "; social_graph :" << social_graph_tail << "; memcached_2 :" << memcached_2_tail << "; mongodb_3 :" << mongodb_3_tail << "; cur_qps: " << cur_qps  << "; cur_round: " << cur_round << std::endl;
	stats_file.close();
	std::cout << "end2end: " << end2end_tail << "; load_balancer: " << load_balancer_tail << "; nginx :" << nginx_tail << "; media :" << media_tail << "; unique_id :" << unique_id_tail << "; url_shorten :" << url_shorten_tail 
        << "; text :" << text_tail << "; user :" << user_tail << "; compose_post :" << compose_post_tail << "; post_storage :" << post_storage_tail << "; memcached_1 :" << memcached_1_tail << "; mongodb_1 :" << mongodb_1_tail 
        << "; user_timeline :" << user_timeline_tail << "; redis_0 :" << redis_0_tail << "; mongodb_2 :" << mongodb_2_tail << "; rabbitmq :" << rabbitmq_tail << "; write_home_timeline :" << write_home_timeline_tail << "; redis_1 :" << redis_1_tail
        << "; social_graph :" << social_graph_tail << "; memcached_2 :" << memcached_2_tail << "; mongodb_3 :" << mongodb_3_tail << "; cur_qps: " << cur_qps  << "; cur_round: " << cur_round << std::endl;
}

int main(int argc, char* argv[]) {
	assert(argc >= 4);
	std::string clusterDir = std::string(argv[1]);
	unsigned numConn = atoi(argv[2]); 
	Time netLat = atoi(argv[3]);

	// std::string raplPolicy = std::string(argv[4]);
	// std::string raplFallbackPolicy = std::string(argv[5]);

	// client config
	std::string cliTm = std::string(argv[4]);
	// define load in terms of rps
	// convert it into us
	// double avgCliLat = atof(argv[6]);

	double kqps = atof(argv[5]);
	std::cout << "user given qps = " << (unsigned)(kqps*1000) << std::endl;

	// set up files
	FILE* f = fopen(stats_output_file.c_str(), "w+");
	if(f == nullptr) {
		std::cout << "Cannot create " << stats_output_file << std::endl;
		exit(-1);
	}
	fclose(f);

	f = fopen(sched_dec_file.c_str(), "w+");
	if(f == nullptr) {
		std::cout << "Cannot create " << sched_dec_file << std::endl;
		exit(-1);
	}
	fclose(f);

	// unsigned ngx_freq = atoi(argv[6]);
	// unsigned memc_freq = atoi(argv[7]);

	// debug
	bool debug = false;
	if(argc == 7 && std::string(argv[6]) == "debug")
		debug = true;

	ClusterParser* parser = new ClusterParser(clusterDir, kqps, debug);

	std::cout << "before parsing" << std::endl;

	Cluster* cluster = parser->parsCluster();
	// delete parser;

	// cluster->setFreq("nginx", ngx_freq);
	// cluster->setFreq("memcached", memc_freq);

	std::cout << "after parsing" << std::endl;

	// set up client
	// Client* client = new Client( numConn, netLat, debug);

	// Client* client = parser->parsClient(raplPolicy, raplFallbackPolicy, numConn, netLat, debug);
	Client* client = parser->parsClient(numConn, netLat, kqps, debug);
	// client->numTotal = 1;


	TimeModel* tm = nullptr;
	if(cliTm == "expo") {
		tm = new ExpoTimeModel(1);
	} else if (cliTm == "const") {
		tm = new ConstTimeModel(1);
	} else {
		printf("Error: Undefined time model for client\n");
		exit(1);
	}
	client->setTimeModel(tm);

	client->setEntry(cluster);
	client->setTimeArray();

	std::cout << "simulation starts..." << std::endl;
	unsigned cur_round = 0;

	// simulation
	Time globalTime = 0;
	while(true) {
		//printf("000000000000000000000000000000000000");
		Time nextClient = client->nextEventTime();
		Time nextCluster = cluster->nextEventTime(globalTime);

		if(nextCluster == INVALID_TIME && client->isAllJobIssued()) {
			// all jobs have finished processing
			// only perf monitoring events are left
			break;
		}


		if(debug) {
			printf("nextClient = %f ms\n", nextClient/1000000.0);
			printf("nextCluster = %f ms\n", nextCluster/1000000.0);
		}

		if(nextClient == INVALID_TIME && nextCluster == INVALID_TIME)
			break;
		else if(nextCluster == INVALID_TIME) {
			// std::cout << "cluster invalid time" << std::endl;
			// std::cout << "before client run" << std::endl;
			// std::cout << "globalTime = " << globalTime << std::endl;

			assert(globalTime <= nextClient);
			globalTime = nextClient;

			if(client->needSched(globalTime)) {
				std::cout << "client make decision at " << nextClient/1000000000.0 << "s, cur_round = "
						<< cur_round << std::endl;

				std::unordered_map<std::string, Time> lat_info;
				cluster->getPerTierTail(lat_info);
				Time end2end_tail = client->getTailLat();
				client->clearRespTime();
				uint64_t cur_qps = client->getCurQps();
				output_stats(cur_round, end2end_tail, lat_info["load_balancer"], lat_info["nginx"], lat_info["media"], lat_info["unique_id"], lat_info["url_shorten"], \
                                lat_info["text"], lat_info["user"], lat_info["compose_post"], lat_info["post_storage"], lat_info["memcached_1"], lat_info["mongodb_1"], lat_info["user_timeline"], \
                                lat_info["redis_0"], lat_info["mongodb_2"], lat_info["rabbitmq"], lat_info["write_home_timeline"], lat_info["redis_1"], lat_info["social_graph"], lat_info["memcached_2"], \
                                lat_info["mongodb_3"], cur_qps);

				std::unordered_map<std::string, unsigned> freq_set;
				//std::cout << "11111111111111111111111111111111" << std::endl;
				while(!get_sched_decision(cur_round, freq_set));
				cur_round += 1;
				std::cout << "decision made load_balancer = " << freq_set["load_balancer"] << ", nginx = " << freq_set["nginx"] << ", media = " << freq_set["media"] << 
					", unique_id = " << freq_set["unique_id"] << ", url_shorten = " << freq_set["url_shorten"] << ", text = " << freq_set["text"] << ", user = " << freq_set["user"] << \
                                        ", compose_post = " << freq_set["compose_post"] << ", post_storage = " << freq_set["post_storage"] << ", memcached_1 = " << freq_set["memcached_1"] << \
                                        ", mongodb_1 = " << freq_set["mongodb_1"] << ", user_timeline = " << freq_set["user_timeline"] << ", redis_0 = " << freq_set["redis_0"] << ", mongodb_2 = " << freq_set["mongodb_2"] << \
                                        ", rabbitmq = " << freq_set["rabbitmq"] << ", write_home_timeline = " << freq_set["write_home_timeline"] << ", redis_1 = " << freq_set["redis_1"] << \
                                        ", social_graph = " << freq_set["social_graph"] << ", memcached_2 = " << freq_set["memcached_2"] << ", mongodb_3 = " << freq_set["mongodb_3"] << std::endl << std::endl; 
				cluster->setFreq("load_balancer", freq_set["load_balancer"]);
				cluster->setFreq("nginx", freq_set["nginx"]);
				cluster->setFreq("media", freq_set["media"]);
				cluster->setFreq("unique_id", freq_set["unique_id"]);
				cluster->setFreq("url_shorten", freq_set["url_shorten"]);
                                cluster->setFreq("text", freq_set["text"]);
                                cluster->setFreq("user", freq_set["user"]);
                                cluster->setFreq("compose_post", freq_set["compose_post"]);
                                cluster->setFreq("post_storage", freq_set["post_storage"]);
                                cluster->setFreq("memcached_1", freq_set["memcached_1"]);
                                cluster->setFreq("mongodb_1", freq_set["mongodb_1"]);
                                cluster->setFreq("user_timeline", freq_set["user_timeline"]);
                                cluster->setFreq("redis_0", freq_set["redis_0"]);
                                cluster->setFreq("mongodb_2", freq_set["mongodb_2"]);
                                cluster->setFreq("rabbitmq", freq_set["rabbitmq"]);
                                cluster->setFreq("write_home_timeline", freq_set["write_home_timeline"]);
                                cluster->setFreq("redis_1", freq_set["redis_1"]);
                                cluster->setFreq("social_graph", freq_set["social_graph"]);
                                cluster->setFreq("memcached_2", freq_set["memcached_2"]);
                                cluster->setFreq("mongodb_3", freq_set["mongodb_3"]);
				client->setLastMonitorTime(globalTime);
			}
			
			client->run(globalTime);
			// std::cout << "client run" << std::endl << std::endl;
		} else if(nextClient == INVALID_TIME) {
			// std::cout << "client invalid time" << std::endl;
			// std::cout << "before cluster run" << std::endl;
			// std::cout << "globalTime = " << globalTime << std::endl;

			assert(globalTime <= nextCluster);
			globalTime = nextCluster;

			if(client->needSched(globalTime)) {
				std::cout << "client make decision at " << nextClient/1000000000.0 << "s, cur_round = "
						<< cur_round << std::endl;

				std::unordered_map<std::string, Time> lat_info;
				cluster->getPerTierTail(lat_info);
				Time end2end_tail = client->getTailLat();
				client->clearRespTime();
				uint64_t cur_qps = client->getCurQps();
				//output_stats(cur_round, end2end_tail, lat_info["frontend"], lat_info["geo"], lat_info["profile"], lat_info["rate"], lat_info["search"], cur_qps);
                                output_stats(cur_round, end2end_tail, lat_info["load_balancer"], lat_info["nginx"], lat_info["media"], lat_info["unique_id"], lat_info["url_shorten"], \
                                lat_info["text"], lat_info["user"], lat_info["compose_post"], lat_info["post_storage"], lat_info["memcached_1"], lat_info["mongodb_1"], lat_info["user_timeline"], \
                                lat_info["redis_0"], lat_info["mongodb_2"], lat_info["rabbitmq"], lat_info["write_home_timeline"], lat_info["redis_1"], lat_info["social_graph"], lat_info["memcached_2"], \
                                lat_info["mongodb_3"], cur_qps);
				
                                std::unordered_map<std::string, unsigned> freq_set;
				//std::cout << "222222222222222222222222222222222222" << std::endl;
				while(!get_sched_decision(cur_round, freq_set));
				cur_round += 1;
                                /*
				std::cout << "decision made frontend = " << freq_set["frontend"] << 
					", geo = " << freq_set["geo"] << 
					", profile = " << freq_set["profile"] << 
					", rate = " << freq_set["rate"] << 
					", search = " << freq_set["search"] << std::endl << std::endl; 
				cluster->setFreq("frontend", freq_set["frontend"]);
				cluster->setFreq("geo", freq_set["geo"]);
				cluster->setFreq("profile", freq_set["profile"]);
				cluster->setFreq("rate", freq_set["rate"]);
				cluster->setFreq("search", freq_set["search"]);
				client->setLastMonitorTime(globalTime);
                                */
                                std::cout << "decision made load_balancer = " << freq_set["load_balancer"] << ", nginx = " << freq_set["nginx"] << ", media = " << freq_set["media"] << 
					", unique_id = " << freq_set["unique_id"] << ", url_shorten = " << freq_set["url_shorten"] << ", text = " << freq_set["text"] << ", user = " << freq_set["user"] << \
                                        ", compose_post = " << freq_set["compose_post"] << ", post_storage = " << freq_set["post_storage"] << ", memcached_1 = " << freq_set["memcached_1"] << \
                                        ", mongodb_1 = " << freq_set["mongodb_1"] << ", user_timeline = " << freq_set["user_timeline"] << ", redis_0 = " << freq_set["redis_0"] << ", mongodb_2 = " << freq_set["mongodb_2"] << \
                                        ", rabbitmq = " << freq_set["rabbitmq"] << ", write_home_timeline = " << freq_set["write_home_timeline"] << ", redis_1 = " << freq_set["redis_1"] << \
                                        ", social_graph = " << freq_set["social_graph"] << ", memcached_2 = " << freq_set["memcached_2"] << ", mongodb_3 = " << freq_set["mongodb_3"] << std::endl << std::endl; 
				cluster->setFreq("load_balancer", freq_set["load_balancer"]);
				cluster->setFreq("nginx", freq_set["nginx"]);
				cluster->setFreq("media", freq_set["media"]);
				cluster->setFreq("unique_id", freq_set["unique_id"]);
				cluster->setFreq("url_shorten", freq_set["url_shorten"]);
                                cluster->setFreq("text", freq_set["text"]);
                                cluster->setFreq("user", freq_set["user"]);
                                cluster->setFreq("compose_post", freq_set["compose_post"]);
                                cluster->setFreq("post_storage", freq_set["post_storage"]);
                                cluster->setFreq("memcached_1", freq_set["memcached_1"]);
                                cluster->setFreq("mongodb_1", freq_set["mongodb_1"]);
                                cluster->setFreq("user_timeline", freq_set["user_timeline"]);
                                cluster->setFreq("redis_0", freq_set["redis_0"]);
                                cluster->setFreq("mongodb_2", freq_set["mongodb_2"]);
                                cluster->setFreq("rabbitmq", freq_set["rabbitmq"]);
                                cluster->setFreq("write_home_timeline", freq_set["write_home_timeline"]);
                                cluster->setFreq("redis_1", freq_set["redis_1"]);
                                cluster->setFreq("social_graph", freq_set["social_graph"]);
                                cluster->setFreq("memcached_2", freq_set["memcached_2"]);
                                cluster->setFreq("mongodb_3", freq_set["mongodb_3"]);
				client->setLastMonitorTime(globalTime);
			}
			
			cluster->run(globalTime);
			// std::cout << "cluster run" << std::endl << std::endl;
		} else {
			// std::cout << "cluster and client valid time " << std::endl;
			// std::cout << "globalTime = " << globalTime << std::endl;
			assert(globalTime <= nextClient);
			assert(globalTime <= nextCluster);
			if(nextClient < nextCluster) {
				globalTime = nextClient;
				// check if needs scheduling
				if(client->needSched(globalTime)) {
					std::cout << "client make decision at " << nextClient/1000000000.0 << "s, cur_round = "
						<< cur_round << std::endl;

					std::unordered_map<std::string, Time> lat_info;
					cluster->getPerTierTail(lat_info);
					Time end2end_tail = client->getTailLat();
					client->clearRespTime();
					uint64_t cur_qps = client->getCurQps();
					//output_stats(cur_round, end2end_tail, lat_info["frontend"], lat_info["geo"], lat_info["profile"], lat_info["rate"], lat_info["search"], cur_qps);
                                        output_stats(cur_round, end2end_tail, lat_info["load_balancer"], lat_info["nginx"], lat_info["media"], lat_info["unique_id"], lat_info["url_shorten"], \
                                        lat_info["text"], lat_info["user"], lat_info["compose_post"], lat_info["post_storage"], lat_info["memcached_1"], lat_info["mongodb_1"], lat_info["user_timeline"], \
                                        lat_info["redis_0"], lat_info["mongodb_2"], lat_info["rabbitmq"], lat_info["write_home_timeline"], lat_info["redis_1"], lat_info["social_graph"], lat_info["memcached_2"], \
                                        lat_info["mongodb_3"], cur_qps);

					std::unordered_map<std::string, unsigned> freq_set;
					//std::cout << "33333333333333333333333333333333333" << std::endl;
					while(!get_sched_decision(cur_round, freq_set));
					cur_round += 1;
                                        /*
					std::cout << "decision made frontend = " << freq_set["frontend"] << 
						", geo = " << freq_set["geo"] << 
						", profile = " << freq_set["profile"] << 
						", rate = " << freq_set["rate"] << 
						", search = " << freq_set["search"] << std::endl << std::endl;  
					cluster->setFreq("frontend", freq_set["frontend"]);
					cluster->setFreq("geo", freq_set["geo"]);
					cluster->setFreq("profile", freq_set["profile"]);
					cluster->setFreq("rate", freq_set["rate"]);
					cluster->setFreq("search", freq_set["search"]);
					client->setLastMonitorTime(globalTime);
                                        */
                                        std::cout << "decision made load_balancer = " << freq_set["load_balancer"] << ", nginx = " << freq_set["nginx"] << ", media = " << freq_set["media"] << 
					        ", unique_id = " << freq_set["unique_id"] << ", url_shorten = " << freq_set["url_shorten"] << ", text = " << freq_set["text"] << ", user = " << freq_set["user"] << \
                                                ", compose_post = " << freq_set["compose_post"] << ", post_storage = " << freq_set["post_storage"] << ", memcached_1 = " << freq_set["memcached_1"] << \
                                                ", mongodb_1 = " << freq_set["mongodb_1"] << ", user_timeline = " << freq_set["user_timeline"] << ", redis_0 = " << freq_set["redis_0"] << ", mongodb_2 = " << freq_set["mongodb_2"] << \
                                                ", rabbitmq = " << freq_set["rabbitmq"] << ", write_home_timeline = " << freq_set["write_home_timeline"] << ", redis_1 = " << freq_set["redis_1"] << \
                                                ", social_graph = " << freq_set["social_graph"] << ", memcached_2 = " << freq_set["memcached_2"] << ", mongodb_3 = " << freq_set["mongodb_3"] << std::endl << std::endl; 
				        cluster->setFreq("load_balancer", freq_set["load_balancer"]);
				        cluster->setFreq("nginx", freq_set["nginx"]);
				        cluster->setFreq("media", freq_set["media"]);
				        cluster->setFreq("unique_id", freq_set["unique_id"]);
				        cluster->setFreq("url_shorten", freq_set["url_shorten"]);
                                        cluster->setFreq("text", freq_set["text"]);
                                        cluster->setFreq("user", freq_set["user"]);
                                        cluster->setFreq("compose_post", freq_set["compose_post"]);
                                        cluster->setFreq("post_storage", freq_set["post_storage"]);
                                        cluster->setFreq("memcached_1", freq_set["memcached_1"]);
                                        cluster->setFreq("mongodb_1", freq_set["mongodb_1"]);
                                        cluster->setFreq("user_timeline", freq_set["user_timeline"]);
                                        cluster->setFreq("redis_0", freq_set["redis_0"]);
                                        cluster->setFreq("mongodb_2", freq_set["mongodb_2"]);
                                        cluster->setFreq("rabbitmq", freq_set["rabbitmq"]);
                                        cluster->setFreq("write_home_timeline", freq_set["write_home_timeline"]);
                                        cluster->setFreq("redis_1", freq_set["redis_1"]);
                                        cluster->setFreq("social_graph", freq_set["social_graph"]);
                                        cluster->setFreq("memcached_2", freq_set["memcached_2"]);
                                        cluster->setFreq("mongodb_3", freq_set["mongodb_3"]);
				        client->setLastMonitorTime(globalTime);
				}
				// std::cout << "before client run" << std::endl;
				client->run(globalTime);
				// std::cout << "client run" << std::endl << std::endl;
			} else {
				// std::cout << "444444444444444444444444444444" << std::endl;
				globalTime = nextCluster;
				// std::cout << "before cluster run" << std::endl;
				cluster->run(globalTime);
				// std::cout << "cluster run" << std::endl << std::endl;
			}
		}
	}

	// check for deadlock
	bool deadlock = cluster->jobLeft();
	assert(!deadlock);

	client->show();
	cluster->showCpuUtil(globalTime);

	delete client;
	delete cluster;
	delete parser;
	return 0;
}