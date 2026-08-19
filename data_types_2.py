#=================================================
# Mega Challenge 2: The "Cloud Server" Disaster
#=================================================

#Master Data
import copy

master_config = {
    "server_name": "Main_Prod",
    "region": "us-east-1",
    "settings": ["auto_scaling", "firewall_on"]  # Ye ek nested list hai (Mutable!)
}

#----------Task 1: The Shallow Copy---------------------
server_A=copy.copy(master_config)

#----------Task 2: The Deep Copy------------------------
server_B=copy.deepcopy(master_config)

#----------Task 3: Modifying Server A-------------------
server_A["server_name"]="Backup_Node"
server_A["settings"].append("public_access")

#----------Task 4: Modifying Server B-------------------
server_B["server_name"]="Secure_Node"
server_B["settings"].append("vpn_only")

#------------------------------Final Report---------------------------------
print("===================CLOUD ARCHITECTURE REPORT===========================")
print(f"Master config name: {master_config.get("server_name")}")
print(f"Master Config settings: {master_config.get("settings")}")
print("---------------------------------------------------------------------")
print(f"Server A (Shallow) settings: {server_A["settings"]}")
print(f"Server B (Deep) settings: {server_B["settings"]}")
print("=======================================================================")