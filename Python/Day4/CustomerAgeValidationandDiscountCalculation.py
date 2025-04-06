customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]
cust=filter(lambda x:x["age"]<=40,customers)

cc=list(map(lambda x:{
    "name":x["name"],
    "age":x["age"],
    "total_purchase":x["total_purchase"]*(0.9 if x["age"]<=25 else 0.95 if (x["age"]>=26 and x["age"]<=40) else 1)
}, cust))
print(cc)