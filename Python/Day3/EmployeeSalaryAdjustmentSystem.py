employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]

salary=list(filter(lambda s:s["salary"],employees))
rating=list(map(lambda r: r["rating"] , employees))

ra=list(map(lambda r: 
            {'name':r["name"],
             'salary': round(r["salary"] * (1.10 if r["rating"]==5  else 1.05 if r["rating"]==3 else 0.98),2),
             'rating':r["rating"] }, employees))
print(ra)



