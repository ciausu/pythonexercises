car={
    "brand": " FORD",
    "model": "MUSTANG",
    "year":"2008"
}
print(car.get("year"))
car["year"]=1964
print(car)
car["color"]="BLUE"
print(car)
car.pop("brand")
print(car)
car.clear()
print(car)
