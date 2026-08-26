# =====================================================
# Mega Challenge 3: The "Secret Agency" Access System
# =====================================================

#Master_Data: Keys are frozen_sets and values are tuples
security_db = {
    frozenset({"Fingerprint", "Iris_Scan"}): ("Vault_Room", {"Read", "Download"}),
    frozenset({"Voice_Pass", "Face_ID", "Iris_Scan"}): ("Server_Room", {"Read", "Write", "Delete"})
}

#-----------------Task 1: The Frozenset Conversion----------------
scanned_data = ["Iris_Scan", "Fingerprint"]
agent_auth=frozenset(scanned_data)

#-----------------Task 2: Dictionary Lookup & Tuple Unpacking------
room_name,permissions=security_db.get(agent_auth)

#-----------------Task 3: Permission Check (Membership)------------
can_download= "Download" in permissions

#-----------------Task 4: The Master Key (Frozenset Math)----------
auth_1=frozenset({"Fingerprint", "Iris_Scan"})
auth_2=frozenset({"Voice_Pass", "Face_ID", "Iris_Scan"})
master_key_combo= auth_1 | auth_2

#=============================================================
#                       FINAL REPORT
#=============================================================
print("============= SECURITY CLEARANCE REPORT =============")
print(f"Scanned Biometrics: {agent_auth})")
print(f"Room Allocated: {room_name}")
print(f"Permissions: {permissions}")
print(f"Download Access: {can_download}")
print("-----------------------------------------------------")
print(f"New Master Key requires: {master_key_combo}")
print("=====================================================")
