#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <libxml/parser.h>
#include <libxml/tree.h>
#include <stdint.h>
#include <stdbool.h>
#include <map>
#include <iostream>
#include <list>
#include <vector>
#include <algorithm>
#include <thread>
#include <mutex>
#include <atomic>
#include <unordered_set>
std::mutex file_mutex; // 用於寫檔案時加鎖
typedef struct Node
{
    int guid;
    char type[16]; // "keyword", "eol", "value"
    char name[256];
    char str[128]; // for keyword
    char macro[128];
    // std::vector<int> prev; // 直接相连的节点，前驱
    std::vector<int> next; // 直接相连的节点，后继
} Node;

std::map<int, Node> nodes_map; // guid -> Node
std::list<int> eol_nodes_list; // eol nodes' guid list
// 获取 XML 属性值
char *get_prop(xmlNodePtr node, const char *name)
{
    xmlChar *val = xmlGetProp(node, (const xmlChar *)name);
    if (!val)
        return NULL;
    char *ret = (char *)malloc(strlen((char *)val) + 1);
    strcpy(ret, (char *)val);
    xmlFree(val);
    return ret;
}
// depth-first search recursive function

void dfs_recursive(int guid_start, int guid_end, std::list<int> &path, std::list<std::list<int>> &paths, std::map<int, bool> &block_nodes_guid)
{
    // printf("dfs_recursive: %d -> %d\n", guid_start, guid_end);
    // printf("%zu ", path.size());

    // 檢查是否已經在 path，避免環路
    if (std::find(path.begin(), path.end(), guid_start) != path.end())
    {
        fprintf(stderr, "found loop: ");
        for (auto it = path.begin(); it != path.end(); ++it)
            fprintf(stderr, "%d ", *it);
        fprintf(stderr, "%d", guid_start);
        // the cdl should not have loop
        // show all the next nodes of the first duplicate node
        // fprintf(stderr, "loop! first duplicate node's next nodes\n");
        // for (auto it = nodes_map[guid_start].next.begin(); it != nodes_map[guid_start].next.end(); ++it)
        //{
        //    fprintf(stderr, " %d", *it);
        //}
        exit(1);
    }
    path.push_back(guid_start);

    if (guid_start == guid_end)
    {
        if (false)
        {
            fprintf(stdout, "found path with length %zu: ", path.size());
            for (auto it = path.begin(); it != path.end(); ++it)
                fprintf(stdout, "%d ", *it);
            fprintf(stdout, "\n");
        }
        paths.push_back(path);
        path.pop_back();
        return;
    }
    for (auto it = nodes_map[guid_start].next.begin(); it != nodes_map[guid_start].next.end(); ++it)
        {
            // check if the next node is in the block_nodes_guid
            if (block_nodes_guid[*it])
            {
                continue;
            }
            dfs_recursive(*it, guid_end, path, paths, block_nodes_guid);
        }
    // this node has no path to guid_end, add it to the block_nodes_guid
    block_nodes_guid[guid_start] = true;
    path.pop_back();
}
void dfs_worker(int root_guid, int eol_guid, FILE *fp)
{
    std::list<int> path;
    std::list<std::list<int>> paths;
    std::map<int, bool> block_nodes_guid;
    // add all nodes's guid to block_nodes_guid
    for (auto it = nodes_map.begin(); it != nodes_map.end(); ++it)
    {
        block_nodes_guid[it->first] = false;
    }
    dfs_recursive(root_guid, eol_guid, path, paths, block_nodes_guid);

    std::lock_guard<std::mutex> lock(file_mutex);
    // write the paths to file

    for (auto it_path = paths.begin(); it_path != paths.end(); ++it_path)
    {
        // reverse the path

        for (auto it_node = it_path->begin(); it_node != it_path->end(); ++it_node)
        {
            if (*it_node == root_guid)
            {
                continue;
            }
            else if (strcmp(nodes_map[*it_node].type, "eol") == 0)
            {
                fprintf(fp, "[eol]");
            }
            else if (strcmp(nodes_map[*it_node].type, "keyword") == 0)
            {
                fprintf(fp, "%s ", nodes_map[*it_node].str);
            }
            else if (strcmp(nodes_map[*it_node].type, "value") == 0)
            {
                fprintf(fp, "[%s] ", nodes_map[*it_node].macro);
            }
            else
            {
                fprintf(fp, "%d ", *it_node);
            }
        }
        fprintf(fp, "\n");
    }
    fflush(fp);
}

int main(int argc, char *argv[])
{
    printf("cdl_search\n");
    char *filepath;
    if (argc > 1)
    {
        filepath = argv[1];
    }
    else
    {
        fprintf(stderr, "Usage: %s <cdl.xml>\n", argv[0]);
        exit(1);
    }

    xmlDocPtr doc = xmlReadFile(filepath, "UTF-8", XML_PARSE_RECOVER);
    if (doc == NULL)
    {
        fprintf(stderr, "Failed to parse cdl.xml\n");
        return 1;
    }
    xmlNodePtr root = xmlDocGetRootElement(doc);
    xmlNodePtr nodes = NULL, edges = NULL;

    for (xmlNodePtr cur = root->children; cur; cur = cur->next)
    {
        if (cur->type == XML_ELEMENT_NODE && strcmp((char *)cur->name, "nodes") == 0)
        {
            nodes = cur;
        }
        else if (cur->type == XML_ELEMENT_NODE && strcmp((char *)cur->name, "edges") == 0)
        {
            edges = cur;
        }
    }

    for (xmlNodePtr cur = nodes->children; cur; cur = cur->next)
    {
        if (cur->type == XML_ELEMENT_NODE && strcmp((char *)cur->name, "keyword") == 0)
        {
            char *guid_str = get_prop(cur, "guid");
            char *str = get_prop(cur, "str");
            char *name = get_prop(cur, "name");
            char *macro = get_prop(cur, "macro");
            int guid = guid_str ? atoi(guid_str) : 0;
            // if guid is not in the map, add it
            if (nodes_map.find(guid) == nodes_map.end())
            {
                Node node;
                node.guid = guid;
                strcpy(node.type, "keyword");
                if (name)
                    strcpy(node.name, name);
                if (str)
                    strcpy(node.str, str);
                if (macro)
                    strcpy(node.macro, macro);
                nodes_map[guid] = node;
            }
            // free the properties
            if (guid_str)
                free(guid_str);
            if (str)
                free(str);
            if (name)
                free(name);
            if (macro)
                free(macro);
        }
    }

    for (xmlNodePtr cur = nodes->children; cur; cur = cur->next)
    {
        if (cur->type == XML_ELEMENT_NODE && strcmp((char *)cur->name, "eol") == 0)
        {
            char *guid_str = get_prop(cur, "guid");
            char *name = get_prop(cur, "name");
            int guid = guid_str ? atoi(guid_str) : 0;
            // if guid is not in the map, add it
            if (nodes_map.find(guid) == nodes_map.end())
            {
                Node node;
                node.guid = guid;
                strcpy(node.type, "eol");
                if (name)
                    strcpy(node.name, name);
                nodes_map[guid] = node;
                eol_nodes_list.push_back(guid);
            }
            if (name)
                free(name);
            if (guid_str)
                free(guid_str);
        }
    }

    for (xmlNodePtr cur = nodes->children; cur; cur = cur->next)
    {
        if (cur->type == XML_ELEMENT_NODE && strcmp((char *)cur->name, "value") == 0)
        {
            char *guid_str = get_prop(cur, "guid");
            char *macro = get_prop(cur, "macro");
            char *name = get_prop(cur, "name");
            int guid = guid_str ? atoi(guid_str) : 0;
            // if guid is not in the map, add it
            if (nodes_map.find(guid) == nodes_map.end())
            {
                Node node;
                node.guid = guid;
                strcpy(node.type, "value");
                if (name)
                    strcpy(node.name, name);
                if (macro)
                    strcpy(node.macro, macro);
                nodes_map[guid] = node;
            }
            if (macro)
                free(macro);
            if (name)
                free(name);
            if (guid_str)
                free(guid_str);
        }
    }

    for (xmlNodePtr cur = edges->children; cur; cur = cur->next)
    {
        if (cur->type == XML_ELEMENT_NODE && strcmp((char *)cur->name, "edge") == 0)
        {
            char *from_guid_str = get_prop(cur, "from-guid");
            char *to_guid_str = get_prop(cur, "to-guid");
            int from_guid = from_guid_str ? atoi(from_guid_str) : -1;
            int to_guid = to_guid_str ? atoi(to_guid_str) : -1;
            if (from_guid < 0 || to_guid < 0)
            {
                if (from_guid_str)
                    free(from_guid_str);
                if (to_guid_str)
                    free(to_guid_str);
                continue;
            }
            // if both from_guid and to_guid are in the map, add the edge relations
            if (nodes_map.find(from_guid) != nodes_map.end() && nodes_map.find(to_guid) != nodes_map.end())
            {
                // add the edge relations if not exist
                if (std::find(nodes_map[from_guid].next.begin(), nodes_map[from_guid].next.end(), to_guid) == nodes_map[from_guid].next.end())
                {
                    nodes_map[from_guid].next.push_back(to_guid);
                }
                // if (std::find(nodes_map[to_guid].prev.begin(), nodes_map[to_guid].prev.end(), from_guid) == nodes_map[to_guid].prev.end())
                //{
                //     nodes_map[to_guid].prev.push_back(from_guid);
                // }
            }
            if (from_guid_str)
                free(from_guid_str);
            if (to_guid_str)
                free(to_guid_str);
        }
    }

    xmlFreeDoc(doc);

    int root_guid = 3840;

    FILE *fp = fopen("cmds.txt", "w");
    if (!fp)
    {
        perror("cmds.txt");
        return 1;
    }
    std::vector<std::thread> threads;
    int max_threads = 1;
    int running_threads = 0;
    // traverse all the EOL nodes
    // find all paths from root to EOL nodes by DFS search
    // and print them to cmds.txt
    printf("found %zu EOL nodes\n", eol_nodes_list.size());
    if (max_threads >= 2)
    {
        for (auto it = eol_nodes_list.begin(); it != eol_nodes_list.end(); ++it)
        {
            // 控制同時最多4個thread
            while (running_threads >= max_threads)
            {
                for (auto t_it = threads.begin(); t_it != threads.end();)
                {
                    if (t_it->joinable())
                    {
                        t_it->join();
                        t_it = threads.erase(t_it);
                        --running_threads;
                    }
                    else
                    {
                        ++t_it;
                    }
                }
                std::this_thread::yield();
            }

            threads.emplace_back(dfs_worker, root_guid, *it, fp);
            ++running_threads;
        }

        // 等待所有thread結束
        for (auto &t : threads)
        {
            if (t.joinable())
                t.join();
        }
    }
    else
    {
        for (auto it = eol_nodes_list.begin(); it != eol_nodes_list.end(); ++it)
        {
            dfs_worker(root_guid, *it, fp);
        }
    }

    fclose(fp);

    return 0;
}