hacker_log = "\n\t  ###  sysTem_WaRning: bOt_aCtiVe , tArgEt: DaTaBaSe , IP: 192.168.0.1  ###  \n\t"
clean_log=(hacker_log.replace("###","").strip().lower())
has_bot=("bot" in clean_log)
a_count=(clean_log.count("a"))
ip_address=(clean_log[-11::])
starts_correct=(clean_log.startswith("system"))
ends_correct=(clean_log.endswith("1"))

print("\n")

print("===================SECURITY REPORT====================")
print(f"Log Data: {clean_log}\nThreat Found: {has_bot}\n'a' count: {a_count}\nHacker IP: {ip_address}\nValid Log: {starts_correct}/{ends_correct} for starts/ends")
print("=======================================================")