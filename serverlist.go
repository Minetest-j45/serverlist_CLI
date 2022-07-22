package main

import (
	"encoding/json"
	"io"
	"log"
	"net/http"
	"os"
	"strings"
)

//ty to the awesome people at https://mholt.github.io/json-to-go/
type SrvList struct {
	Total struct {
		Servers int `json:"servers"`
		Clients int `json:"clients"`
	} `json:"total"`
	TotalMax struct {
		Servers int `json:"servers"`
		Clients int `json:"clients"`
	} `json:"total_max"`
	List []struct {
		Address        string   `json:"address"`
		Clients        int      `json:"clients"`
		ClientsList    []string `json:"clients_list"`
		ClientsMax     int      `json:"clients_max"`
		Creative       bool     `json:"creative"`
		Damage         bool     `json:"damage"`
		Description    string   `json:"description"`
		GameTime       int      `json:"game_time"`
		Gameid         string   `json:"gameid"`
		Lag            float64  `json:"lag,omitempty"`
		Name           string   `json:"name"`
		Password       bool     `json:"password"`
		Port           int      `json:"port"`
		ProtoMax       int      `json:"proto_max"`
		ProtoMin       int      `json:"proto_min"`
		Pvp            bool     `json:"pvp"`
		Uptime         int      `json:"uptime"`
		URL            string   `json:"url,omitempty"`
		Version        string   `json:"version"`
		IP             string   `json:"ip"`
		UpdateTime     int      `json:"update_time"`
		Start          int      `json:"start"`
		ClientsTop     int      `json:"clients_top"`
		Updates        int      `json:"updates"`
		TotalClients   int      `json:"total_clients"`
		PopV           float64  `json:"pop_v"`
		Ping           float64  `json:"ping"`
		GeoContinent   string   `json:"geo_continent,omitempty"`
		Dedicated      bool     `json:"dedicated,omitempty"`
		Rollback       bool     `json:"rollback,omitempty"`
		Mapgen         string   `json:"mapgen,omitempty"`
		Privs          string   `json:"privs,omitempty"`
		CanSeeFarNames bool     `json:"can_see_far_names,omitempty"`
		Mods           []string `json:"mods,omitempty"`
		ServerID       string   `json:"server_id,omitempty"`
		Proto          string   `json:"proto,omitempty"`
	} `json:"list"`
}

var CmdsWParam = []string{"address", "clients", "clients_list", "clients_max", "creative", "damage", "description", "game_time", "gameid", "lag", "name", "password",
	"port", "proto_max", "proto_min", "pvp", "server_id", "uptime", "version", "ip", "update_time", "start", "clients_top", "dedicated", "rollback", "mapgen",
	"privs", "can_see_far_names", "mods", "updates", "total_clients", "pop_v", "geo_continent", "ping"}

func main() {
	args := os.Args[1:]
	if len(args) == 0 {
		log.Fatal("You must have an argument")
	}

	resp, err := http.Get("https://servers.minetest.net/list")
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}

	var srvlist *SrvList
	json.Unmarshal(body, &srvlist)

	var good = false
	if len(args) == 1 {
		arg := args[0]
		if arg == "total_clients" {
			log.Println(srvlist.Total.Clients)
			good = true
		} else if arg == "total_servers" {
			log.Println(srvlist.Total.Servers)
			good = true
		} else if arg == "total_max_clients" {
			log.Println(srvlist.TotalMax.Clients)
			good = true
		} else if arg == "total_max_servers" {
			log.Println(srvlist.TotalMax.Servers)
			good = true
		} else if arg == "serverlist" {
			log.Println(srvlist)
			good = true
		}

		for _, command := range CmdsWParam {
			if arg == command {
				log.Println("You must put a servername after you say `" + command + "`")
				good = true
			}
		}
	}

	if len(args) > 2 {
		arg := args[0]
		name := strings.Join(args[1:], " ")
		servers := srvlist.List
		for _, command := range CmdsWParam {
			if arg == command {
				for _, server := range servers {
					if server.Name == name {
						cmd := strings.Title(command)
						log.Println(server[cmd]) //this bit not working
						good = true
					}
				}
			}
		}
	}

	if !good {
		log.Fatal("Invalid usage")
	}
}
